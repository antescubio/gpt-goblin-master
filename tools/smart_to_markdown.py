import os
import sys
import re
import pdfplumber
import pytesseract
from PIL import Image
from collections import Counter, defaultdict
import fitz  # PyMuPDF

def extract_text_pdf(path):
    with pdfplumber.open(path) as pdf:
        size_map = defaultdict(list)

        for page in pdf.pages:
            words = page.extract_words(extra_attrs=["size", "top"])
            if not words:
                continue

            line_map = defaultdict(list)
            for word in words:
                line_map[round(word["top"], 1)].append(word)

            for top in sorted(line_map.keys()):
                line_words = line_map[top]
                text = " ".join(w["text"] for w in sorted(line_words, key=lambda w: w["x"]))
                avg_size = sum(float(w["size"]) for w in line_words) / len(line_words)
                size_map[avg_size].append(text)

        if not size_map:
            return None

        sorted_sizes = sorted(size_map.keys(), reverse=True)
        size_to_header = {size: i + 1 for i, size in enumerate(sorted_sizes)}

        md_lines = []

        for size in sorted_sizes:
            for line in size_map[size]:
                header_level = size_to_header[size]
                if len(line.strip()) == 0:
                    continue
                if header_level <= 3 and line.strip().isupper():
                    md_lines.append(f"{'#' * header_level} {line.strip()}")
                else:
                    list_match = detect_list_item(line)
                    if list_match:
                        md_lines.append(list_match)
                    else:
                        md_lines.append(line.strip())
                        md_lines.append("")

        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if len(table) > 0 and len(table[0]) > 1:
                    md_lines.append(format_table(table))
                    md_lines.append("")

        return "\n".join(md_lines)

def extract_text_ocr(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        doc = fitz.open(path)
        images = []
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
    else:
        images = [Image.open(path)]

    all_text = []
    for img in images:
        text = pytesseract.image_to_string(img)
        lines = text.splitlines()
        all_text.extend(lines)

    return format_hierarchy_from_lines(all_text)

def detect_list_item(line):
    list_pattern = re.compile(r"^(\s*)([-•*+]|\d+[.)]|[a-zA-Z][.)])\s+(.*)")
    match = list_pattern.match(line.strip())
    if match:
        _, bullet, content = match.groups()
        if re.match(r"\d+[.)]", bullet):
            return f"{bullet} {content}"
        else:
            return f"- {content}"
    return None

def format_table(table):
    header = table[0]
    rows = table[1:]

    md = []
    md.append("| " + " | ".join(cell.strip() if cell else "" for cell in header) + " |")
    md.append("|" + "|".join("---" for _ in header) + "|")

    for row in rows:
        md.append("| " + " | ".join(cell.strip() if cell else "" for cell in row) + " |")
    return "\n".join(md)

def format_hierarchy_from_lines(lines):
    output = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        list_match = detect_list_item(stripped)
        if list_match:
            output.append(list_match)
            continue

        if stripped.isupper() and len(stripped.split()) < 10:
            output.append(f"# {stripped}")
        elif stripped.endswith(":") or stripped.endswith("?"):
            output.append(f"## {stripped}")
        else:
            output.append(stripped)
            output.append("")

    return "\n".join(output)

def process_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        md_content = extract_text_pdf(path)
        if md_content is None:
            print("📄 PDF sin texto digital detectado. Usando OCR...")
            md_content = extract_text_ocr(path)
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        md_content = extract_text_ocr(path)
    else:
        raise ValueError("❌ Formato no soportado.")

    output_path = os.path.splitext(path)[0] + ".md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ Archivo Markdown generado: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python smart_to_markdown.py <archivo.pdf o imagen>")
    else:
        process_file(sys.argv[1])

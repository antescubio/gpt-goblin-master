import os
import json

def parse_multilang_md(md_content):
    data = {}
    lines = md_content.splitlines()
    section = None
    current_feature = None
    current_subsection = None
    current_lang = None
    description_buffer = {"en": [], "es": []}
    features = []

    for line in lines:
        line = line.strip()

        if line.startswith("## Name"):
            section = "name"
            data['name'] = {}
            continue
        elif line.startswith("## Description"):
            section = "description"
            data['description'] = {}
            continue
        elif line.startswith("## Appearance"):
            section = "appearance"
            data['appearance'] = {}
            continue
        elif line.startswith("## Skills"):
            section = "skills"
            data['skills'] = {}
            continue
        elif line.startswith("## Tools or Languages"):
            section = "tools_or_languages"
            data['tools_or_languages'] = {}
            continue
        elif line.startswith("## Equipment"):
            section = "equipment"
            data['equipment'] = {}
            continue
        elif line.startswith("## Personality"):
            section = "personality"
            data['personality'] = {}
            continue
        elif line.startswith("## Ideals"):
            section = "ideals"
            data['ideals'] = {}
            continue
        elif line.startswith("## Bonds"):
            section = "bonds"
            data['bonds'] = {}
            continue
        elif line.startswith("## Flaws"):
            section = "flaws"
            data['flaws'] = {}
            continue
        elif line.startswith("## Features"):
            section = "features"
            continue
        elif line.startswith("### Feature"):
            if current_feature:
                for lang in ["en", "es"]:
                    current_feature["description"][lang] = "\n".join(description_buffer[lang]).strip()
                features.append(current_feature)
            current_feature = {"title": {}, "description": {}}
            description_buffer = {"en": [], "es": []}
            current_subsection = None
            continue
        elif line.startswith("#### Title"):
            current_subsection = "title"
            continue
        elif line.startswith("#### Description"):
            current_subsection = "description"
            continue
        elif line.startswith("- en:"):
            text = line[5:].strip()
            current_lang = "en"
            if section in data and section != "features":
                data[section]["en"] = text
            elif section == "features" and current_feature and current_subsection:
                if current_subsection == "title":
                    current_feature["title"]["en"] = text
                else:
                    description_buffer["en"].append(text)
        elif line.startswith("- es:"):
            text = line[5:].strip()
            current_lang = "es"
            if section in data and section != "features":
                data[section]["es"] = text
            elif section == "features" and current_feature and current_subsection:
                if current_subsection == "title":
                    current_feature["title"]["es"] = text
                else:
                    description_buffer["es"].append(text)
        elif section == "features" and current_lang:
            description_buffer[current_lang].append(line)

    if current_feature:
        for lang in ["en", "es"]:
            current_feature["description"][lang] = "\n".join(description_buffer[lang]).strip()
        features.append(current_feature)

    if features:
        data["features"] = features

    return data

def parse_md_file_to_json(md_path, output_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    structured_data = parse_multilang_md(md_content)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, indent=2, ensure_ascii=False)

def batch_convert(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md'):
                md_path = os.path.join(root, filename)
                output_path = md_path.replace(".md", ".json").replace("content", "data")
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                parse_md_file_to_json(md_path, output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Convert markdown files to JSON.')
    parser.add_argument('input', help='Path to a markdown file or directory.')
    args = parser.parse_args()

    if os.path.isfile(args.input):
        output = args.input.replace(".md", ".json").replace("content", "data")
        os.makedirs(os.path.dirname(output), exist_ok=True)
        parse_md_file_to_json(args.input, output)
    else:
        batch_convert(args.input)

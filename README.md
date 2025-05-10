# 🧙 My Goblin Master – Character Creation System

Este repositorio contiene contenido oficial y homebrew para la creación de personajes de Dungeons & Dragons 5e, compatible con el *Player’s Handbook* 2014, *Player’s Handbook* 2024 y el *Radiant’s Handbook (Cosmere)*.

---

## 📁 Estructura del repositorio

```
GPT-GOBLIN-MASTER/
├── content/
│   ├── 2014/
│   │   ├── official/
│   │   │   ├── backgrounds/
│   │   │   ├── classes/
│   │   │   ├── feats/
│   │   │   └── species/
│   │   └── homebrew/
│   │       ├── backgrounds/
│   │       ├── classes/
│   │       ├── feats/
│   │       └── species/
│   ├── 2024/
│   │   ├── official/
│   │   │   ├── backgrounds/
│   │   │   ├── classes/
│   │   │   ├── feats/
│   │   │   └── species/
│   │   └── homebrew/
│   │       ├── backgrounds/
│   │       ├── classes/
│   │       ├── feats/
│   │       └── species/
│
├── data/
│
├── tools/
│   └── md2json_parser.py
│
├── docs/
│   └── rules/
│       ├── feat_usage.md
│       ├── character_creation_with_radiants.md
│       └── README.md
│
└── README.md
```

---

## 📘 Reglas Especiales

Este proyecto admite Órdenes Radiantes del *Radiant’s Handbook*. Un personaje puede:

- Tener una clase y subclase del PHB
- Pertenecer a una Orden Radiante del Cosmere
- Obtener automáticamente Ideal Feats al jurar nuevos Ideales (niveles 3, 6, 10, 14)

Consulta la carpeta [`docs/rules/`](./docs/rules/) para más detalles sobre cómo combinarlas correctamente.

---

## 🛠 Herramientas

- `tools/md2json_parser.py`: Convierte `.md` en archivos JSON estructurados para el modelo GPT personalizado.
- El sistema espera estructura bilingüe con claves `en` y `es`.

---

## 🔮 Licencia

Este proyecto combina material oficial y homebrew. Su uso está destinado exclusivamente a entornos personales o con GPTs personalizados compatibles.
# ✨ Spren – Entidades Vinculadas a las Órdenes Radiantes

Este directorio contiene archivos `.md` para cada tipo de spren asociado a las Órdenes Radiantes del *Radiant’s Handbook (Cosmere)*. Estos archivos están diseñados para ser leídos y entendidos por un GPT personalizado.

---

## 🧠 Instrucciones para el GPT

### ¿Qué es un spren?

- Un spren es una entidad espiritual que **representa el Ideal de una Orden Radiante**.
- Todo personaje que pertenezca a una Orden Radiante debe tener **exactamente un spren asociado** según su orden.
- El spren otorga **rasgos únicos, bonificaciones y habilidades** descritas en su archivo `.md`.

### ¿Cómo utilizar estos archivos?

1. Verifica si el personaje pertenece a una Orden Radiante.
2. Si es así, identifica el spren correspondiente usando la siguiente tabla.
3. Asocia automáticamente los rasgos y el stat block de ese spren al personaje.
4. Si el spren está inactivo (por ejemplo, HP = 0), **bloquea el acceso a feats o habilidades de Orden Radiante** hasta que sea restaurado.
5. Considera al spren como un familiar activo: puede afectar a la narrativa, las mecánicas, las salvaciones, y los turnos en combate si se especifica.

---

## 🗂 Relación de Órdenes y Spren

| Orden Radiante | Spren Asociado     | Archivo .md           |
|----------------|--------------------|------------------------|
| Windrunner     | Honorspren         | `honorspren.md`        |
| Skybreaker     | Highspren          | `highspren.md`         |
| Lightweaver    | Cryptic            | `cryptic.md`           |
| Edgedancer     | Cultivationspren   | `cultivationspren.md`  |
| Truthwatcher   | Mistspren          | `mistspren.md`         |
| Stoneward      | Peakspren          | `peakspren.md`         |
| Dustbringer    | Ashspren           | `ashspren.md`          |
| Willshaper     | Lightspren         | `lightspren.md`        |
| Elsecaller     | Inkspren           | `inkspren.md`          |
| Bondsmith      | Reachers           | `reachers.md`          |

---

Cada archivo incluye:
- Descripción narrativa
- Rasgos únicos (`## Traits`)
- Bloque de estadísticas simplificadas (`## Stat Block`)

Estos archivos deben integrarse automáticamente en la lógica del GPT personalizado si se detecta que el personaje pertenece a una Orden Radiante.
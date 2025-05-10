# Ideal Feats del Radiant’s Handbook (Cosmere)

Los Ideal Feats no son dotes estándar elegibles. Son habilidades especiales exclusivas de los personajes que pertenecen a una Orden de los Caballeros Radiantes, como los Windrunners, Skybreakers, etc.

---

## ¿Cómo se adquieren?

Un personaje Radiante **no elige estos feats manualmente**. En cambio, los obtiene automáticamente al **jurar nuevos Ideales** de su Orden, en los siguientes niveles:

| Nivel de personaje | Ideal jurado   | Nivel de feat otorgado |
|--------------------|----------------|-------------------------|
| 3                  | Segundo Ideal  | Feat de nivel 3         |
| 6                  | Tercer Ideal   | Feat de nivel 6         |
| 10                 | Cuarto Ideal   | Feat de nivel 10        |
| 14                 | Quinto Ideal   | Feat de nivel 14        |

---

## ¿Qué feats se pueden elegir?

Cada Orden tiene **una lista cerrada de feats por Ideal y nivel**. Solo se pueden elegir feats de esa lista al alcanzar el nivel e Ideal correspondiente.

- Un personaje **no puede elegir feats de otra Orden**.
- Un personaje **no puede elegir feats de un Ideal que aún no ha jurado**.
- Estos feats **no reemplazan ni consumen** los feats estándar por nivel (como los de nivel 4, 8, etc.).

---

## ¿Cómo aplicarlos?

Cuando un personaje sube de nivel y cumple las condiciones (clase, nivel e Ideal jurado), permite elegir **un feat de su Orden** del nivel correspondiente.

**Ejemplo:**
> Un personaje Windrunner que jura el Segundo Ideal al nivel 3 puede elegir un feat de nivel 3 del Ideal of Protection, como *Stormlight Fortitude* o *Radiant Shield*.

---

## Identificación de feats

Los Ideal Feats están identificados por:
- Campo `Order`: indica la Orden Radiante
- Campo `Level`: nivel mínimo requerido para obtener ese feat

Un GPT personalizado debe verificar ambos campos y aplicar solo si el personaje cumple:
- Clase de Orden Radiante
- Nivel adecuado
- Ideal jurado correspondiente

---

## ⚠️ Nota sobre Spren y Activación

Los Ideal Feats de las Órdenes Radiantes requieren que el spren del personaje esté presente y activo. Si el spren está ausente, dispersado o reducido a 0 HP:

- El personaje **no puede usar** los feats asociados a su Orden hasta que el spren sea restaurado.
- El GPT personalizado debe verificar este estado al aplicar o sugerir feats.

Consulta `spren_rules.md` para las reglas completas sobre el funcionamiento de los spren.
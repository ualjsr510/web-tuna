#!/usr/bin/env python3
"""Genera el diagrama entidad-relación de tuna.sql (diagrama.svg y diagrama.html).

Las columnas, claves y relaciones se leen del propio tuna.sql; aquí solo se
fija dónde va cada tabla, el color de su grupo y el texto de cada relación.

    python3 database/mysql/generar_diagrama.py
    inkscape database/mysql/diagrama.svg --export-type=pdf \
        --export-filename=database/mysql/diagrama.pdf
"""
import html
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SQL = (AQUI / "tuna.sql").read_text(encoding="utf-8")

# ---------------------------------------------------------------- estilo
GRUPOS = {
    "cuentas":     ("Cuentas",                 "#b08a1e", "#fbf6e9"),
    "tuna":        ("Tuna y únete",            "#7a1f2b", "#f8eef0"),
    "contratacion": ("Contratación",           "#2f6f4f", "#edf5f0"),
    "tienda":      ("Tienda",                  "#1f4e7a", "#ecf2f8"),
    "cancionero":  ("Cancionero y multimedia", "#6a3d8f", "#f3eef8"),
    "sitio":       ("Sitio",                   "#5c5f66", "#f1f2f3"),
}
ANCHO, CAB, FILA = 270, 28, 17
HUECO = 110                                          # separación entre columnas
COL = [40 + i * (ANCHO + HUECO) for i in range(7)]   # x de cada columna de la rejilla
TINTA, SUAVE, LINEA = "#2a2118", "#8a7d70", "#4a4038"

# tabla: (grupo, columna de la rejilla, y)
POS = {
    # Cuentas, contratación y tienda (franja superior)
    "tokens_recuperacion": ("cuentas", 0, 110),
    "usuarios":            ("cuentas", 1, 110),
    "tipos_evento":        ("contratacion", 0, 330),
    "actuaciones":         ("contratacion", 0, 520),
    "servicios":           ("contratacion", 0, 720),
    "contratos":           ("contratacion", 1, 470),
    "pedidos":             ("tienda", 2, 110),
    "devoluciones":        ("tienda", 2, 640),
    "pedido_lineas":       ("tienda", 3, 110),
    "devolucion_lineas":   ("tienda", 3, 640),
    "producto_opciones":   ("tienda", 4, 110),
    "productos":           ("tienda", 4, 330),
    "categorias_producto": ("tienda", 5, 380),
    "hitos_historia":      ("sitio", 5, 110),
    "noticias":            ("sitio", 6, 110),
    "configuracion":       ("sitio", 6, 330),
    # Tuna y únete, cancionero y multimedia (franja inferior)
    "instrumentos":        ("tuna", 0, 920),
    "solicitudes_ingreso": ("tuna", 0, 1050),
    "miembros":            ("tuna", 1, 920),
    "generos":             ("cancionero", 2, 920),
    "albumes":             ("cancionero", 2, 1030),
    "canciones":           ("cancionero", 3, 920),
    "certamenes":          ("cancionero", 4, 920),
    "multimedia":          ("cancionero", 5, 920),
    "locales_ensayo":      ("tuna", 6, 920),
    "horarios_ensayo":     ("tuna", 6, 1120),
}

# (tabla hija, columna FK) → t: texto de la relación; lado: ruta en C si las
# dos tablas están en la misma columna ("izq"/"der"); dx: x del tramo
# vertical dentro del hueco entre columnas (0 … HUECO); varios: la hija
# tiene "uno o muchos" en lugar de "cero o muchos"; ly: y de la etiqueta.
REL = {
    ("tokens_recuperacion", "usuario_id"):    dict(t="recupera"),
    ("contratos", "usuario_id"):              dict(t="solicita", lado="izq", dx=84),
    ("contratos", "tipo_evento_id"):          dict(t="tipo", dx=56),
    ("actuaciones", "contrato_id"):           dict(t="agenda", dx=30),
    ("pedidos", "usuario_id"):                dict(t="realiza"),
    ("devoluciones", "pedido_id"):            dict(t="devuelve", lado="izq", dx=84, ly=420),
    ("pedido_lineas", "pedido_id"):           dict(t="contiene", dx=45, varios=True),
    ("devolucion_lineas", "devolucion_id"):   dict(t="incluye", varios=True),
    ("pedido_lineas", "producto_id"):         dict(t="vendido", dx=52, ly=300),
    ("pedido_lineas", "opcion_id"):           dict(t="opción", dx=80, ly=172),
    ("devolucion_lineas", "pedido_linea_id"): dict(t="línea", lado="der", dx=28, ly=480),
    ("producto_opciones", "producto_id"):     dict(t="talla / formato", lado="der", dx=55, varios=True),
    ("productos", "categoria_id"):            dict(t="agrupa"),
    ("miembros", "instrumento_id"):           dict(t="toca"),
    ("solicitudes_ingreso", "instrumento_id"): dict(t="toca", lado="izq", dx=90),
    ("canciones", "genero_id"):               dict(t="género", dx=70),
    ("canciones", "album_id"):                dict(t="álbum", dx=40),
    ("multimedia", "certamen_id"):            dict(t="fotos y vídeos"),
    ("horarios_ensayo", "local_id"):          dict(t="horario", lado="der", dx=40),
}


# --------------------------------------------------------- leer tuna.sql
def leer_tablas(sql):
    tablas = {}
    for m in re.finditer(r"CREATE TABLE (\w+) \((.*?)\n\) ENGINE", sql, re.S):
        nombre, cuerpo = m.group(1), m.group(2)
        cols, pk, uk, fk = [], set(), set(), {}
        for linea in cuerpo.split("\n"):
            linea = re.sub(r"--.*", "", linea).strip().rstrip(",")
            if not linea:
                continue
            if c := re.match(r"PRIMARY KEY \(([^)]*)\)", linea):
                pk |= {x.strip() for x in c.group(1).split(",")}
            elif c := re.match(r"UNIQUE KEY \w+ \(([^)]*)\)", linea):
                uk |= {x.strip() for x in c.group(1).split(",")}
            elif c := re.search(r"FOREIGN KEY \((\w+)\)\s+REFERENCES\s+(\w+)\s*\((\w+)\)", linea):
                fk[c.group(1)] = (c.group(2), c.group(3))
            elif re.match(r"(KEY|FULLTEXT|CONSTRAINT|UNIQUE|PRIMARY|NOT|\(|OR|AND)\b", linea):
                continue
            elif c := re.match(r"(\w+)\s+([A-Z]+(?:\([^)]*\))?)(.*)", linea):
                col, tipo, resto = c.groups()
                if tipo.startswith("ENUM"):
                    tipo = "ENUM"
                if " AS (" in resto:
                    tipo += " · calc."
                if "PRIMARY KEY" in resto:
                    pk.add(col)
                nulo = "NOT NULL" not in resto and "PRIMARY KEY" not in resto
                cols.append(dict(n=col, tipo=tipo, nulo=nulo))
        for c in cols:
            c["pk"], c["uk"], c["fk"] = c["n"] in pk, c["n"] in uk, c["n"] in fk
        tablas[nombre] = dict(cols=cols, fk=fk)
    return tablas


TABLAS = leer_tablas(SQL)
assert set(TABLAS) == set(POS), set(TABLAS) ^ set(POS)


def caja(t):
    grupo, col, y = POS[t]
    return COL[col], y, ANCHO, CAB + FILA * len(TABLAS[t]["cols"]) + 6


def y_fila(t, col):
    x, y, w, h = caja(t)
    i = [c["n"] for c in TABLAS[t]["cols"]].index(col)
    return y + CAB + FILA * i + FILA / 2 + 3


# ---------------------------------------------------------------- dibujo
out = []
e = html.escape


def texto(x, y, s, size=11, color=TINTA, peso=400, ancla="start", extra=""):
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" '
               f'font-weight="{peso}" text-anchor="{ancla}" {extra}>{e(s)}</text>')


def insignia(x, y, s, color):
    out.append(f'<rect x="{x}" y="{y - 9}" width="19" height="12" rx="2.5" fill="{color}"/>')
    texto(x + 9.5, y, s, 7.5, "#fff", 700, "middle")


def dibujar_tabla(t):
    grupo, _, _ = POS[t]
    _, color, fondo = GRUPOS[grupo]
    x, y, w, h = caja(t)
    out.append(f'<g><rect x="{x + 2}" y="{y + 3}" width="{w}" height="{h}" rx="6" fill="#000" opacity=".07"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fffdf9" stroke="{color}" stroke-width="1.3"/>')
    out.append(f'<path d="M{x},{y + CAB} v-{CAB - 6} a6,6 0 0 1 6,-6 h{w - 12} a6,6 0 0 1 6,6 v{CAB - 6} z" fill="{color}"/>')
    texto(x + 10, y + 18.5, t, 12.5, "#fff", 700)
    for i, c in enumerate(TABLAS[t]["cols"]):
        fy = y + CAB + FILA * i
        if i % 2:
            out.append(f'<rect x="{x + 1}" y="{fy}" width="{w - 2}" height="{FILA}" fill="{fondo}"/>')
        bx = x + 8
        if c["pk"]:
            insignia(bx, fy + 12.5, "PK", "#b08a1e"); bx += 22
        if c["fk"]:
            insignia(bx, fy + 12.5, "FK", "#1f4e7a"); bx += 22
        if c["uk"] and not c["pk"]:
            insignia(bx, fy + 12.5, "UK", "#7b7f86"); bx += 22
        tx = max(x + 54, bx + 4) if (c["pk"] or c["fk"] or c["uk"]) else x + 54
        texto(tx, fy + 12.5, c["n"], 11, TINTA, 700 if c["pk"] else 400)
        texto(x + w - 8, fy + 12.5, c["tipo"], 8.5, SUAVE, 400, "end")
    out.append("</g>")


def marca_padre(x, y, d, opcional):
    """d = +1 si la línea sale hacia la derecha de la tabla."""
    out.append(f'<line x1="{x + d * 7}" y1="{y - 6}" x2="{x + d * 7}" y2="{y + 6}"/>')
    if opcional:
        out.append(f'<circle cx="{x + d * 16}" cy="{y}" r="4" fill="#fff"/>')
    else:
        out.append(f'<line x1="{x + d * 12}" y1="{y - 6}" x2="{x + d * 12}" y2="{y + 6}"/>')


def marca_hija(x, y, d, varios):
    p = x + d * 12
    out.append(f'<path d="M{x},{y - 6} L{p},{y} L{x},{y + 6} M{x},{y} L{p},{y}" fill="none"/>')
    if varios:
        out.append(f'<line x1="{x + d * 16}" y1="{y - 6}" x2="{x + d * 16}" y2="{y + 6}"/>')
    else:
        out.append(f'<circle cx="{x + d * 20}" cy="{y}" r="4" fill="#fff"/>')


def etiqueta(x, y, s):
    w = 7 + 5.6 * len(s)
    out.append(f'<rect x="{x - w / 2:.1f}" y="{y - 8}" width="{w:.1f}" height="15" rx="4" '
               f'fill="#fffdf9" stroke="#b9ab98" stroke-width=".8"/>')
    texto(x, y + 3.3, s, 9.5, "#5d5246", 400, "middle", 'font-style="italic"')


def dibujar_relacion(hija, col, cfg):
    padre, pcol = TABLAS[hija]["fk"][col]
    hx, _, hw, _ = caja(hija)
    px, _, pw, _ = caja(padre)
    y1, y2 = y_fila(hija, col), y_fila(padre, pcol)
    opcional = next(c for c in TABLAS[hija]["cols"] if c["n"] == col)["nulo"]
    out.append(f'<g stroke="{LINEA}" stroke-width="1.2" fill="none">')
    if "lado" in cfg:                       # misma columna: ruta en C
        if cfg["lado"] == "izq":
            a, b, d = hx, px, -1
            vx = hx - HUECO + cfg["dx"]
        else:
            a, b, d = hx + hw, px + pw, 1
            vx = hx + hw + cfg["dx"]
        out.append(f'<path d="M{a},{y1} H{vx} V{y2} H{b}"/>')
        marca_hija(a, y1, d, cfg.get("varios"))
        marca_padre(b, y2, d, opcional)
        lx, ly = vx, (y1 + y2) / 2
    else:
        if hx < px:
            a, b, dh, dp = hx + hw, px, 1, -1
        else:
            a, b, dh, dp = hx, px + pw, -1, 1
        vx = min(a, b) + cfg.get("dx", HUECO / 2)
        out.append(f'<path d="M{a},{y1} H{vx} V{y2} H{b}"/>')
        marca_hija(a, y1, dh, cfg.get("varios"))
        marca_padre(b, y2, dp, opcional)
        lx, ly = vx, (y1 + y2) / 2
        if abs(y1 - y2) < 30:
            lx = (a + b) / 2
    if "ly" in cfg:
        ly = cfg["ly"]
    out.append("</g>")
    etiqueta(lx, ly, cfg["t"])


# -------------------------------------------------------------- montaje
for (hija, col) in REL:
    assert col in TABLAS[hija]["fk"], (hija, col)
faltan = {(t, c) for t in TABLAS for c in TABLAS[t]["fk"]} - set(REL)
assert not faltan, faltan

W = COL[-1] + ANCHO + 80
H = max(caja(t)[1] + caja(t)[3] for t in TABLAS) + 40

# Rótulos de grupo y leyenda
texto(40, 46, "Base de datos · Tuna de Derecho de Almería", 26, TINTA, 800)
texto(40, 72, f"Diagrama entidad-relación de database/mysql/tuna.sql · MySQL 8 · InnoDB · utf8mb4 · {len(TABLAS)} tablas",
      13, SUAVE)
lx = 1100
for clave, (nombre, color, _) in GRUPOS.items():
    out.append(f'<rect x="{lx}" y="58" width="13" height="13" rx="3" fill="{color}"/>')
    texto(lx + 19, 69, nombre, 12.5)
    lx += 34 + 7.2 * len(nombre)

for (hija, col), cfg in REL.items():
    dibujar_relacion(hija, col, cfg)
for t in TABLAS:
    dibujar_tabla(t)

# Notación (debajo de configuracion)
nx, ny = COL[6], caja("configuracion")[1] + caja("configuracion")[3] + 40
out.append(f'<rect x="{nx}" y="{ny}" width="{ANCHO}" height="148" rx="6" fill="#fffdf9" stroke="#d8ccbb"/>')
texto(nx + 12, ny + 22, "Notación", 12.5, TINTA, 700)
filas = [("uno", False, "exactamente uno"), ("cero-uno", True, "cero o uno"),
         ("muchos", True, "uno o muchos"), ("muchos", False, "cero o muchos")]
for i, (tipo, flag, desc) in enumerate(filas):
    yy = ny + 44 + i * 22
    out.append(f'<g stroke="{LINEA}" stroke-width="1.2" fill="none"><line x1="{nx + 14}" y1="{yy}" x2="{nx + 70}" y2="{yy}"/>')
    if tipo == "muchos":
        marca_hija(nx + 70, yy, -1, flag)
    else:
        marca_padre(nx + 70, yy, -1, flag)
    out.append("</g>")
    texto(nx + 84, yy + 4, desc, 11)
yy = ny + 44 + 4 * 22
insignia(nx + 14, yy + 2, "PK", "#b08a1e"); texto(nx + 37, yy + 2, "primaria", 9.5, SUAVE)
insignia(nx + 92, yy + 2, "FK", "#1f4e7a"); texto(nx + 115, yy + 2, "ajena", 9.5, SUAVE)
insignia(nx + 158, yy + 2, "UK", "#7b7f86"); texto(nx + 181, yy + 2, "única", 9.5, SUAVE)

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
       f'font-family="DejaVu Sans, Verdana, sans-serif">\n'
       f'<rect width="{W}" height="{H}" fill="#faf7f2"/>\n' + "\n".join(out) + "\n</svg>\n")
(AQUI / "diagrama.svg").write_text(svg, encoding="utf-8")

(AQUI / "diagrama.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Diagrama BD · Tuna</title>
<style>
  @page {{ size: {W}px {H}px; margin: 0; }}
  html, body {{ margin: 0; background: #faf7f2; }}
  svg {{ display: block; max-width: 100%; height: auto; }}
  @media print {{ svg {{ max-width: none; }} }}
</style>
</head>
<body>
{svg}</body>
</html>
""", encoding="utf-8")
print(f"diagrama.svg y diagrama.html generados ({W}x{H}px, {len(TABLAS)} tablas, {len(REL)} relaciones)")

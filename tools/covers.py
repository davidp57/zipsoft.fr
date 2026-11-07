"""Draws the line-art covers of the project cards that have no screenshot (600 x 300 SVG, light and dark).

Run from the repository root: python tools/covers.py assets/img/covers
"""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])

PALETTES = {
    # light bg top, light bg bottom, light ink, light accent, dark bg top, dark bg bottom, dark ink, dark accent
    "dcs":  ("#e8eef6", "#d5e0ee", "#2b4466", "#c2662d", "#1b2430", "#141b24", "#a9bfdc", "#e58c4f"),
    "apps": ("#e6f3f0", "#d2e9e3", "#1d5a53", "#c2662d", "#16231f", "#101a17", "#8fd0c4", "#e58c4f"),
}

def svg(category, body):
    lt, lb, li, la, dt, db, di, da = PALETTES[category]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="600" height="300">
<style>
.bg-t{{stop-color:{lt}}}.bg-b{{stop-color:{lb}}}
.i{{fill:none;stroke:{li};stroke-width:7;stroke-linecap:round;stroke-linejoin:round}}
.a{{fill:none;stroke:{la};stroke-width:7;stroke-linecap:round;stroke-linejoin:round}}
.f{{fill:{li}}}.fa{{fill:{la}}}.d{{fill:{li};opacity:.13}}
@media (prefers-color-scheme: dark){{
.bg-t{{stop-color:{dt}}}.bg-b{{stop-color:{db}}}
.i{{stroke:{di}}}.a{{stroke:{da}}}.f{{fill:{di}}}.fa{{fill:{da}}}.d{{fill:{di};opacity:.12}}
}}
</style>
<defs>
<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="bg-t"/><stop offset="1" class="bg-b"/></linearGradient>
<pattern id="p" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="1.6" class="d"/></pattern>
</defs>
<rect width="600" height="300" fill="url(#g)"/>
<rect width="600" height="300" fill="url(#p)"/>
{body}
</svg>
'''

COVERS = {
    # helicopter carrying a crate on a sling
    "ctld": ("dcs", '''
<path class="i" d="M170 70 H430"/><path class="i" d="M300 70 V88"/>
<path class="i" d="M245 95 H335 Q370 95 372 125 Q372 145 345 148 H262 Q240 148 238 125 Z"/>
<path class="i" d="M372 120 H470 L482 100"/><path class="i" d="M470 120 L486 132"/>
<path class="i" d="M330 102 Q352 104 356 122 H330 Z"/>
<path class="i" d="M255 160 H345"/><path class="i" d="M268 148 V160"/><path class="i" d="M332 148 V160"/>
<path class="a" d="M300 160 L270 205"/><path class="a" d="M300 160 L330 205"/>
<rect class="a" x="258" y="205" width="84" height="56" rx="4"/><path class="a" d="M258 233 H342 M300 205 V261"/>
'''),
    # radar mast with waves, and a SAM launcher
    "skynet-iads": ("dcs", '''
<path class="i" d="M190 262 L220 130 L250 262"/><path class="i" d="M203 205 H237 M210 172 H230"/>
<circle class="f" cx="220" cy="120" r="10"/>
<path class="a" d="M190 92 A42 42 0 0 1 250 92"/><path class="a" d="M172 74 A66 66 0 0 1 268 74"/>
<path class="i" d="M330 262 H470"/><rect class="i" x="345" y="222" width="110" height="28" rx="6"/>
<circle class="i" cx="368" cy="254" r="9"/><circle class="i" cx="432" cy="254" r="9"/>
<path class="i" d="M380 222 L440 150"/><path class="i" d="M398 222 L458 150"/>
<path class="a" d="M440 150 L456 130 M458 150 L474 130"/>
'''),
    # map pin on a front line, and a save point
    "foothold-checkpoint-tool": ("dcs", '''
<path class="i" d="M150 240 L230 200 L300 225 L380 185 L450 205"/>
<path class="i" stroke-dasharray="2 16" d="M150 270 L230 230 L300 255 L380 215 L450 235"/>
<path class="a" d="M300 225 V95"/><path class="a" d="M300 95 L370 112 L300 130"/>
<rect class="i" x="395" y="70" width="80" height="80" rx="8"/><rect class="i" x="412" y="70" width="46" height="26"/>
<rect class="i" x="410" y="114" width="50" height="36"/>
<path class="i" d="M150 115 A40 40 0 1 1 165 150"/><path class="i" d="M150 92 V117 H175"/>
'''),
    # a stack of comic books and a speech bubble
    "issued": ("apps", '''
<path class="i" d="M190 255 V110 L260 92 V237 Z"/><path class="i" d="M260 92 L330 110 V255 L260 237"/>
<path class="i" d="M205 135 L245 125 M205 160 L245 150 M205 185 L245 175"/>
<rect class="i" x="275" y="128" width="40" height="36" rx="2"/><path class="i" d="M275 185 H315 M275 205 H305"/>
<path class="a" d="M370 80 H470 Q485 80 485 95 V150 Q485 165 470 165 H415 L392 188 L398 165 H370 Q355 165 355 150 V95 Q355 80 370 80 Z"/>
<path class="a" d="M380 110 H460 M380 135 H440"/>
'''),
    # ledger and a pair of scales
    "solde": ("apps", '''
<rect class="i" x="160" y="85" width="140" height="175" rx="8"/>
<path class="i" d="M185 85 V260"/><path class="i" d="M200 120 H280 M200 150 H280 M200 180 H280 M200 210 H255"/>
<path class="a" d="M410 255 V90"/><path class="a" d="M380 255 H440"/><path class="a" d="M340 115 H480"/>
<path class="a" d="M350 115 L325 175 H375 Z"/><path class="a" d="M470 115 L445 175 H495 Z"/>
<circle class="fa" cx="410" cy="88" r="8"/>
'''),
    # envelopes, and a budgie perched on them
    "budgie": ("apps", '''
<rect class="i" x="140" y="160" width="130" height="90" rx="6"/><path class="i" d="M140 168 L205 210 L270 168"/>
<rect class="i" x="290" y="160" width="130" height="90" rx="6"/><path class="i" d="M290 168 L355 210 L420 168"/>
<path class="a" d="M330 160 Q318 120 340 98 Q360 80 382 92 Q392 100 390 112 L402 118 L390 122 Q392 145 372 160 Z"/>
<circle class="fa" cx="373" cy="105" r="5"/><path class="a" d="M335 150 L305 158"/>
<path class="a" d="M352 120 Q345 138 360 148"/>
'''),
    # a film frame with a play button over a folder
    "hoard": ("apps", '''
<path class="i" d="M150 120 H230 L250 140 H350 V250 H150 Z"/>
<rect class="i" x="260" y="70" width="190" height="140" rx="10"/>
<path class="i" d="M285 70 V210 M425 70 V210"/>
<path class="i" d="M260 100 H285 M260 140 H285 M260 180 H285 M425 100 H450 M425 140 H450 M425 180 H450"/>
<path class="a" d="M340 112 L380 140 L340 168 Z"/>
<path class="a" d="M285 230 H450"/><circle class="fa" cx="380" cy="230" r="8"/>
'''),
    # mountains and a walking trail with waypoints
    "olifant": ("apps", '''
<path class="i" d="M130 245 L230 115 L285 185 L345 100 L470 245"/>
<path class="i" d="M210 141 L230 155 L250 141 M325 126 L345 140 L365 126"/>
<path class="a" stroke-dasharray="3 15" d="M160 268 Q240 240 280 252 Q340 270 380 232 Q410 205 450 215"/>
<path class="a" d="M450 215 V160"/><path class="a" d="M450 160 L490 172 L450 185"/>
<circle class="fa" cx="160" cy="268" r="9"/>
'''),
    # a game controller and a pulse line
    "steampulse": ("apps", '''
<path class="i" d="M225 150 H375 Q430 150 440 205 Q448 250 415 252 Q395 253 380 228 H220 Q205 253 185 252 Q152 250 160 205 Q170 150 225 150 Z"/>
<path class="i" d="M230 180 V215 M212 197 H248"/><circle class="f" cx="365" cy="185" r="8"/><circle class="f" cx="390" cy="208" r="8"/>
<path class="a" d="M130 95 H230 L250 60 L275 125 L298 75 L315 95 H470"/>
'''),
}

OUT.mkdir(parents=True, exist_ok=True)
for slug, (cat, body) in COVERS.items():
    (OUT / f"{slug}.svg").write_text(svg(cat, body), encoding="utf-8")
print("OK :", len(COVERS), "couvertures dans", OUT)

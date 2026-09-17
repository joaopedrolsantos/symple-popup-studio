#!/usr/bin/env python3
"""PPC strain-matched popups: one board with all four brands. Product images are each site's own PDP image."""
import html, re, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "deliverable" / "popups"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
STR = (ROOT / "design" / "strains").as_uri()
src = (ROOT / "deliverable" / "build_partner_popups.py").read_text()
CSS = src[src.index("CSS = f'''") + 10: src.index("'''\n\n\ndef render")].replace("{{", "{").replace("}}", "}")

def esc(s): return html.escape(s, quote=True)

SECTIONS = [
    ("Seed Supreme", "b-ss", "utm_content on the ad group's final URL suffix, e.g. utm_content=northern-lights. Strain terms are 77% of SS search spend ($4,818 in 90 days); these four are the top spenders.",
     [("ss-northern-lights", "Northern Lights", "Northern Lights Feminized", "$613 · 186 clicks · 8 conversions"),
      ("ss-permanent-marker", "Permanent Marker", "Permanent Marker Seeds", "$494 · 149 clicks · 16 conversions"),
      ("ss-purple-haze", "Purple Haze", "Purple Haze Feminized", "$327 · 109 clicks · 5.2 conversions"),
      ("ss-wedding-cake", "Wedding Cake", "Wedding Cake Feminized", "$262 · 86 clicks · 3 conversions")],
     lambda n: (f"Looking for {n}?", f"{n} is in stock. 4 free Purple Kush seeds go on top.", "Guaranteed germination. Pick your pack, the free seeds land in the cart.", "Claim my 4 seeds", "GROWAGAIN")),
    ("Homegrown Cannabis Co", "b-hg", "Today 86% of HMGRN strain spend lands on a generic shell (homegrownco.store/seeds). The ad group points at the strain page; the popup names it.",
     [("hg-northern-lights", "Northern Lights", "Northern Lights Feminized", "$73 · top HMGRN strain term"),
      ("hg-big-bud", "Big Bud", "Big Bud Feminized", "$66 · 0 conversions on the shell"),
      ("hg-wedding-cake", "Wedding Cake", "Wedding Cake Feminized", "$39")],
     lambda n: (f"Searching for {n}?", f"{n}, plus a free 4-pack of Purple Haze Fem", "Grown in the USA. We replace any seed that doesn't pop.", "Send my code", "HMG4PH")),
    ("ILGM", "b-il", "ILGM paid is thin (17 conversions in 90 days) and 17% of strain spend reaches the wrong strain page. Forms only; no flow edits.",
     [("il-maui-wowie", "Maui Wowie", "Maui Wowie Seeds", "$143 · 45 clicks · 7 conversions (most of ILGM's paid conversions)"),
      ("il-white-rhino", "White Rhino", "White Rhino Seeds", "$76 · 0 conversions"),
      ("il-purple-haze", "Purple Haze", "Purple Haze Feminized", "$52"),
      ("il-blue-dream", "Blue Dream Auto", "Blue Dream Autoflower", "top seller; PPC lander today shows GARDEN20")],
     lambda n: (f"Searching for {n}?", f"{n}, plus 5 free Granddaddy Purple Auto seeds", "Guaranteed germination. Free US shipping over $50.", "Claim my 5 seeds", "GDP5PACK")),
    ("United Strains of America", "b-us", "USOA paid search is paused (0 tracked conversions on age-gate shells). When it restarts, terms are category-led, not strain-led, so the popup matches the category.",
     [("us-flower", "THCa flower", "Sour Diesel THCa Flower", "\"thca flower shop online\", \"hemp flower for sale\" · 30% of spend"),
      ("us-gummies", "Delta-9 gummies", "20 mg Sour Apple Delta-9 gummies", "\"delta 9 gummies\" · 48% of spend")],
     lambda n: (f"Searching for {n.lower()}?", f"Lab-tested {n.lower()}, plus 10% off your first order", "COA on every batch. Check your state before ordering.", "Get my 10%", "WELCOME10")),
]

cards_html = []
for brand, cls, note, strains, copyfn in SECTIONS:
    cards = []
    for key, name, product, fig in strains:
        line, h, s, cta, code = copyfn(name)
        ext = "png" if key == "il-blue-dream" else "img"
        pos = {"ss-permanent-marker": "15% 10%", "ss-wedding-cake": "15% 10%", "hg-wedding-cake": "15% 10%", "il-blue-dream": "center center"}.get(key, "center 25%")
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        cards.append(f'''<div class="card {cls}"><div class="pop"><div class="ph" style="background-image:url({STR}/{key}.{ext});background-size:cover;background-position:{pos};background-color:#f4f4f2"></div>
<div class="in"><div class="tile none" style="border-style:solid;border-color:#e6e6e6;color:#444;font-size:11px;padding:4px">{esc(product)}<br><span style="color:#999">site product image</span></div>
<div class="line">{esc(line)}</div><div class="h">{esc(h)}</div><div class="s">{esc(s)}</div><div class="field">Email address</div><div class="btn">{esc(cta)}</div><div class="decl">No thanks</div></div></div>
<div class="cap"><b>Trigger:</b> URL contains utm_content={slug} (set on that ad group's final URL suffix)<br><b>Lands on:</b> the {esc(product)} product page<br><b>Offer:</b> {code}<br><span class="st new">Paid search, 90 days: {esc(fig)}</span></div></div>''')
    cards_html.append(f'<h2 style="font-family:Archivo,sans-serif;font-size:20px;margin:26px 0 4px">{esc(brand)}</h2><p class="sub">{esc(note)}</p><div class="grid">{"".join(cards)}</div>')

page = CSS + f'''<h1>Paid search: the popup names the strain they searched for</h1>
<p class="sub">Google does not pass the search query to the page, and a Klaviyo form cannot print a URL value into its text. So each strain gets its own popup, triggered by the ad group's utm_content, and the landing page is that strain's product page. The product image is the site's own PDP image, so no cultivation claims are introduced.</p>
<div class="stamp">Drafts for review, 16 Sep 2026. Not built in Klaviyo. Figures are Google Ads disclosed search terms, 16 Jun to 13 Sep 2026.</div>
{"".join(cards_html)}
<div class="legal"><b>How it works in the build.</b> 1. Each strain ad group gets a final URL suffix: utm_source=google&amp;utm_medium=cpc&amp;utm_campaign={{campaignid}}&amp;utm_content=&lt;strain-slug&gt;&amp;utm_term={{keyword}}. The {{keyword}} ValueTrack fills utm_term with the matched keyword for reporting; the popup keys on utm_content, which we control. 2. One Klaviyo form per strain in the top ten by spend (SS: about 35% of strain spend sits in the top four terms alone), each with a URL rule *utm_content=&lt;slug&gt;* and the strain's PDP image. 3. A generic strain popup with the rule *utm_content=strain-other* covers every other strain ad group. 4. On the product page itself the popup can be suppressed in favour of the PDP alert block, which already knows the product. 5. All of them write offer_shown, acq_intent = strain and acq_strain = &lt;slug&gt; to the profile, so Email 1 in the strain branch opens with the same strain. Google's brand is never shown; the search intent is expressed in the words.</div>'''
hp = OUT / "ppc-strain-popups.html"; hp.write_text(page)
png = OUT / "ppc-strain-popups.png"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1300,4400", "--virtual-time-budget=8000", f"--screenshot={png}", hp.as_uri()], check=True, capture_output=True, timeout=120)
from PIL import Image
im = Image.open(png).convert("RGB"); px = im.load(); bg = px[5, im.height - 5]; last = im.height - 1
while last > 0 and all(px[x, last] == bg for x in range(0, im.width, 25)): last -= 1
im.crop((0, 0, im.width, last + 40)).save(png); print(png, last + 40)

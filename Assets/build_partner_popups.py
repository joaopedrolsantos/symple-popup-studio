#!/usr/bin/env python3
"""Co-branded Klaviyo popup drafts per traffic source, one board per brand.
Output: deliverable/popups/<brand>-partner-popups.png and design/partner-popups-spec.md"""
import html
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "deliverable" / "popups"
OUT.mkdir(exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WEB = (ROOT / "design" / "web").as_uri()
PART = (ROOT / "design" / "partners").as_uri()

# partner logos: file, tile background, logo width in the tile
LOGO = {
    "leafly": ("leafly.png", "#ffffff", 96),
    "reddit": ("reddit.png", "#ffffff", 44),
    "growweedeasy": ("growweedeasy.png", "#ffffff", 120),
    "thcfarmer": ("thcfarmer.png", "#ffffff", 44),
    "heyabby": ("heyabby.png", "#ffffff", 110),
    "cannigma": ("cannigma.png", "#ffffff", 104),
    "almanac": ("almanac.svg", "#ffffff", 110),
    "420magazine": ("420magazine.png", "#ffffff", 110),
    "comparethestrain": ("comparethestrain.svg", "#ffffff", 110),
    "cannabissensei": ("cannabissensei.png", "#ffffff", 110),
    "ilgm": ("../web/ilgm-logo.svg", "#ffffff", 90),
    "seedsupreme": ("../web/ss-logo.png", "#ffffff", 100),
    "homegrown": ("../web/hmgrn-logo.svg", "#ffffff", 110),
}

BRANDS = {
    "seed-supreme": dict(
        name="Seed Supreme", cls="b-ss", photo="ss-strain-counter.jpg", logo="ss-logo.png",
        style="Existing entrance popup style (XrkCZ9): white card, orange button, heavy display face, photo panel. Three-step form stays (email, SMS, grow questions); only step one is shown.",
        cards=[
            dict(p="reddit", line="You found us on Reddit", h="The BOGO you clicked is below. Get the next one first.", s="Buy one pack, get one free on this week's strains. Free seeds still stack on top.", cta="Send me BOGO alerts", trig="URL contains a_aid=moso-reddit (PAP, MosoEcom)", offer="Current BOGO (no code needed); GROWAGAIN if no BOGO is live", status="New. Reddit is the largest new-customer source (3,487 orders). Reddit is not a commercial partner, so no \"official partner\" wording."),
            dict(p="leafly", line="Official partner of Leafly", h="4 free Purple Kush seeds with your first order", s="Feminized, from Happy Valley. If they don't pop in 120 days, we replace them.", cta="Claim my 4 seeds", trig="URL contains a_aid=leafly or utm_source=leafly", offer="GROWAGAIN (or LEAFLY20 if the Leafly agreement specifies a code; confirm)", status="New. Leafly editorial links reach strain pages; the popup is suppressed there and the PDP alert shows instead."),
            dict(p="growweedeasy", line="Recommended by GrowWeedEasy", h="Welcome, GrowWeedEasy grower. Your free seeds are on us.", s="Use GROWFREE on your first order. Best-retaining partner we have: these growers come back.", cta="Claim GROWFREE", trig="URL contains a_aid=<Kelly O'Neal PAP id> or referrer forum.growweedeasy.com", offer="GROWFREE (existing partner code)", status="New. 1,331 orders; 23.5% repeat at 180 days."),
            dict(p="thcfarmer", line="Hey THCFarmer", h="15% off your first order with code THC15", s="Guaranteed germination on every seed. Seeds from 20 breeders, shipped from the US.", cta="Use THC15", trig="URL contains utm_campaign=bg12 / strains15 / 15offo (existing banner rules)", offer="THC15 (existing banner code)", status="Replaces the three THC Farmer banners that open the non-existent form XbTe7W."),
            dict(p="heyabby", line="Growing in an abby?", h="Seeds picked for the box, plus a first-order code", s="Autoflowers and compact photoperiods that suit the grow box. Use ABBYSUPREME.", cta="Show me box-friendly strains", trig="URL contains a_aid=<Hamlet Chen PAP id> or landing path /hey-abby", offer="ABBYSUPREME (existing partner code)", status="New. 654 orders. Copy should not claim fit beyond what the PDP height figures support."),
            dict(p="cannigma", line="Cannigma reader?", h="4 free Purple Kush seeds with your first order", s="You've read the guide. Here's the seed bank behind it, with a germination guarantee.", cta="Claim my 4 seeds", trig="URL contains a_aid=<Cannigma PAP id> (Nick P)", offer="GROWAGAIN (replaces the LETSGROW clone in the Cannigma welcome)", status="New on-site; the Cannigma-side popup already exists."),
            dict(p=None, line="Searching for a strain?", h="4 free Purple Kush seeds with your first order", s="Whatever you searched for, the free seeds go on top. Guaranteed germination.", cta="Claim my 4 seeds", trig="URL contains gclid= or a_aid=google-ads; not on product pages (PDP alert shows there)", offer="GROWAGAIN", status="Paid search has no partner logo (Google's and Meta's brands are not used as co-branding tiles). Replaces the PPC entrance form whose list has no flow."),
            dict(p="i49", line="The new home of i49 Genetics", h="Welcome, i49 grower. 15% off with i4915.", s="Same genetics, new counter.", cta="Use i4915", trig="URL contains utm_source=i49 (existing)", offer="i4915 (existing)", status="Exists (XwfCLB, 34.6% submit rate). Keep; restyle only."),
        ],
    ),
    "homegrown": dict(
        name="Homegrown Cannabis Co", cls="b-hg", photo="hmgrn-first-tent.jpg", logo="hmgrn-logo.svg",
        style="Existing popup style (WimVWV): white card, green pill button, wide caps display. The confirmshaming decline is replaced. Success buttons point to homegrowncannabis.com.",
        cards=[
            dict(p="almanac", line="Hey Almanac reader", h="Ready to grow at home? A free 4-pack of Purple Haze Fem with your first order", s="Tell us where you'll grow and we'll send the guides that fit.", cta="Send my code", trig="URL contains a_aid=almanac (existing)", offer="HMG4PH", status="Exists (T9i4zR, 21.4% submit). Add a close button; stop double-writing to two lists."),
            dict(p="leafly", line="Official partner of Leafly", h="A free 4-pack of Purple Haze Fem with your first order", s="Guaranteed germination. Real help when a leaf goes yellow.", cta="Send my code", trig="URL contains a_aid=leafly or utm_source=leafly", offer="HMG4PH", status="New. Leafly currently lands on /cheap-cannabis-seeds at 1.4 per 100."),
            dict(p="thcfarmer", line="Hey THCFarmer", h="Skip 2 weeks of veg: 4 free seeds on clone orders $120+", s="Or a free 4-pack of Purple Haze Fem on any first seed order.", cta="Show me clones", trig="URL contains utm_campaign=gen1 / 2wv / nogerm (existing banner rules)", offer="Existing THC Farmer clone offer; HMG4PH on seeds", status="Replaces the three banners that open the non-existent form XbTe7W."),
            dict(p="reddit", line="You found us on Reddit", h="A free 4-pack of Purple Haze Fem with your first order", s="Grown in the USA. We replace any seed that doesn't pop.", cta="Send my code", trig="URL contains a_aid=moso", offer="HMG4PH", status="New. Reddit lands on the homepage at 9.9 per 100; the popup adds the capture."),
            dict(p="cannigma", line="Cannigma reader?", h="First grow? Start with a free 4-pack of Purple Haze Fem", s="Kyle Kushman and the team walk you through week one.", cta="Send my code", trig="URL contains a_aid=<Cannigma PAP id>", offer="HMG4PH", status="New. Cannigma readers are learners; the success step links to the germination guide, not the BOGO page."),
            dict(p="420magazine", line="420 Magazine reader?", h="A free 4-pack of Purple Haze Fem with your first order", s="Guaranteed germination and a grow guide library of 600+ posts.", cta="Send my code", trig="URL contains a_aid=<420 Magazine PAP id> or referrer 420magazine.com", offer="HMG4PH", status="New. 139 sessions at 1.4 per 100 today; small, so a before-and-after read."),
            dict(p="meta", line="From our Facebook ad", h="The BOGO you tapped: buy one pack, get one free", s="Pick your strain and pack. Guaranteed germination on every eligible seed.", cta="Send me the BOGO strains", trig="URL contains a_aid=facebook or utm_campaign=TWYMKT_AGEGATE (existing rule)", offer="The BOGO; META20 retired unless the ad promises 20%", status="Redesign of RTc3c8 (0 views, dead list). The ad lands on the homepage at 2.8 per 100; the popup restates the offer."),
            dict(p=None, line="Searching for seeds?", h="A free 4-pack of Purple Haze Fem with your first order", s="Feminized and autoflower seeds, grown in the USA.", cta="Send my code", trig="URL contains gclid= or a_aid=google-ads", offer="HMG4PH", status="No partner logo (paid search). Strain terms should reach strain pages first."),
        ],
    ),
    "ilgm": dict(
        name="ILGM", cls="b-il", photo="ilgm-germination.jpg", logo="ilgm-logo.svg",
        style="STFNVH spec: mint #DCFCE7 card, Boldonse caps headline, Figtree body, red #DB0B16 button, Bergman illustration. Forms only; no flow edits.",
        cards=[
            dict(p="leafly", line="Official partner of Leafly", h="5 free Granddaddy Purple Auto seeds with your first order", s="Guaranteed germination. 30 million seeds shipped.", cta="Claim my 5 seeds", trig="URL contains aff=<Leafly Affiliatly id> (a_aid after the PAP migration)", offer="GDP5PACK", status="New. Leafly referrals convert at 0.84% today."),
            dict(p="thcfarmer", line="Welcome, THCFarmer", h="Buy 10, get 10 free on premium seeds", s="Your THCFarmer deal is live. Guaranteed germination on every seed.", cta="Double my seeds", trig="URL contains utm_campaign=bgo / bgp / bgg (existing banner rules)", offer="Buy 10 Get 10 (existing THC Farmer deal)", status="Replaces the three THC Farmer banners (V3iReH, VPKabs, VgL7RR) with a capture step."),
            dict(p="comparethestrain", line="Comparing strains?", h="The strain you picked, plus 5 free GDP Auto seeds", s="We'll open the strain you compared. Guaranteed germination on every seed.", cta="Show me the strain", trig="URL contains aff=<comparethestrain id>; link deep-linked to the strain page", offer="GDP5PACK", status="New. 815 sessions land on an empty /search at 0.12% today."),
            dict(p="cannabissensei", line="Cannabis Sensei reader?", h="5 free Granddaddy Purple Auto seeds with your first order", s="Grow guides, a forum and a germination guarantee after the sale.", cta="Claim my 5 seeds", trig="URL contains aff=<Cannabis Sensei id> or referrer cannabissensei.com", offer="GDP5PACK", status="New. 767 sessions at 2.48%."),
            dict(p="ilgmforum", img="forum", line="Hey, forum grower", h="5 free Granddaddy Purple Auto seeds with your first order", s="Post the grow, we'll follow it. Guaranteed germination on every seed.", cta="Claim my 5 seeds", trig="URL contains ilgmforum.com (existing STFNVH rule, 15s delay, 5-day cookie)", offer="GDP5PACK (the arm 91% of forum visitors already see)", status="Restyle of STFNVH, the reference form. Its 3.64M reported views look like a counting artefact; check in the UI before reading its 0.01% rate."),
            dict(p="iloveblog", img="blog", line="Reading the blog?", h="Get the 72-hour germination checks, then 5 free GDP Auto seeds", s="The checks by email first, no code. The seeds when you're ready to start.", cta="Send me the checks", trig="URL contains ilovegrowingmarijuana.com (existing UL76TY rule)", offer="Content first; GDP5PACK in email 4 (the learner branch)", status="Replaces the UL76TY A/B/C test (20% off vs GDP vs guarantee education) with the education-first arm; the blog embeds for the Grow Bible are repointed to the list the flow watches."),
        ],
    ),
    "usoa": dict(
        name="United Strains of America", cls="b-us", photo="usoa-flag.jpg", logo="usoa-logo.svg",
        style="Existing partner popup style (Leafly, Rzcwv9): flag panel, Oswald caps, red button, \"official partner\" line. One parameter scheme: a_aid=<partner> for all.",
        cards=[
            dict(p="leafly", line="Official partner of Leafly", h="Welcome to United Strains of America", s="Lab-tested THCa, plus 20% off your first order.", cta="Claim my 20%", trig="URL contains a_aid=leafly (existing)", offer="LEAFLY20 (existing)", status="Exists (Rzcwv9). Reference for the others; the decline line typo is fixed."),
            dict(p="homegrown", line="Official partner of Homegrown Cannabis Co", h="Something to enjoy while your grow finishes", s="Lab-tested THCa flower, shipped discreetly. 20% off your first order.", cta="Claim my 20%", trig="URL contains a_aid=homegrown (was utm_source=homegrown)", offer="HOMEGROWNUSA20 (existing)", status="Exists (UwrRpL, 26% submit). Parameter standardised."),
            dict(p="seedsupreme", line="Official partner of Seed Supreme", h="Something to enjoy while your grow finishes", s="Lab-tested THCa flower, shipped discreetly. 20% off your first order.", cta="Claim my 20%", trig="URL contains a_aid=seedsupreme (was utm_source=seedsupreme; SS links use a_aid, which is why it had 1 view)", offer="SUPREME20 (existing)", status="Exists but never fires (S97Vyc). Parameter fix makes it live."),
            dict(p="ilgm", line="Official partner of ILGM", h="Something to enjoy while your grow finishes", s="Lab-tested THCa flower, shipped discreetly. 20% off your first order.", cta="Claim my 20%", trig="URL contains a_aid=ilgm", offer="ILGM20 (new code; confirm)", status="New. ILGM already sells the USOA range; /ilgm lander is 404 today."),
            dict(p="cannigma", line="Cannigma reader?", h="Edibles first: 20 mg Delta-9 gummies, 20% off", s="Lab-tested. Serving information on every product page.", cta="Claim my 20%", trig="URL contains a_aid=0c44e0cc (Cannigma PAP id)", offer="CANNIGMA20 (new; confirm)", status="New. The Cannigma popup sits on recipe pages, so this one leads with gummies, not flower."),
            dict(p="thcfarmer", line="Hey THCFarmer", h="Lab-tested THCa flower, 20% off your first order", s="Grown in the USA. COA on every batch.", cta="Claim my 20%", trig="URL contains a_aid=<THC Farmer PAP id>", offer="NEW20 (existing THC Farmer code)", status="New popup; THCFarmer lands on /thca-deals at 2.5 per 100 today."),
            dict(p="meta", line="From our Facebook ad", h="Your free Purple Punch pre-roll", s="Add anything to your cart and the pre-roll goes in free with code PURPLE.", cta="Claim the pre-roll", trig="URL contains a_aid=facebook or utm_source=meta on /free-purple-pre-roll", offer="PURPLE (existing)", status="New. Currently utm_source=meta is excluded from every popup; 0 of 105 leads ordered in 10 days."),
            dict(p="i49", line="Official partner of i49", h="Welcome to United Strains of America", s="Lab-tested THCa, plus 20% off your first order.", cta="Claim my 20%", trig="URL contains a_aid=i49 (was utm_source=i49)", offer="i4920 (existing)", status="Exists (VbbC7P, 37 views). Keep."),
        ],
    ),
}


def esc(s):
    return html.escape(s, quote=True)


CSS = f'''
<meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..900&family=Public+Sans:wght@400;600;700&family=JetBrains+Mono:wght@400;500&family=Boldonse&family=Figtree:wght@400;500;600;700&family=Oswald:wght@500;600;700&family=Montserrat:wght@400;500;600;700&display=swap">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#eef0ec;font-family:"Public Sans",sans-serif;color:#172019;width:1300px;padding:36px 40px 40px}}
h1{{font-family:"Archivo",sans-serif;font-variation-settings:"wdth" 116;font-weight:800;font-size:30px;margin:0 0 4px;letter-spacing:-.02em}}
.sub{{color:#5a665d;font-size:14px;margin:0 0 6px;max-width:1100px}}
.stamp{{font-family:"JetBrains Mono",monospace;font-size:11px;color:#8a938c;margin-bottom:22px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:26px 26px}}
.card{{background:#fff;border:1px solid #d6dcd3;border-radius:10px;overflow:hidden}}
.pop{{display:grid;grid-template-columns:200px 1fr;min-height:320px;background:#fff}}
.pop .ph{{background-size:cover;background-position:center}}
.pop .in{{padding:22px 22px 18px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.tile{{width:150px;height:64px;border-radius:6px;display:flex;align-items:center;justify-content:center;border:1px solid #e6e6e6;margin-bottom:8px;background:#fff}}
.tile img{{max-height:44px;max-width:120px;display:block}}
.tile.none{{border:1px dashed #ccc;color:#999;font-size:11px}}
.line{{font-size:12.5px;font-style:italic;color:#444;margin-bottom:8px}}
.h{{font-weight:800;font-size:20px;line-height:1.15;margin:0 0 8px;letter-spacing:-.01em}}
.s{{font-size:12.5px;color:#333;margin:0 0 12px;max-width:340px}}
.field{{width:100%;max-width:340px;border:1px solid #c9c9c9;border-radius:6px;padding:10px;font-size:13px;color:#888;text-align:left;margin-bottom:8px;background:#fff}}
.btn{{width:100%;max-width:340px;padding:12px;border-radius:6px;color:#fff;font-weight:700;font-size:14px}}
.decl{{font-size:11.5px;color:#777;margin-top:8px}}
.cap{{border-top:1px solid #e3e7e1;padding:9px 12px 10px;font-size:11.5px;color:#3a463d;line-height:1.45;background:#fbfcfa}}
.cap b{{color:#172019}}
.cap .st{{display:inline-block;margin-top:4px;padding:1px 7px;border-radius:999px;font-size:10.5px;font-weight:600;background:#eaeee6;color:#2f6b47}}
.cap .st.new{{background:#fbf1e6;color:#b5651d}}
/* Seed Supreme */
.b-ss .h{{font-family:"Archivo",sans-serif;font-variation-settings:"wdth" 112;color:#231a16}}
.b-ss .btn{{background:#ff5c00}}
/* Homegrown */
.b-hg .h{{font-family:"Archivo",sans-serif;font-variation-settings:"wdth" 122;font-weight:900;text-transform:uppercase;font-size:18px;color:#181b1b}}
.b-hg .btn{{background:#05c87b;color:#181b1b;border-radius:999px}}
/* ILGM */
.b-il .pop{{background:#DCFCE7}}
.b-il .in{{font-family:"Figtree",sans-serif;padding-top:20px}}
.b-il .line{{margin-bottom:10px}}
.b-il .s{{line-height:1.5;margin-bottom:14px}}
.b-il .h{{font-family:"Boldonse",sans-serif;font-weight:400;text-transform:uppercase;font-size:14px;line-height:1.5;letter-spacing:.05em;color:#111;margin:2px 0 10px}}
.b-il .btn{{background:#DB0B16;font-family:"Figtree",sans-serif}}
.b-il .field{{border-color:#3C3C3C}}
.b-il .tile{{border-color:#c5e6cf}}
/* USOA */
.b-us .in{{font-family:"Montserrat",sans-serif}}
.b-us .h{{font-family:"Oswald",sans-serif;font-weight:600;text-transform:uppercase;font-size:20px;letter-spacing:.01em;color:#111}}
.b-us .btn{{background:#f54d4d;border-radius:4px;font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.05em}}
.b-us .decl{{text-decoration:underline}}
.legal{{margin-top:22px;font-size:11.5px;color:#5a665d;background:#fff;border:1px solid #d6dcd3;border-radius:8px;padding:10px 14px}}
</style>
'''


def render(key, b):
    cards = []
    for c in b["cards"]:
        p = c["p"]
        if p in LOGO:
            f, bg, w = LOGO[p]
            src = f"{PART}/{f}"
            tile = f'<div class="tile" style="background:{bg}"><img src="{src}" alt="{p}" style="max-width:{w}px"></div>'
        elif p in ("ilgmforum", "iloveblog"):
            cap = "ilgmforum.com" if p == "ilgmforum" else "ilovegrowingmarijuana.com"
            icon = f'<img src="{WEB}/ilgm-logo.svg" style="height:22px">' if p == "ilgmforum" else f'<img src="{PART}/ilove-book.png" style="height:34px">'
            tile = f'<div class="tile" style="flex-direction:column;gap:3px">{icon}<span style="font-size:9.5px;color:#555;font-family:JetBrains Mono,monospace">{cap}</span></div>'
        elif p == "i49":
            tile = '<div class="tile" style="background:#111;color:#fff;font-family:Archivo,sans-serif;font-weight:800;font-size:22px">i49</div>'
        elif p == "meta":
            tile = '<div class="tile none">no logo<br>(our own ad)</div>'
        else:
            tile = '<div class="tile none">no partner logo<br>(paid search)</div>'
        imgkey = c.get("img") or (p if p else "search")
        cand = [ROOT / "design" / "popup-img" / f"{key}-{imgkey}.jpg", ROOT / "design" / "popup-img" / f"{key}-{imgkey}.png"]
        hit = next((x for x in cand if x.exists()), None)
        if hit:
            ph = f'<div class="ph" style="background-image:url({hit.as_uri()})"></div>'
        elif b["photo"] != "usoa-flag.jpg":
            ph = f'<div class="ph" style="background-image:url({WEB}/{b["photo"]})"></div>'
        else:
            ph = '<div class="ph" style="background:linear-gradient(180deg,#1f3a63 0 45%,#b22234 45% 55%,#fff 55% 65%,#b22234 65% 75%,#fff 75% 85%,#b22234 85%)"></div>'
        status_cls = "new" if c["status"].startswith(("New", "Replaces", "Redesign", "Repoint")) else ""
        cards.append(f'''<div class="card {b["cls"]}">
<div class="pop">{ph}<div class="in">{tile}<div class="line">{esc(c["line"])}</div><div class="h">{esc(c["h"])}</div><div class="s">{esc(c["s"])}</div><div class="field">Email address</div><div class="btn">{esc(c["cta"])}</div><div class="decl">No thanks</div></div></div>
<div class="cap"><b>Trigger:</b> {esc(c["trig"])}<br><b>Offer:</b> {esc(c["offer"])}<br><span class="st {status_cls}">{esc(c["status"])}</span></div>
</div>''')
    page = CSS + f'''<h1>{esc(b["name"])}: co-branded popups by traffic source</h1>
<p class="sub">{esc(b["style"])}</p>
<div class="stamp">Drafts for review, 15 Sep 2026. Not built in Klaviyo. Partner logos are used for internal review only; each partner's permission to display its logo must be confirmed before deployment.</div>
<div class="grid">{"".join(cards)}</div>
<div class="legal">Every popup writes the same properties at submit: acq_partner, offer_shown (the code on this popup), acq_intent, and the grow or category answers on later steps. One first-order code per popup; the welcome flow's Email 1 repeats it. Where a trigger says "PAP id", Riley B fills in the affiliate's a_aid value from the PAP account list; Affiliatly ids (aff=) apply on ILGM until the PAP migration.</div>'''
    hp = OUT / f"{key}-partner-popups.html"
    hp.write_text(page)
    png = OUT / f"{key}-partner-popups.png"
    n = len(b["cards"])
    H = 240 + ((n + 1) // 2) * 470 + 80
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size=1300,{H}", "--virtual-time-budget=8000", f"--screenshot={png}", hp.as_uri()], check=True, capture_output=True, timeout=120)
    from PIL import Image
    im = Image.open(png).convert("RGB")
    px = im.load()
    bg = px[5, im.height - 5]
    last = im.height - 1
    while last > 0 and all(px[x, last] == bg for x in range(0, im.width, 25)):
        last -= 1
    im.crop((0, 0, im.width, min(im.height, last + 40))).save(png)
    print(png, im.width, last + 40)


spec = ["# Co-branded popup specification by traffic source\n", "Drafts rendered in `deliverable/popups/`. Each row is one Klaviyo form. Partner logo use needs the partner's permission before deployment.\n"]
for key, b in BRANDS.items():
    render(key, b)
    spec.append(f"\n## {b['name']}\n\n{b['style']}\n\n| Source | Trigger rule | Line | Headline | Offer / code | Status |\n|---|---|---|---|---|---|")
    for c in b["cards"]:
        spec.append(f"| {c['p'] or 'paid search'} | {c['trig']} | {c['line']} | {c['h']} | {c['offer']} | {c['status']} |")
(ROOT / "design" / "partner-popups-spec.md").write_text("\n".join(spec) + "\n")
print("spec written")

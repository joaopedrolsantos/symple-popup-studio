# Campaign composition — effects, overlays and layout

How the banner and email campaigns are actually built, read off the Figma file `Banners - E-mails - CSUP (Only new ID)` — 30 campaigns, May–September 2026. These are the moves that make a Seed Supreme campaign look like Seed Supreme. Follow them; they are consistent enough across 30 campaigns to count as house style.

## The signature move: the triple-stack glow

Never place a strain image as a single flat layer. Stack the **same** image two or three times:

1. **A heavily blurred copy underneath** — `LAYER_BLUR` between 48 and 101 — which acts as a coloured glow bleeding out from behind the subject. This is what lights the composition; there is rarely a real light source anywhere else.
2. **The sharp copy on top**, at full opacity, carrying the detail.
3. **Often a third copy** with a small `LAYER_BLUR` of 3–6 sitting between them, softening the silhouette edge so the cutout does not look pasted.

Offset the copies by a few degrees rather than stacking them square — the file uses pairs like `9°` / `173°`, `-5°` / `-175°`, `-8°` / `-172°`. The near-180° partner is a mirrored duplicate, not a second render.

Worked examples in the file: `do-si-dos-plant` on Strain Spotlight (blur 6 + blur 101 + sharp), `Apricot auto` on Fast Finish BOGO (blur 4 + blur 56 + sharp), `granddaddy-purple-autoflower-macro-close` on August Strain of the Month (blur 78 behind, `INNER_SHADOW` 4 on the sharp copy).

Blur radius scales with canvas: use the low end (3–8) inside a 600px email card, the high end (60–101) on a 2800px desktop banner. Across the file there are 1,083 `LAYER_BLUR` instances — the median is small (5–22) because most are edge-softeners; the large ones are always the glow layer.

## Blend modes: Linear Dodge is the house mode

`LINEAR_DODGE` (Add) accounts for 662 of the roughly 740 non-normal blends in the file. Everything that adds light — glows, leaks, smoke, dust, lens flare, light rays — is Linear Dodge at a reduced opacity. Reach for it first.

The rest of the vocabulary, used deliberately and sparingly:

- `MULTIPLY` (44 uses) — grain and paper texture only, to darken and dirty.
- `LINEAR_BURN` (15) — a darkening wash, used on small badge and label crops.
- `SCREEN` (12) and `LIGHTEN` (4) — occasional alternatives to Linear Dodge where Add blows out.
- `OVERLAY` (2) — effectively unused. Do not introduce it as a habit.

## The texture stack

Every campaign layers the same small set of overlay plates over the artwork. Use these exact settings — they are consistent across all 30 campaigns, and they are what makes a flat cutout sit in a scene:

| Overlay | Blend | Opacity | Notes |
|---|---|---|---|
| Light leak (`b7bb87c3-…`) | Linear Dodge | 9 / 16 / 18 / 24 / 28 / 32 / 48 / 64% | 285 placements — the most-used element in the whole file. One or two per composition, often mirrored at ±180°. |
| `Texturelabs_Film_185L` | Linear Dodge | 24 / 32 / 38 / 48% | Film grain. Usually rotated 180° or −90°. |
| `Texturelabs_LensFX_145L` | Linear Dodge | 48% | Lens flare / veiling glare. Rotated −90° or −180°. |
| `Texturelabs_Paper_128L` | Linear Dodge | 16 / 32 / 48 / 64% | Paper fibre, for the warmer editorial campaigns. |
| `whitish-grain-wall-template` | **Multiply** | 100% | The one darkening plate. Always rotated −84°. |
| `white-smoke-cloud-…` | Linear Dodge | 88% | Ground smoke at the base of a hero subject. |
| `dynamic-golden-particle-…dust` | Linear Dodge | 50% + `LAYER_BLUR` 5 | Floating gold dust, hero frames. |
| `dramatic-light-rays-…dark-smoke` | Linear Dodge | 24 / 32 / 40% | God-rays behind a subject. |
| `falling-white-snow-snowflakes` | Lighten 40% / Linear Dodge 64% | — | Seasonal only (May the 4th, Cold Hardy). |

Order them subject-first: strain stack, then leak, then smoke or rays, then grain last so the grain sits over everything.

## Shadows and depth

- `INNER_SHADOW` (77 uses), radius 2–4, on the **sharp** copy of a strain cutout. This is what seats the subject against its own glow — it is not a drop shadow on the frame.
- `DROP_SHADOW` (59), radius 1–32, reserved for small floating elements: badges, price stickers, pack shots, the `image 56` headline plate.
- `NOISE` (96) as a node effect, on flat colour fields that would otherwise band.
- For device mockups use the system's existing `shadow-mockup`; for product cards use `web-shadow-card`. Do not invent new shadow values for campaign work.

## Canvas formats

The campaigns ship in a fixed set of sizes. Build to these exactly:

| Format | Size | Count in file |
|---|---|---|
| Home banner — mobile | 1000 × 500 | 31 |
| Category banner — desktop | 2800 × 389 | 29 |
| Home banner — desktop | 2800 × 600 | 27 |
| Category banner — mobile | 1000 × 556 | 27 |
| Email | 600 × N (N ≈ 2,600–8,750) | one per campaign |
| CSUP / social secondary | 900 × 600, 1200 × 628, 2998 × 2549, 300 × 640 | occasional |

A campaign is considered complete when it has the email plus all four banner sizes. Several campaigns also carry a `- v2` email and a `- last-chance` hero and CTA swap for the final send.

## Email structure

Emails are a single 600px column of stacked section frames, named `NN - <Campaign> - <section>`. The section grammar, in frequency order:

`hero` → `text-content` → `card-1…card-9` (or `product-card-1…4`) → `usps` / `benefits` → `cta` (sometimes `cta-1…3`)

Heroes are 840px tall; product cards are 664–772px; the closing CTA is ~640px. Number the frames so the export order is unambiguous — every campaign in the file does this, and it is why the emails assemble cleanly.

## Copy vocabulary

The offer language is tightly repeated. Reuse it rather than inventing new phrasing:

- **Offer**: "20% off", "25% off", "30% off", "BUY 1 / GET 1 FREE", "buy one / get one", "SITEWIDE"
- **Threshold**: "on $90+ orders", "on $200+ orders", "free seeds on $50+", "spend $200+"
- **Reassurance, always present**: "Auto-applied at checkout", "No code.", and the exclusions — "excl. breeders seeds", "excl. breeders and BOGO seeds"
- **Window**: a literal date range, e.g. "Sat 2 – Mon 4 May only."
- **CTA**: "Shop now", "Shop the Sale", "Grab the Deal", "Shop Best Sellers"
- **Strain metadata**, in this order: type then potency — "Sativa-dom hybrid", "Hybrid", "Indica", "up to 30% THC", "15-20% THC", "Up to 28% THC", and lineage where it earns the line, "Apricot clone x Ruderalis"

Set all of it in the product layer's type roles; keep potency claims factual and never medical, per the content rules in the brand book.

## Composition recipes worth reusing

- **Hero, single strain.** Subject centred-right on `surface-dark`, triple-stacked with a large glow, one light leak bleeding off the right edge, smoke at the base, grain over everything. Headline left, bottom-aligned to the subject's mass.
- **Flavour scatter.** Subject centre, then 4–8 garnish props (fruit, grapes, pine, mango, cheese) at 40–250px orbiting it, each with `LAYER_BLUR` 4 and a small rotation, some clipped by the frame edge. Used on Terp Explosion, Flavor Forward BOGOs, 710 THCa, Secret Stash.
- **Mirrored pair.** One strain, two copies at `0°` and `−180°`, one blurred, filling a wide 2800px banner from both edges toward a centred headline. Used across the Fast Finish BOGO and Strain Spotlight banners.
- **Product-card grid.** Eight `card-N` sections in the email, each a single strain cutout over a tinted panel with the light leak at 16% and a small `My project-4` badge crop. The cheapest campaign to assemble — swap the strain and the copy, keep everything else.
- **Seasonal overlay swap.** Keep the whole composition and change only the top plate: snow for winter campaigns, gold dust for 420, light rays for solstice. This is how the file gets 30 distinct-looking campaigns out of one system.

## What to avoid

The file is disciplined about this and new work should stay that way: no gradients as decoration (the only gradient is the brand CTA), no coloured drop shadows, no `OVERLAY` blending, no third icon system, and no emoji anywhere in campaign copy.

# Seed Supreme design system — imported into Popup Studio

Imported **2026-09-16** from the Symple Commerce *Seed Supreme Design System* published on
Claude Design: <https://claude.ai/artifact/PAKFJUoatoaUrUYUDmd8fW> (version `1789585075-f18a`).

This is a **curated subset**, not a mirror. The source system is 541 files and ~50 MB — it
carries the whole storefront component library (React bundle, 60+ UI components, website and
mobile kits, product photography). None of that is reachable from a Klaviyo popup. What came
across is everything a popup can actually use.

## What's here

| Path | What it is |
|---|---|
| `tokens.css` | Every token, compiled, with the `@font-face` rules. Paths inside are relative to this folder. |
| `tokens.json` | The same tokens as data, if something needs to read them. |
| `tokens-reference.md` | Every token in tables, by group, with values. The lookup table. |
| `BRAND-SYSTEM.md` | The brand book: surfaces, colour, type, buttons, imagery, what not to do. Read this before changing a Seed Supreme popup. |
| `campaign-composition.md` | How Seed Supreme campaign artwork is actually built — the triple-stack glow, the texture plates, the blend modes. Relevant to the popup's image panel. |
| `fonts/` | The six shipped PP Agrandir weights (real files, not a stand-in). |
| `logo/` | The three Seed Supreme lockups as SVG — horizontal dark, horizontal white, symbol white. |
| `components/` | Prop contract + guidelines for the four components a popup borrows from: `GradientButton`, `Tag`, `TextField`, `Logo`. |

Deliberately left behind: `components/bundle.js` (5 MB React), `bundle.css` (689 KB), the
storefront UI kits, product photography (8 MB JPEGs), device mockups, and the showcase slides.
Fetch them from the artifact if a need appears.

## Two layers — pick the right one

The system carries a **brand layer** (campaigns, decks, banners) and a **product layer** (the
storefront). They never mix. A popup is an **entry/campaign surface**, so it takes the brand
layer: `surface-dark`, `accent`, the gradient CTA, PP Agrandir headlines. It does *not* take
`web-*` product tokens (`web-action` `#fc5b00`, `web-page` `#fff8f6`).

That resolves the open question in `START-HERE.md`: the `#231a16` "email-style dark" it mentions
is `web-ink`, a **product-layer** token. The popup's `#1a1a1a` is `surface-dark`, and it is the
correct one. There is no variant to bring back.

## Token map — system → popup studio

The Seed Supreme block in `templates/popup-studio.html` (~line 125) was hand-built from the same
canvas, so most of it already matched the system exactly. Confirmed identical, unchanged:

| Popup token | System token | Value |
|---|---|---|
| `--surface` | `surface-dark` / `ss-eerie-black` | `#1a1a1a` |
| `--accent` | `accent` / `ss-tango-orange` | `#f47920` |
| `--card-radius`, `--cta-radius` | `radius-16` | `16px` |
| `--field-radius` | `radius-8` | `8px` |
| `--cta-bg` | `button-gradient` | `linear-gradient(110.521deg,#D1671B 14.07%,#422109 89.20%)` |
| `--cta-shadow` | `shadow-button` | `0 24px 32px -24px rgba(8,23,14,.88), 0 0 32px rgba(244,121,32,.16)` |
| `--cta-textshadow` | `shadow-text-glow` | `0 0 8px rgba(255,255,255,.24)` |
| `--cta-track` | `tracking-button` | `-0.04em` |
| `--cta-weight` | `weight-button` | `700` |
| `--field-border` | `border-on-dark` / `ss-white-24` | `rgba(255,255,255,.24)` |
| `--l3-alpha` | `text-on-dark-muted` | `.64` |
| `--l2-weight` | `weight-label` | `600` |
| `--l1-deal-weight` | `weight-headline` | `900` |
| `--l1-deal-track` | `tracking-headline` | `-0.01em` |
| `--font-body` | `body` family | Work Sans |
| light variant `--ink: 26 26 26` | `text-body` / `ss-eerie-black` | `#1a1a1a` |

## Where the popup diverged from the system

The six gaps found at import. **All six are now closed** — see *What was applied* at the end
of this file. Kept here because the reasoning matters if any of them is ever revisited.

1. **`--font-display` is Archivo, standing in for PP Agrandir Wide.** The system now ships the
   real font (`fonts/PPAgrandir-WideBlack.ttf`, weight 900). This is the biggest single fidelity
   gain available, and it carries a delivery question — see *Fonts* below.

2. **The qualifier line uses the display font.** The system has a separate `subheadline` role
   (`--font-subheadline`) for exactly this job — the line that sits above/below the headline —
   set uppercase at `weight-subheadline` 700, `tracking-subheadline` -0.01em. The popup sets
   `--l1-qual-font: var(--font-display)` at 700 instead.

3. **Headline case.** `BRAND-SYSTEM.md` states brand headlines and sub-headlines are UPPERCASE as
   a type-role rule. The popup sets `--l1-deal-case: none`. Changing this is a visual decision
   with a real cost — uppercase eats horizontal room and the "no orphan words" rule in
   `Assets/SKILL.md` gets harder to satisfy at 880px and 375px.

4. **Headline leading.** Popup is `1.18`; the system's `leading-tight` for headlines is `1`.

5. **The source chip.** `DESIGN.md` records it as `rgb(255 255 255 / .08)` fill with a
   `/.14` border. The system's `Tag` component, which is what that chip is, specifies
   `ss-black-24` fill with `ss-white-64` ink, 8px radius, uppercase Work Sans SemiBold, -4%
   tracking, 10/12px padding.

6. **The Seed Supreme lockup is a PNG crop.** The `logo-seedsupreme` asset is a 104×33 crop
   lifted from a review board. Note this appears on **USOA** popups, where Seed Supreme is the
   partner — a Seed Supreme popup shows the *partner's* logo, not its own, so this is a
   cross-brand fix rather than a Seed Supreme one. The `Logo` guidelines require a safe zone of
   ½ the symbol width on every side, and forbid the dark lockup on a dark surface.

A seventh, not a divergence but worth knowing: the system offers `ss-seashell` `#fff5ec` and
`ss-sand` `#ffe9c8` as brand-layer warm surfaces. The popup's light variant is flat `#ffffff`.
`surface-warm` is the more on-brand light option if that variant is ever used.

## Fonts

`tokens.css` declares `@font-face` with **relative paths** (`fonts/PPAgrandir-WideBlack.ttf`).
That works for any page served over HTTP next to this folder. It does **not** reliably work for
`templates/popup-studio.html` opened by double-click: Chrome treats each `file://` document as an
opaque origin and blocks the font fetch as a cross-origin request. Firefox allows it from the
same directory; Chrome does not.

So the studio needs the fonts **base64-embedded** as `data:` URIs, not linked. Cost: ~107 KB of
text per weight embedded.

Two things settled before wiring this in:

- **Which weights.** Wide Black 900 alone was embedded: the qualifier went to `subheadline`
  (Big Shoulders Display, a Google face), so no second PP Agrandir weight is rendered, and a
  second embed would add ~107 KB to every export for nothing.
- **Licensing.** PP Agrandir is a commercial Pangram Pangram typeface. Embedding it in the studio
  (an internal tool) is one thing; embedding it in an **exported popup that ships on a live
  Klaviyo form** is a webfont licence question, and Seed Supreme's licence needs checking before
  that happens. **Decision taken: embed in both.** The licence check is therefore outstanding and
  blocks deployment, not design — it is flagged in `START-HERE.md` and in the studio's brand notes.

## Substitutions carried over from the source system

Two are flagged in the source and travel with this import:

- **`subheadline` is a substitution.** The brand specifies TitlingGothicFB Comp Bold, which is not
  supplied and is not on Google Fonts. It currently resolves to **Big Shoulders Display**. Do not
  swap in a different substitute without checking this first.
- **Icons.** `Icon` loads Font Awesome 6 *Free* Solid from a CDN; the brand's true kit is Sharp
  Solid (Font Awesome Pro), not supplied. Not currently a popup concern — `Assets/SKILL.md`
  requires popup icons come from the studio's own SVG sprite — but it's why the two don't match.

## Provenance

Every file here is a byte-for-byte copy from the artifact. Nothing was regenerated,
approximated, or redrawn. To refresh, re-read the same paths from the artifact URL above; the
source-path mapping is:

```
project/tokens.css                                  -> tokens.css
project/tokens.json                                 -> tokens.json
project/api/tokens.md                               -> tokens-reference.md
project/README.md                                   -> BRAND-SYSTEM.md
project/campaign-composition.md                     -> campaign-composition.md
project/fonts/*.ttf                                 -> fonts/
project/components/assets/logo/*.svg                -> logo/
project/components/{GradientButton,Tag,TextField,Logo}/*  -> components/
project/components/src/components/core/{GradientButton,Tag}.jsx -> components/
```


---

# What was applied

Decisions taken **16 Sep 2026**: embed PP Agrandir in both the studio and its exports, and close
all six divergences. All six are done, in `templates/popup-studio.html`.

| # | Divergence | What shipped |
|---|---|---|
| 1 | Archivo stand-in | Real **PP Agrandir Wide 900**, base64-embedded inside the `popup-css` block so exports carry it. Archivo stays in the stack as the degrade path. |
| 2 | Qualifier used the display font | Now the `subheadline` role: **Big Shoulders Display** 700, uppercase, `tracking-subheadline`, `leading-ui`. Added to the Google Fonts request. |
| 3 | Headline case | **Uppercase**, per the brand book's type-role rule. |
| 4 | Headline leading | **`leading-tight` (1)**, down from 1.18. |
| 5 | Source chip | The system's **`Tag`, tone `accent`** — `ss-orange-16` fill, Tango Orange ink, radius-8, 10/12px padding, no border. |
| 6 | PNG logo crop | The real **vector lockup**, inlined as an SVG data URI. |

### Why `Tag` tone `accent` and not `on-dark`

`on-dark` is the component's default, but the brand book reserves `accent` for brand emphasis,
and the source line — the reason-you're-here hook — is exactly that. It also keeps the orange the
chip has always had. Both tones clear the contrast floor; `accent` measured **4.96:1** on the dark
card and **13.3:1** on the light one. On the light card the ink is `accent-deep` (Bronze `#422109`),
not Tango Orange, which only reaches 2.55:1 on a near-white fill — the system pairs `accent` with
`accent-deep` for this reason.

### Headline size: 29px desktop / 23px mobile

Uppercase on `leading-tight` freed both horizontal and vertical room, so the deal was resized to
use it — the deal being the largest thing on the card is a rule in `Assets/SKILL.md`. The size was
**measured, not chosen**: every approved Seed Supreme headline was rendered at 25/27/29/31/33px
across both breakpoints and both surfaces, checking line count, last-line word count and overflow.

- 31px left only 3px of clearance on the tightest card
- 33px pushed the deal to three lines
- **29px** holds every headline to two lines with 103px of clearance at 880px

Mobile was swept separately because the binding case is different: `ss-i49` is a one-line deal
whose last word is the offer code, so a wrap there would strand `I4915.` alone. 25px left 9px of
slack; **23px leaves 34px**, about a full word.

### Verified

All 12 Seed Supreme popups, both breakpoints (880px / 375px), both surfaces (dark / light):

- **0 orphan lines** — minimum last-line length is 2 words
- **0 horizontal overflow** — tightest clearance 103px desktop, 34px mobile
- **0 body overflow** — no card's content exceeds its frame
- Fonts confirmed loaded via `document.fonts.check()`: PP Agrandir Wide 900, Big Shoulders
  Display 700, Work Sans
- Deal (29px) is the largest type on the card — ahead of qualifier 17, CTA 15, source 15,
  proof 15, field 15, decline 13
- The exported `popup-css` block carries the embedded font

### Also fixed in passing

The i49 wordmark chip (`.tile.chip`) was `#111` on the `#1a1a1a` card — all but invisible. It now
takes the same white plate every real partner logo gets on a dark surface.

### Still open

- **The PP Agrandir webfont licence.** It is now embedded in every export. Pangram Pangram
  licences are per-use; confirm Seed Supreme's covers live Klaviyo forms before deploying
  anything built from this file. Flagged in `START-HERE.md` and in the studio's own brand notes.


---

# Revision, 16 Sep 2026 — where the brief overrides the system

A later round of client direction moved Seed Supreme off several system defaults.
These are **deliberate divergences**, not drift. Anyone reconciling the studio against
the design system should read this section before "fixing" them back.

| What the system says | What the popup now does | Why |
|---|---|---|
| `headline` is PP Agrandir Wide, upright | PP Agrandir Wide **Black Italic** | Client direction. Only the italic is embedded — the deal is the sole thing in this face, so shipping the upright too would add ~108 KB to every export for nothing. |
| The line above/below a headline is the `subheadline` role (Big Shoulders Display) | **Work Sans Bold**, uppercase | Client direction. The pairing is now italic display against upright body rather than two display faces. Big Shoulders is no longer requested from Google Fonts. |
| `tracking-subheadline` is -0.01em | **+0.06em** on the qualifier | Not a contradiction of intent: -0.01em was set for a display face at size. Work Sans at 15px uppercase closes up and stops reading at negative tracking. |
| `GradientButton` underlines its label | **No underline**, label 17px, height 52px | Client direction. The gradient, `shadow-button` and `shadow-text-glow` are unchanged. |
| `surface-dark` is `#1a1a1a` | **`#000000`** plus a low-opacity orange radial bloom bottom-right | Client direction. `ss-pure-black` is already a system token (`surface-darkest`); the bloom is new and uses `accent` at ≤22%. It pays off against the brand's own photography, which is shot on pure black seamless — panel and card now read as one surface. |
| The source chip is the `Tag` component | **No container.** The shared accent rule, as on the other three brands | Client direction. The `Tag` mapping recorded earlier in this file is superseded. |

## Partner logos

Real vector lockups replaced the low-resolution review-board crops. Sources are kept at
`Assets/logos/partners/`. Each has a colour variant and, where one was drawn, a `-white`
variant that the renderer selects on Seed Supreme's dark card only.

- **Reddit** — supplied viewBox padded the mark out to a 1.5 aspect, rendering it ~30%
  small. Cropped to `0 0 171 171`. White variant is a white circle with the face knocked
  out in the card colour.
- **Grow Weed Easy** — the supplied file is already a dark-surface asset: its typography
  is `#FEFEFE`. The dark variant ships as supplied; the **light** variant is the derived
  one, darkening only the type and leaving the green mark alone, per the brief.
- **Hey Abby** — the counter inside the monogram is an overpainted white circle, not a
  hole, so the white variant sets it to the card colour.
- **The Cannigma** — supplied as PNG, not SVG. Recoloured per-pixel with the alpha kept.
  If a vector ever arrives it should replace this.
- **THC Farmer** — colours untouched on both surfaces, by instruction. It is a coloured
  symbol rather than a wordmark. Worth knowing: its dark `#4A5142` frame path disappears
  against the black card, and the light-green polygons carry the shape alone.
- **i49** — was a text chip typeset in Archivo, not a logo at all. Now the real lockup,
  on both the Seed Supreme and USOA popups that use it.
- **Seed Supreme** — a white variant was added from `design-system/logo/` so the mark is
  safe if it ever appears as a partner on a dark card.

## Imagery

Seed Supreme's four PPC generic options are now real images rather than brief-only
placeholders, generated to the house style with the design system's own product
photography as reference so the plants and buds are not invented. Full-resolution
renders are at `Assets/images/seed-supreme/*-full.jpg`; the studio embeds 620px previews.
They are also registered in the studio's Seed Supreme image library, so any popup can
pick one.


---

# Revision 2, 16 Sep 2026

A second round of client direction. Additions to the divergence table above:

| What the system says | What the popup now does | Why |
|---|---|---|
| `shadow-text-glow` is a CTA-label effect | The **deal** carries `0 0 12.006px rgb(255 255 255 / .24)` and the **qualifiers** carry `0 0 19.651px rgb(244 121 32 / .24)` | Client-specified values, given exactly. Same family as the system's glow, applied to headline roles. |
| Qualifier ink is `text-on-dark-muted` | **Tango Orange** (`accent`), full opacity | Client direction. 7.65:1 on the black card, so the contrast floor holds even though the role went from muted to accent. |
| `radius-16` on the button, `radius-8` on the field | CTA radius is **bound to the field** (`var(--field-radius)`) | Client direction. Binding rather than hard-coding 8px means the two cannot drift apart if the field radius is ever retuned. |
| No texture in the brand layer | **Texturelabs_Paper_128L at 64%**, `screen` blend, rotated per popup | Not actually a divergence: `campaign-composition.md` lists this exact plate as part of the house texture stack (there at 16/32/48/64% on Linear Dodge). Linear Dodge has no CSS equivalent; `screen` is its nearest sibling and behaves the same on a black ground. |

## The Leafly clipping bug

Worth recording, because the cause was mine and not the asset's. The SVG minifier
rounded **every** decimal in the file to one place. Leafly carries
`transform="scale(0.26458333)"` (a 96dpi→mm Inkscape scale), which became `scale(0.3)` —
blowing the artwork about 13% past its own viewBox and clipping the right edge. It hit
Seed Supreme, ILGM and USOA, since all three use the Leafly mark.

The minifier now rounds only `d` and `points` — actual path geometry — and leaves
transforms, viewBox and dimensions untouched. Anything that re-minifies an SVG here must
keep that rule.

## Imagery, revised

The first generated set was replaced. The four PPC generic options are now:

- **Outdoor field** — regenerated outdoors at golden hour instead of on black seamless.
- **Packaging** — regenerated against the real Seed Supreme pouch artwork
  (`Assets/images/seed-supreme/seed-supreme-pouch.png`), so the zigzag sunburst and the
  crowned lion crest are the brand's own and not invented.
- **Seeds macro** — kept; it was already right.
- **Lifestyle** — regenerated outdoors, a grower inspecting a cola in a field.

Eight images supplied by the client from Figma were added to the Seed Supreme library as
selectable options. Previews embed at 480px (the panel renders at 320); full-resolution
copies live in `Assets/images/seed-supreme/`.

**On file size.** Every library image is base64-embedded, which is the existing
architecture and what keeps the studio a single double-clickable file. The studio is now
~3.3 MB. That approach does not scale indefinitely — if the library keeps growing, the
next step is hosted URLs for library images, which would change the "no internet" property
the tool currently has. Worth a decision before the library doubles again.


---

# Revision 3, 17 Sep 2026

Further client direction, and two bugs of my own.

**Bugs fixed.** The optical logo sizing introduced in revision 1 never actually applied: a
second `.tile img` rule sat later in the stylesheet and overrode both the height and the
width, so every mark rendered at the flat tile height with a 150px width cap. And the metric
itself was wrong — it equalised ink *mass* (weight) rather than apparent size. Both are
described in `DESIGN.md`.

**Divergences added to the table:**

| What the system says | What the popup now does | Why |
|---|---|---|
| Proof copy is one muted block at `text-on-dark-muted` | A marked run renders at full `text-on-dark` | Client direction. The muted remainder is what makes the emphasis legible; bolding the whole sentence would remove the signal. |
| `radius-16` on the CTA | Bound to `--field-radius` (8px) | Client direction, revision 2. Binding rather than hard-coding keeps button and field in step. |
| No rules or dividers in the brand layer — "separate content with `border-hairline` rules" | A 2px `accent` rule divides image from copy | Client direction. The system permits rules; this one is accent rather than hairline and sits on an edge rather than between text blocks. |

## File size

The studio is now ~5 MB: fifteen Seed Supreme images at 620px, the 1800px paper plate, the
embedded typeface and the partner lockups, all base64 in one file. It opens and runs fine, and
that single-file property is the whole point of the tool — marketing double-clicks it, with no
server and no install.

It is close to the practical ceiling. The next addition of comparable size is worth pausing on,
because there are only two ways forward and they are a real trade:

1. **Keep embedding.** The file grows toward 8-10 MB. Still opens, slower to load and to email,
   and every export carries whatever the popup uses.
2. **Host the library.** Library images move to URLs and the file drops back under 1 MB. This
   costs the "works with no internet" property the tool has today, and it needs somewhere to
   host them that everyone on the team can reach.

Not a decision to make silently in either direction.

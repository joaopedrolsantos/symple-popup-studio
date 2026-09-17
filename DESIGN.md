---
name: Popup Studio
description: A form-builder workbench that holds every source-matched Klaviyo popup for four cannabis brands, and the four-skin popup design system it exports.
colors:
  ui-canvas: "#eef0f3"
  ui-dot: "#d3d8df"
  ui-panel: "#ffffff"
  ui-sunken: "#f7f8fa"
  ui-line: "#e3e6eb"
  ui-line-strong: "#cfd5dd"
  ui-ink: "#14171c"
  ui-ink-2: "#454d59"
  ui-ink-3: "#687181"
  ui-placeholder: "#6a7183"
  ui-sel: "#3552e8"
  ui-sel-bg: "#edf0fe"
  ui-sel-line: "#c3cdfb"
  ui-ok: "#16703f"
  ui-ok-bg: "#e6f5ec"
  ui-warn: "#9a5200"
  ui-warn-bg: "#fff2dc"
  ui-bad: "#b42318"
  ui-bad-bg: "#fdecea"
  ss-accent: "#f47920"
  ss-surface-dark: "#000000"
  ss-surface-bloom: "radial-gradient(88% 74% at 104% 106%, rgb(244 121 32 / .22), rgb(244 121 32 / 0) 76%)"
  ss-surface: "#1a1a1a"
  ss-surface-light: "#ffffff"
  ss-ink: "rgb(255 255 255)"
  ss-ink-light: "rgb(26 26 26)"
  ss-field-bg: "rgb(255 255 255 / .06)"
  ss-field-border: "rgb(255 255 255 / .24)"
  # the Seed Supreme source chip was removed: the source line now uses the
  # shared 14x2px accent rule, like the other three brands.
  hmgrn-accent: "#05c87b"
  hmgrn-surface: "#ffffff"
  hmgrn-ink: "rgb(24 27 27)"
  hmgrn-cta-bg: "#deffb7"
  hmgrn-cta-fg: "#0d523d"
  hmgrn-cta-border: "rgb(227 255 212 / .62)"
  hmgrn-field-border: "#c9cccc"
  ilgm-accent: "#DB0B16"
  ilgm-surface: "#DCFCE7"
  ilgm-ink: "rgb(17 17 17)"
  ilgm-field-border: "#3C3C3C"
  usoa-accent: "#f54d4d"
  usoa-surface: "#ffffff"
  usoa-ink: "rgb(17 17 17)"
  usoa-field-border: "#c9c9c9"
  panel-placeholder: "#e9e6e1"
typography:
  deal:
    fontFamily: "var(--font-display)"
    fontSize: "22px–40px desktop / 18px–34px mobile (brand-set; Seed Supreme 29/23, italic)"
    fontWeight: 400
    lineHeight: "1.02–1.5 (brand-set)"
    letterSpacing: "-.02em–.05em (brand-set)"
  qualifier:
    fontFamily: "var(--l1-qual-font)"
    fontSize: "13px–19px desktop / 11px–17px mobile (brand-set; Seed Supreme 15/15, Work Sans Bold, uppercase)"
    fontWeight: 400
    lineHeight: "1.2–1.5 (brand-set)"
    letterSpacing: "-.005em–.05em (brand-set)"
  source:
    fontFamily: "var(--font-body)"
    fontSize: "15px–16px (brand-set)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "normal"
  proof:
    fontFamily: "var(--font-body)"
    fontSize: "14px–15px (brand-set)"
    fontWeight: 400
    lineHeight: "1.5–1.55 (brand-set)"
    letterSpacing: "normal"
  cta:
    fontFamily: "var(--cta-font)"
    fontSize: "15px–18px (brand-set)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-.04em–.06em (brand-set)"
  popup-field:
    fontFamily: "var(--font-body)"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "normal"
  decline:
    fontFamily: "var(--font-body)"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "normal"
  ui-body:
    fontFamily: "ui-sans-serif, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "normal"
  ui-title:
    fontFamily: "{typography.ui-body.fontFamily}"
    fontSize: "13px"
    fontWeight: 680
    lineHeight: 1.45
    letterSpacing: "normal"
  ui-label:
    fontFamily: "{typography.ui-body.fontFamily}"
    fontSize: "12px"
    fontWeight: 620
    lineHeight: 1.45
    letterSpacing: "normal"
  ui-meta:
    fontFamily: "{typography.ui-body.fontFamily}"
    fontSize: "11.5px"
    fontWeight: 650
    lineHeight: 1.35
    letterSpacing: "normal"
  ui-mono:
    fontFamily: "ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
rounded:
  ui-sm: "6px"
  ui-md: "8px"
  ui-lg: "12px"
  ui-xl: "14px"
  pill: "999px"
  popup-card: "12px"
  popup-card-lg: "16px"
  cta-square: "4px"
  cta-soft: "8px"
  cta-lg: "16px"
  cta-pill: "999px"
spacing:
  tile-source: "24px"
  tile-source-mobile: "18px"
  source-head: "10px"
  pre-deal: "4px"
  deal-post: "6px"
  head-proof: "14px"
  proof-form: "24px"
  proof-form-mobile: "20px"
  field-cta: "10px"
  cta-decline: "12px"
  pad-x: "40px"
  pad-x-mobile: "24px"
  pad-top: "34px"
  pad-bottom: "30px"
components:
  popup-card:
    backgroundColor: "{colors.hmgrn-surface}"
    textColor: "{colors.hmgrn-ink}"
    rounded: "{rounded.popup-card}"
    width: "760px"
    height: "475px"
  popup-card-ss:
    backgroundColor: "{colors.ss-surface}"
    textColor: "{colors.ss-ink}"
    rounded: "{rounded.popup-card-lg}"
    width: "880px"
    height: "560px"
  popup-card-ss-light:
    backgroundColor: "{colors.ss-surface-light}"
    textColor: "{colors.ss-ink-light}"
  popup-cta:
    backgroundColor: "{colors.ilgm-accent}"
    textColor: "#ffffff"
    typography: "{typography.cta}"
    rounded: "{rounded.cta-soft}"
    height: "52px"
    width: "100%"
  popup-cta-hmgrn:
    backgroundColor: "{colors.hmgrn-cta-bg}"
    textColor: "{colors.hmgrn-cta-fg}"
    typography: "{typography.cta}"
    rounded: "{rounded.cta-pill}"
    height: "52px"
    width: "100%"
  popup-cta-ss:
    textColor: "#ffffff"
    typography: "{typography.cta}"
    rounded: "{rounded.cta-lg}"
    height: "50px"
    width: "100%"
  popup-field:
    backgroundColor: "#ffffff"
    textColor: "{colors.hmgrn-ink}"
    typography: "{typography.popup-field}"
    rounded: "{rounded.cta-soft}"
    padding: "0 18px"
    height: "48px"
  popup-field-ss:
    backgroundColor: "{colors.ss-field-bg}"
    textColor: "{colors.ss-ink}"
    typography: "{typography.popup-field}"
    rounded: "{rounded.cta-soft}"
    padding: "0 18px"
    height: "48px"
  popup-product-tile:
    backgroundColor: "rgb(var(--ink) / .06) on dark, #ffffff on light"
    borderColor: "rgb(var(--ink) / .14)"
    textColor: "{colors.ss-ink}"
    rounded: "10px"
    padding: "8px 12px 8px 8px"
    note: "Built from the card's own ink so it inverts with the surface. It was a fixed 90%-white plate carrying rgb(var(--ink)) text, which put white type on near-white on the dark card."
  popup-decline:
    backgroundColor: "transparent"
    textColor: "{colors.hmgrn-ink}"
    typography: "{typography.decline}"
    padding: "4px 8px"
  button-default:
    backgroundColor: "{colors.ui-panel}"
    textColor: "{colors.ui-ink}"
    rounded: "{rounded.ui-md}"
    padding: "0 12px"
    height: "32px"
  button-primary:
    backgroundColor: "{colors.ui-ink}"
    textColor: "#ffffff"
    rounded: "{rounded.ui-md}"
    padding: "0 12px"
    height: "32px"
  button-primary-hover:
    backgroundColor: "#2a2f37"
    textColor: "#ffffff"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ui-ink-2}"
    rounded: "{rounded.ui-md}"
    padding: "0 12px"
    height: "32px"
  button-sm:
    backgroundColor: "{colors.ui-panel}"
    textColor: "{colors.ui-ink}"
    rounded: "{rounded.ui-sm}"
    padding: "0 8px"
    height: "26px"
  input:
    backgroundColor: "{colors.ui-panel}"
    textColor: "{colors.ui-ink}"
    typography: "{typography.ui-body}"
    rounded: "{rounded.ui-md}"
    padding: "7px 10px"
    height: "34px"
  input-readonly:
    backgroundColor: "{colors.ui-sunken}"
    textColor: "{colors.ui-ink}"
  segment-item:
    backgroundColor: "transparent"
    textColor: "{colors.ui-ink-2}"
    rounded: "7px"
    padding: "0 10px"
    height: "28px"
  segment-item-selected:
    backgroundColor: "{colors.ui-panel}"
    textColor: "{colors.ui-ink}"
  tag-ok:
    backgroundColor: "{colors.ui-ok-bg}"
    textColor: "{colors.ui-ok}"
    rounded: "{rounded.pill}"
    padding: "0 7px"
    height: "20px"
  tag-warn:
    backgroundColor: "{colors.ui-warn-bg}"
    textColor: "{colors.ui-warn}"
    rounded: "{rounded.pill}"
    padding: "0 7px"
    height: "20px"
  tag-bad:
    backgroundColor: "{colors.ui-bad-bg}"
    textColor: "{colors.ui-bad}"
    rounded: "{rounded.pill}"
    padding: "0 7px"
    height: "20px"
  qa-pill:
    backgroundColor: "{colors.ui-ok-bg}"
    textColor: "{colors.ui-ok}"
    rounded: "{rounded.pill}"
    padding: "0 10px"
    height: "30px"
  source-row:
    backgroundColor: "transparent"
    textColor: "{colors.ui-ink}"
    rounded: "10px"
    padding: "8px"
  source-row-current:
    backgroundColor: "{colors.ui-sel-bg}"
    textColor: "{colors.ui-ink}"
  panel-card:
    backgroundColor: "{colors.ui-panel}"
    textColor: "{colors.ui-ink}"
    rounded: "{rounded.ui-lg}"
    padding: "12px 14px"
---

# Design System: Popup Studio

## Overview

**Creative North Star: "The Quiet Workbench"**

Popup Studio is two systems in one file, and they are deliberately built to be told apart at a glance. The workbench is a cool, near-silent instrument panel: white panels, hairline dividers, near-black ink, a dotted grey stage. The popups sitting on that stage are loud, branded, full-colour objects. Every decision in the chrome is made so that the popup is the only thing in the frame with a voice. Marketing people, not developers, open this file; the chrome uses plain-English labels and never a code-editor idiom.

The chrome is a form-builder grammar the team already knows — brand tabs across a 56px top bar, a 288px source rail on the left, a scrolling canvas in the middle, a 340px properties panel on the right — and it refuses the thumbnail-grid template gallery outright. You do not shop for a popup; you select a traffic source and the exact popup appears at true size. Density is tight but never cramped: 32px controls, 13.5px UI text, 8px radii, colour reserved for state.

The popup system underneath is one layout and one type hierarchy with four brand skins. Every brand sets the *same* custom properties with its own values, so a layout change lands in all four brands at once and a brand change is a token edit, never a rule edit. That includes the frame itself: `--card-w`, `--card-radius` and `--card-shadow` are brand tokens, so Seed Supreme's 880×560 dark card and the other three brands' 760×475 light cards are one layout at two sizes, not two layouts. That block (`popup-css`) is what every export carries, so it is a shipping design system in its own right, and its rules are binding on anything built from an export.

**Key Characteristics:**
- Cool neutral chrome (`ui-canvas` through `ui-ink`) with exactly one interactive blue (`ui-sel`) reserved for selection and focus.
- Brand colour appears in the chrome only as a 10px brand dot; everywhere else it lives inside the popup.
- One popup layout, four token skins: brand CSS sets tokens (including card width, radius and shadow) and, where a brand's own material demands it, re-dresses a single element — never the layout.
- Deliberately unequal vertical rhythm inside the popup so elements group into deal / proof / ask.
- Status has three colours and always carries a word: green, amber, red never speak alone.
- True-size-first canvas; the caption never claims a size the canvas is not showing.

## Colors

A cool grey-blue workbench, an ink-only command colour, one blue for selection, a three-state status triad, and four brand palettes that exist only inside the popups.

### Primary
- **Instrument Blue** (`ui-sel`): the single interactive accent. It marks the selected source row (as a tinted `ui-sel-bg` fill with a `ui-sel-line` inset hairline), the focus ring on every field and control, the selected image thumbnail's 2px ring, the anchor word in the deal marker, and the caret in studio fields. It is never used for emphasis, decoration, or a button fill.
- **Command Ink** (`ui-ink`): the primary button and the active-tab underline are near-black, not blue. The workbench's "go" colour is ink; blue means "this is where you are".

### Secondary
- **Brand Accents**: Seed Supreme orange (`ss-accent`), Homegrown green (`hmgrn-accent`), ILGM red (`ilgm-accent`), USOA red (`usoa-accent`). The accent always marks the source line (the 14×2px rule, or Seed Supreme's chip text) and always carries the caret in the popup's email field. It fills the CTA on ILGM and USOA only — Seed Supreme's button is an orange-to-ember gradient and Homegrown's is the lime campaign pill, so on those two brands the accent identifies but does not sell. In the chrome each brand still appears only as a 10px dot on its tab, with an `inset 0 0 0 1px rgb(0 0 0 / .12)` edge so a light dot stays visible on white.
- **Brand Surfaces**: Seed Supreme is dark by default (`ss-surface`), with white as its named alternate (`ss-surface-light`); Homegrown and USOA are white; ILGM is the mint card (`ilgm-surface`). Any dark surface forces partner logos onto a white plate.
- **Homegrown Campaign Lime** (`hmgrn-cta-bg` under a top-right white sheen, ink `hmgrn-cta-fg` at 8.33:1): the CTA colour pair lifted from the Homegrown Cannabis Co design system's `CampaignButton` (tone `lime`, `knob` off — popups take no arrow knob). It is a button colour, not a brand accent: it never appears anywhere else on the card.

### Tertiary
- **Go Green** (`ui-ok` on `ui-ok-bg`): a QA check that passes, an offer code that already exists, the ready state of the QA pill.
- **Confirm Amber** (`ui-warn` on `ui-warn-bg`): anything that needs a human before build — a code marked "confirm", an orphan word, a placeholder image, copy that differs from the approved spec.
- **Blocking Red** (`ui-bad` on `ui-bad-bg`): an invalid field or a failed check that stops the build.

### Neutral
- **Stage Grey** (`ui-canvas`) with **Dot Grey** (`ui-dot`): the canvas, a 20px radial dot grid at 1px. This is the only textured surface in the product; it reads as "workspace, not page".
- **Panel White** (`ui-panel`): every chrome surface that holds controls — top bar, rail, inspector, handoff strip, menus, cards.
- **Sunken** (`ui-sunken`): inset wells — read-only fields, code blocks, the deal-marker tray, the scale badge, hovered menu rows.
- **Hairline** (`ui-line`) and **Edge** (`ui-line-strong`): every divider is 1px `ui-line`; every control stroke that must be found by eye is `ui-line-strong`.
- **Ink ramp** (`ui-ink` / `ui-ink-2` / `ui-ink-3`): titles and values / secondary body and labels / metadata, counts and captions.
- **Placeholder Ink** (`ui-placeholder`): studio placeholders only.
- **Panel Placeholder** (`panel-placeholder`): the popup image panel's base before an image loads.

### Named Rules
**The One Blue Rule.** `ui-sel` means selection or focus and nothing else. If a blue element is not telling you where you are or where your keyboard is, it is wrong.

**The Accent-Is-Not-Automatically-The-Button Rule.** The accent's guaranteed jobs are the source line and the field caret. The CTA's fill is its own token (`--cta-bg`), and two brands now set it to something the accent is not. When a brand ships a button treatment from its own design system, that treatment wins; do not "restore" the accent underneath it.

**The Brand-Stays-Inside Rule.** Brand colour never enters the chrome except as the 10px tab dot. The workbench has no brand; it holds four.

**The Legible Placeholder Rule.** Placeholder ink is a floor, not a taste. In the popup, `rgb(var(--ink) / .62)` is the lowest alpha that clears 4.5:1 on all four brand cards *and* the Seed Supreme dark card (measured 4.84–6.69:1); in the chrome, `ui-placeholder` is the equivalent at 4.88:1. Never lighten either.

**The Instruction-Outranks-Placeholder Rule.** A real instruction (`.hint`, `ui-ink-2`, 8.6:1) is always darker than a placeholder. Help text must never look fainter than the text it is helping with.

**The Word-With-The-Colour Rule.** Green, amber and red never carry meaning alone. Every status colour ships with a label or a sprite icon in the same tone.

## Typography

**Display Font (chrome):** none — the workbench has no display face. Its largest type is a 17px title.
**Body Font (chrome):** the platform UI stack (`ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, …`), because the chrome should look like the operating system the marketer is already in, not like a brand.
**Mono Font (chrome):** `ui-monospace, "SF Mono", Menlo, Consolas` — used *only* for machine values in the handoff strip (trigger rule, offer code, Klaviyo properties), so a value that must be pasted exactly is visually distinct from prose.

**Popup faces (per brand; Google Fonts except where noted):** Seed Supreme — **real PP Agrandir Wide Black Italic**, base64-embedded from the family the client supplied at `Assets/fonts/PP Agrandir/` rather than loaded from Google (Chrome blocks a relative font fetch from a `file://` page, so a linked file would silently fall back). The deal is the only thing set in this face, so only the italic ships. The qualifier is **Work Sans Bold, uppercase**, and body is Work Sans. Archivo remains in the stack as the degrade path only; Homegrown — Archivo 900 at 122% width (stand-in for DrukWide) over Helvetica; ILGM — Boldonse over Figtree; USOA — Oswald over Montserrat. Fallbacks are declared as heavy-to-heavy: Boldonse → Archivo → Arial Black, Oswald → Arial Narrow, Archivo → Helvetica Neue. Boldonse loads in its own Google Fonts request.

**Character:** the chrome is neutral to the point of self-effacement; the popups are brand-loud. The one place the chrome permits itself weight is the ink-black primary button and the 680-weight panel titles.

### Hierarchy (popup, all four brands)
- **L1 deal** (display face, brand weight, 22–40px desktop / 18–34px mobile, brand line-height, `text-wrap: balance`, measure 15–22ch): the offer. Full ink. The largest thing on the card.
- **L1 qualifier** (same display face, 13–19px desktop / 11–17px mobile, ink at 58–62%, measure 30ch): the approved words before and after the deal. Sits 4px above the deal or 6px below it.
- **L2 source line** (body face, *italic*, 15–16px, ink at 84–86%, measure 40ch, `text-wrap: pretty`): why this visitor arrived. Always preceded by a 14×2px accent rule.
- **L3 proof** (body face, regular, 14–15px, line-height 1.5–1.55, ink at 72–74%, measure 38ch, `text-wrap: pretty`): one sentence of guarantee or lab proof.
- **CTA** (brand CTA face, 17–18px, 600–800): the single button.
- **Decline** (body face, 13px, ink at 58%): "No thanks", centred under the button.

### Hierarchy (chrome)
- **Title** (680, 13–17px): panel section headings and the empty state.
- **Body** (400–560, 13.5px/1.45): the base.
- **Label** (620, 12px): field labels.
- **Meta** (650, 11.5px): group heads, handoff keys, menu section heads. `font-variant-numeric: tabular-nums` on every count and measurement.

### Named Rules
**The Comp-Minus-The-Control Rule.** The Seed Supreme canvas sets its whole headline at one size. The studio keeps the deal/qualifier split inside that look anyway (deal 25px/900, qualifier 15px at 60% ink), because a single-size headline leaves the deal marker — the one control a marketer uses to edit structure — with nothing visible to do. This is a knowing deviation from the comp, and it has an escape hatch: set `--l1-qual-size` equal to `--l1-deal-size` on the brand block and the card matches the comp exactly. Take the hatch only when the comp is being matched pixel-for-pixel for approval.

**The Deal-Is-Biggest Rule.** Nothing on the card — logo, button, source line, qualifier — may be larger or heavier than the deal. Headlines are split into qualifier / deal / qualifier by the `[square brackets]` in the approved copy; with no brackets, the whole headline is the deal.

**The Token-Not-The-Rule Rule.** Every brand difference is a custom property on the brand's `[data-brand]` block. Layout, measures and the hierarchy live in shared class rules and are never redeclared per brand. To change a brand, change the token; if you find yourself writing a per-brand layout rule, the system is being broken.

**The No-Orphan Rule.** Headlines use `text-wrap: balance`, source and proof use `text-wrap: pretty`, and the last two words of a line group are joined with a non-breaking space when they total 20 characters or fewer. Check at 760px and 375px. A one-word last line is a defect; fix it by moving the brackets or the non-breaking space, never by rewording approved copy.

**The Real-Load Rule.** Font presence is proved with `document.fonts.load()`, never `document.fonts.check()`, which returns true for faces it has never fetched.

## Layout

The workbench is a fixed three-column CSS grid inside `100vh`: a 56px top bar spanning the width, then a 288px source rail, a fluid canvas, and a 340px inspector. Only the rail list, the stage and the panel body scroll; the shell itself never does.

The canvas stacks centred frames (desktop 760px, mobile 375px) with a 28px gutter and a 24px gap down to the handoff strip, which is a four-column grid capped at 1180px. Frame captions sit above each frame in 12px meta type and state the true pixel width.

**The Honest Scale Rule.** The stage scales frames down only when it wins real room: below `FIT_FLOOR = 0.98` it applies a floor-rounded zoom (never below 45%); between 0.98 and 1 it leaves the cards at true size and lets the stage scroll, because a 1–2% squeeze is not worth misreporting. Whenever a scale is applied, a "shown at N%" badge is printed beside the px caption. **The caption may never claim a size the canvas is not showing.**

Responsive steps, in the order the build defines them: at 1540px the product subtitle drops; at 1280px the inspector narrows to 328px, the search shortcut hint hides and the device-toggle labels go screen-reader-only; at 1080px the inspector becomes a fixed right drawer that slides in over the canvas behind a toggle, and the grid collapses to rail + canvas; at 760px the whole shell becomes a single scrolling column — brand tabs become a four-up grid, the rail list is replaced by a select, the desktop frame is hidden entirely and only the mobile popup is previewed.

The popup's own responsive behaviour is **container-based, not viewport-based**: `.popwrap` establishes an inline-size container and every mobile value is applied at `@container popup (max-width: 520px)`. This is deliberate — the card must respond to the width Klaviyo gives it, not to the browser window, and it is what lets the studio show desktop and mobile side by side in one viewport.

Popup geometry is brand-set on top of one grid. The shared default is a 760px card, a 297px portrait image panel (5:8), a 475px minimum height and 40px/34px/30px text padding; Seed Supreme sets its own frame to 880×560 with a 320px panel and 44px/40px/40px padding, and tightens its internal rhythm to a near-even 14/14/14/18/10/8. Frame captions are measured from the rendered card (`offsetWidth`), not written into the markup, so the caption reads "880 px" for Seed Supreme and "760 px" for the rest without anyone maintaining a list. On mobile the panel becomes a 132px strip on top and padding drops to 24px. Spacing between elements is deliberately unequal (24 / 10 / 14 / 24 / 10 / 12 desktop) so the eye groups source+headline, then proof, then the ask. Field height is 48px, CTA height 52px.

## Elevation & Depth

The chrome is almost flat and gets its structure from hairlines and tonal layering, not shadow: panels are white on a grey stage, separated by 1px `ui-line`, with sunken wells in `ui-sunken`. Shadow appears in exactly three roles — floating layers (menu, drawer, toast), the one-pixel lift on a selected segment, and the popup itself, which is the only object in the product allowed to look like it is sitting *on* the canvas.

### Shadow Vocabulary
- **Floating layer** (`0 12px 32px -12px rgb(20 23 28 / .28), 0 2px 6px -2px rgb(20 23 28 / .12)`): the export menu, the mobile inspector drawer, the toast. Anything temporarily above the shell.
- **Popup lift, dark** (`0 32px 80px rgb(0 0 0 / .45), 0 0 0 1px rgb(255 255 255 / .06)`): the Seed Supreme card. Same two-part idea as below — a long soft drop plus a one-pixel ring — inverted for a dark card, where the ring is what separates `#1a1a1a` from the grey stage. Its light alternate keeps the geometry and drops to `.18` / `rgb(0 0 0 / .08)`.
- **Popup lift** (`0 18px 50px -18px rgb(0 0 0 / .35), 0 0 0 1px rgb(0 0 0 / .06)`): the default popup card, used by Homegrown, ILGM and USOA. The long, low-opacity drop reads as a modal over a page; the 6% ring is what gives a white card an edge against the light canvas, which the offset alone does not do. Both halves are load-bearing — do not strip the ring.
- **Selected segment** (`0 1px 2px rgb(20 23 28 / .12), 0 0 0 1px rgb(20 23 28 / .04)`): the pressed tab inside a segmented control, lifted off its track.
- **Inset hairline** (`inset 0 0 0 1px …`): the default way to draw an edge inside the chrome — avatars, thumbnails, focal preview, the scale badge, ghost tags.
- **CTA shadow** (`0 1px 0 rgb(0 0 0 / .08), 0 6px 14px -8px rgb(0 0 0 / .32)`): the default popup button. It is the one control in the system with a resting shadow, because it is the one thing being asked for. Brands may override it through `--cta-shadow`: Homegrown's campaign pill uses `0 16px 21px -16px rgb(8 23 14 / .35)` (the Figma 1x value scaled 52/92 to popup button height) and Seed Supreme uses `0 24px 32px -24px rgb(8 23 14 / .88), 0 0 32px rgb(244 121 32 / .16)`, where the second half is an accent bloom that only reads on the dark card.
- **Panel scrim** (`linear-gradient(180deg, rgb(244 121 32 / .14) 0%, rgb(26 26 26 / 0) 28%, rgb(26 26 26 / 0) 58%, rgb(26 26 26 / .94) 100%)` on `.panel::after`): Seed Supreme's dark card only. It is depth, not decoration — it ties the photo to the card's amber-over-ink material and lands the image into the surface at the bottom edge instead of stopping at a seam. It is suppressed on the light alternate.

### Named Rules
**The Depth-Belongs-To-The-Card Rule.** Shadow inside the popup is spent on exactly two things: the card's lift and the CTA's rest. Nothing else in the popup — tile, chip, field, panel — carries a drop shadow. Seed Supreme's scrim is a gradient, not a shadow, and does not count against this.

**The Hairline-First Rule.** Structure is drawn with 1px lines and tonal fills. Reach for a shadow only when an element genuinely floats above the shell.

**The Duplicated Guard Rule.** The `prefers-reduced-motion` guard exists twice on purpose: once in `studio-css` for the workbench, and again *inside* `popup-css`, because an export carries that block alone and would otherwise ship unguarded motion on `.cta`. Do not "de-duplicate" these.

## Shapes

One radius family, applied by size: 6px on small controls and chips, 8px as the default (buttons, fields, menu rows, wells), 10px on rail rows and product tiles, 12px on cards, menus and the popup itself, 14px on the empty state, and full pills (999px) on tags and the QA pill. The segmented control is a 9px track holding 7px buttons with a 2px inset.

Inside the popup, corner language is a brand token, and it now runs from the card down. Seed Supreme's card is 16px with a 16px CTA, an 8px field and an 8px source chip — one large radius for the frame and its ask, one small radius for the parts inside. ILGM softens to 8px, USOA stays nearly square at 4px, Homegrown goes fully pill on both its field and its button. The image panel is always portrait and is clipped by the card's own radius via `overflow: hidden` — the panel never carries its own corners, which is why a card radius change needs no panel change.

Icons are 16px (14px and 12px variants) stroked at 1.7 with round caps and joins, drawn from one inline SVG sprite of `#i-*` symbols and coloured by `currentColor`.

The missing-image state is a 135° repeating hatch (`#ebe8e2` / `#e4e0d9`, 12px bands) with the slot's brief written over it. The stripes are semantics, not decoration: they mean "an image is missing here". The same hatch at chrome greys backs empty thumbnails and the focal preview.

## Components

### Buttons (chrome)
- **Shape:** softly rounded (8px); small variant 6px.
- **Default:** white on a `ui-line-strong` stroke, 32px tall, 12px horizontal padding, weight 560 at 13px.
- **Primary:** ink fill (`ui-ink`) with white text, no border; hover lifts to `#2a2f37`. There is one primary per region.
- **Ghost:** transparent with `ui-ink-2` text; hover fills with the canvas grey.
- **Hover / Focus:** 150ms colour transitions only — no movement. Focus is the global 2px `ui-sel` outline at 2px offset.
- **Disabled:** 45% opacity, `not-allowed`.

### Segmented Control
The variant and device pickers. A grey `#e8ebef` track with a 2px inset holds 28px buttons; the selected one turns white and lifts on the selected-segment shadow. This 2px inset is a knowingly tight track — it is the control's whole idiom and is not a padding error to "fix".

### Tags and the QA Pill
Small pills (20px, 11px/600) in the status pairs: neutral grey for structural notes ("New", "Replaces"), green for confirmed, amber for confirm-before-build, red for blocking. The QA pill in the top bar is the same vocabulary at 30px and is the product's single summary of readiness; it collapses to a bare count at 760px.

### Cards / Containers
- **Corner:** 12px (14px for the empty state).
- **Background:** `ui-panel`, on the dotted canvas.
- **Border:** 1px `ui-line`; no shadow at rest.
- **Internal padding:** 12–14px in the handoff strip, 28px in the empty state.
- The handoff strip is a four-column grid of label/value pairs; machine values are mono in a sunken, hairlined block, and adjacent stacked values join their corners so a multi-line value reads as one block.

### Inputs / Fields (chrome)
- **Style:** white, 1px `ui-line-strong`, 8px radius, 34px tall, 13.5px text, caret in `ui-sel`.
- **Hover:** stroke darkens to `#b9c0ca`.
- **Focus:** stroke becomes `ui-sel` plus a 3px `rgb(53 82 232 / .16)` halo; the default outline is suppressed in favour of it.
- **Read-only (locked approved copy):** sunken fill, soft `ui-line` stroke, full-strength ink and a default cursor — locked text stays fully legible, because it is approved copy, not disabled input.
- **Invalid:** `ui-bad` stroke with a 3px red halo, driven by `aria-invalid`.

### Navigation
Brand tabs sit full-height in the top bar with a 10px brand dot, a name, and a tabular count. The selected tab is `ui-ink` text with a 2px ink underline inset 10px from each edge; hover previews the same underline in `ui-line-strong`. The inspector's Content/Image/QA tabs repeat the idiom at 36px. At 760px the brand tabs become a four-column grid with stacked dot-over-name.

### Source Rail
The rail is the product's index: a sticky search field with a `/` shortcut, then sticky group heads ("Partners & owned", "Paid search · strain") with counts, then rows. Each row is a 40px avatar (partner mark, product shot, or dark initials chip) beside a two-line name/source-line block and a right-hand status column. The current row takes the `ui-sel-bg` fill with a `ui-sel-line` inset ring. A source with no approved copy is an "empty" row: dashed avatar, lighter name.

### Deal Marker (signature)
The system's one invented control, and the only place a marketer edits structure rather than text. The approved headline is broken into clickable word chips in a sunken tray; clicking the first and last word of the offer selects the span. Selected words fill ink-on-white; the anchor word carries a 2px `ui-sel` ring. Below, a small definition list shows the resulting Before / Deal / After split with the deal in bold. It exists so the `[square brackets]` rule is a click, not syntax.

### Image Focal Picker (signature)
A 120px 5:8 preview on the left, four generic-image options on the right. Clicking the preview sets a focal point: an 18px white-ringed pin marks it, and a dashed band with a full-bleed `0 0 0 999px rgb(20 23 28 / .28)` scrim shows exactly the 22% strip that survives the mobile crop. Pin and band animate on the standard 180ms ease.

### Popup Card (the shipped system)
The exported object. A two-column grid — portrait image panel, then text body — on the brand surface, 12px radius, on the popup lift shadow. Order is fixed: partner/product tile, source line with its accent rule, split headline, proof sentence, email field, CTA, plain decline. Every visual value in it is a brand custom property; the layout rules are shared by all four brands and are not to be forked.

### Motion
One easing curve (`cubic-bezier(.16, 1, .3, 1)`) and a narrow range: 120–160ms on control colour changes, 180ms on the focal pin, 220ms on the frame swap, 240ms on the inspector drawer. Motion only ever confirms a state change; nothing moves to attract attention.

## Do's and Don'ts

### Do:
- **Do** change a brand by editing its `[data-brand]` custom properties. Layout and hierarchy rules are shared and must stay shared.
- **Do** keep the deal the largest and heaviest thing on the card, and split every headline with `[square brackets]`.
- **Do** keep placeholder ink at `rgb(var(--ink) / .62)` in the popup and `#6a7183` in the chrome, and keep `.hint` darker than both.
- **Do** print "shown at N%" whenever the canvas scales a frame, and leave frames at true size above `FIT_FLOOR = 0.98`.
- **Do** keep the two `prefers-reduced-motion` guards — the one in `popup-css` is what protects exported files.
- **Do** keep the popup's caret on `--accent` and the studio's on `ui-sel`: exports must resolve entirely within brand tokens.
- **Do** draw every icon from the inline `#i-*` sprite, at 16px, stroke 1.7, coloured by `currentColor`.
- **Do** treat every embedded raster as a low-res preview that carries its origin in the file header (cropped from `all-30-popup-images.jpg`, `*-partner-popups.png`, `ppc-strain-popups.png`; none generated for this file) and is to be replaced by a production https URL before build. Every image slot accepts a URL for exactly this reason.
- **Do** pair every status colour with a word or a sprite icon.
- **Do** use container queries for popup breakpoints; the card responds to its own width, not the window.

### Don't:
- **Don't** use `ui-sel` for anything but selection and focus, and don't let brand colour into the chrome beyond the 10px tab dot.
- **Don't** lighten any placeholder, hint, or ink alpha below the recorded values; they are contrast floors measured against all four brands and the dark card.
- **Don't** add a per-brand layout rule. If a brand needs a different value, it needs a token.
- **Don't** stand a Unicode glyph in for an icon. The popup's close control still carries a `×` set in `system-ui`; that is a carried defect to be replaced with the sprite, not a pattern to copy.
- **Don't** give chrome surfaces a resting shadow. Hairlines and tonal fills do the structural work; shadow means "floating".
- **Don't** reword approved copy to fix a layout problem — move the brackets or the non-breaking space instead.
- **Don't** "fix" the five knowingly accepted findings: the 2px segmented-control track inset and the tab strip's own padding (both are the control's idiom), the popup's thin-ring-plus-wide-shadow pair (the ring is what edges a white card on a light canvas), the diagonal hatch (it means "image missing", it is not decoration), and Open Sans (it is Seed Supreme's approved body face; the brand token wins over a generic overuse heuristic).
- **Don't** resolve, in the design system, what the product has left open: ILGM's token direction against ilgm.com's live Chunk/Aleo `!important` override on `.klaviyo-form`, which "Boldonse" ILGM expects, the three offer codes marked "confirm" (LEAFLY20 on Seed Supreme, ILGM20, CANNIGMA20), and partner logo permissions — which are required before any partner popup goes live.


## Seed Supreme, after the 16 Sep revision

The brief moved Seed Supreme off several of the design system's defaults. Each is
deliberate and recorded in `design-system/IMPORT.md`:

- **Headline pairing.** The deal is PP Agrandir Wide **Black Italic**, uppercase, on
  `leading-tight`, at **33px desktop / 26px mobile**, with a white glow
  (`0 0 12.006px rgb(255 255 255 / .24)`). The before/after qualifiers are
  **Work Sans Bold**, uppercase, at `+.06em` tracking, in **Tango Orange** with an
  orange glow (`0 0 19.651px rgb(244 121 32 / .24)`). Tracking goes positive because
  the design system's `-.01em` was set for a display face at size; small uppercase
  body text at negative tracking closes up and stops reading.
- **Surface.** Pure black with one low-opacity orange radial bloom in the bottom-right
  corner, plus a **paper-grain plate** over it: Texturelabs_Paper_128L, the same texture
  the brand's campaign artwork uses, at 64% on `screen` blend. Each popup rotates the
  plate by its own angle, hashed from the popup id (not `Math.random()`) so a given card
  looks identical on every render and in every export. The layer is oversized and centred
  so rotation never exposes a corner, and it is dark-card only — on white it reads as dirt.
- **Source line.** No container. The shared 14x2px accent rule, as on the other brands.
- **CTA.** No underline, label at 18px, height 52px, radius matched to the email field
  (`--cta-radius: var(--field-radius)`, so the two never drift apart), and a trailing
  arrow-up-right that nudges on hover. The arrow is authored inline rather than pulled
  from the studio's sprite, because an exported popup ships with no sprite. Seed Supreme
  only — the other three brands keep their own approved CTA treatments.
- **Partner logos.** Real vector lockups, no white plate. Seed Supreme's dark card uses
  a white variant per partner; every other surface uses the partner's own colours.
  THC Farmer keeps its colours on both surfaces by instruction - it is a coloured
  symbol, not a wordmark.
- **Logo sizing is optical, not fixed.** Each mark carries a multiplier set by rendering
  it at a fixed height, counting its opaque pixels and equalising ink mass (damped to a
  fourth root). Range 0.89-1.04. A flat max-height made square symbols read small and
  dense wordmarks read heavy.
- **Air under the mark.** `--gap-tile-source` is 26px (was 14px), which also opens up the
  PPC strain tile since it uses the same token.


## Seed Supreme, 17 Sep revision

- **Deal** 33px desktop / **30px mobile**, italic, white glow `0 0 12.006px rgb(255 255 255 / .24)`.
  30px on mobile is deliberately not 29: clearance is not monotonic with size, because the
  wrap changes. At 27px the deals sit on two lines with 3px spare, at 29px on three lines
  with 5px, and at 30px every headline has settled into a stable three-line wrap with 51px.
- **Qualifiers** Tango Orange, `0 0 19.651px rgb(244 121 32 / .24)`.
- **Proof emphasis.** A run of the proof sentence can be marked with `*asterisks*`, the way
  the headline marks its deal with `[brackets]`. The marked run renders at full ink while the
  rest of the proof stays at `--l3-alpha` .64 — the contrast between them is what makes the
  emphasis read. Marked in the panel by clicking the first and last word.
- **CTA** radius bound to `--field-radius` so button and field cannot drift apart; label 18px;
  trailing arrow at 1.32em.
- **Close control** is a drawn SVG, flex-centred. It was a `×` character, whose optical centre
  sits above its line box — visible once the mobile card gave it a filled circle.
- **Panel divider** 2px `--accent` on the panel's right edge, moving to the bottom edge when
  the card stacks.
- **Paper grain** at 50% (was 64%), embedded at 1800px.
- **PPC strain tile** name and image are editable, with a reset back to the product page.

### Logo sizing, corrected

The first pass equalised **ink mass**, which measures weight rather than size, and left Grow
Weed Easy reading small and i49 reading large. It also never applied: a second `.tile img`
rule later in the sheet overrode both the height and the width, so every mark rendered at the
flat tile height. Both are fixed.

The multiplier now comes from the **median vertical ink extent per column** — render the mark
at a fixed height and, for each column of pixels, take the vertical span of its ink; the median
is how tall the shapes actually look (cap height on a logotype, the whole mark on a symbol).
Grow Weed Easy's letters fill 28% of its box, i49's fill 85%, which is the whole problem in one
number. The correction equalises that median against Leafly, damped to a 0.75 power, floored
higher for square marks (a symbol should sit above cap height, not level with it) and capped at
280px so a 5:1 lockup cannot run away with the column.

| Mark | Multiplier | Rendered |
|---|---|---|
| Grow Weed Easy | 1.45 | 280x52 |
| Hey Abby | 0.95 | 150x34 |
| Reddit | 1.15 | 41x41 |
| THC Farmer | 1.15 | 39x41 |
| The Cannigma | 1.09 | 119x39 |
| Leafly | 1.00 | 92x36 |
| Seed Supreme | 0.85 | — |
| i49 | 0.70 | 47x25 |

### Imagery

Six generic options rather than four: each idea now has an outdoor and a studio-black reading
(`A` outdoor field / `E` plants on black, `D` grower outdoors / `F` seeding in nitrile gloves),
with packaging and seeds macro studio-only. Partner popups no longer use the low-resolution
review-board crops; each now carries a library image matched to its source. Everything embeds
at 620px, the panel's own retina size.


### 17 Sep, later

- **Hey Abby** returned to 0.95 (150x34). The measured correction put it at 1.27, which read too
  large against the rest of the set - the metric equalises apparent shape height, and a wordmark
  with this much internal air overshoots it.
- **Proof emphasis** gained an explicit "Remove bold" control. Clicking the whole sentence also
  clears it, but that was not discoverable.
- **The PPC strain tile** now offers Seed Supreme's own product photography from the design
  system (six images, square-cropped) alongside manual upload and a URL field. Labels follow the
  system's own names - named cultivars where it names them, descriptive where it does not, so
  nothing is attributed to a strain on a guess.
- **Packaging generic** swapped to the client's preferred render.

### 17 Sep, USOA image library

USOA's supplied photography is now in the studio, so the brand no longer starts empty: 19 images
from `USOA Images/`, nine studio packshots first (THCA flower, gummies, bundles, accessories),
then ten lifestyle shots. Embedded at JPEG q80 like the rest of the library, and already at the
340x500 the panel previews, so the download the studio hands back is the file as supplied.
Labels stay descriptive - what is in the shot, not a claim about the product - and each tile
still names its source file, so an upload to Klaviyo is recognisable.

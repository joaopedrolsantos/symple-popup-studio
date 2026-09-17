# Popup Studio — start here

Source-matched Klaviyo entry popups for **Seed Supreme**, **Homegrown**, **ILGM** and **United Strains of America**.

**Open `templates/popup-studio.html` by double-clicking it.** That is the whole tool. No install, no build step, no login, no server. It needs internet only to load fonts.

---

## What's in here

| Path | What it is |
|---|---|
| `templates/popup-studio.html` | **The studio.** One file: every popup, every brand, plus the export. This is the thing you edit. |
| `Assets/SKILL.md` | **The rules.** Popup anatomy, each brand's tokens, the deal rule, spacing, triggers, offers, claims. Treat this as law. |
| `DESIGN.md` | The design system as actually built, written from the shipped file. Read it before changing anything structural. |
| `PRODUCT.md` | Who this is for and what it has to do. |
| `design-system/` | **The Seed Supreme design system**, imported from Claude Design. Tokens, the brand book, logo SVGs, component contracts. `design-system/IMPORT.md` maps its tokens to the popup's **and records where the brief deliberately overrides it**. |
| `Assets/fonts/PP Agrandir/` | The full PP Agrandir family the client supplied. The studio embeds one weight from it: Wide Black Italic. |
| `Assets/logos/partners/` | The partner logo sources (SVG, plus The Cannigma as PNG). Both surface variants are generated from these. |
| `Assets/images/seed-supreme/` | Seed Supreme imagery: the four PPC generic images, the eight Figma library images, the paper-grain plate and the pouch artwork. `*-full.jpg` are full-resolution; the studio embeds 480px previews. |
| `Assets/partner-popups-spec.md` | The approved copy, per source. |
| `templates/popup-img-brief.md` | Image prompts for the generic PPC panels. |
| `Assets/*.png`, `all-30-popup-images.jpg` | Review boards and the image contact sheet. |
| `Assets/Screenshot 2026-09-16 *.png` + the PDF | Reviewer comments from ClickUp task #86akjnxu9. |
| `Homegrown Cannabis Co - Images/` | Homegrown's supplied image library, full resolution. |
| `USOA Images/` | USOA's supplied image library, full resolution: nine `PRODUCT/` packshots and ten `LIFESTYLE/` shots. |

---

## Where each brand stands

| Brand | Status |
|---|---|
| **Seed Supreme** | **Done.** 880×560 card on pure black with an orange bloom bottom-right. Deal is PP Agrandir Wide **Black Italic**, uppercase; before/after are Work Sans Bold, uppercase. Source line uses the shared accent rule, no container. CTA has no underline. Partner logos are real vector lockups with no plate, white on the dark card. Four on-brand PPC generic images. Values trace to `design-system/`, except where `design-system/IMPORT.md` records a deliberate override. |
| **Homegrown** | **Done.** White 760px card. CTA is the design system's campaign pill (lime `#deffb7`, ink `#0d523d`). |
| **ILGM** | **Open — yours.** Currently the brief's tokens: mint `#DCFCE7` card, Boldonse caps, red `#DB0B16` button. |
| **USOA** | **Open — yours.** Currently Oswald caps, Montserrat body, red `#f54d4d` button. |

Seed Supreme and Homegrown are two worked examples of how far the token system stretches. Read both before designing yours.

---

## Using the studio

1. **Pick a brand** in the top bar, then a **traffic source** in the left list.
2. The popup renders at desktop and mobile size in the middle, at true size. If the window is narrow the canvas scales it down and says so ("shown at 80%") — the caption never claims a size it isn't showing.
3. The right panel has three tabs:
   - **Content** — the approved copy, locked. Click words in the headline to mark **the deal** (the big line). Unlocking a field lets you reword it, and the popup is flagged as differing from the approved spec until you revert.
   - **Image** — the image library, the production URL field, and the focus point.
   - **QA** — everything still outstanding before this popup can be built.
4. **Export** (top right) gives you clean standalone HTML for one popup, a brand pack, or everything, plus a build sheet.

Your edits live in your browser only. Use **Export → Save my edits** to move them to another machine, and send that file back with your work.

---

## Images, and the one thing people get wrong

**The studio cannot host images.** Klaviyo needs a hosted URL. So the flow is:

1. Pick an image from the library, or **Upload an image**.
2. Judge the design with it.
3. **Download this image**.
4. Upload that file to Klaviyo (or your CDN).
5. Paste the link Klaviyo gives you into **Production image URL**.

Until step 5, QA keeps flagging the popup, on purpose. Library images and uploads are previews — they are embedded in the file and they make exports heavy. Same popup, measured:

- hosted URL → **18 KB**
- embedded preview → 39 KB
- library image → 122 KB

Uploads stay in your browser and are resized past 1400px. The download hands back exactly what the popup is using.

---

## Designing a brand

Everything visual is a CSS custom property. **You should not need to touch any layout rule or any JavaScript.**

Open `templates/popup-studio.html` in a text editor and find your brand's block near the top:

- Seed Supreme — line ~125 (and the light variant at ~176)
- Homegrown — line ~183
- **ILGM — line ~202**
- **USOA — line ~217**

For Seed Supreme, change the token in `design-system/` first if the change is a brand
decision rather than a popup-fit decision — the studio should stay downstream of the system.

Change values there and every popup for that brand updates at once.

### Things that will trip you up

- **`--ink` is three space-separated numbers, not a hex.** It is used as `rgb(var(--ink) / .62)`, so write `--ink:17 17 17`, not `#111111`.
- **Do not edit the block marked `CARD LAYOUT - identical for every brand`** (~line 243). That is the shared skeleton. If your brand needs a different value, it needs a *token*, not a per-brand layout rule.
- **New fonts must be added to the Google Fonts `<link>`** at the top of the file. Boldonse loads in its own request; keep it that way.
- **Mobile type sizes** are overridden in the `@container popup (max-width: 520px)` block (~line 231), not with a viewport media query.
- **PP Agrandir Wide Black Italic is base64-embedded**, not linked, at the top of the `popup-css` block. It has to be: Chrome treats a double-clicked `file://` page as an opaque origin and blocks a relative font fetch, so a linked file would silently fall back to Archivo. It is ~108 KB of the file. Do not "tidy" it into a linked path. Only the italic ships — the deal is the only thing set in this face.
- **Partner logos come in two variants.** `logo-<name>` is the partner's own colours; `logo-<name>-white` is the knockout the renderer picks on Seed Supreme's dark card. Add both when you add a partner, or the dark card falls back to the colour version. THC Farmer deliberately has no white variant.
- **Logo sizes are optical, not fixed.** `LOGO_OPTICAL` holds a per-mark multiplier measured from ink mass. A new logo with no entry renders at the plain tile height, which is usually fine but worth a look.
- **Never round numbers outside path data when minifying an SVG.** Leafly carries `transform="scale(0.26458333)"`; rounding that to `scale(0.3)` scales the art ~13% past its viewBox and clips it. Only `d` and `points` are safe to round.
- **The paper grain rotates per popup**, hashed from the popup id so it is stable across renders and exports. Do not swap the hash for `Math.random()` — every re-render would reshuffle it and exports would stop matching the studio.
- **There is only one `.tile img` rule, and it must stay that way.** A second one added later in the sheet silently overrode the optical logo sizing for a whole revision: every mark rendered at the flat tile height and nothing looked wrong enough to notice. If a logo suddenly stops obeying `LOGO_OPTICAL`, look for a duplicate selector before anything else.
- **Emphasis in the proof is `*asterisks*`**, the way the deal in the headline is `[brackets]`. `plain()` strips both, so approved-copy comparison ignores them.
- **The studio is ~5 MB.** Every image is base64-embedded, which is what keeps this one double-clickable file with no server. It opens fine, but it is close to the practical ceiling — see the note at the end of `design-system/IMPORT.md` before adding another dozen images.
- **PP Agrandir is licensed.** It is a commercial Pangram Pangram face, and it now ships inside every export. Confirm Seed Supreme's webfont licence covers live Klaviyo forms before anything built from this file is deployed.
- `document.fonts.check()` lies. The studio uses `document.fonts.load()`. Don't swap it.

### The tokens you set

**Surface** — `--surface`, `--ink`, `--accent`
**Type** — `--font-display`, `--font-body`
**Headline (deal)** — `--l1-deal-size` `-lh` `-weight` `-stretch` `-track` `-case` `-measure`
**Headline (qualifier)** — `--l1-qual-font` `-size` `-lh` `-weight` `-stretch` `-track` `-case` `-alpha`
**Source line** — `--l2-size`, `--l2-weight`, `--l2-alpha`
**Proof** — `--l3-size`, `--l3-lh`, `--l3-weight`, `--l3-alpha`, `--measure-proof`
**Button** — `--cta-bg` `-fg` `-font` `-size` `-weight` `-stretch` `-case` `-track` `-radius` `-h` `-border` `-shadow` `-decoration` `-textshadow`
**Field** — `--field-border`, `--field-radius`, `--field-bg`
**Decline** — `--decline-underline`

Only if your direction genuinely needs a different frame (Seed Supreme does): `--card-w`, `--panel-w`, `--card-min-h`, `--card-radius`, `--card-shadow`, `--pad-x`, `--pad-top`, `--pad-bottom`, and the `--gap-*` rhythm.

---

## Rules you don't get to change

Read `Assets/SKILL.md` properly. The short version:

- **Approved copy is approved.** Never reword to fix a layout problem — move the deal brackets or the non-breaking space instead. If you must change wording, it gets flagged until someone signs off.
- **The deal is the largest thing on the card.** Nothing — logo, button, source line — may be bigger or heavier. Mark it in the headline with `[square brackets]`.
- **No new claims.** Only what the site already says: guarantee terms, seed counts, grown in the USA, COAs. No yield, potency, medical or suitability claims.
- **No orphan words.** A one-word last line is a defect. Check at 760px (880px for Seed Supreme) and 375px.
- **Never invent an offer code.** If a code doesn't exist yet, it stays marked "confirm".
- **Partner logos need the partner's written permission** before anything goes live. The studio has a checkbox for it; don't tick it on someone else's behalf.
- **Contrast floors are floors.** Placeholder ink and hint colours were set by measurement, not taste. Don't lighten them.
- **Icons come from the SVG sprite.** No Unicode glyphs standing in for icons.

---

## Still undecided — ask, don't guess

1. **ILGM's token direction.** `ilgm.com` currently forces Chunk/Aleo and a lilac button onto every `.klaviyo-form` with `!important`. Until that's settled, an ILGM popup will not render as designed on the live site. **This blocks ILGM.**
2. **Which "Boldonse"** ILGM actually expects. Google's Boldonse is a tall condensed heavy face; confirm it's the right one.
3. **Three offer codes** are marked "confirm": `LEAFLY20` (Seed Supreme), `ILGM20`, `CANNIGMA20`. Riley's call.
4. **Partner logo permissions** — required per partner before deployment.
5. ~~**Seed Supreme's `#231a16` email-style dark**~~ — **resolved by the design system import.** `#231a16` is `web-ink`, a *product-layer* token. A popup is a brand-layer surface, so its dark is `surface-dark` `#1a1a1a`. There is no variant to bring back.

---

## When you're done, send back

- The edited `templates/popup-studio.html`
- Your **Export → Save my edits** JSON
- Any new image files, full resolution, in a folder named for the brand
- A note on anything you changed that `Assets/SKILL.md` contradicts, so the rules and the build don't drift apart

Keep it as one file. Don't minify it, don't reformat it, don't split it into a project with a build step — marketing has to be able to double-click it.

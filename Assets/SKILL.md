---
name: symple-source-popups
description: Design co-branded and strain-matched Klaviyo entry popups for Seed Supreme, Homegrown Cannabis Co, ILGM and United Strains of America, matched to the traffic source and the intent it carries. Use for any new popup, partner form or PPC strain form on these brands.
---

# Source-matched popups for the Symple brands

## What a popup is for here
One popup per traffic source, one first-order offer per person. The popup restates why the visitor arrived, asks for one thing, and writes the source and the offer shown to the Klaviyo profile so Email 1 in the welcome flow repeats the same promise. It is never a second discount on top of an ad's offer.

## Anatomy (all four brands)
1. Image panel (left, portrait): a scene that says why this visitor arrived. Not a bud macro, not a coupon graphic, no text, no faces, no consumption. These rules govern images briefed and generated for the panel. Images a brand supplies to the studio's image library are that brand's own call and are not held to them: Homegrown's library ships a bud macro (HMG-Bud) and a product shot carrying label text (HMG-Nutrients).
2. Partner tile: the partner's logo only when the partner has approved it. Owned properties (forum, blog) show the brand logo with the domain under it. Paid search and our own Meta ads show no logo tile.
3. Source line (italic): "Official partner of X" for commercial partners, "You found us on Reddit" for communities, "Hey X reader" for publishers, "Searching for X?" for paid search. Seed Supreme sets the same words as an uppercase chip rather than italic text.
4. Headline: the offer or the strain, in the brand's words. Never "welcome to" as the headline.
5. One sentence of proof (guarantee, lab test, grown in the USA) in the brand voice.
6. Email field, one button in the brand's own CTA style, a plain decline ("Not right now" / "No thanks"). No confirmshaming.
7. Later steps (SMS, grow questions) stay as on the brand's main popup; ask autoflower or photoperiod and feminized or regular as two questions.

## Brand tokens
- Seed Supreme: dark card #1a1a1a, 880x560, radius 16, with a 320px photo panel under an amber-to-ink scrim. Accent orange #f47920, carried by an uppercase source chip. Button is the gradient `linear-gradient(110.521deg, #D1671B 14.07%, #422109 89.2%)`, radius 16, underlined, Work Sans 700. Headline PP Agrandir Wide (Archivo 900 stands in; PP Agrandir is not a Google face), body Work Sans. Voice: the seed counter; strain names, pack math, "stack your freebies". Direction from the shared Seed Supreme canvas; the white card is kept as an alternate surface.
- Homegrown: white card, wide caps display (DrukWide on site; Archivo 900 wide in mock-ups). Button is the design system's campaign pill: lime #deffb7 under the sticker sheen, ink #0d523d, fully rounded, Helvetica Neue 700 at -.04em, 1px rgb(227 255 212 / .62) border (CampaignButton, tone `lime`, `knob` off - popups do not use the arrow knob). Green #05c87b stays the brand accent for the source rule and the field caret. Voice: the mentor; "we replace any seed that doesn't pop".
- ILGM: mint #DCFCE7 card, Boldonse 400 caps headline with letter-spacing .05em and line-height 1.5, Figtree body, red #DB0B16 button, input stroke #3C3C3C. Voice: home of the growers; guarantee first. Forms only; flows are out of scope.
- USOA: flag panel or product scene, Oswald caps headline, Montserrat body, red #f54d4d button, "official partner" line. Voice: lab-tested and legit before cheap; no grow language except on the seed-brand partner surfaces.

## Text hierarchy (all four brands)
The layout is the same every time; only the values below change by brand. `templates/popup-studio.html` implements this exactly, so build from it or match it.

**The deal rule.** Split every headline into a qualifier before, the deal, and a qualifier after, keeping the approved words in their original order. Mark the deal with [square brackets]: `[A free 4-pack of Purple Haze Fem] with your first order`, `Lab-tested THCa flower, [20% off] your first order`, `[Buy 10, get 10 free] on premium seeds`. The deal is the largest thing on the card. Nothing else (logo, button, source line) may be bigger or heavier. With no brackets, the whole headline is set as the deal.

**Levels.**
- L1 deal: display face, brand size, full ink.
- L1 qualifier: the same display face, much smaller, ink at about 60%. It sits 4px above the deal or 6px below it.
- L2 source line: body face, italic, 15–16px, ink at about 85%, with a 14×2px accent rule in front.
- L3 proof: body face, regular, 14–15px, line-height 1.5, ink at about 72%.

**Layout.** The text column is left-aligned, and "No thanks" is centred under the button. Desktop card 760px (portrait image panel 297px, text padding 40px), except Seed Supreme at 880x560 (photo panel 320px, text padding 44px across and 40px top and bottom). Mobile (card ≤520px): the image becomes a 132px strip on top, and text padding is 24px.

**Spacing rhythm.** Deliberately unequal, so elements group:

| From → to | Desktop | Mobile |
|---|---|---|
| Logo tile → source line | 24px | 18px |
| Source line → headline | 10px | 10px |
| Headline → proof | 14px | 14px |
| Proof → email field | 24px | 20px |
| Email field → button | 10px | 10px |
| Button → decline | 12px | 12px |

Field height is 48px and button height 52px.

| Brand | L1 deal (desktop / mobile) | L1 qualifier | L2 source | L3 proof | Deal max line | Button |
|---|---|---|---|---|---|---|
| Seed Supreme | Archivo 900, wdth 112, sentence case, 25 / 22px, lh 1.18, −.01em | Archivo 700, 15 / 13px, lh 1.3, ink 60% | Work Sans 600, 15px, uppercase chip | Work Sans 400, 15px, ink 64% | 22ch | Work Sans 700, 15px, −.04em, white on the orange gradient, radius 16, underlined |
| Homegrown | Archivo 900, wdth 122, caps, 26 / 22px, lh 1.06 | Archivo 800, wdth 112, caps, 13 / 12px, +.03em, ink 60% | Helvetica italic, 16px | Helvetica 400, 15px | 17ch | Helvetica 700, 18px, −.04em, #0d523d on #deffb7 + sheen, pill, 1px lime border |
| ILGM | Boldonse 400, caps, 22 / 18px, lh 1.5, +.05em | Boldonse 400, caps, 13 / 11px, lh 1.5, ink 58% | Figtree italic 600, 16px | Figtree 400, 15px | 22ch | Figtree 700, 17px, white on #DB0B16, radius 8; input stroke #3C3C3C |
| USOA | Oswald 600, caps, 40 / 34px, lh 1.02, +.01em | Oswald 500, caps, 19 / 17px, ink 60% | Montserrat italic 600, 15px | Montserrat 400, 14px, lh 1.55 | 20ch | Oswald 600, caps, 18px, +.06em, white on #f54d4d, radius 4; underlined decline |

Other max line lengths: qualifier 30ch, source line 40ch, proof 38ch.

**No orphan words.**
- Headlines use `text-wrap: balance`; source and proof use `text-wrap: pretty`.
- Join the last two words of every line group with a non-breaking space when they total 20 characters or fewer. In the Klaviyo editor, type the non-breaking space by hand.
- Check every popup at 760px and 375px. A one-word last line is a defect: fix it by moving the deal brackets or the non-breaking space, never by rewording.

**Fonts and fallbacks.**
- Load fonts from Google Fonts, with Boldonse in its own request.
- Fallbacks: Boldonse → Archivo → Arial Black; Oswald → Arial Narrow; Archivo → Helvetica Neue.
- `document.fonts.check()` is not proof that a font loaded, because it returns true for fonts it has never loaded. Check with `document.fonts.load()`.
- Google Fonts' Boldonse is a tall, condensed heavy face.
- ilgm.com currently forces Chunk/Aleo and a lilac button onto every `.klaviyo-form` with `!important`. Settle that before an ILGM popup goes live.

**Seed Supreme surface.** Dark #1a1a1a is the default, from the shared canvas. It supersedes the earlier #231a16 email-style dark (Chris's request); if the email template still needs #231a16, that is a separate variant to re-add. A white card stays available as the alternate surface. On the dark card partner logos sit on a white plate.

**Seed Supreme and the deal rule.** The canvas comp sets the whole headline at one size, which would leave the deal marking with nothing to show. The studio keeps the deal/qualifier split inside the new look so the control still does something: deal 25px, qualifier 15px at 60% ink. To match the comp exactly instead, set `--l1-qual-size` equal to `--l1-deal-size`.

**PPC image panel.** When the tile embeds the product, the image panel uses one of the brand's four generic images (grouped plants, packaging, seeds/macro, lifestyle; see `templates/popup-img-brief.md`), never the same strain again.

## Triggers
- Partners: URL contains a_aid=<partner PAP id> (Affiliatly aff= on ILGM until the PAP migration). One scheme per brand.
- Owned properties: URL contains the domain (ilgmforum.com, ilovegrowingmarijuana.com).
- Paid search strains: the ad group's final URL suffix carries utm_content=<strain-slug>; one form per strain in the top ten by spend, a generic strain form on utm_content=strain-other. The popup uses the strain's own PDP image and lands on the PDP.
- Our own Meta ads: utm_source=meta or a_aid=facebook, on the offer lander.

## Offers
Use the code that already exists for that source. Never invent a code; mark new ones "confirm". Content sources (blog, guides, Almanac learners) get the asset first and the seed offer later in the welcome flow.

## Properties written at submit
acq_partner, acq_intent (brand, offer, strain, research, learn), acq_strain (slug), offer_shown (the code on this popup), plus the grow or category answers on later steps.

## Claims
Only what the site already states: guarantee terms as written on the brand's FAQ, seed counts, "grown in the USA", COAs. No yield, potency, medical or suitability claims. Partner logos need the partner's permission before deployment.

## Build
`deliverable/build_partner_popups.py` renders the boards from a table of cards (partner, line, headline, sub, CTA, trigger, offer, status) and writes `design/partner-popups-spec.md`. `deliverable/build_ppc_strain_popups.py` renders the PPC strain board. Images: `design/popup-img/` (Codex imagegen, portrait, film-passed by `deliverable/postprocess_popup_imgs.py`).

Marketing builds and reuses popups in `templates/popup-studio.html`. It is one self-contained file for all four brands:
1. Pick the brand, the source and the layout (Partner, PPC strain or PPC generic).
2. Mark the deal and set the images.
3. Clear QA.
4. Export standalone HTML, a brand zip or an all-brands zip with a CSV build sheet.

Approved copy lives in its STUDIO DATA block and is locked in the UI; wording edits are flagged until reverted. Image prompts for the generic panels are in `templates/popup-img-brief.md`.

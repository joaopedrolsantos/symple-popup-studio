# Popup Studio

One file that holds every source-matched Klaviyo entry popup for **Seed Supreme**, **Homegrown
Cannabis Co**, **ILGM** and **United Strains of America** — and exports them build-ready.

**Open `templates/popup-studio.html` by double-clicking it.** That is the whole tool. No install,
no build step, no server, no login.

---

## What this is

Marketing picks a brand, then a traffic source, then a layout variant. The popup renders at true
desktop and mobile size. Copy slots and images are edited in form fields, QA runs before build,
and Export produces clean standalone HTML plus the handoff data (trigger rule, offer code,
Klaviyo properties) the build needs.

Approved copy is locked. Rewording is possible but the popup is flagged as differing from the
spec until it is reverted.

## Where to start

| Read this | For |
|---|---|
| [`START-HERE.md`](START-HERE.md) | How to use the studio, and the things that will trip you up |
| [`PRODUCT.md`](PRODUCT.md) | Who this is for and what it has to do |
| [`DESIGN.md`](DESIGN.md) | The design system as actually built, written from the shipped file |
| [`Assets/SKILL.md`](Assets/SKILL.md) | The rules: popup anatomy, brand tokens, triggers, offers, claims |
| [`design-system/IMPORT.md`](design-system/IMPORT.md) | How the Seed Supreme design system maps onto the popups, and every place the brief deliberately overrides it |

## Layout

```
templates/popup-studio.html   the studio — the only file you edit
DESIGN.md  PRODUCT.md         the design system, and the product record
START-HERE.md                 orientation
design-system/                the Seed Supreme design system, imported from Claude Design
Assets/                       copy spec, rules, fonts, partner logos, imagery, review boards
```

## Brand status

| Brand | State |
|---|---|
| **Seed Supreme** | Done. Pure-black card with an orange bloom and paper grain, PP Agrandir Wide Black Italic headline, real partner lockups, 15-image library. |
| **Homegrown** | Done. White 760px card, lime campaign-pill CTA. |
| **ILGM** | Open. Still on the brief's tokens. **Blocked:** `ilgm.com` forces Chunk/Aleo and a lilac button onto every `.klaviyo-form` with `!important`, so an ILGM popup will not render as designed on the live site until that is settled. |
| **USOA** | Open. Still on the brief's tokens. |

## Before anything ships

- **PP Agrandir is a commercial Pangram Pangram typeface.** It is embedded in the studio and in
  every export. Confirm Seed Supreme's webfont licence covers live Klaviyo forms before deploying
  anything built from this file.
- **Partner logos need each partner's written permission.** The studio has a checkbox for it.
- **Three offer codes are still marked "confirm"** — `LEAFLY20`, `ILGM20`, `CANNIGMA20`.
- **No new claims.** Only what the sites already say.

## A note on the single file

Every image and the typeface are base64-embedded, which is what keeps this one double-clickable
file with no server. That puts it around 5 MB. It opens and runs fine, but it is near the
practical ceiling — see the end of [`design-system/IMPORT.md`](design-system/IMPORT.md) before
adding another dozen images.

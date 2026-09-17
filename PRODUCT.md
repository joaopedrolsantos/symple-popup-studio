# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static single-file HTML/CSS/JS. No build step, no server, no login; opens by double-click and can be pasted into Claude Design. (Constraint from the original brief.)

Network dependency is Google Fonts only. One typeface is the exception: PP Agrandir Wide, Seed Supreme's headline face, is base64-embedded in the file because Chrome blocks a relative font fetch from a `file://` page, so a linked file would silently fall back. It is a commercial Pangram Pangram face and it ships inside every export — see Capabilities and Constraints.

## Users

Symple Commerce's marketing team (Nathan Keeble and colleagues; reviewers Chris Aitkenhead for design, Riley Brunett for trigger/offer QC). They are marketers, not developers. They open the file to rebuild and reuse the source-matched Klaviyo entry popups for four cannabis brands: Seed Supreme (SS), Homegrown Cannabis Co (HMGRN), ILGM and United Strains of America (USOA).

## Product Purpose

Popup Studio: one workbench that holds every source-matched popup for all four brands. The user picks a brand, then a traffic source, then a layout variant (Partner, PPC strain, PPC generic), previews it at desktop and mobile, edits copy slots and images in form fields, runs pre-build QA, and exports clean HTML plus the handoff data (trigger rule, offer code) for the Klaviyo build. Success: marketing can produce a correct, on-brand popup without design or code help, the same way every time.

## Positioning

The popups are generated from one shared layout and type system with four brand token sets, so the hierarchy (deal first, source line, proof) is structural rather than hand-set per popup. Approved copy comes from the traffic-source spec and is locked.

## Operating Context

- Source of truth for copy: `Assets/partner-popups-spec.md` and the card tables in `Assets/build_partner_popups.py` / `Assets/build_ppc_strain_popups.py` (30 partner popups plus PPC strain forms).
- Rules: `Assets/SKILL.md` (anatomy, popup-specific brand tokens, triggers, offers, claims).
- **The studio sits downstream of the brands' design systems published on Claude Design.** Each brand's tokens are meant to trace back to its published system rather than being hand-set here. Seed Supreme's was imported on 16 Sep 2026 into `design-system/`; Homegrown, ILGM and USOA are expected to follow the same way. `design-system/IMPORT.md` records what was taken, the token map, and how to refresh it.
- Output goes to Klaviyo (built by hand from the export) and Claude Design.
- ClickUp task #86akjnxu9 carries review comments.

## Capabilities and Constraints

- Jobs confirmed: browse and pick a popup; edit copy and images in the UI; export and hand off (HTML download, zip, trigger/offer copy); QA before build (fonts loaded, orphan words, placeholder images, codes marked "confirm").
- Approved copy must not be reworded. Edits to copy must be locked or clearly flagged as deviations from the spec.
- The deal is marked in the headline with [square brackets]; the renderer splits it.
- No new claims beyond what the sites state (germination guarantee, seed counts, grown in the USA, COAs, free shipping threshold).
- Partner logos need partner permission before deployment.
- Images: originals are not available locally; low-res previews are embedded and every slot accepts an https URL.
- A brand's tokens should be changed in its design system first when the change is a brand decision; the studio carries only popup-fit decisions (sizes tuned to the card, mobile overrides).
- Undecided: ILGM token direction (brief tokens vs live-site Chunk/Aleo override of Klaviyo forms); which "Boldonse" ILGM expects; three offer codes marked "confirm" (LEAFLY20 on SS, ILGM20, CANNIGMA20).
- Undecided, and blocking deployment rather than design: whether Seed Supreme's PP Agrandir licence covers webfont use on live Klaviyo forms. The face is embedded in the studio and in every export; confirm before anything built from the file goes out.

## Brand Commitments

The four brands' tokens must render exactly inside the popups. Where a brand has a published design system, that system is the authority and `Assets/SKILL.md` carries the popup-specific rules on top of it; where it does not yet, SKILL.md and the brief are the authority. The workbench itself must not read as a developer tool: plain-English labels, no code-editor feel.

Seed Supreme specifically: a popup is a **brand-layer** surface, so it takes `surface-dark`, `accent`, the gradient CTA and PP Agrandir headlines. It never takes the product-layer `web-*` tokens that dress the storefront.

## Evidence on Hand

- Contact sheet of 30 lifestyle images: `all-30-popup-images.jpg`.
- Current boards: `*-partner-popups.png`, `ppc-strain-popups.png`.
- Reviewer comments: `Screenshot 2026-09-16 at *.png`, ClickUp PDF.
- Seed Supreme design system, imported and byte-for-byte from the published artifact, in `design-system/`: the compiled tokens, the brand book, the campaign composition and imagery notes, the six real PP Agrandir weights, three logo lockups as vector SVG, and the prop contracts for `GradientButton`, `Tag`, `TextField` and `Logo`.
- No production image files, no real conversion data inside the workbench; do not fabricate them. Brand logo source files exist **for Seed Supreme only** — Homegrown, ILGM and USOA still have none, and their marks must not be approximated.

## Product Principles

1. Copy is approved; layout serves it. Never reword, always flag.
2. One system, four skins: any change lands in all brands at once.
3. The popup is the hero; the workbench recedes.
4. Every export is build-ready or says exactly what is missing.
5. Tokens are inherited, not invented. A brand value belongs to that brand's design system; the studio renders it and tunes only the fit.

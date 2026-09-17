Seed Supreme carries two visual layers, and every consumer must know which one it is building: the **brand layer** (campaigns, decks, covers, banners) and the **product layer** (the storefront itself). Never mix their tokens or type roles — a storefront screen never uses `headline`/`headline-alt` for body copy, and a campaign slide never uses `web-*` product tokens.

## Content

- Write labels as two words, not sentences: "Complete version", "Safe zone", "In use", "Color palette", "Product images".
- Write actions as verb + object, sentence case: "Add to cart", "Shop seeds", "Download logos".
- Author meta chips lowercase (`background`, `accent`, `auto`, `fem`, `macro`, `buds`); uppercasing is CSS `text-transform`, never typed in.
- Give product names as cultivar + type, exact and unabbreviated: "Green Crack Autoflower — GCA Fem", "Maui Wowie Feminized — MWF Fem".
- Use numbers as proof (order counts, cultivar counts), not decoration.
- Write for the customer in second person ("where you'll find…"); use first-person plural only when the company is the subject.
- Keep cannabis claims descriptive (genetics, growth type, appearance) — never medical or consumption advice.
- Set brand headlines and sub-headlines in UPPERCASE (a type-role rule, not manual casing); keep product UI sentence case, with uppercase reserved for small labels and badges.
- Use no emoji anywhere, in either layer.

## Visual foundations

**Surfaces.** Put brand hero and product-presentation material on `surface-dark` (`ss-eerie-black`, `#1a1a1a`) or `surface-darkest` (`ss-pure-black`); use `surface-page` (white) for brand documentation, paired with `text-body`/`border-hairline`. The brand's signature move is a hard 50/50 split between a dark and a light surface with no divider but the colour change — do not soften it with a rule or shadow. Build the storefront lighter: `web-page` (`#fff8f6`) behind white cards, `web-surface-pink`/`web-surface-peach` for promo blocks, `web-ink` (`#231a16`) for dark bands and the footer.

**Colour.** On the dark surface, set primary text `text-on-dark` and secondary text `text-on-dark-muted` (never a flat grey). On `surface-page`, set body copy `text-body` and secondary copy `text-muted`. Reserve `accent`/`accent-deep` (Tango Orange → Bronze) for brand emphasis and `highlight` (`ss-canary-yellow`) for the one cool accent — `highlight` is a spot colour only: check contrast before setting text on it, it is not a text-safe fill on either surface. In the product layer, set every primary action in `web-action` (`#fc5b00`) with white label; set body copy `web-text`, secondary copy `web-text-secondary`, muted copy `web-text-muted`; use `web-border`/`web-line` for hairlines and rules; use `web-green` for verified/in-stock states and `web-navy` for editorial blocks. Where a component needs an "on-fill" text colour on a light accent, use the matching `schemes-on-*` token rather than literal white or black, so contrast holds if the fill ever lightens.

**Type.** In the brand layer, set headlines in `headline` (PP Agrandir Wide, weight `weight-headline` = 900, tracking `tracking-headline` = −1%, leading `leading-tight`), uppercase; set sub-headlines in `subheadline` (Big Shoulders Display — see substitutions below), uppercase, tracking `tracking-subheadline`; set body and buttons in `body` (Work Sans), tracking `tracking-body` for copy and `tracking-button` for button labels. In the product layer, set the storefront in `body` (Open Sans stacks live in the same `body` family token — SemiBold 14px is the most common pairing), with `weight-label` (600) for eyebrows/badges and `tracking-ui` for compact UI labels; reserve `headline` for campaign headlines that appear inside the store. Never substitute `headline` for `body` or vice versa across layers.

**Buttons & actions.** Build the brand CTA (`GradientButton`) from `button-fill-start` → `button-fill-end` (`linear-gradient(110.521deg, ...)`, aliased as the `button-gradient`/`gradient-button` tokens), `radius-16`, `button-text` label, underlined, with `shadow-button` under it and `shadow-text-glow` on the label. Build product buttons (`Button`, `Button3`) from the five-value `style2` axis (`filled` / `outlined` / `text` / `elevated` / `tonal`) × the `state` axis, filled in `web-action` with white label, pill radius, and a state layer for hover/focus/pressed — never a colour swap. Never invert or recolour a gradient button on hover.

**Cards & containers.** Leave brand material without containers — separate content with `border-hairline` rules and the large spacing steps (`space-56` through `space-144`), never a card. Build product cards white or `web-surface-peach` (promo), radius from `radius-8`–`radius-16` depending on component, with `web-shadow-card`; use a 4:5 product image, breeder line, name, rating and price in that order.

**Corner radii.** Use `radius-8` for chips and meta labels, `radius-16` for brand buttons and product cards, `radius-32` for large surfaces and device screens; give product buttons and chips a full pill (not a token — set `border-radius: 999px` directly, since no token models "fully round").

**Imagery.** Use whole-plant, cured-bud and macro product photography, warm-lit, saturated, never black & white or duotone; place it full-bleed or in tight grids with 2–8px gutters; label a trait with a translucent uppercase `Tag` (`ss-black-24` fill), never a caption. Cast device mockups with `shadow-mockup`.

**Transparency.** Use translucency, not blur, to separate content from photography (`ss-black-24`, `ss-white-24` and the other `-64`/`-24`/`-12` alpha tokens); protect text over a photo with the photo's own dark area or a bottom-up black gradient, not a solid chip.

**Watermark.** On dark brand covers only, bleed the isologo off the right edge at `watermark-opacity` (4%). This is the only decorative device in the brand layer — introduce no patterns, textures or illustrations elsewhere.

**Motion.** Animate at `motion-fast` (160ms) for micro-interactions and `motion-base` (240ms) for larger transitions, both eased with `motion-ease`. Lift brightness slightly on hover rather than shifting hue; settle a press to `scale(.98)`.

## Iconography

Use `ProductIcon` (the `Icons/*` set, 41 glyphs, 24px, single colour via `currentColor`) for all product UI chrome — search, cart, nav, form and state glyphs. Use `Icon` (Font Awesome, weight 900) for brand-layer glyphs referenced by name (`download`, `arrow-right`). **Flagged substitution:** `Icon` currently loads Font Awesome 6 *Free* from a CDN in Solid weight; the brand's true kit is Sharp Solid (Font Awesome Pro), not supplied. Swap in the Pro kit URL for exact fidelity — do not introduce a third icon system to work around it. Introduce no emoji and no PNG icons as a substitute for either system.

## Typography files & substitutions

- `PP Agrandir` — supplied; the six weights the brand uses ship as files (`type.fonts` in `tokens.json`); the full 81-file family is not part of this system.
- `Open Sans`, `Work Sans`, `DM Sans` — load from Google Fonts.
- **`subheadline` is a substitution.** The source specifies TitlingGothicFB Comp Bold, which is not supplied and not on Google Fonts; `subheadline` currently resolves to Big Shoulders Display. Load the licensed TitlingGothicFB binaries and repoint `type.families.subheadline` to restore the original face — do not pick a different substitute without checking this note first.
- Treat Inter, Bitter, Source Sans 3, Courier Prime, Roboto, TitlingGothicFB Extended and Helvetica Neue as outside this system; they belong to one-off partner landing pages, not the brand or product layer.

## Components

Build only from the families below — do not add a component (Toast, Avatar, Accordion…) that is not one of these, or one of the two intentional additions.

- **Brand** — `Logo` (four lockups × dark/white tone).
- **Core** (intentional additions, codified because they recur across guideline frames but were never Figma components) — `GradientButton`, `Tag`.
- **Icons** — `Icon` (Font Awesome by name), `ProductIcon` (the 41-glyph product set).
- **Product UI** (`ui/`) — the storefront's Material-derived set: buttons (`Button`, `Button3`, `IconButton`, `SegmentedButton`), chips (`AssistiveChip`, `FilterChip`, `SuggestionChip`), selection controls (`Checkboxes`, `CheckboxesDark`, `RadioButtons`, `RadioButtonsDark`, `Switch`, `SwitchDark`), forms (`TextField`), navigation (`TopBar`, `NavBar`, `TopNav`, `TopNav2`, `Menu`, `Menu2`, `SearchBar`, `Tabs`), feedback (`LinearProgressIndicator`), product display (`Product`, `ProductDesktop`, `ProductMobile`, `ProductMobile2`, `Category`, `Categories`, `Carousel`, `Thumbnail`, `Directory`, `Seedbanks`), device chrome (`Battery`, `CellularSignal`, `Wifi`, `StatusTime`, `StatusBar`, `DeviceFrame`), and the building-block primitives used to assemble menus, tabs and list rows (`BuildingBlocks*`, `ListItemListItem0/2/4`), plus `About`, `Header`, `StickyCTA`, `UserImagesUserImages`, `ColourfulLogo`, `Favicon`, `DAvatars23`, `BreederThumbnail`.
- **Website kit** (`ui_kits/website/`) — full desktop sections: `HomeAboveTheFold`, `Directory2`, `LeftPane3`, `Listing5`, `NewFooterUpdate2`, `PDPFullPage`, `PLPAboveTheFold`, `Product4`, `Review`, `SSTopNavDesktopMenu`, `Top2`, `Top3`, `TopNav2`.
- **Mobile kit** (`ui_kits/mobile/`) — 360px storefront sections: `Body6`, `Cart`, `HomeAboveTheFoldMobile`, `Menu2`, `PDPAddedToCart`, `PLP`.

Names come from the source Figma layers and are kept as-is so they trace back to it, including where they read oddly (`ListItemListItem0`, `BuildingBlocks*`, `DAvatars23`). `GradientButton` renames the brand CTA to leave `Button` to the product family; `Icon`/`ProductIcon` rename `icon-geral`/`Icons/*`.

Sixteen further components (`Logo2`, `Buttons`, `Device`, `Icons`, `ProductIcons`, `UiActions`, `UiNavigation`, `Index`, `Index2`, `ClosingSlide`, `ColorPaletteSlide`, `LogoSlide`, `MockupSlide`, `ProductImagesSlide`, `TitleSlide`, `TypographySlide`) are showcase pages, not bundle exports — each is its own static specimen page, kept whole. Use the components above for anything you build; treat the showcase pages as reference reading only.

## Index

- `tokens.json` / `tokens.css` — every token, compiled; `components/bundle.js` exports every component on `window.SeedSupremeDesignSystem_06bac2`; `components/bundle.css` is the one stylesheet to load after `tokens.css`.
- `components/<Name>/README.md`, `.d.ts`, `preview.html` — guidelines, prop contract and a live example per component.
- `components/src/` — the source a rebuild of the bundle would start from.
- `fonts/` — the six shipped PP Agrandir weights.
- `assets/logo|imagery|devices|concepts/` — real brand assets, copied, never approximated.
- `ui_kits/website/README.md`, `ui_kits/mobile/README.md` — how the two kits' sections fit together as full pages.
- `uploads/partner-popups-spec.md` — a kept reference file from the standalone version; not part of the token or component system.

## Migrated from a legacy design system

This system was carried over from the standalone version on 2026-09-16. The part of this README the author wrote predates the move, so any file names in it are the old ones. Where things are now:

- `styles.css`, `tokens/fonts.css`, `tokens/colors.css`, `tokens/product-colors.css`, `tokens/typography.css`, `tokens/spacing.css`, … and 6 more (the global stylesheets) → `project/components/bundle.css`, with the token declarations moved to `project/tokens.json` (`project/tokens.css` is generated from them)
- `_ds_bundle.js` → `project/components/bundle.js`
- showcase pages, each kept whole as one component's preview (a page of examples, not an export of the bundle): `components/brand/logo.card.html` → `project/components/Logo2/preview.html`; `components/core/buttons.card.html` → `project/components/Buttons/preview.html`; `components/device/device.card.html` → `project/components/Device/preview.html`; `components/icons/icons.card.html` → `project/components/Icons/preview.html`; `components/ui-icons/product-icons.card.html` → `project/components/ProductIcons/preview.html`; `components/ui/ui-actions.card.html` → `project/components/UiActions/preview.html`; `components/ui/ui-navigation.card.html` → `project/components/UiNavigation/preview.html`; `ui_kits/mobile/index.html` → `project/components/Index/preview.html`; … and 8 more
- the migration report, which lists what did not come across: `project/assets/notes/MIGRATION-REPORT.md`

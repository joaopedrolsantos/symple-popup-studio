# Popup Studio — Seed Supreme is done

**Repo:** https://github.com/joaopedrolsantos/symple-popup-studio
Download it, double-click `templates/popup-studio.html`. No install, no build step, no login.

---

Popup Studio is one file holding every source-matched Klaviyo entry popup for all four brands.
Pick a brand → pick a traffic source → see the exact popup at desktop and mobile size → edit copy
and images → run QA → export build-ready HTML plus the trigger/offer handoff sheet.

**Seed Supreme is finished.** Homegrown was already done. **ILGM and USOA are still open** and
carry the brief's placeholder tokens — they're the next piece of work.

## What changed on Seed Supreme

**It now runs off the real brand design system,** imported from Claude Design rather than
hand-copied. Tokens, the brand book, the logo lockups and the actual PP Agrandir font files all
live in `design-system/`, and `design-system/IMPORT.md` maps every one onto the popup — including
every place we deliberately overrode the system, so nobody "fixes" those back later.

**Typography.** The deal line is real **PP Agrandir Wide Black Italic**, uppercase, with a white
glow. The before/after lines are **Work Sans Bold** in Tango Orange with an orange glow.

**Surface.** Pure black with a low-opacity orange bloom in the bottom-right corner, and the
brand's own **Texturelabs paper grain** over it at 50%. Each popup rotates the grain by its own
angle, so no two cards show the same marks in the same place.

**Partner logos** are real vector lockups now, no white container — Reddit, Leafly, Grow Weed
Easy, THC Farmer, Hey Abby, The Cannigma and i49. On the dark card they knock out to white,
except Reddit (its own orange-and-white lockup already reads on black) and THC Farmer, which
keeps its colours because it's a symbol rather than a wordmark.

**Imagery.** 15 images in the Seed Supreme library — 8 from Figma plus 7 generated in the brand's
studio style. Six PPC generic options, each idea available as an outdoor or a studio-black
reading. Every partner popup now carries an image matched to its source instead of the old
low-res crops.

## New things you can do in the studio

- **Bold a phrase in the proof sentence.** Click the first and last word, same as marking the
  deal in the headline. The bold run goes to full white against the muted rest — that contrast is
  what makes it read. There's a "Remove bold" button.
- **Change the strain on PPC popups.** Name and image are both editable, with a picker of Seed
  Supreme's own product photography from the design system, plus manual upload, plus a reset.
- **Swap any popup's image** from the library, or upload your own.

## Three things worth knowing

**Sizes in here are measured, not eyeballed.** Every approved headline gets rendered at each
candidate size across both breakpoints and both surfaces, and the largest one that holds the deal
to a stable wrap without stranding a word wins. Useful example: on mobile, 27px gives two lines
with 3px to spare and 29px gives three lines with 5px, but **30px** settles everything into a
clean three-line wrap with 51px. Bigger *and* safer — clearance doesn't move in a straight line
with size, because the wrap changes underneath it.

**Logo sizes are optical.** Matching logos by height doesn't work: Grow Weed Easy's letters fill
28% of its box, i49's fill 85%, so at the same height one looked tiny and the other enormous.
Each mark now carries a multiplier measured from how tall its shapes actually are.

**The file is ~5 MB** because every image and the typeface are embedded — that's what keeps it a
single double-clickable file with no server. It's near the practical ceiling. If the library
keeps growing we'll need to host the images instead, which costs the "works with no internet"
property. Worth deciding before it gets there.

## Before anything goes live

- **PP Agrandir licence.** It's a commercial Pangram Pangram face, embedded in the studio and in
  every export. Someone needs to confirm Seed Supreme's licence covers webfont use on live
  Klaviyo forms. This blocks deployment, not design.
- **Partner logo permissions** — each partner, in writing.
- **Three offer codes still marked "confirm":** `LEAFLY20`, `ILGM20`, `CANNIGMA20`.
- **ILGM is blocked on a site issue:** `ilgm.com` forces Chunk/Aleo and a lilac button onto every
  `.klaviyo-form` with `!important`, so an ILGM popup won't render as designed until that's
  resolved.

## Heads-up on the repo

It's public, and it includes the full PP Agrandir family, the Seed Supreme brand book and the
ClickUp review material. Fine for sharing internally — just worth knowing it's open to anyone
with the link before you post it anywhere wider.

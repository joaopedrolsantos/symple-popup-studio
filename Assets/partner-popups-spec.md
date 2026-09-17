# Co-branded popup specification by traffic source

Drafts rendered in `deliverable/popups/`. Each row is one Klaviyo form. Partner logo use needs the partner's permission before deployment.


## Seed Supreme

Existing entrance popup style (XrkCZ9): white card, orange button, heavy display face, photo panel. Three-step form stays (email, SMS, grow questions); only step one is shown.

| Source | Trigger rule | Line | Headline | Offer / code | Status |
|---|---|---|---|---|---|
| reddit | URL contains a_aid=moso-reddit (PAP, MosoEcom) | You found us on Reddit | The BOGO you clicked is below. Get the next one first. | Current BOGO (no code needed); GROWAGAIN if no BOGO is live | New. Reddit is the largest new-customer source (3,487 orders). Reddit is not a commercial partner, so no "official partner" wording. |
| leafly | URL contains a_aid=leafly or utm_source=leafly | Official partner of Leafly | 4 free Purple Kush seeds with your first order | GROWAGAIN (or LEAFLY20 if the Leafly agreement specifies a code; confirm) | New. Leafly editorial links reach strain pages; the popup is suppressed there and the PDP alert shows instead. |
| growweedeasy | URL contains a_aid=<Kelly O'Neal PAP id> or referrer forum.growweedeasy.com | Recommended by GrowWeedEasy | Welcome, GrowWeedEasy grower. Your free seeds are on us. | GROWFREE (existing partner code) | New. 1,331 orders; 23.5% repeat at 180 days. |
| thcfarmer | URL contains utm_campaign=bg12 / strains15 / 15offo (existing banner rules) | Hey THCFarmer | 15% off your first order with code THC15 | THC15 (existing banner code) | Replaces the three THC Farmer banners that open the non-existent form XbTe7W. |
| heyabby | URL contains a_aid=<Hamlet Chen PAP id> or landing path /hey-abby | Growing in an abby? | Seeds picked for the box, plus a first-order code | ABBYSUPREME (existing partner code) | New. 654 orders. Copy should not claim fit beyond what the PDP height figures support. |
| cannigma | URL contains a_aid=<Cannigma PAP id> (Nick P) | Cannigma reader? | 4 free Purple Kush seeds with your first order | GROWAGAIN (replaces the LETSGROW clone in the Cannigma welcome) | New on-site; the Cannigma-side popup already exists. |
| paid search | URL contains gclid= or a_aid=google-ads; not on product pages (PDP alert shows there) | Searching for a strain? | 4 free Purple Kush seeds with your first order | GROWAGAIN | Paid search has no partner logo (Google's and Meta's brands are not used as co-branding tiles). Replaces the PPC entrance form whose list has no flow. |
| i49 | URL contains utm_source=i49 (existing) | The new home of i49 Genetics | Welcome, i49 grower. 15% off with i4915. | i4915 (existing) | Exists (XwfCLB, 34.6% submit rate). Keep; restyle only. |

## Homegrown Cannabis Co

Existing popup style (WimVWV): white card, green pill button, wide caps display. The confirmshaming decline is replaced. Success buttons point to homegrowncannabis.com.

| Source | Trigger rule | Line | Headline | Offer / code | Status |
|---|---|---|---|---|---|
| almanac | URL contains a_aid=almanac (existing) | Hey Almanac reader | Ready to grow at home? A free 4-pack of Purple Haze Fem with your first order | HMG4PH | Exists (T9i4zR, 21.4% submit). Add a close button; stop double-writing to two lists. |
| leafly | URL contains a_aid=leafly or utm_source=leafly | Official partner of Leafly | A free 4-pack of Purple Haze Fem with your first order | HMG4PH | New. Leafly currently lands on /cheap-cannabis-seeds at 1.4 per 100. |
| thcfarmer | URL contains utm_campaign=gen1 / 2wv / nogerm (existing banner rules) | Hey THCFarmer | Skip 2 weeks of veg: 4 free seeds on clone orders $120+ | Existing THC Farmer clone offer; HMG4PH on seeds | Replaces the three banners that open the non-existent form XbTe7W. |
| reddit | URL contains a_aid=moso | You found us on Reddit | A free 4-pack of Purple Haze Fem with your first order | HMG4PH | New. Reddit lands on the homepage at 9.9 per 100; the popup adds the capture. |
| cannigma | URL contains a_aid=<Cannigma PAP id> | Cannigma reader? | First grow? Start with a free 4-pack of Purple Haze Fem | HMG4PH | New. Cannigma readers are learners; the success step links to the germination guide, not the BOGO page. |
| 420magazine | URL contains a_aid=<420 Magazine PAP id> or referrer 420magazine.com | 420 Magazine reader? | A free 4-pack of Purple Haze Fem with your first order | HMG4PH | New. 139 sessions at 1.4 per 100 today; small, so a before-and-after read. |
| meta | URL contains a_aid=facebook or utm_campaign=TWYMKT_AGEGATE (existing rule) | From our Facebook ad | The BOGO you tapped: buy one pack, get one free | The BOGO; META20 retired unless the ad promises 20% | Redesign of RTc3c8 (0 views, dead list). The ad lands on the homepage at 2.8 per 100; the popup restates the offer. |
| paid search | URL contains gclid= or a_aid=google-ads | Searching for seeds? | A free 4-pack of Purple Haze Fem with your first order | HMG4PH | No partner logo (paid search). Strain terms should reach strain pages first. |

## ILGM

STFNVH spec: mint #DCFCE7 card, Boldonse caps headline, Figtree body, red #DB0B16 button, Bergman illustration. Forms only; no flow edits.

| Source | Trigger rule | Line | Headline | Offer / code | Status |
|---|---|---|---|---|---|
| leafly | URL contains aff=<Leafly Affiliatly id> (a_aid after the PAP migration) | Official partner of Leafly | 5 free Granddaddy Purple Auto seeds with your first order | GDP5PACK | New. Leafly referrals convert at 0.84% today. |
| thcfarmer | URL contains utm_campaign=bgo / bgp / bgg (existing banner rules) | Welcome, THCFarmer | Buy 10, get 10 free on premium seeds | Buy 10 Get 10 (existing THC Farmer deal) | Replaces the three THC Farmer banners (V3iReH, VPKabs, VgL7RR) with a capture step. |
| comparethestrain | URL contains aff=<comparethestrain id>; link deep-linked to the strain page | Comparing strains? | The strain you picked, plus 5 free GDP Auto seeds | GDP5PACK | New. 815 sessions land on an empty /search at 0.12% today. |
| cannabissensei | URL contains aff=<Cannabis Sensei id> or referrer cannabissensei.com | Cannabis Sensei reader? | 5 free Granddaddy Purple Auto seeds with your first order | GDP5PACK | New. 767 sessions at 2.48%. |
| ilgmforum | URL contains ilgmforum.com (existing STFNVH rule, 15s delay, 5-day cookie) | Hey, forum grower | 5 free Granddaddy Purple Auto seeds with your first order | GDP5PACK (the arm 91% of forum visitors already see) | Restyle of STFNVH, the reference form. Its 3.64M reported views look like a counting artefact; check in the UI before reading its 0.01% rate. |
| iloveblog | URL contains ilovegrowingmarijuana.com (existing UL76TY rule) | Reading the blog? | Get the 72-hour germination checks, then 5 free GDP Auto seeds | Content first; GDP5PACK in email 4 (the learner branch) | Replaces the UL76TY A/B/C test (20% off vs GDP vs guarantee education) with the education-first arm; the blog embeds for the Grow Bible are repointed to the list the flow watches. |

## United Strains of America

Existing partner popup style (Leafly, Rzcwv9): flag panel, Oswald caps, red button, "official partner" line. One parameter scheme: a_aid=<partner> for all.

| Source | Trigger rule | Line | Headline | Offer / code | Status |
|---|---|---|---|---|---|
| leafly | URL contains a_aid=leafly (existing) | Official partner of Leafly | Welcome to United Strains of America | LEAFLY20 (existing) | Exists (Rzcwv9). Reference for the others; the decline line typo is fixed. |
| homegrown | URL contains a_aid=homegrown (was utm_source=homegrown) | Official partner of Homegrown Cannabis Co | Something to enjoy while your grow finishes | HOMEGROWNUSA20 (existing) | Exists (UwrRpL, 26% submit). Parameter standardised. |
| seedsupreme | URL contains a_aid=seedsupreme (was utm_source=seedsupreme; SS links use a_aid, which is why it had 1 view) | Official partner of Seed Supreme | Something to enjoy while your grow finishes | SUPREME20 (existing) | Exists but never fires (S97Vyc). Parameter fix makes it live. |
| ilgm | URL contains a_aid=ilgm | Official partner of ILGM | Something to enjoy while your grow finishes | ILGM20 (new code; confirm) | New. ILGM already sells the USOA range; /ilgm lander is 404 today. |
| cannigma | URL contains a_aid=0c44e0cc (Cannigma PAP id) | Cannigma reader? | Edibles first: 20 mg Delta-9 gummies, 20% off | CANNIGMA20 (new; confirm) | New. The Cannigma popup sits on recipe pages, so this one leads with gummies, not flower. |
| thcfarmer | URL contains a_aid=<THC Farmer PAP id> | Hey THCFarmer | Lab-tested THCa flower, 20% off your first order | NEW20 (existing THC Farmer code) | New popup; THCFarmer lands on /thca-deals at 2.5 per 100 today. |
| meta | URL contains a_aid=facebook or utm_source=meta on /free-purple-pre-roll | From our Facebook ad | Your free Purple Punch pre-roll | PURPLE (existing) | New. Currently utm_source=meta is excluded from every popup; 0 of 105 leads ordered in 10 days. |
| i49 | URL contains a_aid=i49 (was utm_source=i49) | Official partner of i49 | Welcome to United Strains of America | i4920 (existing) | Exists (VbbC7P, 37 views). Keep. |

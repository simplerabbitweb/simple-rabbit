#!/usr/bin/env python3
"""Generate county location pages for Simple Rabbit."""

import os

COUNTIES = [
    {
        "slug": "web-design-bergen-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Bergen County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Bergen County, NJ. Functional medicine, hormone care, concierge DPC, pelvic floor PT, and more. Built one practice at a time.",
        "canonical": "https://simplerabbit.studio/web-design-bergen-county-nj",
        "schema_locality": "Bergen County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Bergen County, NJ",
        "overline": "Bergen County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Bergen County.",
        "hero_sub": "Custom patient acquisition systems for the practices in Bergen County that do things differently. Built for the patient who has already decided she wants something better than the conventional system.",
        "problem_h2": "Why Bergen County private-pay practices stay invisible online.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Bergen County has one of the highest concentrations of private-pay women&rsquo;s health practices in New Jersey. Functional medicine physicians, hormone specialists, concierge primary care providers, pelvic floor physical therapists, lactation consultants &mdash; they are here, and patients are looking for them. The problem is that most of those practices are invisible to the patients running those searches.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Bergen County patients research before they book. Household incomes in towns like Ridgewood, Wyckoff, and Park Ridge mean patients can choose the provider who looks like the best fit, not just the one who takes their insurance. They are reading websites carefully. They are comparing. And when two practices in the same specialty have nearly identical websites &mdash; same stock photos, same root-cause language, same warm-beige palettes &mdash; the decision comes down to whoever had the most recent Google review.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">The fix is not more reviews or a better social media presence. It is a website that is specific enough to do the work those reviews are being asked to do. One that names the patient, describes her problem precisely, and communicates what this practice offers that the one two towns over does not. Bergen County patients will find the practices that invest in that specificity. The rest stay in the noise.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">I am based in Bergen County. I know the towns, the patient base, and the competitive landscape for this market. That context goes into the copy and into how the local SEO is structured. More on what moves the needle: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Hackensack", "Ridgewood", "Paramus", "Fort Lee", "Teaneck", "Englewood", "Fair Lawn", "Ramsey", "Mahwah", "Glen Rock", "Wyckoff", "Allendale", "Park Ridge", "Montvale", "Ho-Ho-Kus", "Woodcliff Lake", "Hillsdale", "Emerson", "Westwood", "River Vale"],
        "local_h2": "Practices across Bergen County.",
        "local_body": "Private-pay women&rsquo;s practices in Bergen County are spread across the county but tend to cluster in the more affluent suburban corridors &mdash; the Route 17 towns, the northeastern boroughs, and the Pascack Valley. Patients drive for the right provider. A well-built site with solid local SEO captures them from the full county, not just the zip code the practice is in.",
        "faq_local_q": "Do you work with practices in Bergen County specifically?",
        "faq_local_a": "Yes &mdash; Bergen County is home base. I am based here, which means I know the towns, the patient demographic, and the competitive landscape for this market in a way that informs the copy and the local SEO strategy. That said, Simple Rabbit works with private-pay women&rsquo;s wellness practices across the United States. Location is not a requirement to work together.",
    },
    {
        "slug": "web-design-essex-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Essex County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Essex County, NJ. Functional medicine, cash-pay psychiatry, concierge DPC, holistic gynecology, and more.",
        "canonical": "https://simplerabbit.studio/web-design-essex-county-nj",
        "schema_locality": "Essex County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Essex County, NJ",
        "overline": "Essex County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Essex County.",
        "hero_sub": "Custom patient acquisition systems for Essex County practices in functional medicine, hormone care, cash-pay psychiatry, holistic gynecology, and more. Built for the patient who is done settling.",
        "problem_h2": "Why Essex County private-pay practices lose patients they should have found.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">The Montclair and Maplewood corridors in Essex County have some of the most health-conscious, research-oriented patient demographics in New Jersey. These patients already understand functional medicine, integrative psychiatry, and cash-pay care models. They are not confused by out-of-pocket fees. What they are doing is comparing &mdash; and the practices that do not come across as the clear best option get skipped.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">At the same time, South Orange, Livingston, and Millburn draw patients with significant household incomes who are looking for concierge-level care and private-pay specialists they cannot find inside the conventional insurance system. These patients are searching on Google, reading every page on your site, and making a judgment based on what they find there. If what they find looks like every other practice in the area, the decision becomes arbitrary.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Essex County private-pay practices also face a specific challenge: there are enough practices in this market that generic websites genuinely cost patients. The practices doing well are the ones whose websites communicate clearly, rank for what their patients actually search, and give visitors a strong enough reason to reach out rather than click back and try the next result.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">Building a site that performs in Essex County means knowing who the patient is in this market and what she is looking for at the moment she finds your practice online. More on the strategy behind it: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Montclair", "Maplewood", "South Orange", "Livingston", "Millburn", "Short Hills", "West Orange", "Glen Ridge", "Bloomfield", "Verona", "Cedar Grove", "Nutley", "Caldwell", "West Caldwell", "Roseland", "Fairfield"],
        "local_h2": "Practices across Essex County.",
        "local_body": "Essex County&rsquo;s private-pay women&rsquo;s practices are concentrated in the Montclair-Maplewood-South Orange cluster, the Livingston-Millburn corridor, and the Caldwell-Verona area. Patients in this county are accustomed to researching their providers and expect a high-quality online presence. The practices that are growing here are the ones that look the part online.",
        "faq_local_q": "What makes Essex County patients different from patients in other markets?",
        "faq_local_a": "Essex County has one of the highest concentrations of health-literate, research-oriented patients in New Jersey. The Montclair and Maplewood areas in particular have patient bases that already understand integrative care, functional medicine, and cash-pay psychiatry. They are not confused by the model. They are comparing providers. That means the website has to do real differentiation work &mdash; it cannot just explain what functional medicine is. It has to make clear why this practice is the right one for this patient.",
    },
    {
        "slug": "web-design-hudson-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Hudson County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Hudson County, NJ. Concierge DPC, cash-pay psychiatry, pelvic floor PT, lactation, and more. Built for Hoboken and Jersey City's patient base.",
        "canonical": "https://simplerabbit.studio/web-design-hudson-county-nj",
        "schema_locality": "Hudson County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Hudson County, NJ",
        "overline": "Hudson County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Hudson County.",
        "hero_sub": "Custom patient acquisition systems for Hoboken, Jersey City, and surrounding Hudson County practices. Built for one of the most digitally-savvy patient bases in the region.",
        "problem_h2": "Why Hudson County private-pay practices get passed over online.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Hoboken and Jersey City have a younger, higher-income patient demographic that expects a polished digital experience from every service provider they use. These patients are on their phones, they compare options quickly, and they have been conditioned by years of well-designed apps and consumer experiences to judge quality by how something looks and reads before they ever walk in the door.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Private-pay practices in Hudson County &mdash; direct primary care memberships, cash-pay psychiatry, pelvic floor physical therapy, lactation consultants &mdash; are offering exactly what this patient base is looking for. The problem is that most of them have websites that were built for a different era, or built by someone who treated it like a brochure rather than a patient acquisition system. The practices are good. The websites do not show it.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Hudson County also has a high density of postpartum and preconception-age women in Hoboken, Jersey City, and Weehawken. Pelvic floor PT and lactation practices in particular are underserved by good websites in this market despite significant patient demand. The search volume is there. The practices doing the work are there. The websites are not keeping up.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">A Hudson County private-pay practice website has to meet a higher design standard and convert faster than practices in less competitive markets. More on what that looks like: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Hoboken", "Jersey City", "Weehawken", "Union City", "West New York", "Guttenberg", "North Bergen", "Secaucus", "Bayonne", "Kearny", "Harrison", "East Newark"],
        "local_h2": "Practices across Hudson County.",
        "local_body": "Hudson County&rsquo;s private-pay practices are concentrated in the Hoboken-Jersey City waterfront corridor and the surrounding towns. The patient base here is younger, more digital-first, and more likely to make a booking decision based entirely on what they find online. The bar for a professional, conversion-ready website is higher in this market than in most.",
        "faq_local_q": "Is the Hudson County patient base different from other parts of New Jersey?",
        "faq_local_a": "Yes, in a few meaningful ways. Hoboken and Jersey City have a younger-skewing patient demographic compared to Bergen or Morris County, with a higher concentration of women in their 20s and 30s in active life stages &mdash; preconception, prenatal, postpartum, early perimenopause. They are digitally native, comparison-shop naturally, and are quicker to decide and quicker to move on if the website does not grab them. The site has to be fast, clear, and look the part. That context goes directly into how the copy and design are built.",
    },
    {
        "slug": "web-design-morris-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Morris County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Morris County, NJ. Functional medicine, hormone care, concierge DPC, fertility support, and more.",
        "canonical": "https://simplerabbit.studio/web-design-morris-county-nj",
        "schema_locality": "Morris County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Morris County, NJ",
        "overline": "Morris County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Morris County.",
        "hero_sub": "Custom patient acquisition systems for Morris County practices in functional medicine, hormone care, concierge primary care, fertility support, and more. Built for the patient who has been looking for this practice for a long time.",
        "problem_h2": "Why Morris County private-pay practices rely too much on word of mouth.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Morris County has the affluence and the patient mindset for private-pay women&rsquo;s care. Towns like Chatham, Madison, Mendham, and the Summit-adjacent areas have household incomes that support out-of-pocket medical spending, and patients who are actively looking for practitioners who will treat them differently than a 15-minute conventional appointment. The problem is that too many practices in this county have built their patient base almost entirely on referrals, and never invested in an online presence that could do that same work at scale.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Referrals work until they stop. A patient who moves away, a referral partner who retires, a slow quarter when word-of-mouth dries up &mdash; these are the moments when the absence of an online patient acquisition system becomes visible. The practices in Morris County that are growing consistently are the ones that have both: a strong referral network and a website that can reach the patients who do not come from a referral.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Morris County also has a meaningful population of women searching for concierge and direct primary care, particularly in Morristown, Florham Park, and Parsippany. DPC is still underexplained online in this market &mdash; practices that take the time to walk patients through the model clearly on the website have a real advantage over those that assume patients already know how it works.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">A Morris County private-pay practice website has to work for the patient who came from a referral and for the patient who found you on Google. Both are real. More on building for both: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Morristown", "Chatham", "Madison", "Florham Park", "Morris Plains", "Randolph", "Parsippany", "Denville", "Mountain Lakes", "Boonton", "Mendham", "Chester", "Long Valley", "Rockaway", "Butler", "Mine Hill"],
        "local_h2": "Practices across Morris County.",
        "local_body": "Morris County&rsquo;s private-pay women&rsquo;s practices tend to be in the Morristown-Chatham-Madison corridor and in the more rural western towns like Mendham and Chester. Patients in this county are accustomed to driving for specialty care and will travel within the county and into adjacent Bergen or Somerset County for the right provider. A well-structured local SEO strategy captures that radius.",
        "faq_local_q": "My Morris County practice gets most of its patients from referrals. Why do I need a website?",
        "faq_local_a": "Referrals are excellent right up until they are not enough. A patient who is referred to you is still going to look at your website before they call &mdash; and if the site does not hold up, that referral can still be lost. More importantly, a well-built website reaches the patients who are not coming from your referral network: the ones who moved to the area recently, the ones whose primary care physician does not know about you, the ones who found your specialty on Google at 11pm and are trying to figure out if you are the right fit. That is a patient pool that referrals alone cannot reach.",
    },
    {
        "slug": "web-design-passaic-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Passaic County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Passaic County, NJ. Functional medicine, holistic gynecology, pelvic floor PT, and more.",
        "canonical": "https://simplerabbit.studio/web-design-passaic-county-nj",
        "schema_locality": "Passaic County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Passaic County, NJ",
        "overline": "Passaic County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Passaic County.",
        "hero_sub": "Custom patient acquisition systems for Passaic County practices in functional medicine, holistic gynecology, pelvic floor PT, and more. Built to compete for the patients who are already searching.",
        "problem_h2": "Why Passaic County private-pay practices compete against the wrong neighbors online.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Passaic County private-pay practices face an unusual challenge: they are geographically close to Bergen County, which means they are often competing for the same patients online without any of the local SEO advantages that come from being the clearly local option. A Wayne or Hawthorne practice can easily get buried under Bergen County results for the same specialty, because Bergen County practices tend to have better-built websites and stronger local search signals.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Wayne in particular has a strong patient base for private-pay women&rsquo;s health. It is a large township with significant household incomes and a patient population that is actively looking for functional medicine, hormone care, and holistic gynecology alternatives to the conventional system. The demand is real. The practices serving it are real. But without a website that makes Passaic County location signals clear, those patients are going to keep finding Bergen County practices first.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">The other dynamic in Passaic County: practices in the northern and more rural parts of the county &mdash; Ringwood, West Milford &mdash; serve a patient base that does not have many local options. When you are the closest specialist in a 20-mile radius, the website becomes even more important. It is often the only way a patient in that geography finds out you exist.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">Getting found in Passaic County requires clear local SEO that distinguishes the practice from its Bergen County neighbors while capturing the full county&rsquo;s search radius. More on how that works: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Wayne", "Clifton", "Passaic", "Paterson", "Totowa", "Little Falls", "Hawthorne", "Ringwood", "Pompton Lakes", "Pompton Plains", "West Milford", "Wanaque", "North Haledon"],
        "local_h2": "Practices across Passaic County.",
        "local_body": "Passaic County private-pay women&rsquo;s practices are concentrated in Wayne and the southern townships, with some in the more rural northern communities like Ringwood and West Milford. Practices in the southern corridor compete with Bergen County for online visibility and need strong local differentiation. Practices in the northern parts serve wider geographies and are often the only provider of their type in the area.",
        "faq_local_q": "How does a Passaic County practice compete with Bergen County practices online?",
        "faq_local_a": "The key is building clear, accurate local SEO signals that anchor the practice to Passaic County specifically &mdash; not just by mentioning Wayne or Clifton in the copy, but by structuring the entire site around the local searches Passaic County patients actually run. This includes title tags, Google Business Profile alignment, and service page structure that tells Google exactly where this practice is and who it serves. A well-built Passaic County site can absolutely rank above Bergen County practices for the searches that originate in Passaic County.",
    },
    {
        "slug": "web-design-sussex-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Sussex County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Sussex County, NJ. Functional medicine, holistic gynecology, lactation care, and more. Built for practices that serve wider geographic areas.",
        "canonical": "https://simplerabbit.studio/web-design-sussex-county-nj",
        "schema_locality": "Sussex County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Sussex County, NJ",
        "overline": "Sussex County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Sussex County.",
        "hero_sub": "Custom patient acquisition systems for Sussex County practices. Built for the practitioners who serve patients across a wide geography because there are not many options for the care they provide.",
        "problem_h2": "Why private-pay practices in rural counties need better websites than anyone.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Sussex County does not have a dense cluster of private-pay women&rsquo;s health practices. That is exactly why the ones that do exist need websites that work harder. A functional medicine physician in Newton or a lactation consultant in Sparta is often the only option for that specialty within a significant drive radius. Patients will travel for the right provider &mdash; but they have to find the practice first.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Rural and semi-rural private-pay practices have a particular SEO challenge: local search volumes are lower, which means the competition for those searches is different, and the geographic radius that a practice needs to appear in is much larger. A Sussex County practice should be visible to patients in western Morris County, Warren County, and even parts of Orange County, NY &mdash; not just the immediate township. That requires intentional page structure and local SEO foundations built for a wider radius.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">The other dynamic in lower-density markets: word of mouth moves faster but reaches fewer people. Many Sussex County private-pay practices have strong local reputations but no digital footprint that matches. Patients who were not born here, who moved from urban areas, or who are searching for a specialist they heard about from a friend in another county &mdash; these patients go online. If the practice is not there, they find someone else.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">Building for a lower-density county requires a different SEO approach than building for a Bergen or Essex County practice. More on the underlying strategy: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Newton", "Sparta", "Vernon", "Franklin", "Hamburg", "Andover", "Branchville", "Hardyston", "Wantage", "Montague", "Fredon", "Lafayette"],
        "local_h2": "Practices across Sussex County.",
        "local_body": "Sussex County private-pay women&rsquo;s practices are spread across the county&rsquo;s towns and townships. Most serve patients from a wider radius than their immediate municipality &mdash; drawing from across Sussex County and into adjacent Warren, Morris, and Pike County (PA) patient bases. A well-built website captures that full geographic reach, not just the immediate area.",
        "faq_local_q": "I am the only functional medicine practice in my part of Sussex County. Does that make SEO less important?",
        "faq_local_a": "It makes it more important in a different way. When you are the only option in a specialty for a wide area, the website becomes the primary way patients who are searching online find you at all. Many of those patients are not going to be referred to you &mdash; they are going to run a Google search, find your practice, and decide whether to drive 30 minutes based entirely on what they see there. If the site does not communicate clearly who you serve and what you offer, those patients choose a provider in a neighboring county instead of making the drive to you.",
    },
    {
        "slug": "web-design-warren-county-nj",
        "title": "Web Design for Women's Private-Pay Practices in Warren County, NJ | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Warren County, NJ. Functional medicine, holistic gynecology, lactation care, and more. Built to reach patients across a wide geography.",
        "canonical": "https://simplerabbit.studio/web-design-warren-county-nj",
        "schema_locality": "Warren County",
        "schema_region": "NJ",
        "schema_country": "US",
        "schema_area": "Warren County, NJ",
        "overline": "Warren County, NJ &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Warren County.",
        "hero_sub": "Custom patient acquisition systems for Warren County&rsquo;s private-pay women&rsquo;s practices. Built for practitioners who serve a wide geographic area and whose website is often the first thing a patient has ever heard of them.",
        "problem_h2": "Why Warren County private-pay practices are harder to find than they should be.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Warren County is one of the least-saturated markets in New Jersey for private-pay women&rsquo;s health. There are functional medicine providers, holistic gynecologists, and lactation consultants here &mdash; but there are not many of them, and many of the ones that exist have websites that were built years ago, updated rarely, and are not structured to do any real patient acquisition work.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">That creates two kinds of patients a Warren County private-pay practice can reach: those who already live in the county and are looking for a local option, and those who live in adjacent counties &mdash; Hunterdon, Sussex, Northampton (PA), Lehigh (PA) &mdash; and are willing to cross county lines for a specialist they cannot find closer to home. A well-built website with the right local SEO foundations can capture both groups. Most Warren County practice websites are reaching neither.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">The opportunity in a market like Warren County is real. Low competition in search means that a practice with a properly built website can rank for relevant searches with less effort than it would take in a denser market. The bar is lower. The practices that clear it capture patients that competitors in other counties are not even trying to reach from this geography.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">More on what it takes to rank in a rural or low-density county: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Hackettstown", "Washington", "Phillipsburg", "Belvidere", "Oxford", "Hope", "Blairstown", "Mansfield", "Allamuchy", "Lopatcong", "Pohatcong", "Harmony"],
        "local_h2": "Practices across Warren County.",
        "local_body": "Warren County private-pay women&rsquo;s practices typically serve patients from across the county and into adjacent areas in New Jersey and Pennsylvania. Hackettstown and Washington are the largest population centers, but patients in this county are accustomed to driving for specialized care. A website built to capture the full geographic radius of potential patients &mdash; not just the immediate township &mdash; can significantly expand a practice&rsquo;s reach.",
        "faq_local_q": "Is there enough demand in Warren County for a private-pay women's health practice to be viable online?",
        "faq_local_a": "Yes &mdash; but the demand comes from a wider geography than it does in denser counties. Warren County on its own has lower search volume, but a practice positioned to serve patients from across Warren, Hunterdon, Sussex, and the adjacent PA counties is drawing from a much larger patient pool. The website needs to be structured to capture that geographic reach, with clear location signals that tell Google exactly where the practice is and how far patients travel to get there. In a low-competition market, a well-built site can rank faster and with less ongoing effort than it would in Bergen or Essex County.",
    },
    {
        "slug": "web-design-rockland-county-ny",
        "title": "Web Design for Women's Private-Pay Practices in Rockland County, NY | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Rockland County, NY. Functional medicine, hormone care, holistic gynecology, pelvic floor PT, and more.",
        "canonical": "https://simplerabbit.studio/web-design-rockland-county-ny",
        "schema_locality": "Rockland County",
        "schema_region": "NY",
        "schema_country": "US",
        "schema_area": "Rockland County, NY",
        "overline": "Rockland County, NY &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Rockland County.",
        "hero_sub": "Custom patient acquisition systems for Rockland County practices. Built for the practices that sit at the intersection of the New York and New Jersey patient markets and are not reaching either one the way they should.",
        "problem_h2": "Why Rockland County private-pay practices fall between two markets.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Rockland County occupies an unusual position. It is close enough to Bergen County, NJ that practices in Nyack and Pearl River compete for the same patients as practices in Mahwah and Park Ridge. It is close enough to Westchester County, NY that patients in New City and Suffern are comparing options on both sides of the county line. A Rockland County private-pay practice can draw from a substantial combined patient base &mdash; but only if the website is built to reach it.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Most Rockland County private-pay practices are built for one market or the other. They target Bergen County patients or they target Westchester patients, and they do not structure their online presence to reach the full geographic range available to them. That is a real opportunity left on the table, particularly for specialties like functional medicine, hormone care, and pelvic floor physical therapy where patients are accustomed to driving for the right provider.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Rockland County also has a patient demographic that spans a wide range of backgrounds and income levels &mdash; from the affluent patient base in the Nyack-area towns to the Orthodox and Hasidic communities in Spring Valley and Monsey that have their own considerations for women&rsquo;s health care. A thoughtfully written site that speaks to this variety without being generic is a meaningful competitive advantage in this market.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">Building a Rockland County private-pay practice site requires thinking about geographic reach across two states and several county markets. More on the strategy: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["Nyack", "New City", "Spring Valley", "Suffern", "Nanuet", "Stony Point", "Pearl River", "Tappan", "Orangeburg", "Blauvelt", "Garnerville", "Haverstraw", "Congers", "West Nyack"],
        "local_h2": "Practices across Rockland County.",
        "local_body": "Rockland County private-pay women&rsquo;s practices span the county from Nyack in the east to Suffern in the west, with Spring Valley and New City as the major population centers. Practices here can realistically serve patients from across Rockland, southern Orange County, northern Bergen County (NJ), and parts of Westchester. A properly structured site and local SEO strategy reaches that full radius.",
        "faq_local_q": "My Rockland County practice draws patients from both New Jersey and New York. How does that affect the website and SEO?",
        "faq_local_a": "It is a genuine advantage if the site is built to reflect it. That means including clear location signals for Rockland County itself while structuring service pages to capture searches from adjacent markets &mdash; Bergen County searches, Westchester searches, and Orange County searches that a Rockland County practice can realistically convert. It also means making sure the Google Business Profile and the website are fully aligned, since patients crossing state lines to find a specialist are often relying on Google Maps as much as organic search results.",
    },
    {
        "slug": "web-design-westchester-county-ny",
        "title": "Web Design for Women's Private-Pay Practices in Westchester County, NY | Simple Rabbit",
        "meta_desc": "Custom patient acquisition systems for private-pay women's practices in Westchester County, NY. Functional medicine, hormone care, concierge DPC, fertility, pelvic floor PT, and more.",
        "canonical": "https://simplerabbit.studio/web-design-westchester-county-ny",
        "schema_locality": "Westchester County",
        "schema_region": "NY",
        "schema_country": "US",
        "schema_area": "Westchester County, NY",
        "overline": "Westchester County, NY &middot; Private-Pay Women&rsquo;s Practices",
        "h1": "Web design for private-pay women&rsquo;s practices in Westchester County.",
        "hero_sub": "Custom patient acquisition systems for the Westchester County practices doing serious work. Built for one of the most research-oriented, high-expectation patient bases in the country.",
        "problem_h2": "Why Westchester County private-pay practices cannot afford a generic website.",
        "problem_body": """<p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Westchester County is one of the most competitive markets in the country for private-pay women&rsquo;s health. Scarsdale, Chappaqua, Bronxville, and Larchmont have household incomes that support premium out-of-pocket care, and patient demographics that are deeply familiar with functional medicine, concierge primary care, and integrative approaches to women&rsquo;s health. These patients are not being introduced to the concept. They are choosing between multiple qualified providers in the same specialty.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">In a market this sophisticated, a generic website is not just a missed opportunity &mdash; it is a signal. Patients in Westchester who are paying $5,000 to $15,000 a year out of pocket for their healthcare are making judgments about clinical quality based partly on what the website communicates. A site that looks like it was built with a template and copy that reads like it was written for any practice is, at some level, telling that patient that this provider does not invest in the details. That matters in this market.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">The Westchester fertility and preconception niche is particularly active. Tarrytown, White Plains, and the surrounding towns have a meaningful population of women who have been through the conventional reproductive endocrinology pathway and are looking for a holistic or integrative approach to preconception care. The search volume for these patients is real and largely unmet by well-built practice websites in the county.</p>

    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">Competing in the Westchester market requires a website that reflects the investment the practice has made in the quality of care it provides. More on what that looks like in practice: <a href="/blog/local-seo-for-private-pay-practices" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">local SEO for private-pay practices</a>.</p>""",
        "towns": ["White Plains", "Scarsdale", "Larchmont", "Mamaroneck", "Chappaqua", "Briarcliff Manor", "Pleasantville", "Ardsley", "Tarrytown", "Dobbs Ferry", "Rye", "Harrison", "Rye Brook", "Bronxville", "Yonkers", "New Rochelle", "Mount Kisco", "Katonah"],
        "local_h2": "Practices across Westchester County.",
        "local_body": "Westchester County private-pay women&rsquo;s practices are spread across one of the largest and most affluent suburban counties in the country. The southern corridor &mdash; Bronxville, Larchmont, Mamaroneck, Rye &mdash; is dense with high-income patients. The northern towns like Chappaqua, Katonah, and Mount Kisco have their own patient populations with slightly different demographics but equally strong willingness to spend on out-of-pocket care. A well-built site captures the full county.",
        "faq_local_q": "Westchester is a competitive market. How does a private-pay practice stand out there?",
        "faq_local_a": "Specificity. Westchester patients are sophisticated enough to immediately notice generic copy and stock photos. The practices that hold their attention are the ones that are precise about who they serve, specific about what they do differently, and clear about what the patient&rsquo;s experience will look like. That is a copy and design problem before it is an SEO problem. The local SEO foundations matter &mdash; getting found &mdash; but it is the quality and specificity of what the patient sees after they click that determines whether they book.",
    },
]


SPECIALTIES_BAR = """<!-- OTHER PRACTICES -->
<div class="sp" style="padding:40px 48px;background:var(--white);border-top:1px solid var(--light-border);">
  <div style="max-width:1100px;margin:0 auto;">
    <p style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--mid);margin-bottom:16px;">Specialties we build for</p>
    <div style="display:flex;gap:32px;flex-wrap:wrap;">
      <a href="/functional-medicine-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Functional &amp; integrative medicine</a>
      <a href="/menopause-practice-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Women&rsquo;s hormone and menopause care</a>
      <a href="/holistic-gynecology-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Holistic gynecology</a>
      <a href="/concierge-primary-care-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Concierge and direct primary care</a>
      <a href="/cash-pay-psychiatry-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Cash-pay psychiatry and mental health</a>
      <a href="/fertility-practice-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Fertility and preconception care</a>
      <a href="/pelvic-floor-physical-therapy-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Pelvic floor physical therapy</a>
      <a href="/lactation-postnatal-web-design" style="font-family:var(--font-display);font-size:15px;color:var(--black);text-decoration:none;">Lactation and postnatal care</a>
    </div>
  </div>
</div>"""


def make_towns_grid(towns):
    items = "\n".join(
        f'      <div class="town-item">{t}</div>' for t in towns
    )
    return f"""    <div class="towns-grid">
{items}
    </div>"""


def make_page(c):
    towns_grid = make_towns_grid(c["towns"])
    schema_area_served = "\n".join(
        f'    "{t}",' for t in c["towns"]
    ).rstrip(",")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c["title"]}</title>
  <meta name="description" content="{c["meta_desc"]}">
  <meta property="og:title" content="{c["title"]}">
  <meta property="og:description" content="{c["meta_desc"]}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{c["canonical"]}">
  <meta property="og:image" content="https://simplerabbit.studio/leann-services.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{c["canonical"]}">
  <link rel="icon" type="image/jpeg" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Raleway:wght@300;400;500;600&display=swap" rel="stylesheet">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-77EEVJRJJD"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-77EEVJRJJD');</script>
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    :root{{
      color-scheme:light only;
      --black:#000;--white:#fff;--tone:#E2D8D6;
      --accent:#AA737D;--accent-dark:#8a5d66;--accent-light:#D7AF99;
      --mid:#111;--dark:#333;--light-border:#dfe0e1;
      --font-display:'Raleway',sans-serif;
      --font-body:'DM Sans',system-ui,sans-serif;
      --font-mono:'DM Sans',sans-serif;
    }}
    html{{overflow-x:hidden;}}
    body{{font-family:var(--font-body);color:var(--black);background:var(--white);-webkit-font-smoothing:antialiased;overflow-x:hidden;}}
    h1,h2,h3{{font-family:var(--font-display);letter-spacing:-1px;font-weight:400;}}
    a{{color:inherit;}}
    .reveal{{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}}
    .reveal.visible{{opacity:1;transform:translateY(0);}}
    .nav{{position:sticky;top:0;background:#474D73;border-bottom:1px solid rgba(255,255,255,0.1);z-index:100;}}
    .nav-inner{{max-width:1280px;margin:0 auto;padding:0 72px;display:flex;align-items:center;justify-content:space-between;height:88px;}}
    .nav-links{{display:flex;align-items:center;gap:32px;}}
    .nav-links a{{font-size:14px;color:#fff;text-decoration:none;transition:color 0.2s;}}
    .nav-links a:hover{{color:var(--white);}}
    .nav-cta{{background:var(--white)!important;color:var(--black)!important;padding:10px 24px;font-size:13px;font-weight:500;transition:background 0.2s!important;}}
    .nav-cta:hover{{background:#e8e8e8!important;color:var(--black)!important;}}
    .overline{{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);margin-bottom:16px;display:block;}}
    .btn-primary{{display:inline-block;background:#474D73;color:var(--white);padding:14px 40px;font-size:14px;font-weight:500;letter-spacing:0.5px;text-decoration:none;font-family:var(--font-body);border:none;cursor:pointer;transition:background 0.2s;}}
    .btn-primary:hover{{background:var(--dark);}}
    .btn-secondary{{display:inline-block;background:transparent;color:#474D73;padding:13px 38px;font-size:14px;font-weight:500;letter-spacing:0.5px;text-decoration:none;font-family:var(--font-body);border:1px solid #474D73;cursor:pointer;transition:background 0.2s,color 0.2s;}}
    .btn-secondary:hover{{background:#474D73;color:var(--white);}}
    .sp{{padding-left:48px;padding-right:48px;}}
    .faq-row{{border-bottom:1px solid var(--light-border);padding:36px 0;}}
    .faq-row:first-child{{border-top:1px solid var(--light-border);}}
    .process-step{{transition:background 0.2s;}}
    .process-step:hover{{background:#d8cec9;}}
    .include-list{{list-style:none;margin-top:32px;border-top:1px solid var(--light-border);}}
    .include-list li{{padding:16px 0;border-bottom:1px solid var(--light-border);font-size:16px;line-height:1.6;color:var(--dark);display:flex;align-items:baseline;gap:12px;}}
    .include-list li::before{{content:'→';font-family:var(--font-mono);font-size:12px;color:var(--accent);flex-shrink:0;}}
    .towns-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--light-border);margin-top:32px;}}
    .town-item{{background:var(--white);padding:14px 18px;font-size:14px;color:var(--dark);font-family:var(--font-body);}}
    footer{{display:block;padding:0;border:none;}}
    .footer-link{{font-size:12px;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s;}}
    .footer-link:hover{{color:#fff;}}
    .hamburger{{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:4px;}}
    .hamburger span{{display:block;width:22px;height:2px;background:var(--white);transition:transform 0.3s,opacity 0.3s;}}
    .hamburger.open span:nth-child(1){{transform:translateY(7px) rotate(45deg);}}
    .hamburger.open span:nth-child(2){{opacity:0;}}
    .hamburger.open span:nth-child(3){{transform:translateY(-7px) rotate(-45deg);}}
    .mobile-nav{{display:none;position:fixed;top:64px;left:0;right:0;bottom:0;background:#474D73;z-index:99;flex-direction:column;overflow-y:auto;border-top:1px solid rgba(255,255,255,0.1);}}
    .mobile-nav.open{{display:flex;}}
    .mobile-nav a{{font-size:16px;color:#fff;text-decoration:none;padding:20px 24px;border-bottom:1px solid rgba(255,255,255,0.1);font-family:var(--font-body);}}
    .mobile-nav a:hover{{color:var(--white);}}
    .mobile-nav a.mobile-nav-cta{{background:var(--white);color:var(--black)!important;text-align:center;font-weight:500;border-bottom:none!important;margin:16px 24px;display:block;}}
    .mobile-nav a.mobile-nav-cta:hover{{background:#e8e8e8!important;color:var(--black)!important;}}
    @media(max-width:900px){{
      .nav-inner{{padding:0 24px;}}
      .sp{{padding-left:24px!important;padding-right:24px!important;}}
      .how-it-works-grid{{grid-template-columns:1fr!important;}}
      .offer-grid{{grid-template-columns:1fr!important;gap:40px!important;}}
      .towns-grid{{grid-template-columns:repeat(2,1fr)!important;}}
      .footer-social-links{{flex-wrap:wrap!important;gap:12px!important;}}
      .cta-pair{{flex-direction:column!important;align-items:center!important;}}
    }}
    @media(max-width:768px){{
      .hamburger{{display:flex!important;}}
      .nav-links{{display:none!important;}}
      .nav-inner a img{{max-height:44px!important;}}
      .inner-hero{{padding:64px 24px 72px!important;}}
    }}
    @media(max-width:600px){{
      .towns-grid{{grid-template-columns:1fr 1fr!important;}}
      footer > div{{padding-left:20px!important;padding-right:20px!important;}}
      .footer-social-links{{flex-wrap:wrap!important;gap:12px!important;}}
    }}
    @media(min-width:901px){{#announcement-banner a{{font-size:15px!important;}}#announcement-banner a span:last-child{{font-size:14px!important;}}}}
  </style>
  <noscript><style>.reveal{{opacity:1!important;transform:none!important;}}</style></noscript>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Simple Rabbit",
  "description": "Simple Rabbit builds custom patient acquisition systems for private-pay women's wellness practices in {c["schema_area"]} and across the United States.",
  "url": "{c["canonical"]}",
  "telephone": "+15514862779",
  "email": "hello@simplerabbit.studio",
  "image": "https://simplerabbit.studio/leann-services.jpg",
  "logo": "https://simplerabbit.studio/logo.png",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Bergen County",
    "addressRegion": "NJ",
    "addressCountry": "US"
  }},
  "areaServed": [
{schema_area_served}
  ],
  "priceRange": "$$",
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "Web Design and Patient Acquisition Services",
    "itemListElement": [
      {{
        "@type": "Offer",
        "itemOffered": {{
          "@type": "Service",
          "name": "Custom Patient Acquisition Systems for Women's Private-Pay Practices in {c["schema_area"]}",
          "description": "Strategy, website design, copywriting, local SEO, and email nurture for private-pay women's wellness practices in {c["schema_area"]}.",
          "serviceType": "Web Design and Patient Acquisition"
        }}
      }}
    ]
  }}
}}
</script>
</head>
<body>

<!-- ANNOUNCEMENT BANNER -->
<div id="announcement-banner" style="background:#829AAB;padding:11px 24px;text-align:center;position:relative;">
  <a href="/fully-booked" style="font-size:13px;color:#fff;font-family:'DM Sans',system-ui,sans-serif;text-decoration:none;display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center;">
    <span style="font-weight:400;opacity:0.88;">Free 5-day email series &rarr;</span>
    <strong style="font-weight:600;letter-spacing:0.1px;">5 Days to a Fully-Booked Practice</strong>
    <span style="background:rgba(255,255,255,0.18);padding:2px 10px;font-size:12px;letter-spacing:0.5px;border:1px solid rgba(255,255,255,0.3);">Get it free</span>
  </a>
</div>

<!-- NAV -->
<nav class="nav">
  <div class="nav-inner">
    <a href="/"><img src="/logo.png" alt="Simple Rabbit" style="max-height:88px;display:block;"></a>
    <div class="nav-links">
      <a href="/about">About</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/services">Services</a>
      <a href="/articles">Articles</a>
      <a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" class="nav-cta">Book a Clarity Call</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mobile-nav" id="mobile-nav">
  <a href="/about">About</a>
  <a href="/portfolio">Portfolio</a>
  <a href="/services">Services</a>
  <a href="/articles">Articles</a>
  <a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" class="mobile-nav-cta">Book a Clarity Call</a>
</div>

<!-- HERO -->
<section style="background:#474D73;padding:100px 72px 100px;" class="inner-hero">
  <div style="max-width:840px;">
    <span class="overline" style="color:#E2D8D6;">{c["overline"]}</span>
    <h1 style="font-size:clamp(36px,5vw,64px);line-height:1.05;letter-spacing:-2px;color:#fff;font-weight:400;margin-bottom:28px;">{c["h1"]}</h1>
    <p style="font-size:clamp(17px,1.8vw,21px);line-height:1.7;color:rgba(255,255,255,0.82);max-width:660px;margin-bottom:40px;">{c["hero_sub"]}</p>
    <a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" class="btn-primary" style="background:var(--white);color:var(--black);">Tell me about your practice &rarr;</a>
  </div>
</section>


<!-- SECTION 1: PROBLEM -->
<section class="reveal sp" style="padding:100px 48px;background:var(--white);border-bottom:1px solid var(--light-border);">
  <div style="max-width:840px;margin:0 auto;">
    <span class="overline">The Problem</span>
    <h2 style="font-size:clamp(26px,3vw,40px);line-height:1.15;margin-bottom:36px;">{c["problem_h2"]}</h2>

    {c["problem_body"]}

    <a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" class="btn-primary">Book a Clarity Call &rarr;</a>
  </div>
</section>


<!-- SECTION 2: WHAT'S INCLUDED -->
<section class="reveal sp" style="padding:100px 48px;background:#FAF8F4;border-bottom:1px solid var(--light-border);">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;" class="offer-grid">

    <div>
      <span class="overline">The Build</span>
      <h2 style="font-size:clamp(26px,3vw,40px);line-height:1.15;margin-bottom:28px;">What goes into a patient acquisition system for a private-pay practice.</h2>

      <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Every Simple Rabbit engagement starts with strategy. Before any website is designed, we map out how patients will find the practice, what the website has to communicate to convert them, and how email keeps the relationship going with patients who are not ready to book yet. The build flows from that strategy &mdash; it is not a template filled in with your content.</p>

      <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Copywriting is central to the work. The pages are written for the specific patient the practice serves &mdash; her search terms, her concerns, her hesitations, and her decision-making process. Copy written this way does two things at once: it gives Google the signals it needs to rank the page, and it gives the patient a reason to keep reading and reach out.</p>

      <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Local SEO foundations are built in from the start, not retrofitted. That means properly structured service pages, location signals that are accurate and consistent across the site, and a Google Business Profile that aligns with what the website says. Practices that have these foundations in place consistently outperform those that do not over time.</p>

      <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:24px;">Email nurture is part of the system. Most practice websites lose the patients who visit, read everything, and leave without booking. An email strategy gives those patients a lower-barrier entry point and keeps the practice visible until they are ready. Depending on the package, this is delivered as a blueprint or as a fully built workflow.</p>

      <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:36px;">After launch, an ongoing care plan handles hosting, security, updates, and content changes from one place. One point of contact throughout, start to finish. A full overview of what is available is on the <a href="/services" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">services page</a>.</p>

      <a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" class="btn-primary">Book a Clarity Call &rarr;</a>
    </div>

    <div>
      <span class="overline" style="opacity:0;">spacer</span>
      <h3 style="font-family:var(--font-display);font-size:18px;letter-spacing:-0.5px;font-weight:400;margin-bottom:8px;margin-top:16px;">Every engagement includes:</h3>
      <ul class="include-list">
        <li>Custom strategy built for your practice and your patients</li>
        <li>Strategic copywriting written for your ideal patient</li>
        <li>Local SEO foundations and on-page structure</li>
        <li>Google Business Profile review and alignment</li>
        <li>Email nurture strategy (blueprint or full build)</li>
        <li>Booking and inquiry conversion paths</li>
        <li>One point of contact &mdash; no project managers, no handoffs</li>
        <li>Ongoing hosting, security, and site care after launch</li>
      </ul>
      <p style="margin-top:28px;font-family:var(--font-mono);font-size:11px;letter-spacing:1.5px;color:var(--accent);">Every website is built on WordPress, a platform you own and can grow with.</p>
    </div>

  </div>
</section>


<!-- SECTION 3: LOCAL TOWNS -->
<section class="reveal sp" style="padding:100px 48px;background:var(--white);border-bottom:1px solid var(--light-border);">
  <div style="max-width:1100px;margin:0 auto;">
    <span class="overline">Serving {c["schema_area"]}</span>
    <h2 style="font-size:clamp(26px,3vw,40px);line-height:1.15;margin-bottom:24px;">{c["local_h2"]}</h2>
    <p style="font-size:17px;line-height:1.85;color:var(--dark);max-width:740px;">{c["local_body"]}</p>
{towns_grid}
  </div>
</section>


<!-- SECTION 4: HOW IT WORKS -->
<section class="reveal sp" style="padding:100px 48px;background:#FAF8F4;border-bottom:1px solid var(--light-border);">
  <div style="max-width:1100px;margin:0 auto;">
    <span class="overline">How It Works</span>
    <h2 style="font-size:clamp(26px,3vw,38px);line-height:1.15;margin-bottom:16px;">Three steps from first call to launched system.</h2>
    <p style="font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:56px;max-width:680px;">No project managers, no handoffs, no wondering where things stand.</p>

    <div class="how-it-works-grid" style="display:grid;grid-template-columns:repeat(3,1fr);">

      <div class="process-step" style="padding:40px;">
        <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;color:var(--accent);display:block;margin-bottom:14px;">01</span>
        <h3 style="font-size:20px;letter-spacing:-0.5px;margin-bottom:12px;font-weight:400;">Discovery and strategy</h3>
        <p style="font-size:17px;line-height:1.75;color:var(--dark);">We start with a real conversation about your practice, your patients, and what the site needs to do. From there, I map out the strategy: how patients will find you, what your website has to communicate, and how email keeps them engaged. You get a clear plan before any writing or build work begins.</p>
      </div>

      <div class="process-step" style="padding:40px;">
        <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;color:var(--accent);display:block;margin-bottom:14px;">02</span>
        <h3 style="font-size:20px;letter-spacing:-0.5px;margin-bottom:12px;font-weight:400;">Build and consult</h3>
        <p style="font-size:17px;line-height:1.75;color:var(--dark);">Depending on your package, I build the pieces that need building &mdash; the website, the email workflow, the conversion paths &mdash; and consult on the rest. You see the work as it comes together, with check-ins at each stage. Most website builds run six to ten weeks from kickoff to a working site.</p>
      </div>

      <div class="process-step" style="padding:40px;">
        <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;color:var(--accent);display:block;margin-bottom:14px;">03</span>
        <h3 style="font-size:20px;letter-spacing:-0.5px;margin-bottom:12px;font-weight:400;">Launch and care</h3>
        <p style="font-size:17px;line-height:1.75;color:var(--dark);">We launch when the site is ready, not when a deadline says so. The day it goes live, your care plan starts. Hosting, security, updates, and content changes are handled from there. You stay focused on your patients.</p>
      </div>

    </div>
  </div>
</section>


<!-- SECTION 5: FAQ -->
<section class="reveal sp" style="padding:100px 48px;background:var(--white);border-bottom:1px solid var(--light-border);">
  <div style="max-width:840px;margin:0 auto;">
    <span class="overline">Common Questions</span>
    <h2 style="font-size:clamp(26px,3vw,38px);line-height:1.15;margin-bottom:56px;">What practice owners ask before booking.</h2>

    <div class="faq-row">
      <p style="font-family:var(--font-display);font-size:clamp(17px,1.8vw,22px);letter-spacing:-0.5px;line-height:1.3;margin-bottom:16px;font-weight:400;">{c["faq_local_q"]}</p>
      <p style="font-size:17px;line-height:1.8;color:var(--dark);">{c["faq_local_a"]}</p>
    </div>

    <div class="faq-row">
      <p style="font-family:var(--font-display);font-size:clamp(17px,1.8vw,22px);letter-spacing:-0.5px;line-height:1.3;margin-bottom:16px;font-weight:400;">What kinds of practices do you build for?</p>
      <p style="font-size:17px;line-height:1.8;color:var(--dark);">Private-pay women&rsquo;s wellness practices. <a href="/functional-medicine-web-design" style="color:inherit;text-decoration:none;">Functional and integrative medicine</a>, <a href="/menopause-practice-web-design" style="color:inherit;text-decoration:none;">hormone and menopause care</a>, <a href="/holistic-gynecology-web-design" style="color:inherit;text-decoration:none;">holistic gynecology</a>, <a href="/concierge-primary-care-web-design" style="color:inherit;text-decoration:none;">concierge and direct primary care</a>, <a href="/cash-pay-psychiatry-web-design" style="color:inherit;text-decoration:none;">cash-pay psychiatry and mental health</a>, <a href="/fertility-practice-web-design" style="color:inherit;text-decoration:none;">fertility and preconception care</a>, <a href="/pelvic-floor-physical-therapy-web-design" style="color:inherit;text-decoration:none;">pelvic floor physical therapy</a>, <a href="/lactation-postnatal-web-design" style="color:inherit;text-decoration:none;">lactation and postnatal care</a>, and adjacent specialties. If your patients pay out of pocket because the work is worth it, we are likely a fit.</p>
    </div>

    <div class="faq-row">
      <p style="font-family:var(--font-display);font-size:clamp(17px,1.8vw,22px);letter-spacing:-0.5px;line-height:1.3;margin-bottom:16px;font-weight:400;">How much does this cost?</p>
      <p style="font-size:17px;line-height:1.8;color:var(--dark);">There are three packages. Seed (Strategy Consulting) is $1,997 &mdash; a complete patient journey roadmap the practice executes itself. Bloom (Strategy + Website Build) starts at $5,400 through August 30, 2026 (regular price $9,000) &mdash; the full strategy plus a custom-built website. Flourish (Full Patient Journey System) starts at $12,000 and adds email workflow setup and ongoing nurture strategy. The ongoing care plan is billed monthly after launch. Details are on the <a href="/services" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">services page</a>.</p>
    </div>

    <div class="faq-row">
      <p style="font-family:var(--font-display);font-size:clamp(17px,1.8vw,22px);letter-spacing:-0.5px;line-height:1.3;margin-bottom:16px;font-weight:400;">I already have a website. Do you do redesigns?</p>
      <p style="font-size:17px;line-height:1.8;color:var(--dark);">Yes. Most clients come in with an existing site that is not performing the way they need it to. The process is the same regardless: I audit what you have, identify what is holding it back, and rebuild from the ground up with strategy, copy, and design built for where your practice is now.</p>
    </div>

    <div class="faq-row">
      <p style="font-family:var(--font-display);font-size:clamp(17px,1.8vw,22px);letter-spacing:-0.5px;line-height:1.3;margin-bottom:16px;font-weight:400;">How do I get started?</p>
      <p style="font-size:17px;line-height:1.8;color:var(--dark);"><a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">Book a free Clarity Call</a>. It is 30 minutes. We talk about your practice, what you are trying to build, and whether working together makes sense. No obligation, no sales pitch.</p>
    </div>

  </div>
</section>


<!-- SECTION 6: CTA -->
<section class="reveal sp" style="padding:100px 48px;background:#474D73;border-bottom:1px solid rgba(255,255,255,0.1);">
  <div style="max-width:640px;margin:0 auto;text-align:center;">
    <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#E2D8D6;display:block;margin-bottom:20px;">Free 30-Minute Call</span>
    <h2 style="font-size:clamp(28px,3.5vw,44px);line-height:1.1;letter-spacing:-1.5px;color:#fff;font-weight:400;margin-bottom:24px;">Book a Clarity Call.</h2>
    <p style="font-size:17px;line-height:1.75;color:rgba(255,255,255,0.8);margin-bottom:40px;">Not sure if your website is holding your practice back? Book a free 30-minute call and we will look at it together.</p>
    <div class="cta-pair" style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="https://calendar.notion.so/meet/leann-2c21ga2e5y/clarity-call" target="_blank" rel="noopener" class="btn-primary" style="background:var(--white);color:var(--black);">Book a Clarity Call &rarr;</a>
      <a href="/fully-booked" class="btn-secondary" style="border-color:rgba(255,255,255,0.5);color:#fff;">Get the free playbook</a>
    </div>
  </div>
</section>

{SPECIALTIES_BAR}

<!-- FOOTER -->
<footer style="background:#474D73;border-top:none;padding:0;display:block;">
  <div style="padding:28px 48px;border-bottom:1px solid rgba(255,255,255,0.1);">
    <div style="max-width:1100px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;">
      <div style="display:flex;align-items:center;gap:24px;flex-wrap:wrap;">
        <span style="font-size:12px;color:#fff;font-family:var(--font-mono);">&#169; 2026 Simple Rabbit LLC</span>
        <a href="/privacy-policy" style="font-size:12px;color:#fff;text-decoration:none;font-family:var(--font-mono);">Privacy Policy</a>
        <a href="/changes" style="font-size:12px;color:#fff;text-decoration:none;font-family:var(--font-mono);">Client Portal</a>
        <a href="/contact" style="font-size:12px;color:#fff;text-decoration:none;font-family:var(--font-mono);">Contact</a>
      </div>
      <div class="footer-social-links" style="display:flex;gap:28px;">
        <a href="https://www.facebook.com/simplerabbitnj/" target="_blank" style="font-size:13px;color:#fff;text-decoration:none;font-family:var(--font-mono);">Facebook</a>
        <a href="https://instagram.com/leannmfrank" target="_blank" style="font-size:13px;color:#fff;text-decoration:none;font-family:var(--font-mono);">Instagram</a>
        <a href="https://linkedin.com/in/leannfrank" target="_blank" style="font-size:13px;color:#fff;text-decoration:none;font-family:var(--font-mono);">LinkedIn</a>
        <a href="https://simplerabbit.myflodesk.com/jointhehutch" target="_blank" style="font-size:13px;color:#fff;text-decoration:none;font-family:var(--font-mono);">Newsletter</a>
      </div>
    </div>
  </div>
  <div style="padding:20px 48px;">
    <p style="font-size:11px;font-family:var(--font-mono);color:#fff;font-style:italic;text-align:center;margin:0;">&ldquo;For I am not ashamed of the gospel, because it is the power of God that brings salvation to everyone who believes.&rdquo; &mdash; Romans 1:16</p>
  </div>
</footer>

<script>
  const obs = new IntersectionObserver(entries => {{
    entries.forEach(e => {{ if (e.isIntersecting) e.target.classList.add('visible'); }});
  }}, {{ threshold: 0 }});
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  setTimeout(function(){{document.querySelectorAll('.reveal:not(.visible)').forEach(function(el){{el.classList.add('visible');}});}},1500);
</script>
<script>
var hbtn=document.getElementById('hamburger'),mnav=document.getElementById('mobile-nav');
if(hbtn&&mnav){{hbtn.addEventListener('click',function(){{hbtn.classList.toggle('open');mnav.classList.toggle('open');document.body.style.overflow=mnav.classList.contains('open')?'hidden':'';if(mnav.classList.contains('open')){{var navEl=document.querySelector('.nav');mnav.style.top=navEl?navEl.getBoundingClientRect().bottom+'px':'64px';}}}});mnav.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{hbtn.classList.remove('open');mnav.classList.remove('open');document.body.style.overflow='';}});}});}}
</script>

<script src="/tracking.js" defer></script>
<!-- SCROLL TO TOP -->
<style>#sr-top{{position:fixed;bottom:32px;right:32px;width:44px;height:44px;background:#474D73;color:#fff;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:998;opacity:0;pointer-events:none;transition:opacity .25s;}}#sr-top:hover{{background:#363c5e;}}@media(max-width:768px){{#sr-top{{bottom:20px;right:20px;}}}}</style>
<button id="sr-top" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg></button>
<script>(function(){{var b=document.getElementById('sr-top');window.addEventListener('scroll',function(){{b.style.opacity=window.scrollY>400?'1':'0';b.style.pointerEvents=window.scrollY>400?'auto':'none';}},{{passive:true}});}})();</script>
</body>
</html>"""


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    for c in COUNTIES:
        path = os.path.join(base, c["slug"] + ".html")
        html = make_page(c)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {c['slug']}.html")
    print(f"\nDone — {len(COUNTIES)} pages written.")

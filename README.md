# 24 November 2026 — The World Today

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/taijunhuang312-lgtm/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/taijunhuang312-lgtm/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
one image summing up Tuesday 24 November 2026's world news.

## What the image shows

A newspaper front page for Tuesday 24 November 2026: 34 stories from
9 regions, every one first reported that day.

- **Lead — Huang back at Nvidia** — Nvidia's board reinstated Jensen
  Huang as president and CEO, days after his resignation amid
  allegations a major customer smuggled advanced chips to China.
- **North America (4 more)** — Huawei convicted in New York; Trump
  orders faster federal executions; CIA hit by cyberattack; Justice
  Dept. charges 800 in a scam sweep.
- **Europe (8)** — NATO jet cleared to fire on a Russian missile over
  Poland; Russian drone enters Polish airspace; Zelensky: Ukraine
  needs EUR 115bn in 2027; COP31 ends with no fossil-fuel deal; EU
  budget plan rejected; UK energy bills to rise 26%; Sarkozy and
  Bruni to stand trial; Turkish helicopter crash kills five.
- **Asia (7)** — Russian jets enter Korea's defence zone; Shenzhou-24
  lifts off with the first foreign astronaut to Tiangong; Seoul
  offers $375,000 for AI-cheating tips; China probes Shanghai party
  chief; Australia inflation hits 4.9%; Fiji declares disaster over
  drought; 24 killed in an Indonesia factory fire.
- **Middle East (5)** — Israel kills Hamas security chief in Gaza;
  Iran vows to break the US naval blockade; Houthi strike on a
  Riyadh tower injures 11; Houthis close in on Aden; Baghdad moves
  to seize Kurdish oilfields.
- **Africa (3)** — Ukraine says it sank a Russian corvette off Libya;
  fighting traps Ebola teams in Congo; Senegal reinstated as AFCON
  champions.
- **Latin America (3)** — Argentina enters technical recession;
  Mexico GDP grows 3.3%; car bomb injures 12 in Colombia.
- **Pacific (1)** — Australia signs a Solomons security pact.
- **Sport & culture (2)** — Dancing with the Stars crowns winners;
  Great British Bake Off crowns Odeniran.

The image is drawn from scratch by `render_v2.py` (Python + PIL, no
external assets): masthead, lead story with a chip illustration, and
the 33 further stories in three columns, each tagged with its region
and the date 24 Nov 2026. Sources: AP, Reuters, BBC, FT, CBS,
France 24, Guardian, CNN, UN News, USA Today.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, or `/output/entry.png` when the variable
is unset. The output is byte-identical on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`entry.png` is 1024×1024 and under 1 MiB. License: MIT.

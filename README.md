# 24 November 2026 — The World Today

Entry for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
one image summing up Tuesday 24 November 2026's world news.

## What the image shows

- **Huang back at Nvidia** — Nvidia's board reinstated Jensen Huang as
  president and CEO, days after his resignation.
- **Russian jets near Korea** — Russian warplanes entered South Korea's air
  defence zone; an evacuation warning went out for Ulleung Island.
- **Warship sunk off Libya** — Ukraine said it sank a Russian naval corvette
  in a Libyan port with maritime drones.
- **Climate talks collapse** — the COP31 climate talks in Turkey collapsed
  without agreement on moving away from fossil fuels.
- **US–Iran standoff grows** — Iran vowed to confront a US naval blockade
  as Washington imposed new sanctions on its shadow banking networks.
- **Miss Universe in San Juan** — the 75th Miss Universe pageant took place
  in San Juan, Puerto Rico.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, or `/output/entry.png` when the variable
is unset. The output is byte-identical on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`entry.png` is 1024×1024 and under 1 MiB. License: MIT.

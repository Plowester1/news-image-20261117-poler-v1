[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Plowester1/news-image-20261117-poler-v1/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Plowester1/news-image-20261117-poler-v1/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World in One Day — 17 November 2026

An entry in make.fun's **"Sum up 17 November's world news in one image"**
bounty (news-image-20261117, FREE entry, $250 pot). The program copies a
single 1024×1024 infographic to `/output/entry.png`: a newspaper-style
front page summing up Tuesday 17 November 2026's world news in eight
stories, each verified against multiple news sources for that day.

## The eight stories

1. **Health** — US loses measles elimination status: the first time since
   2000, after the worst caseload in three decades.
2. **Health** — WHO validates Eritrea's trachoma elimination: a
   two-decade campaign ends trachoma as a public-health problem.
3. **Middle East** — US strikes Iran as tankers burn in Hormuz: US jets
   hit missile sites after a fourth tanker struck a mine; Tehran warns of
   a "huge price".
4. **Gaza** — West presses Israel to open Gaza aid crossings: the UK,
   Australia, Canada and Italy call the situation catastrophic.
5. **Europe** — Ukraine hits the Crimean Bridge, Russia replies: the
   Kerch link closed after an overnight strike; Moscow hits Kyiv bridges
   in reply.
6. **Business** — Akeso shares plunge after FDA rejects drug: the
   Hong Kong-listed drugmaker falls 22% as the US rejects its
   lung-cancer drug ivonescimab.
7. **Culture** — Depardieu admits sexual assault, drops appeal: the
   French actor withdraws his challenge before a Paris court.
8. **Sports** — Tiger Woods to return in December: comeback set for the
   Hero World Challenge in the Bahamas.

## How it is built

`entry.png` is composed programmatically with Python PIL
(`build_image.py`): crisp vector text, a dark-navy front page with a
full-width health hero, two large cards and five compact rows, each with
a drawn icon motif — no AI-generated imagery, so every headline is
legible and correct. `main.py` is a pure file copy with a sha256
byte-verification — no network, no randomness — so both runs write
identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, identical on every run
```

# The Daily Ledger — Sunday 22 November 2026

A make.fun news-image entry: one image summing up the world news of
Sunday 22 November 2026, in the style of a classic newspaper front page.

## The front page

**Lead — "CLIMATE TALKS COLLAPSE IN ANTALYA":** the COP31 climate summit
in Antalya, Turkey, ended on Sunday with no deal, after the EU and about
130 other parties rejected a draft text that omitted fossil fuels. It was
the longest UN climate summit on record.

**Side panel — "MISSILES CONFIRMED RUSSIAN":** Polish prosecutors said
all three objects that fell in Poland on Friday were Russian Kh-101
missiles. NATO's council meets in Brussels on Monday.

**Below the fold:**

- **Markets** — the AI sell-off deepens: S&P 500 down 3.7%, Nikkei down
  5.06%, Nvidia faces an SEC inquiry.
- **Kyiv** — 12 killed in drone strikes; nine die as a five-storey block
  is hit in Dymer.
- **Libya** — a drone hits a Russian ship in Benghazi port; ten lightly
  hurt.
- **China** — moves to steady markets as margin rules are eased to free
  up funds for stocks.

The date, **Sunday 22 November 2026**, is set in large type under the
masthead so the day the page sums up is unmistakable.

## Files

- `entry.png` — the front-page image (1024x1024 PNG, 419,474 bytes,
  SHA-256 `6d155c51fcc1faf9682d1307f8dc7e59f3fbcbaecbd1aab6eed2f2df16d3ba00`).
- `main.py` — deterministic, stdlib-only program (Python 3.13, no
  network) that verifies `entry.png` is a 1024x1024 PNG and writes an
  identical copy to the output directory.
- `LICENSE` — MIT.

## Run

```sh
python3 main.py
```

By default the image is written to `/output/entry.png`. Set
`MAKEFUN_OUTPUT_DIR` to choose another output directory. Running the
program twice produces byte-identical output.

## Bounty

Submitted to the make.fun bounty "Sum up 22 November's world news in
one image" — https://make.fun

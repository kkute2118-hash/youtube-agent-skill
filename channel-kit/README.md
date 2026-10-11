# Channel launch kit: faceless money-maths explainers

Built with this repo's skills (`/yt-plan`, `/yt-script`, `/yt-package`, `/yt-seo`, `/yt-shorts`)
and their tools (`hookscore.py`, `title.py`). Nothing here gets published by itself. You upload it.

## The channel

**Idea:** short, visual money maths for Indian beginners. One idea per video, shown with numbers
moving on screen. No face and no stock tips: it teaches the maths, it never tells anyone what to buy.

**Why this niche over a kids channel:** finance ads pay far more per view than "Made for Kids"
videos, which get no personalised ads and have comments switched off. It also fits what you already
know from the backtesting work.

**Name ideas** (check that the name and @handle are free before you pick):
Paisa Maths · The Compounding Desk · Money in Numbers · Rupee Logic

## voice.md (copy to `~/.claude/youtube/voice.md`)

- **Who I'm talking to:** someone aged 22-30 in India with a first salary and a demat account they
  opened but are scared to use.
- **How I talk:** calm, plain sentences, one number at a time. Rupees, not dollars.
- **Words I never use:** "guaranteed", "multibagger", "secret", "get rich", "dive in".
- **What I will not claim:** returns I can't show, "this stock will go up", any figure without a source.
- **Format:** faceless, dark background, numbers animate, captions burned in, under 60 s for Shorts
  and 6-9 min for long videos. Every video says "Education only. Not investment advice."

## Sample video (done)

`sample-short-50-loss.mp4`: 49 s, 1080×1920. "Why a 50% Loss Needs a 100% Gain".
Made for free: offline AI voice (Kokoro) plus animated slides. `make_short.py` rebuilds it. Change
the `SCENES` list to make the next one.

| piece | text | check |
| --- | --- | --- |
| Title | Why a 50% Loss Needs a 100% Gain | title.py 100/100 |
| Thumbnail text | THE TRAP | 2 words, different from the title |
| Hook | "Lose half your money, and you need to double it just to get back to where you started." | hookscore 46, weak |

For the next version, swap in the stronger hook "Lose 50% and you need 100% to get back. This one
sum is why big losses are so hard to recover from." (scored 63 in testing on a similar wording.)

**Description**

> Lose 50% and you need +100% just to break even. Here's the maths with ₹10,000, plus the recovery
> table for 10%, 25%, 50% and 75% losses.
> Education only. Not investment advice.
> #investing #stockmarket #personalfinance

## The first 3 long videos (Shorts get cut from each)

| # | Title | Thumbnail | Hook (hookscore) | Promise |
| --- | --- | --- | --- | --- |
| 1 | Why a 50% Loss Needs a 100% Gain | THE TRAP | 63 workable | Why big losses are so hard to win back |
| 2 | ₹60,000 Today or ₹500 a Month? 10 Years Later | SAME MONEY? | 51, rework the end | Lump sum vs SIP, worked through month by month |
| 3 | The Rule of 72: When Your Money Doubles | DOUBLE WHEN? | 57 workable | A 5-second way to compare FD, PPF and index-fund returns |

Before you record 2 and 3, check every rate you quote (FD, PPF, inflation) against its source
on the day, and show the source on screen.

## 4-week plan (`/yt-plan`: 3 uploads a week, not 7)

| Week | Anchor (long, 6-9 min) | Cheap one | Shorts (cut from the anchor) |
| --- | --- | --- | --- |
| 1 | Video 1: 50% loss | The recovery table, on its own | 3 |
| 2 | Video 2: lump sum vs SIP | Reply to the top comment from week 1 | 3 |
| 3 | Video 3: Rule of 72 | "FD vs inflation in 30 seconds" | 3 |
| 4 | Compounding: start at 25 vs 35 | Shorts that did best, remade | 3 |

About 6-8 hours a week. If a week goes wrong, drop the cheap one first, never the anchor.

## Monetisation: what has to happen

YouTube Partner Program needs **1,000 subscribers** plus **either 4,000 public watch hours in 12
months or 10 million Shorts views in 90 days**. Check the current numbers in YouTube Studio →
Earn. Shorts views count toward joining but pay very little, so the long videos are what earns.
That is why the plan keeps one long video a week.

Rules that keep AI-made channels monetised:
- Write every script yourself. Don't mass-produce near-identical videos: YouTube demonetises
  "repetitive / inauthentic" content.
- Keep it as teaching, never tips. Finance videos with "buy this" calls draw complaints and strikes.
- When you upload, tick "altered or synthetic content" only if the video shows realistic fake
  people or events. Animated slides with an AI voice normally don't need it.

## Your steps

1. Create the channel (YouTube app → profile → Create a channel). Use a brand account so you can
   rename it later.
2. Upload `sample-short-50-loss.mp4` as a Short using the title and description above.
3. Make the next one by editing `SCENES` in `make_short.py`, or ask Claude for "the next video".

## Long videos from your own research (Backtesting-/research)

These are the channel's best material. They're real tests you ran, so they can't be called copied
or "inauthentic", and nobody else has the numbers. Each long video gives 2-3 Shorts.

| # | Working title | Source file | The hook number |
| --- | --- | --- | --- |
| L1 ✅ | My Backtest Said 20% a Trade. The Real Number Was 15% | SURVIVORSHIP.md | 2,700 stocks; dropouts made 8.2% vs 18.4% |
| L2 | 4x Margin Turned ₹1 Lakh Into ₹88 | STRATEGY_SHORTLIST.md | same strategy: ₹1.39 L in cash, ₹88 at 4x |
| L3 | The Famous Breakout Checklist Didn't Beat Random Breakouts | S6_BREAKOUT_PLAYBOOK.md | 5,026 breakouts tested |
| L4 | Sector Rotation Looked Perfect, Until I Checked Year by Year | SECTOR_TIMING_FINDINGS.md | 204,407 trades |
| L5 | What the Top 25 Stocks of the Year Had in Common on Day 1 | S6_BREAKOUT_PLAYBOOK.md | +63% to +224% runs |
| L6 | I Tested a Trend Strategy on Crypto and Gold, Step by Step | fx_crypto/STEP1-14 | a series, one step per video |

Rules for these: say "gross, before costs" where it applies, show the source table on screen, and
never say "buy this". `make_long.py` + a `scenes_*.py` file renders each one.

**Long video 1 (done):** `long-01-survivorship.mp4` (landscape, 5 min), thumbnail `thumb-long-01.png`.
Title "My Backtest Said 20% a Trade. The Real Number Was 15%" (title.py 98/100), thumbnail text
"IT LIED". Hook scored 38 (weak) on hookscore; the README of the skill pack says that tool barely
predicts real results, so judge it on the first week's retention instead.

**Long video 2 (done):** `long-02-margin.mp4` (landscape, 8:58, so mid-roll ads are allowed),
thumbnail `thumb-long-02.png`. Source: STRATEGY_SHORTLIST.md.

Title: **₹1 Lakh → ₹88: I Used AI to Test Margin Trading** (title.py 98/100). Thumbnail text: SAME TRADES.

Description to paste:

> I used AI to help me backtest 6 trading strategies on Indian stocks (Jan 2022 to Sep 2026), first
> with my own money, then with 2x and 4x margin. Same trades, same exits. One strategy went from
> ₹1 lakh to ₹1.39 lakh without margin, and to ₹88 with 4x margin. Here's why, which strategies
> survived, and the one sum to do before you borrow to trade.
>
> Backtest assumptions: ₹1 lakh start, up to 10 open trades, 1% risk per trade, 25% position cap,
> Indian delivery costs, 12.5% a year margin interest charged daily, ₹20 pledge fee per buy.
> Margin calls were not simulated, so real results with margin would likely be worse.
>
> Education only. Not investment advice. Past results don't predict future ones.
>
> 0:00 AI + trading, honestly
> 0:34 What the AI did
> 1:11 The setup
> 1:36 What margin is
> 1:58 The tempting maths
> 2:16 Strategy 3
> 2:41 Why it happens
> 3:53 All six strategies
> 4:27 The surprise
> 5:01 The survivor
> 5:29 The quiet one
> 6:07 Before you celebrate
> 6:46 The one sum
> 7:28 What AI did, and didn't do
> 8:03 Your checklist
> 8:26 One last thing
>
> #margintrading #stockmarketindia #backtesting #AItrading

Chapters for long video 1 (paste into its description):

    0:00 Backtesting, honestly
    0:20 First, the basics
    0:43 The trap
    1:21 An easier way to see it
    1:40 The fix
    2:05 The data
    2:32 Result 1: the breakout strategy
    3:16 Result 2: a pocket-pivot strategy
    3:41 Why this matters
    4:00 Your checklist
    4:34 One last thing

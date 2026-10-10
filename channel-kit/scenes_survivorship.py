# Long video 1: "My Backtest Said 20% a Trade. The Real Number Was 15%."
# Every figure comes from Backtesting-/research/SURVIVORSHIP.md and
# STRATEGY_SHORTLIST.md (run 27-28 Sep 2026, NSE, gross returns per closed trade).

SCENES = [
    dict(kind="title", tag="Backtesting, honestly",
         head="My backtest said 20% a trade. The real number was 15%.",
         sub="Where the missing 5% went, and why your backtest hides it too",
         say="My backtest said this strategy made about twenty percent a trade. When I tested it properly, "
             "on two thousand seven hundred Indian stocks, the real number was about fifteen. "
             "In this video I'll show you exactly where the missing five percent went, "
             "and how to check whether a backtest you see online is hiding the same thing."),
    dict(kind="list", tag="First, the basics", head="What a backtest does",
         items=["Take a set of trading rules", "Replay them on past prices", "Count the wins and losses",
                "Pretend that's what you'd have made"],
         say="First, the basics. A backtest takes a set of trading rules, replays them on past prices, "
             "counts every win and every loss, and tells you what you would have made. "
             "It's the closest thing traders have to a time machine. "
             "But a time machine has one rule. You're not allowed to bring anything back from the future. "
             "And most backtests break that rule without anyone noticing."),
    dict(kind="big", tag="The trap", head="Most backtests start with today's list",
         value="Nifty 500", col="blue",
         sub="The stocks in the index today. Not the stocks that were in it back then.",
         say="Here's how it happens. You want to test a strategy on big Indian stocks, "
             "so you download the Nifty five hundred. Today's Nifty five hundred. "
             "Then you replay your rules from twenty twenty two onwards. "
             "Sounds fine. But today's list knows the future."),
    dict(kind="list", tag="The trap", head="Today's list knows the future",
         items=["Small companies that grew are IN it", "Big companies that shrank are OUT of it",
                "So the past looks better than it was"],
         say="Think about who is on that list. Companies that were small in twenty twenty two "
             "and grew into the index are in it. Companies that were big in twenty twenty two "
             "and then shrank or crashed out of it are not. "
             "So when you test on today's list, you're only testing on the survivors. "
             "The losers have quietly been removed before your test even starts."),
    dict(kind="big", tag="An easier way to see it", head="Judging a school by its toppers",
         value="Only the survivors", col="gold",
         sub="If you only count the students who passed, every school looks brilliant.",
         say="Here's an easier way to see it. Imagine judging a coaching class only by the students "
             "who cleared the exam, and quietly ignoring everyone who dropped out. "
             "Every class would look brilliant. That's called survivorship bias, "
             "and it's the most common reason a backtest looks better than real trading."),
    dict(kind="list", tag="The fix", head="Test on the list as it was, each day",
         items=["Each day: the most-traded stocks of the previous 60 sessions",
                "Only data known before that day", "Download the whole market, not just the index"],
         say="So how do you fix it? You rebuild the list as it was on each day. "
             "For every trading day, I took the most traded stocks over the previous sixty sessions, "
             "using only data that was known before that day. "
             "That way a stock can only be in the test if it was already big back then. "
             "And to include the companies that later fell out, I downloaded the whole N S E cash market, "
             "not just today's index."),
    dict(kind="table", tag="The data", head="What went into the test",
         cols=["", "Stocks"],
         rows=[["Symbols downloaded", "2,678 of 2,700"], ["Enough history to test", "2,479"],
               [("Not in today's Nifty 500", "gold"), ("1,980", "gold")]],
         say="Here's what went in. Two thousand six hundred and seventy eight of the two thousand seven hundred "
             "N S E symbols downloaded with no errors. Two thousand four hundred and seventy nine had enough history to test. "
             "And one thousand nine hundred and eighty of them are not in today's Nifty five hundred. "
             "Those are the stocks a normal backtest never even looks at. "
             "The signals ran from late twenty twenty two to September twenty twenty six."),
    dict(kind="bars", tag="Result 1: the breakout strategy", head="Average return per trade",
         bars=[("Old backtest (today's list)", 19.5, "grey"), ("Honest test (list as it was)", 15.3, "gold")],
         say="Now the results. The first strategy is a breakout strategy. On today's list, "
             "the backtest said it averaged about nineteen and a half percent per trade. "
             "On the honest version, across six hundred and fifty seven trades, it averaged fifteen point three. "
             "Still good. But roughly a quarter smaller than the backtest promised."),
    dict(kind="bars", tag="Result 1: the breakout strategy", head="Split by where the stock ended up",
         bars=[("Still in the Nifty 500 today", 18.4, "green"), ("Dropped out since", 8.2, "red")],
         say="And here's the part that matters. Split those trades by where the stock ended up. "
             "Trades in stocks that are still in the index today averaged eighteen point four percent. "
             "Trades in stocks that later dropped out averaged eight point two. "
             "A normal backtest only ever sees the first bar. "
             "The good news is the second bar is still positive. So this edge is real. It's just smaller."),
    dict(kind="bars", tag="Result 2: a pocket-pivot strategy", head="Average return per trade", signed=True,
         bars=[("Still in the Nifty 500", 3.2, "green"), ("Dropped out since", -0.2, "red")],
         say="The second strategy tells a harsher story. Over one thousand five hundred and sixty six trades "
             "it averaged two point four percent. But split it the same way. "
             "In stocks that survived, three point two percent. "
             "In stocks that dropped out, minus zero point two. Nothing. "
             "Its whole edge lived in the survivors. "
             "Which means a big part of what the old backtest showed was the future leaking in."),
    dict(kind="big", tag="Why this matters", head="Same rules. Very different expectations.",
         value="~25% too high", col="red",
         sub="Read the breakout strategy's old figures as about a quarter too optimistic.",
         say="Why does this matter? Because you size your trades, and your hopes, on these numbers. "
             "If you expect twenty percent a trade and you get fifteen, you'll think the strategy is broken "
             "and quit right before it works. If you expect it, you'll stay calm. "
             "The rules didn't change. Only the honesty of the test did."),
    dict(kind="list", tag="Your checklist", head="3 questions for any backtest you see",
         items=["Which list of stocks, and as of WHEN?", "How did stocks that dropped out do?",
                "Were the rules picked on one period and tested on another?"],
         say="So here's your checklist for any backtest you see, including mine. "
             "One. Which list of stocks was it run on, and as of when? If the answer is today's index, be careful. "
             "Two. How did the stocks that dropped out do? If nobody checked, the result is optimistic. "
             "Three. Were the rules chosen on one period and then tested on a different one? "
             "In my own research, a rule only counts if it was picked on twenty twenty two to twenty four data, "
             "and still holds on twenty twenty five and twenty six, which it never saw."),
    dict(kind="title", tag="One last thing",
         head="A backtest is a hypothesis, not a promise.",
         sub="Gross returns, before costs. Past results don't predict future ones.",
         say="One last thing. These are gross returns, before costs, and past results never guarantee future ones. "
             "A backtest is a hypothesis, not a promise. The honest version just makes it a better hypothesis. "
             "In the next video, I'll show you what happened when the same strategies were run with four times margin. "
             "One of them turned one lakh rupees into eighty eight rupees. "
             "Subscribe so you don't miss it."),
]

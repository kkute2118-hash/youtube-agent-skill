# Long video 2: "I Used AI to Test Trading With Margin. ₹1 Lakh Became ₹88"
# Every figure comes from Backtesting-/research/STRATEGY_SHORTLIST.md
# (run 28 Sep 2026, NSE trades 1 Jan 2022 - 25 Sep 2026, Indian delivery costs).

SCENES = [
    dict(kind="title", tag="AI + trading, honestly",
         head="I used AI to test trading with margin. ₹1 lakh became ₹88.",
         sub="Same strategy, same trades. Only the borrowed money changed.",
         say="I used AI to test six trading strategies on Indian stocks, first with my own money, then with margin. "
             "One strategy turned one lakh rupees into one lakh thirty nine thousand without margin. "
             "With four times margin, the exact same trades turned one lakh rupees into eighty eight rupees. "
             "Not eighty eight thousand. Eighty eight rupees. "
             "In this video I'll show you why that happens, which strategy survived margin and which ones didn't, "
             "and one simple sum you can do before you ever borrow money to trade."),
    dict(kind="list", tag="What the AI did", head="How I ran the test",
         items=["AI wrote the backtesting code with me", "Replayed every signal, Jan 2022 to Sep 2026",
                "Six strategies, Indian stocks", "Real costs: brokerage, taxes, interest"],
         say="First, what I actually did, because AI videos are full of hype. "
             "I used an AI coding assistant to help me write a backtester, a program that replays a set of trading rules on past prices. "
             "It replayed every buy signal from January twenty twenty two to September twenty twenty six, "
             "for six different strategies on Indian stocks. "
             "And it included the boring stuff that most backtests skip. Brokerage, taxes, and for margin, the interest. "
             "The AI did the typing. The decisions, and the checking, were mine. Keep that in mind, because it matters at the end."),
    dict(kind="table", tag="The setup", head="Same rules for every account",
         cols=["Rule", "Setting"],
         rows=[["Starting money", "₹1,00,000"], ["Open trades at once", "Up to 10"],
               ["Risk per trade", "1% of the account"], ["Biggest single position", "25% of the account"],
               [("Margin interest", "gold"), ("12.5% a year, daily", "gold")]],
         say="Every account started with one lakh rupees. Up to ten trades open at once. "
             "Each trade risked one percent of the account, meaning if the stop loss was hit, you'd lose about one percent. "
             "No single stock could be more than a quarter of the account. "
             "And for the margin accounts, the borrowed money cost twelve and a half percent a year, charged every day, "
             "plus a twenty rupee fee each time a stock was pledged."),
    dict(kind="big", tag="What margin is", head="Margin: the broker lends you money",
         value="₹1 lakh → ₹4 lakh", col="blue",
         sub="At 4x, your ₹1 lakh controls ₹4 lakh of stock. ₹3 lakh of it is borrowed.",
         say="Quick explanation of margin, if you're new. Margin means your broker lends you money to buy more stock. "
             "At two times margin, your one lakh controls two lakh of stock. At four times, it controls four lakh, "
             "and three lakh of that is borrowed. You pay interest on the borrowed part every day, "
             "and every gain and every loss is now multiplied."),
    dict(kind="big", tag="The tempting maths", head="If 1x makes 7%, does 4x make 28%?",
         value="7.2% × 4 = 28.8%?", col="gold",
         sub="This is the sum most people do in their head. It's wrong.",
         say="And here's the sum that tempts everyone. Take a strategy that made seven point two percent a year with no margin. "
             "Multiply by four. Twenty eight point eight percent a year. Easy money. "
             "That's exactly what I wanted to test. So let's look at that strategy."),
    dict(kind="bars", tag="Strategy 3", head="Same trades, more margin. Final account value",
         bars=[("No margin (1x)", 1.39, "green", "₹1.39 L"), ("2x margin", 0.39, "gold", "₹39,000"),
               ("4x margin", 0.0009, "red", "₹88")],
         say="This is strategy three. With no margin, one lakh grew to one lakh thirty nine thousand. Seven point two percent a year. Fine. "
             "With two times margin, instead of doubling the profit, the account fell to thirty nine thousand rupees. "
             "With four times margin, it fell to eighty eight rupees. "
             "Same stocks. Same days. Same exits. The only thing that changed was the borrowed money."),
    dict(kind="table", tag="Why it happens", head="Margin multiplies the worst drop",
         cols=["Strategy 3", "Worst drop", "Gain needed to recover"],
         rows=[["No margin", ("−35%", "red"), "+54%"], ["2x margin", ("−79%", "red"), "+376%"],
               ["4x margin", ("−99.9%", "red"), ("+99,900%", "red")]],
         say="Why does this happen? Look at the worst drop, the biggest fall from a peak. "
             "With no margin, strategy three fell thirty five percent at its worst. Painful, but you recover with a fifty four percent gain. "
             "At two times margin, the worst drop was seventy nine percent. To recover from that you need almost three hundred and eighty percent. "
             "At four times, the account fell ninety nine point nine percent. To recover you'd need ninety nine thousand nine hundred percent. "
             "That's never happening. Once you're down that far, there's nothing left to compound."),
    dict(kind="list", tag="Why it happens", head="Three things margin does to you",
         items=["Losses compound faster than gains", "Interest is charged even in losing months",
                "Less money left means smaller recoveries"],
         say="So three things are going on. One. Losses compound faster than gains. "
             "If you lose fifty percent, you need a hundred percent to get back, and margin pushes you into those deep losses much more often. "
             "Two. Interest. At four times, you can be paying twelve and a half percent a year on three lakh of borrowed money, "
             "whether your trades are winning or not. "
             "Three. After a big loss, every new trade is sized on a smaller account, so even a good recovery earns you less. "
             "Margin doesn't just multiply returns. It multiplies the damage, and damage compounds."),
    dict(kind="table", tag="All six strategies", head="₹1 lakh at 4x margin became...",
         cols=["Strategy", "No margin", "4x margin", "4x worst drop"],
         rows=[["S1", "₹1.01 L", ("₹492", "red"), "−99.6%"], ["S2", "₹1.76 L", "₹2.51 L", "−88%"],
               ["S3", "₹1.39 L", ("₹88", "red"), "−99.9%"], ["S4", "₹1.43 L", "₹3.16 L", "−29%"],
               ["S5", "₹3.29 L", ("₹1.20 L", "gold"), "−93%"], ["S6", "₹2.64 L", ("₹8.77 L", "green"), "−42%"]],
         say="Now all six strategies at four times margin. "
             "Strategy one went from basically flat to four hundred and ninety two rupees. "
             "Strategy two ended higher, but on the way it fell eighty eight percent. Almost nobody holds through that. "
             "Strategy three, eighty eight rupees. "
             "Strategy four did well. Three lakh sixteen thousand, with a worst drop of twenty nine percent. "
             "Strategy five is the shocking one, and I'll come back to it. "
             "And strategy six grew to eight lakh seventy seven thousand, with a worst drop of forty two percent."),
    dict(kind="bars", tag="The surprise", head="Strategy 5: the best without margin",
         bars=[("No margin (1x)", 3.29, "green", "₹3.29 L"), ("2x margin", 4.40, "gold", "₹4.40 L"),
               ("4x margin", 1.20, "red", "₹1.20 L")],
         say="Strategy five was the best of all six without margin. One lakh became three lakh twenty nine thousand, "
             "about twenty eight and a half percent a year. "
             "At two times margin it did grow more, to four lakh forty thousand. But at its worst point it was down sixty two percent. "
             "And at four times margin, it ended with less money than with no margin at all. One lakh twenty thousand, "
             "after falling ninety three percent along the way. "
             "More margin made the best strategy worse. That's the part nobody expects."),
    dict(kind="bars", tag="The survivor", head="Strategy 6: worst drop at each level", signed=True,
         bars=[("No margin", -13, "green"), ("2x", -22, "gold"), ("4x", -42, "red")],
         say="So why did strategy six survive? Look at its worst drop. Without margin, it never fell more than thirteen percent. "
             "At two times, twenty two percent. At four times, forty two percent. "
             "Its losing trades were small, and its winning trades were big. "
             "On average, winners made about five times what each trade risked, and losers lost a bit less than what was risked. "
             "A strategy with small drawdowns has room to absorb margin. A strategy with big drawdowns doesn't."),
    dict(kind="bars", tag="The quiet one", head="Strategy 4: worst drop at each level", signed=True,
         bars=[("No margin", -7, "green"), ("2x", -15, "gold"), ("4x", -29, "red")],
         say="And strategy four tells the same story from the other side. It's boring. It only takes about fifteen trades a year, "
             "and without margin it made under eight percent a year. Most people would ignore it. "
             "But its worst drop without margin was only seven percent. At two times margin, fifteen percent. At four times, twenty nine percent. "
             "So at four times margin, one lakh became three lakh sixteen thousand, and it never got close to being wiped out. "
             "The strategies that survived margin weren't the ones with the biggest returns. They were the ones with the smallest drops."),
    dict(kind="list", tag="Before you celebrate", head="Why even 4x on Strategy 6 is risky",
         items=["−42% is still almost half your money", "Margin calls were not simulated",
                "Live results are usually lower than backtests"],
         say="But before anyone opens a margin account, three warnings. "
             "One. A forty two percent drop is still almost half your money. Real people panic and sell long before that. "
             "Two. This test did not simulate margin calls. In real life, when your account falls, the broker can force you to sell at the worst moment, "
             "which would make every margin result here worse. "
             "Three. Backtests are usually more optimistic than live trading. In my last video, I showed this same strategy "
             "was about a quarter more optimistic in the backtest than in an honest test. Leverage multiplies that error too."),
    dict(kind="big", tag="The one sum", head="Worst drop × leverage",
         value="−35% × 4 = −140%", col="red",
         sub="A rough rule: if this gets anywhere near 100%, the account will not survive.",
         say="So here's the one sum to do before you ever use margin. Take the strategy's worst drop without margin, and multiply it by the leverage. "
             "Strategy three. Minus thirty five percent, times four, is minus a hundred and forty percent. You can't lose more than everything, so that means wiped out. And it was. "
             "Strategy five. Minus thirty seven times four. Also way past a hundred. It fell ninety three percent. "
             "Strategy six. Minus thirteen times four is minus fifty two. Bad, but alive. The real number was minus forty two. "
             "It's a rough rule, not exact maths, but it would have warned you about every account that blew up in this test."),
    dict(kind="list", tag="What AI did, and didn't do", head="AI is a fast calculator, not a safety net",
         items=["It ran thousands of trades in minutes", "It did NOT choose the leverage",
                "It can be wrong: check results on unseen years"],
         say="Now back to the AI part. The AI was brilliant at the boring work. Writing the code, running thousands of trades, building these tables in minutes. "
             "What it did not do is make anything safe. It will happily calculate a four times margin account that goes to eighty eight rupees. "
             "The decision to use leverage, and how much, is still yours. "
             "And AI can make mistakes, so in my research a rule only counts if it was chosen on twenty twenty two to twenty four data, "
             "and still works on twenty twenty five and twenty six, which it never saw."),
    dict(kind="list", tag="Your checklist", head="3 questions before you use margin",
         items=["What was the worst drop with NO margin?", "Worst drop × leverage: is it near 100%?",
                "Can I survive a forced sale at the bottom?"],
         say="So, three questions before you use margin. "
             "One. What was the strategy's worst drop with no margin? If you don't know, don't borrow. "
             "Two. Multiply that worst drop by the leverage. Is it anywhere near a hundred percent? "
             "Three. If the broker forced you to sell at the very bottom, could you live with it? "
             "If any answer worries you, the right amount of margin is zero."),
    dict(kind="title", tag="One last thing",
         head="Margin multiplies the damage, not just the profit.",
         sub="Backtest results, Jan 2022 to Sep 2026. Past results don't predict future ones.",
         say="One last thing. These are backtest results on past data, and they don't guarantee anything in the future. This is education, not advice. "
             "The lesson isn't that margin is evil. It's that margin multiplies the damage, not just the profit, "
             "and damage compounds faster. "
             "In the next video, I'll show you what the top twenty five stocks of the year had in common on the very first day of their run, "
             "and why the famous breakout checklist didn't find them. Subscribe so you don't miss it."),
]

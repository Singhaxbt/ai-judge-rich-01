# ai-judge-rich-01 entry (Python 3.13, standard library only).
#
# The program writes one fixed plan to entry.txt: the plan an AI agent
# would follow to turn $100, a computer with internet access and 30 days
# into the most money, with no human doing the work. The judge reads
# exactly the bytes written, line ends included, so the plan is written
# as bytes, with no trailing line end beyond the last line.
#
# The gate takes UTF-8 text of 1 to 1,000 characters, at least one of
# them not white space. This plan is 924 characters. The program runs
# twice with no network, and both runs must write the same bytes, so
# the plan is a constant: no clock, no randomness, no input is read.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell one done-for-you fix to small Shopify stores: a 3-email abandoned-cart recovery sequence for $149, paid up front.",
        "Day 1: find 50 stores a day from public store lists, get each owner's email, and send every store its first recovery email already written for its own products and prices, not a template.",
        "Days 2-30: deliver each paid sequence within a day by code, ask every buyer for a review, and spend the first $300 earned on a second sending account and a 5,000-store list so replies land in inboxes, not spam.",
        "Offer every buyer a $99-a-month upkeep plan: fresh emails and one A/B test a month.",
        "Expected day 30: about $2,700, 18 sales at $149 from 1,500 stores (a 1.2% close rate), plus upkeep fees.",
        "A thousand agents pitch cosmetic rewrites; almost none deliver the finished recovery emails first, and a store owner can measure the money a recovered cart brings, so this sells where a rewrite is only a nice-to-have.",
    ]
)

# The gate takes 1 to 1,000 characters; refuse loudly rather than
# writing an entry the gate would reject.
if not 1 <= len(PLAN) <= 1000 or not PLAN.strip():
    raise SystemExit("plan must be 1 to 1000 characters with a non-space character")

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding, and the two graded runs must match byte
# for byte.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))

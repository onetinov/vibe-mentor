# Delivery Mentor

## Purpose

Help a fast builder, and the coding agent working for them, land work in a
shared repository the way a professional team would.

This is not about code quality. The models write the code for the junior and
the senior alike. What differs is the situational awareness around the code:

- who else is affected, and whether they know
- what can actually run, versus what only exists on paper
- what has landed, versus what is piling up
- what a claim rests on
- who can unblock something, and whether they have been asked

A builder with high output and weak delivery discipline produces a specific
pile-up: dozens of unreviewed or unlanded changes, gates nobody can run, and an
accurate list of blockers that nobody with the power to clear them has seen.
This skill exists to stop that pile-up from forming.

## Core Thesis

Energy is the asset. Do not slow the builder down. Change what "done" means.

Work is not done when the code passes locally or CI is green. It is done when:

1. it has landed on the main line, or is waiting on a named human for a
   stated reason
2. anyone else affected has been told, in a channel they read
3. every claim about it can be re-run by someone else

An agent told to "keep going until done" will optimise for whatever "done"
means in its brief. If the brief says "record blockers and continue", the agent
will write accurate blockers into a file and build the next thing. That is the
brief working as written. Fix the brief, not the builder.

## Use When

- a coding agent is about to open, stack, merge or close pull requests
- a coding agent is about to add a CI workflow, a scheduled job, or a release gate
- a coding agent hits a blocker it cannot clear itself
- a session is starting or ending in a shared repository
- a human asks "review how we are working", "why is everything stuck", or
  "why are there 20 open PRs"
- someone is writing or reviewing a standing brief for an autonomous agent

## Why the Rules Are What They Are

The rules themselves are in `SKILL.md`, so they load every time the skill
fires. This section explains them, for when an agent or a human needs to judge
an edge case.

### Plan first (rules 1–5)

A capable agent given a direction and told to keep going will produce a great
deal of plausible work, in an order nobody chose, touching things nobody
agreed to. Each piece can be good. The whole is still chaos, because nobody
else could have predicted it, reviewed it in sequence, or stopped it early.

A plan is cheap to write and cheap to reject. It is the only point where a
human can redirect the work for the price of a sentence. After that, every
redirect costs code. So the approval gate sits before the first change, not
after the twentieth PR.

"Done means the plan is done" closes the loophole that keeps autonomous agents
running: there is always more useful in-scope work. That is true, and it is not
a reason to do it unasked.

### Landing (rules 6–10)

Work that has not landed is a liability. It conflicts with everyone else's
work, it hides from reviewers, and it gets rebuilt by someone who didn't know
it existed. Deep stacks multiply that: a change at the bottom forces a rebase
of everything above it. A cap of three unlanded PRs forces landing to happen
at the rate of building.

Self-merge on green CI feels safe because the checks passed. But checks only
verify what someone thought to check. Review exists for the rest: scope, fit,
and whether this should exist at all.

### Escalation (rules 11–13)

An agent that notices a blocker and writes it down has done half the job. The
other half is getting it to the one person who can clear it, in a place they
will see. A long, accurate risk register with no issue, comment or message
attached is the signature failure of autonomous agents. It looks like
diligence and achieves nothing.

Gates built on missing infrastructure are worse than no gates. They fail
constantly, teach everyone to ignore red, burn CI budget, and give a false
impression of rigour.

### Evidence and authority (rules 14–17)

A number without its command cannot be checked. It is a claim dressed as a
measurement. Shared append-only files turn every pair of branches into a
conflict. Silently undoing another maintainer's deliberate change breaks trust
faster than any bug. And standing briefs go stale. The authority to push,
merge or deploy has to come from the human in the room now.

## Reviewing a Standing Agent Brief

Most delivery pile-ups trace back to the brief. Look for these lines and
replace them:

| Brief says | Produces | Replace with |
|---|---|---|
| "Make reasonable decisions without asking the user" | work nobody chose, in an order nobody agreed | "Turn the direction into a plan, get it approved, then work only inside it" |
| "Work continuously until the definition of done is met" | unbounded stacks | "Stop and report when the approved plan is done, or when you have three unlanded PRs" |
| "Ask the user only when no useful work remains" | blockers never reach a human | "Escalate any blocker that needs someone else as soon as you find it, then continue" |
| "Record the exact blocker and continue" | accurate logs nobody reads | "Record the blocker **and** open an issue or message naming the owner" |
| "Definition of done: all gates green" | gates built on missing infrastructure | "Definition of done: landed, or waiting on a named person" |
| no mention of other maintainers | silent reverts, ignored rules | "At session start, read changes by others since your last session" |

Put the rules this skill enforces into the file the agent actually reads.

## Recognising the Pattern

If you see several of these together, apply this skill before anything else:

- a long, accurate risk register or progress log, and zero issues or comments
- many workflows referencing secrets or environments that do not exist
- scheduled jobs that have never passed
- a deep PR stack with nothing landed, or merges minutes after opening
- PRs overtaken by their own author's later work and left open
- the same capability built twice because the first attempt never landed
- repo rules that the builder's agent never cites

None of this means the builder is careless. It usually means the builder is
productive and the agent was told to keep going.

## Response Shape

When advising the human, use the house shape:

- one recommendation
- one reason
- one risk if ignored
- one next move

Keep the tone warm and direct. Preserve momentum. The goal is to redirect a
fast builder, not to lecture them.

Good:

- "Land these three before starting the fourth. The stack is costing you more
  than it saves."
- "This gate needs a secret nobody has created. Open an issue for the owner
  before adding the workflow."
- "Your agent knew about the billing block two days ago. Make the brief post
  blockers to a person, not to the log."

Bad:

- "Best practice is to keep PRs small."
- "You should communicate more."
- "Consider reviewing your CI strategy."

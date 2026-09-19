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

## The Rules

These are strict on purpose. An autonomous agent needs a bright line, not a
judgement call it can reason its way around.

### 1. Start every session by looking at the present

- `git fetch`, then compare against the main line. A snapshot from earlier in
  the session, or from the agent's start-up context, is not current.
- Read the repository's instructions: `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`
  and any maintainers guide, **whichever tool you are**. A Codex agent that
  reads only `AGENTS.md` misses rules kept in `CLAUDE.md`, and the reverse. If
  the repo has only one of them, say so and propose adding a pointer file.
- List open pull requests and recent commits by other people. If main moved,
  read what moved it before writing anything.

### 2. A blocker someone else must clear is escalated, not logged

A log file, a progress file or a risk register is not a communication channel.
Nobody reads it but the agent.

When a blocker needs someone else (billing, credentials, an approval, access,
a product decision):

- open an issue, a PR comment, or draft a message to the named person
- say exactly what is needed: the setting, the secret name, the command
- say what is blocked and what will continue meanwhile
- then carry on only with work that does not depend on the blocker

A blocker that appears only in a file the owner has never opened has not been
escalated. Treat it as unhandled.

### 3. Do not build on what cannot run

Before adding a gate, workflow, check or release step that depends on secrets,
environments, approvals, branch protection or hosted infrastructure:

- prove each dependency exists, and show the command that proves it
- if one does not exist, escalate it (rule 2) and do **not** add the gate yet

Never merge a scheduled job that cannot pass today. A cron that fails every
fifteen minutes is noise that trains everyone to ignore red.

### 4. Every automated trigger has a cost and an owner

CI minutes are money, and someone else usually pays for them.

- Before adding or widening a trigger, estimate runs per day × minutes per run.
- Heavy jobs (CodeQL, SBOMs, attestations, full matrices) run on the main line,
  nightly or on demand, not on every push to every PR.
- If the repo's CI is paused, blocked or deliberately manual, run checks
  locally and say so in the PR. Do not keep pushing into a pipeline you know
  cannot run.

### 5. Land what you open

- **At most three open, unlanded PRs per builder.** At the fourth, stop
  building and land, close or hand over.
- **Stacks deeper than three are a warning.** Each layer multiplies the cost of
  a change at the bottom.
- When the main line moves under you, rebase within the same session, and say
  what changed.
- When later work overtakes one of your open PRs, close it or rebase it the
  same day, with a comment saying where its content went. An abandoned PR
  hides work. The next person rebuilds it without knowing it exists.

### 6. One PR, one purpose

A "fix CI" PR fixes CI. If a feature turns up while fixing something else, it
goes on a new branch. Mixed PRs get stranded: the fix is urgent, the feature
needs review, and the whole thing waits for the slower of the two.

### 7. Green CI is not review

- Never merge your own PR on the strength of green checks alone.
- If there is no reviewer, ask for one by name and work on something else while
  you wait.
- An admin bypass of a review rule is a human's decision, made on purpose, and
  recorded in the PR with the reason. An agent never makes it.
- A PR merged minutes after it was opened has not been reviewed.

### 8. Size PRs for a human

Aim for a change a reviewer can read properly in thirty minutes: roughly 400
lines of hand-written change, excluding generated files. Anything much larger
needs either splitting or an agreed plan with the reviewer before it is opened.
A 100,000-line PR is not a PR. It is a fork being merged back.

### 9. Numbers carry the command that produced them

Every figure in a PR body, such as test counts, timings or "zero findings",
comes with the exact command, and with a CI run link if there is one. "3,600
tests passed" with no command cannot be reproduced, so it is not evidence.

Say what was not verified as plainly as what was.

### 10. No shared file that every change touches

An append-only log, changelog or progress file edited by every commit makes
every pair of branches conflict. Put status in the PR, the issue, or a
per-branch note that is deleted when the branch lands.

### 11. Other people's changes are signals

When someone else commits to the main line, especially rules, docs or config,
read it. If your work disagrees with it, for example re-pinning a version they
deliberately unpinned, say so in your PR. Do not quietly undo it.

### 12. The agent's autonomy has edges

Push, open a PR, merge, deploy and delete branches only on an explicit human
instruction **in the current session**. A standing brief does not authorise
these forever. When the instruction is ambiguous, prepare everything and ask.

## Reviewing a Standing Agent Brief

Most delivery pile-ups trace back to the brief. Look for these lines and
replace them:

| Brief says | Produces | Replace with |
|---|---|---|
| "Work continuously until the definition of done is met" | unbounded stacks | "Stop and summarise when you have three unlanded PRs" |
| "Ask the user only when no useful work remains" | blockers never reach a human | "Escalate any blocker that needs someone else as soon as you find it, then continue" |
| "Record the exact blocker and continue" | accurate logs nobody reads | "Record the blocker **and** open an issue or message naming the owner" |
| "Definition of done: all gates green" | gates built on missing infrastructure | "Definition of done: landed, or waiting on a named person" |
| no mention of other maintainers | silent reverts, ignored rules | "At session start, read changes by others since your last session" |

Put the rules this skill enforces into the file the agent actually reads.

## Session Close

Before ending a session, the agent reports, in the chat and in the PR where it
applies:

- **landed:** what reached the main line, with commit or PR links
- **open:** each open PR, what it is waiting on, and who it is waiting on
- **escalated:** each blocker, with a link to where the owner was told
- **not verified:** anything claimed but not run, and why
- **next:** the single next move

Nothing is left in a state that only the agent understands.

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

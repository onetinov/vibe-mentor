---
name: delivery-mentor
description: "Rules for how a coding agent does work in a shared repository: turn direction into a plan a human approves, work only inside that plan, land what it opens, escalate blockers to a named owner, never build gates on infrastructure that does not exist, no self-merge on green CI, reproducible claims. Use at the start of any piece of work, before opening, stacking or merging a PR, before adding CI workflows or scheduled jobs, when blocked on something only a person can fix, at session end, and when someone asks why work is piling up or reviews an agent brief."
---

# Delivery Mentor

These rules override any standing brief, prompt or habit that says to keep
going without asking, to record blockers and continue, or to decide for the
user. When they conflict, these win, and you say so.

The builder may give you vibes: a direction, an ambition, a feeling about what
the product should do. That is fine. Your job is to turn vibes into a plan, get
it approved, and then follow it. You do not turn vibes into code on your own.

## Plan First

1. **No plan, no code.** Before changing anything, write a plan and stop for
   approval. The plan states: the goal in one sentence; what is in and out of
   scope; the PRs you will open, in order, each with one purpose and a rough
   size; anything you will touch that someone else owns; every blocker you can
   already see, and who can clear it; and what "done" means.
2. **The plan lives where people read it.** Put it in an issue, or in the
   description of the first PR. Never only in a log file, a scratch file or
   your own memory.
3. **Work only inside the approved plan.** A new idea goes on the plan's
   "later" list. It does not become a branch until a human approves it.
4. **Done means the plan is done.** Then stop and report. Do not invent the
   next piece of work because "useful in-scope work remains".
5. **If reality breaks the plan, stop and re-plan.** A bigger change, an
   unexpected dependency or a blocker you can't clear means you update the plan
   and ask again. You do not quietly change course.

## Landing

6. **Start from the present.** Run `git fetch`, then compare against the main
   line. Read `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` and any contribution
   guide, whichever tool you are. Read what other people merged since your last
   session.
7. **At most three open, unlanded PRs.** At the fourth, stop building and land,
   close or hand over. A stack deeper than three is a warning.
8. **One PR, one purpose, reviewable in thirty minutes.** That is roughly 400
   hand-written lines. A fix PR carries no features.
9. **Green CI is not review.** Never merge your own PR. Ask a named reviewer.
   Bypassing a review rule is a human's decision, made on purpose and recorded
   in the PR. You never make it.
10. **Close or rebase what gets overtaken, the same day,** with a comment saying
    where its content went.

## Escalation

11. **A blocker only a person can clear is escalated, not logged.** Open an
    issue or comment, or draft a message, to the named person. Say what is
    needed (the setting, the secret name, the command), what it blocks, and
    what you will do meanwhile. A blocker written only in a file the owner has
    never opened has not been escalated.
12. **Do not build on what cannot run.** Before adding a gate, workflow or
    scheduled job, prove every secret, environment, approval and piece of
    infrastructure it needs exists, and show the command that proves it. If any
    is missing, escalate it and do not add the gate. Never merge a scheduled job
    that cannot pass today.
13. **CI minutes are someone's money.** Estimate runs per day × minutes before
    adding a trigger. Heavy jobs run on the main line or on demand. If CI is
    paused or manual, verify locally and say so.

## Evidence and Authority

14. **Numbers carry their command.** Every figure in a PR comes with the command
    that produced it. Say what you did not verify as plainly as what you did.
15. **No shared file that every change touches.** Status goes in the PR or the
    issue, not an append-only log.
16. **Other people's decisions are signals.** If your change undoes something a
    maintainer did on purpose, say so in the PR. Never do it silently.
17. **Push, open PRs, merge, deploy and delete branches only on explicit
    instruction in this session.** A brief written last week does not count.

## Session Close

End every session with: **landed**, **open** (and what each is waiting on, and
who), **escalated** (with links), **not verified**, and **next**: the single next
move in the plan.

## More

Read [`references/delivery-mentor.md`](references/delivery-mentor.md) when
reviewing an agent brief, when advising a human about how work is landing, or
when you need the reasoning behind a rule.

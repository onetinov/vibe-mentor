# Go-Forward Guidance

## Purpose

Use this document as the standing translation layer between:

- Rob's evolving perspective
- reviewer feedback about what vibe coders actually respond to
- the practical product constraints of `vibe-mentor`

The goal is not to freeze the content. The goal is to keep future additions
relevant, usable, and aligned with the actual job of the skill.

## The Core Product Constraint

`vibe-mentor` is an advisory shaping skill, not a teaching skill.

That means the skill should primarily help the user:

- recognize what kind of system they are building
- spot likely architectural mistakes early
- choose a stronger default
- make the next move with confidence

It should not primarily try to:

- teach fundamentals from first principles
- win architecture debates
- enumerate every possible option
- impress the user with theory

## The User We Are Designing For

The target user is often a vibe coder or fast-moving builder who:

- wants progress, not a seminar
- may have weak system boundaries but decent product instinct
- may already be mid-build and reluctant to rewrite
- benefits from short, decisive corrections more than broad instruction

The skill should respect momentum while still correcting structure.

## The Standing Test For New Content

Before adding new content to a shipped skill, ask:

1. Does this help the model make a better recommendation quickly?
2. Does this change the next move for the user?
3. Does this sharpen classification, boundaries, or defaults?
4. Does this stay useful across many real projects?
5. Would a tired builder actually act on it?

If the answer is mostly no, the content probably belongs in intent docs, notes,
or a specialist reference rather than the front-door skill.

## What The Skill Must Optimize For

### 1. Intervention Timing

The skill must work at three stages:

- `before`: choose the initial shape and place boundaries early
- `during`: catch drift and move logic to a better home without rewriting
- `after`: triage what to keep, refactor, remove, and strengthen next

Advice should change based on stage.

### 2. Boundary Enforcement

The skill is most useful when it makes placement clearer:

- where state lives
- where business logic lives
- where secrets and trust boundaries live
- what is synchronous versus asynchronous
- what must be deterministic
- what must be durable, replayable, or auditable

### 3. Defaults Over Debates

Prefer:

- one recommendation
- one reason
- one risk if ignored
- one next move

Do not default to long option lists unless the trade-off truly matters.

### 4. Momentum-Preserving Correction

The skill should usually say:

- keep the feature, move the logic
- keep the intent, change the placement
- keep the prototype shape where it is harmless
- strengthen only the parts that create real risk

Avoid turning every answer into a rewrite plan.

## Tone Rules

The skill voice should be:

- direct
- calm
- slightly opinionated
- low-ceremony
- practical
- non-preachy

Avoid:

- academic explanation
- superiority
- generic best-practice sludge
- flattery
- sarcasm

Good:

- "Use Postgres here unless you have a strong reason not to."
- "Keep the UI thin and move the business rules into the backend."
- "This works for a demo, but if retries matter, put it in a worker."

Bad:

- "You should study the trade-offs before proceeding."
- "This violates separation of concerns."
- "Best practice would suggest..."

## What Belongs In The Skill

Put these in the shipped skill content:

- durable classification heuristics
- project pattern taxonomy
- stage-aware advice
- boundary questions
- strong defaults
- common failure patterns
- concise review framing
- specific recommendations where Rob has a strong durable opinion
- search directions for current research

## What Usually Does Not Belong In The Skill

Keep these out of the front-door skill unless they are compact and durable:

- long educational explanations
- giant checklists
- static vendor-link collections
- framework-specific recipes with short shelf life
- broad surveys of alternatives
- speculative content not tied to a decision

These may belong in:

- intent docs
- specialist skills
- reference docs
- future implementation examples

## How To Translate Rob's Perspective Into Skill Content

When Rob provides a strong opinion, convert it into one of these forms:

- a classifier rule
- a boundary rule
- a default recommendation
- a failure pattern
- a review heuristic
- a routing rule into a specialist skill

Do not preserve it only as narrative if it can be operationalized.

Examples:

- "less code, more agent" became:
  use deterministic infrastructure for durability and narrow agents for
  routing/synthesis/specialist tool use
- "LangChain deepagents are a good pattern" became:
  recommend `Temporal + deepagents + Pydantic structured-output control` when
  durable multi-turn agents are being built
- "the skill should shape minds on what to look at" became:
  add search directions instead of brittle static links

## Architecture Mentor Response Shape

The front-door skill should generally optimize for:

- `Intent`
- `Keep`
- `Refactor`
- `Remove`
- `Recommendation`
- `Trade-offs`

But the actual guidance should be short and usable.

For many answers, the best internal target is:

- one recommendation
- one reason
- one risk if ignored
- one next move

Do not let the output template become an excuse for verbosity.

## Stage-Aware Guidance Rules

### Before Build

Focus on:

- classifying the project shape
- choosing the simplest viable topology
- placing state, logic, secrets, async work, and persistence explicitly

Win condition:

- stop bad topology before it spreads

### Mid Build

Focus on:

- drift detection
- blurred boundaries
- moving logic to the correct owner
- preventing shortcuts from hardening into architecture

Win condition:

- preserve momentum while correcting placement

### After Build / Review

Focus on:

- triage, not purity
- what is safe to keep
- what must move
- what is dangerous
- what next strengthening step matters most

Win condition:

- give a realistic next strengthening move

## Agentic Guidance Rules

Agentic advice is one important area, but not the whole product.

Default stance:

- treat `agentic` as a modifier unless the product is fundamentally an agent
  runtime/platform
- do not let agentic guidance swallow general architecture guidance

When agentic systems do fit, preserve the specific Rob opinion:

- durable shell over prompt-buried control flow
- deterministic orchestration over agent sprawl
- narrow specialist agents over giant general agents
- skills/tools/schemas before more custom orchestration code
- explicit model-made versus code-enforced boundaries

## Search Guidance Rule

The skill should teach the model to point users toward:

- good search directions
- current standards
- vendor docs when specifics matter

The skill should not pretend that fast-moving implementation details are static.

## Go-Forward Editing Rule

When updating the skill in future sessions:

1. preserve the front-door simplicity
2. convert useful opinions into operational heuristics
3. keep advice stage-aware
4. prefer decisive defaults over neutral summaries
5. cut anything that feels like a lecture
6. keep specialist depth behind the umbrella where possible

## Use In Future Sessions

When starting future work on the repo:

- read this document early
- use it to evaluate whether new content belongs in:
  - the front-door skill
  - a specialist skill
  - a shared reference
  - an intent/planning note

If a proposed addition is insightful but would slow down or dilute the
front-door skill, do not force it in. Route it to the right layer instead.

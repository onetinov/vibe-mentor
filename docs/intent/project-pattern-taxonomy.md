# Project Pattern Taxonomy

## Purpose

Define the minimum useful taxonomy for vibe-coded projects so the front door
skill can classify them quickly and route to stronger advice.

The taxonomy should be simple enough to use early, but sharp enough to change
architecture recommendations.

## Decision

Use one primary pattern plus optional modifiers.

Do not mix:

- product audience such as internal vs external
- topology such as app, workflow, or event-driven
- specialist concerns such as agentic or regulated

Those are different axes and become noisy when treated as one flat list.

## Primary Patterns

Every project should have one default primary pattern:

1. `static frontend`
2. `app + backend + DB`
3. `app + worker`
4. `API / integration backend`
5. `workflow / automation system`
6. `event-driven / dataflow system`
7. `data / compute system`
8. `multi-service platform`

## Pattern Notes

### `static frontend`

Use when the product is mostly a published UI with little owned server logic.

Typical advice:

- keep hosting simple
- push secrets and trust boundaries out of the browser
- do not invent a backend until state, auth, or integration needs force one

### `app + backend + DB`

Use for the default software product shape: UI, backend, owned state.

Typical advice:

- prefer this as the baseline for most products
- keep it monolithic until async work or ownership boundaries are real
- centralize business logic and credential use in the backend

### `app + worker`

Use when the product still has a normal app core, but some work is slow,
retryable, scheduled, or batch-oriented.

Typical advice:

- keep request/response and async execution separate
- make jobs idempotent and restart-safe
- prefer this before jumping to a workflow engine or event mesh

### `API / integration backend`

Use when the main job is serving APIs, brokering systems, or enforcing policy at
service boundaries.

Typical advice:

- make contracts and trust boundaries explicit
- own rate limiting, idempotency, and integration failure handling
- avoid leaking third-party quirks into the rest of the system

### `workflow / automation system`

Use when the product is mostly orchestration of steps, approvals, retries,
timers, or human handoffs.

Typical advice:

- separate step logic from workflow state
- make pause/resume/retry semantics explicit
- use a durable workflow surface when business process continuity matters

### `event-driven / dataflow system`

Use when queues, topics, streams, or async fan-out are the core coordination
mechanism rather than an implementation detail.

Typical advice:

- design for ordering, duplication, replay, and observability
- treat schemas and idempotency as first-class
- avoid eventing when a simpler app+worker design is enough

### `data / compute system`

Use when the core value is pipelines, analysis, model training, batch compute,
or large-scale transformation.

Typical advice:

- optimize for reproducibility, throughput, and lineage
- make storage and compute ownership explicit
- keep user-facing app concerns secondary unless they are truly central

### `multi-service platform`

Use only when multiple services with distinct ownership are already justified.

Typical advice:

- require a clear reason for each service boundary
- distinguish platform needs from premature splitting
- preserve operability over architectural neatness

## Modifiers

Modifiers change the advice, but should not replace the primary pattern:

- `internal tool`
- `external product`
- `integration-heavy`
- `regulated / high-trust`
- `agentic`

More modifiers can be added later, but the umbrella skill should keep the base
set small.

## Agentic Decision

Default rule:

- `agentic` is a modifier, not a primary pattern

Reason:

- agentic describes how some logic is executed
- it does not by itself tell you where state lives, how retries work, or what
  the deployment topology should be
- most real systems with LLMs are still fundamentally one of the primary
  patterns above
- the strongest agentic pattern is usually not "more agent everywhere"; it is a
  durable deterministic shell with narrow agentic decision or synthesis points

Examples:

- chat product with normal backend and DB plus tool-using assistant:
  `app + backend + DB` + `agentic`
- internal ops copilot that kicks off background jobs:
  `app + worker` + `agentic`
- approval-heavy AI task runner:
  `workflow / automation system` + `agentic`
- event-consuming classification pipeline with LLM enrichment:
  `event-driven / dataflow system` + `agentic`

Preferred implementation shape in many cases:

- use a normal app, worker, or workflow topology as the backbone
- keep state, retries, continuity, and branching in deterministic infrastructure
- use agents mainly for routing, synthesis, and specialist tool use
- add capability mostly by adding skills/tools/schemas, not by expanding custom
  orchestration code

Treat `agentic` as a primary concern only when the thing being built is mainly:

- an agent runtime
- a multi-agent orchestration environment
- a tool/skill execution substrate
- an agent platform where pause/resume, memory, tool contracts, and human
  approval semantics are the product

In those cases, the primary topology still matters, but routing into
`agentic-systems-mentor` should happen early.

## Routing Heuristics For The Front Door Skill

Start with the primary pattern first.

Then route deeper based on modifiers and failure modes:

- route to `agentic-systems-mentor` when `agentic` is present and the main risk
  is orchestration, tool contracts, memory, or deterministic-vs-heuristic
  boundaries
- route to `agentic-systems-mentor` early when the builder is trying to bury
  workflow control logic in prompts instead of using a durable execution layer
- route to `auth-and-credentials-mentor` when trust, delegated auth, workload
  identity, or secret handling is central
- route to `prototype-to-production-review` when the main issue is durability,
  operability, or laptopware risk
- route to `platform-shape-advisor` when the primary pattern itself is unclear

## Minimum Useful Rule

If the classifier cannot confidently distinguish a more specialized pattern,
default to:

- `app + backend + DB`

Then add:

- `app + worker` if async work is structurally important
- `workflow / automation system` if long-running process state is the product
- `event-driven / dataflow system` if events are the coordination backbone
- `agentic` if LLM behavior materially changes the design

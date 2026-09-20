# Skill Family Map

## Overview

`vibe-mentor` is likely a family of skills, not a single forever-skill.

The current plan is:

- one umbrella front door skill
- several specialist skills behind it
- shared content where possible

## Front Door

### `architecture-mentor`

Use for:

- greenfield architecture guidance
- in-flight architecture steering
- architecture review
- prototype-to-production sanity checks

Responsibilities:

- classify project shape
- classify maturity and risk
- identify the likely advice mode
- give first-pass recommendations
- do first-pass production-readiness triage
- pull in specialist depth when needed

## Specialist Skills

### `prototype-to-production-review`

Use for:

- "What is still laptopware here?"
- "What would need to change before production?"
- "This works, but is it production-worthy?"

Responsibilities:

- deployability
- observability
- retries and recovery
- state ownership
- config and environment discipline
- operational hardening
- operational ownership
- sequencing hardening work across multiple gaps

Boundary from `architecture-mentor`:

- `architecture-mentor` should catch the biggest production-readiness problem
  and recommend the next strengthening move
- `prototype-to-production-review` should go deeper when the user wants a real
  hardening audit, sequencing, or multi-area operational diagnosis

### `auth-and-credentials-mentor`

Use for:

- auth model selection
- enterprise SSO
- Entra / OIDC / OAuth guidance
- service-to-service trust boundaries
- secret storage and retrieval patterns

Responsibilities:

- auth architecture
- workload identity
- Vault / Secrets Manager / secret injection patterns
- delegated token ownership
- audit and rotation expectations

### `agentic-systems-mentor`

Use for:

- LLM + tool orchestration design
- prompt / skill / schema / workflow boundaries
- MCP-related system shape questions
- productionizing agent behavior

Responsibilities:

- orchestration shape
- tool contracts
- deterministic vs heuristic boundaries
- pause / resume / retry semantics
- human-in-the-loop design
- durable workflow shell plus narrow specialist-agent pattern
- skill/schema/tool boundaries with minimal custom control code

### `platform-shape-advisor`

Use for:

- "What pattern am I really building?"
- "Should this be monolith, app+worker, workflow, event-driven, microservices?"
- "What is the simplest viable topology?"

Responsibilities:

- project-shape classification
- topology recommendation
- scaling / complexity trade-offs

### `integration-and-mcp-advisor`

Use for:

- external systems
- integration platform shape
- MCP/tool surface design
- third-party tool boundaries

Responsibilities:

- API/integration contracts
- delegated auth for integrations
- tenancy, rate limits, idempotency
- safe action boundaries

### `incident-architecture-review`

Use for:

- resilience review
- failure-mode analysis
- incident learning and redesign

Responsibilities:

- blast radius
- graceful degradation
- recovery paths
- replay / restart safety

### `delivery-mentor`

Use for:

- "Why is everything stuck?" / "Why are there twenty open PRs?"
- an agent about to open, stack, merge or close pull requests
- an agent about to add CI workflows, scheduled jobs or release gates
- a blocker only someone else can clear
- session start and close in a shared repository
- reviewing a standing brief for an autonomous coding agent

Responsibilities:

- plan first: turn direction into a plan a human approves, work only inside it,
  stop when it is done
- escalation of blockers to a named owner, in a channel they read
- landing discipline: cap on unlanded PRs, stack depth, closing overtaken PRs
- review discipline: no self-merge on green CI; bypass is a recorded human decision
- gates and schedules only when their dependencies provably exist
- CI cost awareness
- reproducible claims: every number carries its command

Boundary from `architecture-mentor`:

- `architecture-mentor` covers the shape of the system, including repo scope
  and git hygiene as architecture concerns
- `delivery-mentor` covers how work moves from a builder's branch onto the main
  line alongside other people, and how an autonomous agent's brief shapes that

## Shared Content Areas

These should probably be shared across multiple skills:

- project taxonomy
- production-readiness lens:
  `laptopware / deployability / observability / config / recovery / ownership`
- review framing:
  `Intent / Keep / Refactor / Remove / Recommendation / Trade-offs`
- mentoring tone
- architecture heuristics
- ask-only-necessary-questions rule

## Recommended Build Order

1. `architecture-mentor`
2. `prototype-to-production-review`
3. `auth-and-credentials-mentor`
4. `agentic-systems-mentor`
5. `platform-shape-advisor`
6. `integration-and-mcp-advisor`
7. `incident-architecture-review`

# Session Sequence Guide

## Purpose

Use this guide to continue work across multiple fresh sessions without losing
the plan.

The recommended workflow is:

1. start a fresh session
2. load the current intent docs
3. focus on one skill or one topic only
4. combine internet research, model knowledge, and Rob-specific interview input
5. update the repo docs and skill content

## Always Load First In A Fresh Session

Read these first:

- `README.md`
- `TODO.md`
- `docs/intent/vibe-mentor-intent.md`
- `docs/intent/go-forward-guidance.md`
- `docs/intent/skill-family-map.md`
- `docs/intent/session-sequence-guide.md`

If working on the current main skill, also read:

- `content/architecture-mentor.md`
- `content/architecture-mentor-review.md`
- `skills/architecture-mentor/SKILL.md`

## Recommended Session Sequence

### Session 1: Front Door Skill Shape

Goal:

- tighten `architecture-mentor` as the umbrella skill
- refine its entry points and modes

Key questions:

- what should trigger it?
- what modes should it expose?
- what should stay in the umbrella vs split out?

Likely outputs:

- improved `skills/architecture-mentor/SKILL.md`
- refined shared architecture guidance

### Session 2: Project Pattern Taxonomy

Goal:

- settle the high-level project patterns
- decide how to treat agentic systems

Topics:

- static frontend
- app + backend + DB
- app + worker
- API / integration platform
- workflow / automation system
- event-driven system
- data / compute system
- multi-service platform

Question to settle:

- is agentic a top-level pattern or a modifier?

Likely outputs:

- project-shape classifier content
- trigger and routing heuristics
- `docs/intent/project-pattern-taxonomy.md`

### Session 3: Prototype-to-Production Review

Goal:

- define the hardening / review skill more clearly
- tighten how the umbrella skill handles production-readiness advice during and
  after the build

Topics:

- laptopware detection
- deployability
- observability
- config discipline
- recovery and retry
- operational ownership

Likely outputs:

- `docs/intent/prototype-to-production-review.md`
- shipped `architecture-mentor` hardening guidance
- maybe first specialist skill scaffold later

### Session 4: Auth And Credential Patterns

Goal:

- capture auth and secret-management advice

Topics:

- auth models
- enterprise SSO / Entra / OIDC
- delegated OAuth
- workload identity
- Vault
- AWS Secrets Manager
- EC2 vs k8s vs serverless credential patterns
- env vars vs mounted secrets vs identity-based fetch

Likely outputs:

- `auth-and-credentials-mentor` intent doc
- shared credential-pattern reference

### Session 5: Agentic Systems

Goal:

- define how agentic architecture advice differs from generic app advice

Topics:

- workflow vs agent loop
- MCP vs API vs internal tool calls
- prompts vs schemas vs orchestration
- durable execution and human-in-the-loop

Likely outputs:

- `agentic-systems-mentor` intent doc
- maybe first shared reference doc

### Session 6: Platform Shape Advisor

Goal:

- make topology advice sharper and more explicit

Topics:

- monolith vs modular monolith
- app+worker
- workflow engines
- eventing
- microservices
- when not to split

### Session 7: Integration And MCP Advice

Goal:

- define integration and MCP-specific guidance

Topics:

- MCP server shape
- integration boundaries
- auth delegation
- idempotency and safe actions

### Session 8: Packaging And Live Install Testing

Goal:

- test actual install behavior in Codex and Claude

Topics:

- `codex plugin marketplace add onetinov/vibe-mentor`
- `claude plugin marketplace add onetinov/vibe-mentor`
- direct plugin install behavior
- trigger behavior in each client

## Standard Method For Topic Sessions

When focusing on a topic:

1. gather official/current internet references
2. summarize the general model knowledge
3. interview Rob for the delta:
   what do you believe, where do you disagree, what do you care about most?
4. convert that into durable heuristics
5. decide whether it belongs in:
   - shared content
   - umbrella skill
   - specialist skill

## Good User Entry Points To Preserve

- "I am building an app to do X. I want good architecture advice."
- "I have been coding this app for a while. I want an architecture review."
- "I have a working prototype. Can you review whether it is well coded?"
- "How should auth and credentials work here?"
- "How should this agentic system be structured?"

## Notes For Fresh Session Use

If starting a new session, tell the model something like:

> Read `docs/intent/vibe-mentor-intent.md`,
> `docs/intent/skill-family-map.md`, and
> `docs/intent/session-sequence-guide.md` first.
> Then help me continue with session N or topic X.

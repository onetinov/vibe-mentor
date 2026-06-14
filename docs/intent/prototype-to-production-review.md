# Prototype To Production Review

## Purpose

Define the minimum useful shape for production-readiness review inside
`vibe-mentor`.

This topic matters because many systems fail in the same predictable way:

- they demo well
- they ship with blurred ownership
- they depend on one builder's laptop or memory
- they have no safe story for deploy, restart, retry, observe, or hand off

The goal is not to turn the front door skill into a giant checklist engine.
The goal is to help the model spot the most important hardening gap quickly and
recommend the next strengthening move without killing momentum.

## Product Constraint

This remains an advisory shaping capability, not a teaching capability.

The hardening advice should usually reduce to:

- one recommendation
- one reason
- one risk if ignored
- one next move

Long production-readiness audits should be a deeper layer, not the default
front-door behavior.

## Minimum Useful Session 3 Structure

Session 3 only needs three durable outputs:

1. define the hardening review lens the umbrella skill should always apply
2. define the boundary between `architecture-mentor` and a future
   `prototype-to-production-review` specialist skill
3. capture the deeper hardening taxonomy in intent docs so it can split cleanly
   later

That is enough for now. A full specialist skill scaffold is optional.

## Hardening Review Lens

The minimum durable review lens is:

1. laptopware detection
2. deployability
3. observability
4. config and environment discipline
5. retry / recovery / restart safety
6. operational ownership

These are useful because they surface whether the system can survive normal
production reality instead of only ideal-path demos.

## What `architecture-mentor` Should Own

The umbrella skill should own first-pass production-readiness triage.

That means it should:

- detect when the main risk is operational, not conceptual
- name the most important hardening gap in plain language
- preserve the working prototype where it is harmless
- recommend the smallest architecture or ownership change that makes deployment
  safer
- adapt the advice by stage:
  `during` means fix the highest-leverage boundary without stalling delivery;
  `after` means triage what can stay, what must move, and what next hardening
  step matters most

The umbrella skill should not default to exhaustive audit mode.

## What A Future Specialist Skill Should Own

`prototype-to-production-review` should exist when the deeper layer is needed.

That specialist should own:

- fuller production-readiness audits
- sequencing of multiple hardening moves
- operational trade-offs across topology, deployment model, and team ownership
- deeper recovery, rollback, DR, and on-call realism
- stage-specific hardening plans for systems that are already deployed or close
  to deployment

In short:

- umbrella skill: first-pass correction and routing
- specialist skill: deeper hardening diagnosis and sequencing

## Shipped Content Vs Intent / Reference

Add to shipped `architecture-mentor` content:

- the hardening sequence:
  `git scope -> grounding docs -> reproducible build -> deploy realism ->
  observability -> recovery -> low-ops ownership`
- concise laptopware heuristics
- deployment-intent classes and how they change rigor
- maturity-triggered grounding-doc rules
- stage-aware rules for mid-build and post-build production-readiness advice
- default wording that favors one hardening recommendation over a long list

Keep in intent or future specialist/reference material:

- detailed multi-area audit frameworks
- long deploy checklists
- vendor-specific observability and platform recipes
- rollback / DR / SRE process depth
- environment-matrix detail by cloud, container, VM, or serverless platform

## Durable Heuristics Per Hardening Area

### Repo Boundary And Git Hygiene

Signals:

- the repo root is too high or captures unrelated files
- vendored dependencies, generated artifacts, or secrets are tracked as if they
  were owned source
- `.gitignore` does not cleanly separate owned code from bulk noise
- the builder cannot explain what belongs in the repo and what does not

Default correction:

- narrow the repo boundary and fix `.gitignore` before deeper hardening
- treat git as the first escape from local-only development, not as an archive
  of the whole laptop

### Grounding Docs And Drift Control

Signals:

- the project has become an app, grown beyond trivial scope, or become
  collaborative
- there is no short durable statement of what is being built
- long sessions are causing context rot or silent direction drift

Default correction:

- add one short intent doc and one short session/state doc
- keep them compact enough for repeated rereads

### Reproducible Build And Runtime Discipline

Signals:

- it works only on one laptop
- local shell history is the real build system
- the path from source to runtime is implicit
- existing container or CI paths were ignored for convenience

Default correction:

- make the build work off-laptop
- containers are a strong default, but runtime reproducibility is the real goal

### Deployment-Surface Realism

Signals:

- the user expects a public surface but deployment mechanics are hand-waved
- hosted web apps and APIs have no explicit story for ingress, TLS, or secret
  handling
- deployment intent implies malicious actors, but the architecture still thinks
  like a private local app

Default correction:

- classify deployment intent explicitly and raise rigor accordingly
- do not let public or commercial systems pretend they are harmless experiments

### Observability

Signals:

- failures are discovered by user reports
- logs are ad hoc or local-only
- no clear way to trace a request, job, or workflow across boundaries
- token spend, support load, or operational investigations are expected but not
  instrumented

Default correction:

- add enough logs, metrics, and identifiers to debug the primary failure path

### Retry / Recovery / Restart Safety

Signals:

- retries can duplicate side effects
- restart loses important progress
- timeouts, backoff, and compensation rules are undefined

Default correction:

- make critical units idempotent and make recovery ownership explicit

### Low-Ops Ownership

Signals:

- nobody clearly owns deploy, alert response, or data repair
- service boundaries exist without corresponding team or runtime ownership
- handoff would fail because the reasoning is trapped in one person's head
- future agents would struggle to inspect or explain failures

Default correction:

- align system boundaries with actual ownership and write the minimum runbook
- prefer traces and workflow surfaces that make robotic investigation easier

## Routing Rule

Route from `architecture-mentor` into the future specialist skill when:

- the first-pass recommendation is clearly "this needs a hardening review, not a
  topology debate"
- multiple production-readiness gaps interact and sequencing matters
- the user asks for a real production-readiness audit, not just next-move advice

## Minimum Useful Future Specialist Structure

When the specialist is eventually created, keep it compact:

1. when to use
2. review lens
3. severity order
4. output shape
5. routing back to umbrella or adjacent specialist skills

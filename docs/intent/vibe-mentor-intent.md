# Vibe Mentor Intent

## Purpose

Build a public repository of mentoring skills that help a builder use AI coding
tools with stronger software architecture, operational judgment, and production
thinking.

The repo name is broader than the first skill on purpose:

- repo / marketplace umbrella: `vibe-mentor`
- first concrete skill: `architecture-mentor`

The goal is not personality simulation. The goal is to capture durable
engineering judgment and make it reusable across Claude Code and OpenAI Codex.

## Core Thesis

The junior builder and the senior builder can use the same models and tools.
What differs is usually:

- project classification
- pattern recognition
- trust-boundary awareness
- operational realism
- prompting and decomposition discipline

This repo tries to package those differences into reusable skills.

## Product Goal

Create a shared source of truth for mentoring skills that can be distributed as:

- Claude plugins / skills
- Codex plugins / skills

without duplicating the real content unnecessarily.

## Initial User Promise

These skills should help users:

- choose a sane architecture early
- recover from messy vibe-coded divergence
- review prototypes charitably but rigorously
- harden systems toward production
- reason better about auth, credentials, integrations, and agentic patterns

## What This Repo Is Not

It is not:

- a single giant monolithic skill forever
- a repo-specific `agentmaker` persona
- architecture dogma for its own sake
- enterprise ceremony pasted onto every project

## First Skill Direction

The first skill is `architecture-mentor`.

It should be the front door skill that helps a user say things like:

- "I am building an app to do X. What architecture should I use?"
- "I have been coding this app for a while. Can you review the architecture?"
- "I have a working prototype. Is it well coded?"
- "Do this the way Rob would."

## Key Knowledge Areas Captured So Far

- project-shape classification
- architecture review and trade-off analysis
- prototype-to-production hardening
- agentic system design as a modifier or specialist area
- durable-shell agentic patterns: less orchestration code, more skill-grounded
  agents inside deterministic workflow/backends
- auth and credential patterns as a cross-cutting area
- platform selection and operational maturity

## Working Principle

Prefer one natural front door and several specialist skills behind it.

That means:

- keep the first entry point simple
- let deeper areas split into focused skills as the content hardens

## Current Public Repo

- GitHub repo: `https://github.com/onetinov/vibe-mentor`

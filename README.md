# ai-project-setup

> A Cursor Skill that initializes AI collaboration documentation infrastructure for any project.

[中文版](./README.zh-CN.md) | English

---

## What Problem Does It Solve?

When you bring AI into a real project, these failures happen constantly:

- **AI modifies code it shouldn't** — no protected zones defined, AI casually "improves" stable modules
- **AI forgets decisions from the last session** — no MEMORY.md, every new conversation starts from scratch
- **AI-generated code doesn't follow team standards** — no Cursor Rules, only verbal reminders
- **Architecture decisions aren't recorded** — no ADR, three months later you discover deep coupling

This Skill solves all of the above in under 5 minutes.

---

## Install

Copy `SKILL.md` into your Cursor Skills directory:

```bash
# Personal global use (recommended)
~/.cursor/skills/ai-project-setup/SKILL.md

# Project-level use (shared with team)
.cursor/skills/ai-project-setup/SKILL.md
```

---

## Usage

Just tell Cursor:

```
setup AI project documentation
```

or:

```
initialize AI collaboration docs for this project
```

The Skill will ask you 6 questions, then generate a complete documentation skeleton tailored to your project.

---

## Generated File Structure

```
your-project/
├── AGENTS.md                         ← AI onboarding file (core)
├── MEMORY.md                         ← Cross-session progress tracking
├── ROADMAP.md                        ← Phase plan + Definition of Done
├── docs/
│   ├── ARCHITECTURE.md               ← System architecture skeleton
│   ├── decisions/
│   │   ├── README.md                 ← ADR index
│   │   └── YYYY-MM-DD-tech-stack.md  ← Initial tech stack decision
│   └── anti-patterns.md              ← Mistake log
├── .cursor/
│   └── rules/
│       ├── general.mdc               ← General standards (auto-injected)
│       ├── git-commits.mdc           ← Commit standards (auto-injected)
│       └── [typescript|python].mdc   ← Tech stack rules (generated on demand)
├── .github/
│   └── copilot-instructions.md       ← Copilot config (Copilot users only)
└── eval/
    └── eval.py | eval.js             ← AI output eval (AI features only)
```

---

## Core Concepts

### AGENTS.md — AI Onboarding File

Every time a new conversation starts, the AI reads this to align on context. Contains:
- Project overview and tech stack
- **Protected zones** — which code must not be touched
- **Critical Rules** — non-negotiable red lines
- **Agentic Guardrails** — shell command allow/deny lists for autonomous tasks
- **Definition of Done** — doc sync discipline (MEMORY + ROADMAP + ADR + anti-patterns)
- Code standards
- "Where to Look" index

### MEMORY.md — Cross-Session Memory

AI's biggest engineering problem is no persistent memory. MEMORY.md is a manually maintained "progress tracker" — updated after every session, read at the start of the next one so the AI can resume exactly where it left off.

**Iron rule: MEMORY.md not updated = session not closed.**

### ROADMAP.md — Phase Planning

Phase-based roadmap with explicit Definitions of Done. Each Phase has hard exit criteria — the next Phase cannot start until all DoD items are checked off. Includes a **completion discipline table** that runs after every task.

### docs/decisions/ — Architecture Decision Records (ADR)

Every important decision gets a date-named Markdown file recording Context → Decision → Alternatives → Consequences. AI reads `docs/decisions/` newest-first, so it won't circle back to the same questions.

### docs/ARCHITECTURE.md — Architecture Skeleton

A structured template for documenting the system's high-level architecture, module breakdown, data flow, and key design decisions. Starts as a skeleton — fill it in as the project grows.

### .cursor/rules/ — Auto-Injected Code Standards

Rules files are injected automatically into every conversation — no need for the AI to actively read them. Generated per tech stack (TypeScript strict mode, Python type annotations, Git commit format, etc.).

---

## Use Cases

| Scenario | Benefit |
|----------|---------|
| Starting a new project | AI collaboration foundation ready in 5 minutes |
| Retrofitting an existing project | Add missing AGENTS.md and MEMORY.md |
| Team sharing | Put Skill in `.cursor/skills/` for a consistent onboarding flow |
| Personal open-source projects | Lets contributors (human or AI) ramp up quickly |

---

## Relationship to ai-memory

[ai-memory](https://github.com/hyxnj666-creator/ai-memory) is **extraction** — automatically extracts knowledge from AI conversation history and writes it into AGENTS.md.

This Skill is **active setup** — manually builds the documentation skeleton at project initialization, telling AI what the rules are from the start.

They complement each other: use this Skill to build the skeleton, then use ai-memory to continuously extract new knowledge from conversations and fill it in.

---

## Background

This Skill is distilled from real-world experience on two projects:

- **conor-site**: Next.js + AI Persona engine, managed with MEMORY.md + Feature Gates
- **ai-memory**: Open-source CLI tool, managed with ADR + Spike-First discipline

Full write-up: [AI Dev Standards: An Engineering System for Stable AI Collaboration](https://blog.conorliu.com/series/topics/14-ai-dev-standards/)

---

## Language Support

| File | Language |
|------|----------|
| `SKILL.md` | English (primary) |
| `SKILL.zh.md` | 中文 |
| `README.md` | English |
| `README.zh-CN.md` | 中文 |

---

## License

MIT

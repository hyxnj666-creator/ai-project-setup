---
name: ai-project-setup
description: >-
  Initialize AI collaboration documentation infrastructure for any project.
  Use when starting a new project, setting up AI development rules from scratch,
  or when asked to create AGENTS.md, MEMORY.md, ROADMAP.md, ADR folders,
  Cursor Rules, or any AI-readable project documentation baseline.
---

# AI Project Setup

Initialize any project into a state where AI can collaborate reliably — generating AGENTS.md, MEMORY.md, ROADMAP.md, ADR directory, Cursor Rules, ARCHITECTURE skeleton, and more.

---

## Step 0: Gather Information Before Starting

**Do not start generating files immediately. Ask the user these questions first:**

### Required (6 questions — list all at once, wait for answers)

```
Before I start, I need to understand your project:

1. **Project type** (pick the closest one)
   - Frontend app (Next.js / Vue / React)
   - Backend service (Node.js / Python / Go)
   - CLI tool / open-source library
   - Full-stack monorepo
   - Other: ___

2. **Main tech stack**
   e.g. TypeScript + Next.js 14 + Prisma + PostgreSQL

3. **Any code that must be protected from AI changes?**
   e.g. v1 is live and stable, a core module that shouldn't be touched, production DB off-limits
   Say "none" if not applicable.

4. **Any AI-driven core features?**
   e.g. LLM API calls, RAG retrieval, AI-generated content
   (If yes, an optional Prompt eval scaffold will be generated)

5. **Which AI editors / agents do you use?** (multi-select)
   - Cursor
   - Claude Code
   - GitHub Copilot
   - Codex CLI
   - Other: ___
   (Determines which config files to generate)

6. **Will the project use MCP (Model Context Protocol) tools?**
   e.g. filesystem MCP, database MCP, ai-memory MCP
   Say "none" if not applicable.
```

After receiving answers, proceed to Step 1.

---

## Step 1: Generate AGENTS.md

Generate `AGENTS.md` in the project root using the template below. Fill in all `[placeholders]` with the user's answers:

```markdown
# [Project Name] — AI Development Rules

> This file applies to all AI coding assistants (Cursor, Claude Code, GitHub Copilot, Codex CLI, and any other agents).
> Read this file in order before starting any development work.

---

## 1. Mandatory Reading Order

Before writing any code, read these files in order:

```
1. ROADMAP.md       ← Current phase and goals (WHAT)
2. MEMORY.md        ← Where we left off, known landmines (WHERE WE LEFT OFF)
3. docs/decisions/  ← Key decision records, newest-first (WHY)
```

**If anything is unclear, stop and ask. Do not read and modify code at the same time.**

---

## 2. Project Overview

[One sentence describing what this project does]

**Tech stack**: [user's tech stack]

**Target users**: [who this is for]

---

## 3. 🔒 Protected Zones (Do Not Touch)

[If the user has protected areas, fill in here; otherwise delete this section or write "No special restrictions"]

The following code / paths / resources **must NOT be modified without explicit confirmation**:

- `[protected path or module]`: [reason, e.g. v1 is live, changes affect production]

Any modification to the above requires explicit confirmation first.

---

## 4. Critical Rules (Non-Negotiable)

1. **All new features must have tests** — code without tests is not done
2. **Breaking changes require explicit authorization** — don't "casually refactor" stable modules
3. **Minimize dependencies** — confirm there's no built-in alternative before adding a new package
4. **Keep docs in sync** — if code changes, MEMORY.md must be updated in the same session
5. **No write operations on production paths** — don't modify production DB / production API without confirmation

---

## 5. Agentic Execution Guardrails

> Extra constraints for autonomous agentic tasks (AI independently reading/writing files, running commands, calling APIs).

**Shell commands**:
- ✅ Safe to run autonomously: `git status / diff / log`, `npm run test / build / lint`, read-only queries
- ⚠️ Must notify before running: `git commit / push`, `npm publish`, `docker`
- 🚫 Strictly forbidden: `rm -rf`, `DROP TABLE`, write operations to production APIs, modifying `.env` / secrets

**File system**:
- Must not read or write `.env`, `*.secret`, `*.key`, `credentials.*`
- Must not modify any files inside protected zones (see Section 3)
- Before overwriting an existing file, confirm with the user first

---

## 6. Definition of Done (Doc Sync Discipline)

**After completing any piece of work, check off the following in the same session:**

| # | Document | When Required |
|---|----------|---------------|
| 1 | `MEMORY.md` | **Always** — update current status + next steps + completed items |
| 2 | `ROADMAP.md` | When Phase progress changes — check off the relevant sub-item |
| 3 | Relevant ADR | When a decision is revised — append revision history (don't edit original) |
| 4 | `docs/anti-patterns.md` | When a mistake is made — record the anti-pattern + correct approach |

**Incomplete checklist = work is not done. Do not move to the next task / commit / tell the user "it's done".**

---

## 7. Code Standards

### General
- Use descriptive names — avoid tmp/data/obj/info and other meaningless words
- Each function does one thing — consider splitting if over 50 lines
- Errors must be handled — no empty catch blocks
- No dead code — delete commented-out old code, don't leave it

### [Tech Stack Specifics]

[Fill in based on tech stack, e.g.:]

**TypeScript**:
- No `any` — use `unknown` + type guards
- async functions must have try/catch
- Exported functions must have JSDoc

**Python**:
- Full type annotations (function parameters and return values)
- Use dataclass / Pydantic instead of bare dicts
- Be specific with exceptions — no bare `Exception`

---

## 8. Architecture Patterns

**Separate business logic from I/O**:
- Business logic as pure functions (no side effects, easy to test)
- File I/O, network requests, and DB operations in thin outer wrappers

**Error handling**:
- External API failures return empty values / defaults rather than throwing
- The caller decides whether a "failure" is an error

---

## 9. MCP Configuration

[Only fill in if the project uses MCP; otherwise delete this section]

**Allowed MCP tools**:
- `[mcp-name]`: [purpose, e.g. filesystem — read/write local files]

**MCP tools forbidden in production**:
- `[mcp-name]`: [reason]

---

## 10. Common Task Checklists

### Adding a New Feature
1. Clarify requirements, record plan in MEMORY.md
2. (For complex features) Write a spike doc before writing code
3. Implement, following Critical Rules and Agentic Guardrails
4. Write tests
5. Run DoD checklist (Section 6)

### Fixing a Bug
1. Reproduce the issue, confirm root cause
2. Fix + add regression test
3. Run DoD checklist (Section 6)

### Recording a Key Decision
1. Write ADR to `docs/decisions/YYYY-MM-DD-topic.md`
2. Add entry to the index in `docs/decisions/README.md`

---

## 11. Where to Look

| Question | Where to go |
|----------|------------|
| What are we working on / progress | `MEMORY.md` |
| This Phase's goals / DoD | `ROADMAP.md` |
| Why was this decision made | `docs/decisions/` newest-first |
| What mistakes have been made | `docs/anti-patterns.md` |
| What is the system architecture | `docs/ARCHITECTURE.md` |
| How to release / deploy | `docs/DEPLOY.md` (if exists) |
```

---

## Step 1.5: Generate ROADMAP.md

Generate `ROADMAP.md` in the project root:

```markdown
# [Project Name] Roadmap

> **WHAT layer**: Goals, deliverables, and Definition of Done for each Phase.
> For WHY, see `docs/decisions/`.
> For progress, see `MEMORY.md`.
>
> **Rule: Each Phase has a hard DoD. You may not advance to the next Phase until it is met.**

---

## 🔴 Development Discipline (Run After Every Task)

After completing any piece of work, complete the relevant items below in the same session:

| # | Document | When Required | Update |
|---|----------|---------------|--------|
| 1 | `MEMORY.md` | **Always** | Current status + next steps + completed items |
| 2 | `ROADMAP.md` | When Phase progress changes | Check off sub-items in the current Phase |
| 3 | Relevant ADR | When a decision is revised | Append revision history (don't edit original) |
| 4 | `docs/anti-patterns.md` | When a mistake is made | Anti-pattern + correct approach |

**Incomplete checklist = work is not done. Do not move on / commit / say "it's done".**

---

## Current Status

| Item | Value |
|------|-------|
| Current Phase | **Phase 0 · Documentation Foundation** |
| Next Phase | Phase 1 · [fill in next phase name] |
| Live Version | Not yet released |
| Last Updated | [today's date] |

---

## Phase Overview

| Phase | Name | Status | Est. Duration | Prerequisites |
|-------|------|--------|---------------|---------------|
| **0** | Documentation Foundation | ✅ Done | 0.5 days | — |
| **1** | [First Phase Name] | ⏸ Not started | [estimate] | Phase 0 closed |
| **2** | [Second Phase Name] | ⏸ Not started | [estimate] | Phase 1 closed |

---

## Phase 0 · Documentation Foundation

**Goal**: Build the AI collaboration document skeleton so any AI assistant can onboard quickly.

**Deliverables**:
- [x] AGENTS.md
- [x] MEMORY.md
- [x] ROADMAP.md
- [x] docs/decisions/ directory + initial ADR
- [x] docs/ARCHITECTURE.md skeleton
- [x] .cursor/rules/ standards files

**Definition of Done**:
- [ ] AGENTS.md has protected zones + Critical Rules + DoD checklist
- [ ] MEMORY.md has current status + next steps
- [ ] docs/decisions/ has a tech stack ADR

---

## Phase 1 · [Phase Name]

**Goal**: [What this phase needs to accomplish]

**Deliverables**:
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Definition of Done**:
- [ ] [Acceptance criteria 1]
- [ ] [Acceptance criteria 2]

---

## Decision Log

| Date | Decision | See |
|------|----------|-----|
| [today's date] | Initialize project documentation foundation | — |
```

---

## Step 2: Generate MEMORY.md

Generate `MEMORY.md` in the project root:

```markdown
# Development Progress

> Update this file after every development session. **Not updated = session not closed.**
> AI assistants must read this file at the start of each new session.

---

## Current Status

**Date**: [today's date]
**Phase**: Phase 0 · Documentation Foundation (complete)

**Working on**: Waiting for user to start Phase 1

**Next steps**:
- [ ] Fill in Phase 1 deliverables and DoD in ROADMAP.md
- [ ] Start the first task of Phase 1

---

## Completed

- [today's date] Initialized AI documentation foundation (AGENTS.md, MEMORY.md, ROADMAP.md, ADR directory, ARCHITECTURE skeleton)

---

## Notes / Known Landmines

> AI assistants: read this section at the start of every new session

[No known issues yet. Record any problems encountered here: date + description + solution]
```

---

## Step 3: Generate docs/decisions/ Directory

Create the `docs/decisions/` directory with two files:

### docs/decisions/README.md

```markdown
# Architecture Decision Records (ADR)

Records every important technical / architectural / product decision in this project.

**AI assistants: read from the newest file first (files are sorted by date, descending).**

---

## File Naming

```
YYYY-MM-DD-decision-topic.md
```

## ADR Structure

```markdown
# ADR YYYY-MM-DD — [Decision Title]

**Status**: Accepted | Superseded by [new ADR]

## Context
Why this decision needed to be made

## Decision
What was decided

## Alternatives
- Option A: why it wasn't chosen
- Option B: why it wasn't chosen

## Consequences
- Benefits
- Costs / constraints
```

---

## Decision Index

| Date | File | Summary |
|------|------|---------|
| [today's date] | [today's date]-tech-stack.md | Initial tech stack selection |
```

### docs/decisions/[today's date]-tech-stack.md

```markdown
# ADR [today's date] — Tech Stack Selection

**Status**: Accepted

## Context

Project initialization — need to decide on the primary tech stack.

## Decision

Using [user's tech stack].

## Alternatives

[If the user mentioned alternatives, fill in here; otherwise write "No detailed comparison at initialization — major changes in the future require a new ADR"]

## Consequences

- Once set, changing core frameworks requires a new ADR
- [Other implications]
```

---

## Step 3.5: Generate docs/ARCHITECTURE.md Skeleton

Generate `docs/ARCHITECTURE.md`:

```markdown
# System Architecture

> Describes [project name]'s overall architecture, module breakdown, data flow, and key design decisions.
> For decision rationale, see `docs/decisions/`.

---

## High-Level Architecture

[Use ASCII art or Mermaid to describe the overall system structure]

```
[Placeholder — draw your architecture diagram here]

Example (web app):
Browser → Nginx → Next.js (App Router) → API Routes → Service Layer → PostgreSQL
                                                     ↓
                                                  Redis (Cache)

Example (CLI tool):
CLI Entry → Argument Parser → Commands → Core Logic → File System / API
```

---

## Module Breakdown

| Module | Path | Responsibility |
|--------|------|----------------|
| [Module name] | `[path]` | [One-line description] |

---

## Data Flow

### [Main Business Flow Name]

```
Step 1: [description]
  ↓
Step 2: [description]
  ↓
Step 3: [description]
```

---

## Key Design Decisions

| Decision | Choice | See |
|----------|--------|-----|
| Tech stack | [fill in] | `docs/decisions/[date]-tech-stack.md` |

---

## External Dependencies

| Dependency | Purpose | Notes |
|------------|---------|-------|
| [fill in] | [fill in] | [version constraints or notes] |

---

## Performance / Security Boundaries

- [Performance target, e.g. API response time < 200ms p95]
- [Security constraint, e.g. sensitive data must not appear in logs]
- [Capacity constraint, e.g. single file upload max 10MB]
```

---

## Step 4: Generate .cursor/rules/ Files

Generate Cursor Rules based on the user's tech stack.

### Always generate (all projects)

**`.cursor/rules/general.mdc`**:

```yaml
---
description: General development standards, applies to all files
alwaysApply: true
---

# General Standards

- Use descriptive names — avoid tmp/data/obj/info and other meaningless words
- No dead code (commented-out old code)
- No console.log left in production code
- Errors must be handled — no empty catch blocks
- New features must have tests — code without tests is not done

# Completion Discipline

After finishing any work, update MEMORY.md in the same session.
When Phase progress changes, update ROADMAP.md as well.
Not updated = not done.
```

**`.cursor/rules/git-commits.mdc`**:

```yaml
---
description: Git commit message standards
alwaysApply: true
---

# Commit Message Format

Use Conventional Commits format:

type(scope): description

Allowed types:
- feat: new feature
- fix: bug fix
- refactor: refactoring (no behavior change)
- test: test-related
- docs: documentation
- chore: tooling, dependencies, configuration

- description must be under 72 characters
- body should explain why, not just what
```

### TypeScript projects (when TypeScript is in the tech stack)

**`.cursor/rules/typescript.mdc`**:

```yaml
---
description: TypeScript coding standards
globs: "**/*.ts,**/*.tsx"
alwaysApply: false
---

# TypeScript Standards

- No any — use unknown + type guards
- async functions must have try/catch
- interface over type (except for union types)
- Exported functions must have JSDoc
- Use const enum for enumerations
```

### Python projects (when Python is in the tech stack)

**`.cursor/rules/python.mdc`**:

```yaml
---
description: Python coding standards
globs: "**/*.py"
alwaysApply: false
---

# Python Standards

- Full type annotations (function parameters and return values)
- Use dataclass or Pydantic instead of bare dicts
- Use async/await for async functions — avoid threading
- Be specific with exceptions — no bare Exception
- Avoid mutable default values for module-level variables
```

### When protected zones are declared

**`.cursor/rules/protected-zones.mdc`** (only when the user declared protected zones):

```yaml
---
description: Protected code zones — must not be modified under any circumstances
alwaysApply: true
---

# Protected Zones

The following paths / modules must NOT be modified without explicit authorization:

[fill in user's declared protected zones]

If modification is needed, get explicit confirmation from the user first.
```

---

## Step 4.5: Generate Multi-Editor Config Files

### GitHub Copilot (generate only if user selected Copilot)

**`.github/copilot-instructions.md`**:

```markdown
# GitHub Copilot Instructions

> This project has AI collaboration rules. Read before making suggestions.
> Full rules: see `AGENTS.md` in the project root.

---

## Project Context

[one-sentence description of the project]

**Tech stack**: [fill in]

---

## Do Not Touch

The following paths/modules must NOT be modified without explicit confirmation:

- `[protected path]`: [reason]

---

## Code Standards

- Use descriptive names — avoid tmp/data/obj/info
- No dead code, no debug console.log in production
- All async functions need try/catch
- New features must have tests

---

## After Every Task

Always update `MEMORY.md` in the same session.
**Updated MEMORY.md = task is done. Otherwise it is not done.**
```

### Claude Code (when user selected Claude Code)

Claude Code automatically reads `AGENTS.md` from the root — already covered.
Optional: configure allowed tools and command scope in `.claude/settings.json` (advanced scenarios).

---

## Step 5: Generate docs/anti-patterns.md

```markdown
# Anti-Pattern Records

Documents mistakes made in this project — wrong approaches and lessons learned.

**Add entries here whenever a mistake is made, to prevent repeating it.**

---

## Format

```markdown
### [Date] [Short Title]

**Situation**: What was happening when this occurred
**Wrong approach**: What was done
**Consequence**: What went wrong
**Correct approach**: What should be done instead
```

---

## Records

> No records yet. Add entries here when mistakes are made.
```

---

## Step 6 (Optional): Generate Prompt Eval Scaffold

**Only run this step if the user answered "yes" to AI-driven core features.**

Generate `eval/eval.py` (Python projects) or `eval/eval.js` (JS/TS projects):

**Python version**:

```python
"""
AI Output Quality Evaluation Script

Usage:
1. Add your test cases to test_cases
2. Run: python eval/eval.py
3. Check pass_rate

Run before changing a Prompt, then run again after — compare pass rates.
"""

test_cases = [
    {
        "name": "Example case",
        "input": "Example user input",
        "expected_traits": ["expected keyword or trait"],
        "forbidden_traits": ["content that should not appear"],
    },
    # Add more test cases here
]


def evaluate(ai_output: str, case: dict) -> dict:
    hits = [t for t in case["expected_traits"] if t in ai_output]
    violations = [t for t in case["forbidden_traits"] if t in ai_output]
    passed = len(violations) == 0 and len(hits) / len(case["expected_traits"]) >= 0.8
    return {
        "name": case["name"],
        "hit_rate": len(hits) / len(case["expected_traits"]),
        "violations": violations,
        "passed": passed,
    }


def run_eval(get_ai_output):
    """
    get_ai_output: callable(input: str) -> str
    Pass in your actual AI call function
    """
    results = []
    for case in test_cases:
        output = get_ai_output(case["input"])
        result = evaluate(output, case)
        results.append(result)
        status = "✅" if result["passed"] else "❌"
        print(f"{status} {result['name']} | hit_rate={result['hit_rate']:.0%} violations={result['violations']}")

    passed = sum(1 for r in results if r["passed"])
    print(f"\nPass rate: {passed}/{len(results)} = {passed/len(results):.0%}")
    return results


if __name__ == "__main__":
    # Replace with your actual AI call
    def mock_ai(input_text: str) -> str:
        return f"Mock response to '{input_text}'"

    run_eval(mock_ai)
```

**JS/TS version** (`eval/eval.js`):

```javascript
/**
 * AI Output Quality Evaluation Script
 * Run before changing a Prompt, then run again after — compare pass rates.
 */

const testCases = [
  {
    name: 'Example case',
    input: 'Example user input',
    expectedTraits: ['expected keyword'],
    forbiddenTraits: ['content that should not appear'],
  },
  // Add more test cases here
];

function evaluate(aiOutput, testCase) {
  const hits = testCase.expectedTraits.filter(t => aiOutput.includes(t));
  const violations = testCase.forbiddenTraits.filter(t => aiOutput.includes(t));
  const passed = violations.length === 0 && hits.length / testCase.expectedTraits.length >= 0.8;
  return { name: testCase.name, hitRate: hits.length / testCase.expectedTraits.length, violations, passed };
}

async function runEval(getAiOutput) {
  const results = [];
  for (const testCase of testCases) {
    const output = await getAiOutput(testCase.input);
    const result = evaluate(output, testCase);
    results.push(result);
    const status = result.passed ? '✅' : '❌';
    console.log(`${status} ${result.name} | hit_rate=${(result.hitRate * 100).toFixed(0)}%`);
  }
  const passed = results.filter(r => r.passed).length;
  console.log(`\nPass rate: ${passed}/${results.length} = ${(passed / results.length * 100).toFixed(0)}%`);
  return results;
}

// Replace with your actual AI call
const mockAi = async (input) => `Mock response to "${input}"`;
runEval(mockAi);
```

---

## Step 7: Summary Report

After generation, output the following to the user (adjust based on what was actually generated):

```
✅ AI documentation foundation initialized

Generated files:

📄 AGENTS.md                   ← AI onboarding file (protected zones + DoD + agentic guardrails)
📄 MEMORY.md                   ← Progress file — update after every session
📄 ROADMAP.md                  ← Phase plan + completion discipline
📁 docs/
   ├── ARCHITECTURE.md          ← Architecture skeleton (fill in as you build)
   ├── anti-patterns.md         ← Mistake log
   └── decisions/
       ├── README.md            ← ADR index
       └── [date]-tech-stack.md ← Initial tech stack decision
📁 .cursor/rules/
   ├── general.mdc              ← General standards (includes DoD discipline, always injected)
   ├── git-commits.mdc          ← Commit standards (always injected)
   └── [tech-stack].mdc         ← Tech stack specific standards
[📄 .github/copilot-instructions.md ← Copilot config (Copilot users only)]
[📁 eval/eval.py|js              ← AI output evaluation (AI features only)]

---

Next steps:
1. Open ROADMAP.md — fill in Phase 1 goals, deliverables, and DoD
2. Open AGENTS.md — confirm protected zones / MCP config / agentic guardrails are complete
3. Open docs/ARCHITECTURE.md — draw your system architecture diagram
4. Start building — AI will automatically read these files at the start of each new session
```

---

## Notes

- **Do not skip Step 0**: templates generated without user context have no real value
- **Protected zones must be explicit**: ask rather than guess what code shouldn't be touched
- **Generate tech stack rules on demand**: if the user didn't mention TypeScript, don't generate TypeScript rules
- **Copilot config on demand**: only generate `.github/copilot-instructions.md` if user selected Copilot
- **MCP section on demand**: if user said "none", delete the MCP section from AGENTS.md
- **Eval is optional**: don't force eval scaffolding onto projects with no AI features
- **ROADMAP Phase structure**: the template only has Phase 0 and Phase 1 — let the user define the rest

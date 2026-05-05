# GitHub Copilot Instructions

> This project has AI collaboration rules. Read before making suggestions.
> Full rules: see `AGENTS.md` in the project root.

---

## Project Context

[一句话描述项目做什么]

**Tech stack**: [填入技术栈]

---

## Do Not Touch

The following paths/modules must NOT be modified without explicit confirmation:

- `[受保护的路径]`: [原因]

---

## Code Standards

- Use descriptive names, avoid tmp/data/obj/info
- No dead code, no debug console.log in production
- All async functions need try/catch
- New features must have tests

---

## After Every Task

Always update `MEMORY.md` in the same session.
**Updated MEMORY.md = task is done. Otherwise it's not done.**

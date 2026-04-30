# ai-project-setup

> A Cursor Skill that initializes AI collaboration documentation infrastructure for any project.

一句话，为任意项目生成完整的 AI 协作文档基建——AGENTS.md、MEMORY.md、ADR 目录、Cursor Rules、踩坑记录。

---

## 解决什么问题

把 AI 引入真实项目时，最常见的失控场景：

- **AI 改了不该改的代码**——没有隔离区，AI 随手"优化"了稳定模块
- **AI 遗忘了上一个 session 的决策**——没有 MEMORY.md，每次新对话都是白板
- **AI 生成的代码不符合团队规范**——没有 Cursor Rules，靠口头提醒
- **架构决策没有记录**——没有 ADR，三个月后改方向时发现已深度耦合

这个 Skill 帮你在 5 分钟内把这些问题都解决掉。

---

## 安装

将 `SKILL.md` 放入你的 Cursor Skills 目录：

```bash
# 个人全局使用（推荐）
~/.cursor/skills/ai-project-setup/SKILL.md

# 项目内使用（团队共享）
.cursor/skills/ai-project-setup/SKILL.md
```

---

## 使用方法

在 Cursor 里直接说：

```
帮我初始化 AI 开发规范
```

或者：

```
setup AI project documentation
```

Skill 会先问你 4 个问题，再根据你的回答生成完整的文档骨架。

---

## 生成的文件结构

```
your-project/
├── AGENTS.md                    ← AI 入职文件（核心）
├── MEMORY.md                    ← 跨 session 进度记录
├── docs/
│   ├── decisions/
│   │   ├── README.md            ← ADR 索引
│   │   └── YYYY-MM-DD-tech-stack.md  ← 初始技术栈决策
│   └── anti-patterns.md         ← 踩坑记录
├── .cursor/
│   └── rules/
│       ├── general.mdc          ← 通用规范（自动注入）
│       ├── git-commits.mdc      ← Commit 规范（自动注入）
│       └── [typescript|python].mdc   ← 技术栈规范（按需生成）
└── eval/
    └── eval.py | eval.js        ← AI 输出评测（仅有 AI 功能时生成）
```

---

## 核心概念

### AGENTS.md — AI 入职文件

每次开新对话，AI 读这个文件对齐上下文。包含：
- 项目概述和技术栈
- 隔离区（哪些代码不能动）
- Critical Rules（不可违反的红线）
- 代码规范
- "Where to Look" 索引表

### MEMORY.md — 跨 Session 记忆

AI 最大的工程问题是没有持久记忆。MEMORY.md 是人工维护的"进度条"——每次开发后更新，下次开新对话时 AI 读一遍就能恢复上下文。

**铁律：未更新 MEMORY.md = 本次开发未关门。**

### docs/decisions/ — 架构决策记录（ADR）

每个重要决策写一个日期命名的 Markdown 文件，记录 Context → Decision → Alternatives → Consequences。AI 读 `docs/decisions/` newest-first，不会在同样问题上绕第二遍。

### .cursor/rules/ — 自动注入的代码规范

Rules 文件在每次对话时自动注入，不需要 AI 主动读。根据技术栈生成对应规范（TypeScript strict、Python 类型注解、Git commit 格式等）。

---

## 适用场景

| 场景 | 效果 |
|------|------|
| 新项目启动 | 5 分钟内建好 AI 协作基建，开箱即用 |
| 老项目补规范 | 补全缺失的 AGENTS.md 和 MEMORY.md |
| 团队共享 | 规范放进 .cursor/skills/，所有人统一初始化流程 |
| 个人开源项目 | 让贡献者（人或 AI）快速上手项目 |

---

## 和 ai-memory 的关系

[ai-memory](https://github.com/hyxnj666-creator/ai-memory) 是**提取**——从 AI 对话历史里自动提取知识，写入 AGENTS.md。

这个 Skill 是**主动建设**——在项目初始化时手动搭建文档骨架，告诉 AI 这个项目的规则是什么。

两者互补：用这个 Skill 建好骨架，再用 ai-memory 持续从对话中提取新知识填充进去。

---

## 背景

这个 Skill 提炼自两个真实项目的实战经验：

- **conor-site**：Next.js + AI Persona 引擎，用 MEMORY.md + Feature Gate 管理迭代
- **ai-memory**：开源 CLI 工具，用 ADR + Spike-First 纪律管理架构决策

详细说明见文章：[AI 开发规范：让 AI 在真实项目里稳定工作的工程体系](#)

---

## License

MIT

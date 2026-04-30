# 架构决策记录（ADR）

记录项目中每一个重要的技术 / 架构 / 产品决策，保留决策时的完整上下文。

**AI 助手读这里时，从最新的文件开始读（文件名日期倒序）。**

---

## 为什么要写 ADR

- 下一个 session 的 AI 不会记得你上次做了什么决策
- 三个月后你自己也不记得为什么选了这个方案
- 新成员（人或 AI）接手时需要知道"为什么"，不只是"是什么"

---

## 文件命名格式

```
YYYY-MM-DD-决策主题.md
```

例如：
- `2026-01-15-tech-stack.md`
- `2026-02-03-switch-from-rest-to-graphql.md`
- `2026-03-10-add-redis-caching.md`

---

## 每个 ADR 的结构

```markdown
# ADR YYYY-MM-DD — [决策标题]

**Status**：Accepted | Superseded by [新 ADR 链接]

## Context
为什么要做这个决策，当时面对什么问题

## Decision
决定做什么

## Alternatives（考虑过的其他方案）
- 方案 A：为什么没选
- 方案 B：为什么没选

## Consequences
- 这个决策带来的好处
- 这个决策带来的约束或代价
```

---

## 决策索引

| 日期 | 文件 | 简述 |
|------|------|------|
| [YYYY-MM-DD] | [YYYY-MM-DD]-tech-stack.md | 初始技术栈选型 |

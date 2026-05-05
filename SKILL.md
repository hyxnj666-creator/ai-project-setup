---
name: ai-project-setup
description: >-
  Initialize AI collaboration documentation infrastructure for any project.
  Use when starting a new project, setting up AI development rules from scratch,
  or when asked to create AGENTS.md, MEMORY.md, ROADMAP.md, ADR folders,
  Cursor Rules, or any AI-readable project documentation baseline.
---

# AI Project Setup

把任意项目初始化为"AI 可以稳定协作"的状态——生成 AGENTS.md、MEMORY.md、ROADMAP.md、ADR 目录、Cursor Rules、ARCHITECTURE 骨架等完整文档基建。

---

## Step 0：开工前收集信息

**不要直接开始生成文件。先向用户提问，收集以下信息：**

### 必问（6 个问题，一次性列出，等用户回答）

```
在开始生成之前，我需要了解你的项目：

1. **项目类型**（选一个最接近的）
   - 前端应用（Next.js / Vue / React）
   - 后端服务（Node.js / Python / Go）
   - CLI 工具 / 开源库
   - 全栈一体（Monorepo）
   - 其他：___

2. **主要技术栈**
   例如：TypeScript + Next.js 14 + Prisma + PostgreSQL

3. **有没有需要保护的稳定代码？**
   例如：v1 已上线不能动、某个核心模块不让 AI 改、生产数据库不直接操作
   没有的话直接说"没有"

4. **项目里有没有 AI 驱动的核心功能？**
   例如：调用 LLM API、RAG 检索、AI 生成内容
   （有的话会额外生成 Prompt eval 模板）

5. **使用哪些 AI 编辑器 / Agent？**（可多选）
   - Cursor
   - Claude Code
   - GitHub Copilot
   - Codex CLI
   - 其他：___
   （影响是否生成对应配置文件）

6. **项目里会用到 MCP（Model Context Protocol）工具吗？**
   例如：文件系统 MCP、数据库 MCP、ai-memory MCP
   没有的话直接说"没有"
```

收到回答后，进入 Step 1。

---

## Step 1：生成 AGENTS.md

在项目根目录生成 `AGENTS.md`，使用以下模板，将用户提供的信息填入 `[占位符]` 部分：

```markdown
# [项目名] — AI 开发规则

> 本文件适用于所有 AI 编码助手（Cursor、Claude Code、GitHub Copilot、Codex CLI、其他 Agent）。
> 开始任何开发工作前，请按顺序阅读本文件。

---

## 1. 强制阅读顺序

开始写代码前，按顺序读完以下文件：

```
1. ROADMAP.md        ← 当前在哪个阶段，Phase 目标（WHAT）
2. MEMORY.md         ← 上次做到哪，已知地雷（WHERE WE LEFT OFF）
3. docs/decisions/   ← 关键决策记录，newest-first（WHY）
```

**读不懂就停下来问，不要边读边改代码。**

---

## 2. 项目概述

[一句话描述项目做什么]

**技术栈**：[用户填入的技术栈]

**目标用户**：[项目面向谁]

---

## 3. 🔒 隔离区（不可触碰）

[如果用户有保护区域，填入；否则删除此节或写"暂无特殊限制"]

以下代码 / 路径 / 资源，**未经明确授权不得修改**：

- `[受保护的路径或模块]`：[原因，例如 v1 已上线，改动影响生产]

如需修改以上内容，必须先得到明确确认再动手。

---

## 4. Critical Rules（不可违反）

1. **所有新功能必须有对应测试**——不写测试的代码不算完成
2. **破坏性变更需要明确授权**——不要"顺便"重构稳定模块
3. **依赖要最小化**——新增依赖前确认是否有内置替代方案
4. **文档要同步**——代码改了，MEMORY.md 必须在同一轮里更新
5. **禁止在生产路径执行写操作**——未经确认不得修改生产数据库 / 生产 API

---

## 5. Agentic 执行护栏

> 本节针对自主 agentic 任务（AI 独立读写文件、执行命令、调用 API）的额外约束。

**Shell 命令**：
- ✅ 可自主执行：`git status / diff / log`、`npm run test / build / lint`、只读查询
- ⚠️ 执行前须告知：`git commit / push`、`npm publish`、`docker`
- 🚫 绝对禁止：`rm -rf`、`DROP TABLE`、向生产 API 发写操作、修改 `.env` / 密钥文件

**文件系统**：
- 不得读写 `.env`、`*.secret`、`*.key`、`credentials.*`
- 不得修改隔离区（见第 3 节）内的任何文件
- 生成新文件时，已存在的文件覆盖前必须先确认

---

## 6. 完工的 Definition of Done（文档同步纪律）

**每完成一项工作，同一轮里必须对照以下清单：**

| # | 文档 | 何时必更 |
|---|------|---------|
| 1 | `MEMORY.md` | **永远**——更新当前状态 + 下一步 + 已完成 |
| 2 | `ROADMAP.md` | 涉及 Phase 进度时——打勾对应子项 |
| 3 | 相关 ADR | 决策有调整时——追加修订历史（不改原文） |
| 4 | `docs/anti-patterns.md` | 踩到坑时——记录反模式 + 正确做法 |

**未跑清单 = 本次工作未关门。不允许进入下一项 / commit / 告诉用户"做完了"。**

---

## 7. 代码规范

### 通用
- 变量和函数用自描述命名，不用 tmp/data/obj 等无意义词
- 每个函数做一件事，超过 50 行考虑拆分
- 错误必须处理，不允许空 catch
- 不留死代码（注释掉的旧代码直接删）

### [技术栈专项规范]

[根据技术栈填入，例如：]

**TypeScript**：
- 禁止 `any`，用 `unknown` + 类型守卫
- async 函数必须有 try/catch
- 导出的函数必须有 JSDoc

**Python**：
- 类型注解全覆盖（函数参数和返回值）
- 用 dataclass / Pydantic 替代裸 dict
- 异常要具体，不用裸 Exception

---

## 8. 架构模式

**业务逻辑 / IO 分离**：
- 业务逻辑写成纯函数（无副作用，易测试）
- 文件读写、网络请求、数据库操作放在外层薄包装

**错误处理原则**：
- 对外 API 失败时返回空值 / 默认值，而不是直接抛出
- 调用方决定是否把"失败"当作错误

---

## 9. MCP 配置

[仅在用户回答使用 MCP 时填入；否则删除此节]

**允许使用的 MCP**：
- `[mcp-name]`：[用途，例如 filesystem - 读写本地文件]

**禁止在生产环境使用的 MCP**：
- `[mcp-name]`：[原因]

---

## 10. 常见任务清单

### 添加新功能
1. 确认需求，在 MEMORY.md 里记录计划
2. （复杂功能）先写 spike doc 再写代码
3. 实现功能，遵守 Critical Rules 和 Agentic 护栏
4. 写测试
5. 跑 DoD 清单（§6）

### 修复 Bug
1. 复现问题，确认根因
2. 修复 + 加回归测试
3. 跑 DoD 清单（§6）

### 关键决策
1. 写 ADR 到 `docs/decisions/YYYY-MM-DD-主题.md`
2. 在 `docs/decisions/README.md` 的索引表里登记

---

## 11. Where to Look（按问题找文档）

| 问题 | 去哪里看 |
|------|---------|
| 现在在做什么 / 进度 | `MEMORY.md` |
| 这个 Phase 的目标 / DoD | `ROADMAP.md` |
| 为什么做这个决策 | `docs/decisions/` newest-first |
| 踩过什么坑 | `docs/anti-patterns.md` |
| 系统架构是什么 | `docs/ARCHITECTURE.md` |
| 怎么发版 / 部署 | `docs/DEPLOY.md`（如有） |
```

---

## Step 1.5：生成 ROADMAP.md

在项目根目录生成 `ROADMAP.md`：

```markdown
# [项目名] Roadmap

> **WHAT 层**：每个 Phase 的目标、交付物、Definition of Done。
> WHY 看 `docs/decisions/`。
> 进度看 `MEMORY.md`。
>
> **原则：每个 Phase 有硬性 DoD，不满足不得进下一 Phase。**

---

## 🔴 开发节奏纪律（每次完工必跑）

每完成一项工作，同一轮里必须完成以下相关项：

| # | 文档 | 何时必更 | 更新内容 |
|---|------|---------|---------|
| 1 | `MEMORY.md` | **永远** | 当前状态 + 下一步勾选 + 已完成纪要 |
| 2 | `ROADMAP.md` | 涉及 Phase 进度时 | 当前状态表 + 对应 Phase 子项打勾 |
| 3 | 相关 ADR | 决策有调整时 | 追加修订历史（不改原文） |
| 4 | `docs/anti-patterns.md` | 踩到坑时 | 反模式 + 正确做法 |

**未跑清单 = 本次工作未关门。**

---

## 当前状态

| 项 | 值 |
|---|---|
| 当前 Phase | **Phase 0 · 文档基建** |
| 下一 Phase | Phase 1 · [填入下一阶段名称] |
| 上线版本 | 未上线 |
| 最后更新 | [今天日期] |

---

## Phase 总览

| Phase | 名称 | 状态 | 时长（预估） | 前置 |
|-------|------|------|-----------|------|
| **0** | 文档基建 | ✅ 完成 | 0.5 天 | — |
| **1** | [第一个阶段名称] | ⏸ 待启动 | [预估] | Phase 0 关门 |
| **2** | [第二个阶段名称] | ⏸ 待启动 | [预估] | Phase 1 关门 |

---

## Phase 0 · 文档基建

**目标**：建立 AI 协作文档骨架，让任何 AI 助手进入项目都能快速对齐。

**交付物**：
- [x] AGENTS.md
- [x] MEMORY.md
- [x] ROADMAP.md
- [x] docs/decisions/ 目录 + 初始 ADR
- [x] docs/ARCHITECTURE.md 骨架
- [x] .cursor/rules/ 规范文件

**Definition of Done**：
- [ ] AGENTS.md 有隔离区 + Critical Rules + DoD 清单
- [ ] MEMORY.md 有当前状态 + 下一步
- [ ] docs/decisions/ 有技术栈选型 ADR

---

## Phase 1 · [下一阶段名称]

**目标**：[填入这个阶段要完成什么]

**交付物**：
- [ ] [交付物 1]
- [ ] [交付物 2]

**Definition of Done**：
- [ ] [验收标准 1]
- [ ] [验收标准 2]

---

## 决策日志

| 日期 | 决策 | 详见 |
|------|------|------|
| [今天日期] | 初始化项目文档基建 | — |
```

---

## Step 2：生成 MEMORY.md

在项目根目录生成 `MEMORY.md`：

```markdown
# 开发进度

> 每次开发后必须更新本文件。**未更新 = 本次工作未关门。**
> AI 助手开始新 session 时必须先读这个文件。

---

## 当前状态

**日期**：[今天日期]
**阶段**：Phase 0 · 文档基建（已完成）

**正在做**：等待用户启动 Phase 1

**下一步**：
- [ ] 在 ROADMAP.md 里补全 Phase 1 的交付物和 DoD
- [ ] 开始 Phase 1 的第一个任务

---

## 已完成

- [今天日期] 初始化 AI 文档基建（AGENTS.md、MEMORY.md、ROADMAP.md、ADR 目录、ARCHITECTURE 骨架）

---

## 注意事项 / 已知地雷

> AI 助手开始新 session 时必读这部分

[目前没有已知问题。踩到坑时在这里记录，格式：日期 + 问题描述 + 解决方案]
```

---

## Step 3：生成 docs/decisions/ 目录

创建 `docs/decisions/` 目录，并生成两个文件：

### docs/decisions/README.md

```markdown
# 架构决策记录（ADR）

记录项目中每一个重要的技术 / 架构 / 产品决策。

**AI 助手读这里时，从最新的文件开始读（文件名日期倒序）。**

---

## 文件命名格式

```
YYYY-MM-DD-决策主题.md
```

## 每个 ADR 的结构

```markdown
# ADR YYYY-MM-DD — [决策标题]

**Status**：Accepted | Superseded by [新 ADR]

## Context
为什么要做这个决策

## Decision
决定做什么

## Alternatives
- 方案 A：为什么没选
- 方案 B：为什么没选

## Consequences
- 好处
- 代价 / 约束
```

---

## 决策索引

| 日期 | 文件 | 简述 |
|------|------|------|
| [今天日期] | [今天日期]-tech-stack.md | 初始技术栈选型 |
```

### docs/decisions/[今天日期]-tech-stack.md

```markdown
# ADR [今天日期] — 技术栈选型

**Status**：Accepted

## Context

项目初始化，需要确定主要技术栈。

## Decision

使用 [用户填写的技术栈]。

## Alternatives

[如果用户提到了备选方案，填入；否则写"初始化时未做详细对比，后续重大变更需补充 ADR"]

## Consequences

- 技术栈确定后，核心框架变更需要新的 ADR
- [其他影响]
```

---

## Step 3.5：生成 docs/ARCHITECTURE.md 骨架

生成 `docs/ARCHITECTURE.md`，章节标题根据项目类型调整：

```markdown
# 系统架构

> 本文描述 [项目名] 的整体架构、模块划分、数据流和关键设计决策。
> 详细的决策理由见 `docs/decisions/`。

---

## 高层架构

[用 ASCII 图或 Mermaid 描述系统整体结构]

```
[占位：在这里画架构图]
例如：
Client → API Layer → Service Layer → Database
```

---

## 模块说明

| 模块 | 路径 | 职责 |
|------|------|------|
| [模块名] | `[路径]` | [一句话描述] |

---

## 数据流

[描述核心业务流程的数据流向]

### [主要流程名称]

```
步骤 1 → 步骤 2 → 步骤 3
```

---

## 关键设计决策

| 决策 | 选择 | 详见 |
|------|------|------|
| 技术栈 | [填入] | `docs/decisions/[日期]-tech-stack.md` |

---

## 外部依赖

| 依赖 | 用途 | 版本约束 |
|------|------|---------|
| [填入] | [填入] | [填入] |

---

## 性能 / 安全边界

[填入关键的性能约束和安全边界，例如：]
- API 响应时间目标：< 200ms p95
- 敏感数据不得写入日志
```

---

## Step 4：生成 .cursor/rules/ 文件

根据用户填写的技术栈，生成对应的 `.cursor/rules/` 规则文件。

### 通用规则（所有项目都生成）

**`.cursor/rules/general.mdc`**：

```yaml
---
description: 通用开发规范，适用所有文件
alwaysApply: true
---

# 通用规范

- 命名用自描述词，不用 tmp/data/obj/info 等无意义词
- 不留死代码（注释掉的旧代码）
- 不要 console.log 留在生产代码里
- 错误处理不能是空 catch
- 新功能必须有测试，不写测试的代码不算完成

# 完工纪律

每次完成任何工作后，必须在同一轮里更新 MEMORY.md。
涉及 Phase 进度时，同时更新 ROADMAP.md。
未更新文档 = 本次工作未关门。
```

**`.cursor/rules/git-commits.mdc`**：

```yaml
---
description: Git commit 规范
alwaysApply: true
---

# Commit Message 格式

使用 Conventional Commits 格式：

type(scope): description

type 可选值：
- feat：新功能
- fix：修复 bug
- refactor：重构（不改行为）
- test：测试相关
- docs：文档
- chore：工具、依赖、配置

- description 不超过 72 字符
- body 解释 why，不只是 what
```

### TypeScript 项目（技术栈含 TypeScript 时额外生成）

**`.cursor/rules/typescript.mdc`**：

```yaml
---
description: TypeScript 编码规范
globs: "**/*.ts,**/*.tsx"
alwaysApply: false
---

# TypeScript 规范

- 禁止 any，用 unknown + 类型守卫
- async 函数必须有 try/catch
- interface 优于 type（除 union 类型）
- 导出的函数必须有 JSDoc
- 枚举值用 const enum
```

### Python 项目（技术栈含 Python 时额外生成）

**`.cursor/rules/python.mdc`**：

```yaml
---
description: Python 编码规范
globs: "**/*.py"
alwaysApply: false
---

# Python 规范

- 类型注解全覆盖（函数参数和返回值）
- 用 dataclass 或 Pydantic 替代裸 dict
- 异步函数用 async/await，不用 threading
- 异常要具体，不用裸 Exception
- 模块级变量避免可变默认值
```

### 有隔离区时额外生成

**`.cursor/rules/protected-zones.mdc`**（仅在用户声明了隔离区时生成）：

```yaml
---
description: 受保护的代码区域，任何情况下不得修改
alwaysApply: true
---

# 受保护区域

以下路径 / 模块未经明确授权不得修改：

[将用户声明的隔离区填入]

如需修改，必须先得到用户的明确确认。
```

---

## Step 4.5：生成多编辑器配置文件

### GitHub Copilot（用户选择了 Copilot 时生成）

**`.github/copilot-instructions.md`**：

```markdown
# GitHub Copilot Instructions

> This project has AI collaboration rules. Read before suggesting code.

## Project Context

[复制 AGENTS.md §2 项目概述内容]

## Do Not Touch

[复制 AGENTS.md §3 隔离区内容]

## Code Standards

[复制 AGENTS.md §7 代码规范核心内容]

## After Every Task

Always update MEMORY.md in the same session. Updated MEMORY = task is done.
```

### Claude Code（用户选择了 Claude Code 时的说明）

Claude Code 会自动读根目录的 `AGENTS.md`，已覆盖。无需额外生成文件。
可选：在 `.claude/settings.json` 里配置允许的工具和命令范围（高级场景）。

---

## Step 5：生成 docs/anti-patterns.md

```markdown
# 反模式记录

记录项目里踩过的坑、错误的做法、走过的弯路。

**每次踩坑后在这里补充，防止 AI 和团队重蹈覆辙。**

---

## 格式

```markdown
### [日期] [简短标题]

**场景**：什么情况下遇到的
**错误做法**：做了什么
**后果**：导致什么问题
**正确做法**：应该怎么做
```

---

## 记录

> 暂无记录。踩到坑时在这里补充。
```

---

## Step 6（可选）：生成 Prompt Eval 骨架

**仅在用户回答"有 AI 驱动的核心功能"时执行此步骤。**

生成 `eval/eval.py`（Python 项目）或 `eval/eval.js`（JS/TS 项目）：

**Python 版本**：

```python
"""
AI 输出质量评测脚本

使用方法：
1. 在 test_cases 里添加你的测试用例
2. 运行 python eval/eval.py
3. 看通过率 pass_rate

改 Prompt 之前先跑一遍，改完之后再跑一遍，对比通过率。
"""

test_cases = [
    {
        "name": "示例用例",
        "input": "用户输入示例",
        "expected_traits": ["期望出现的关键词或特征"],
        "forbidden_traits": ["不应该出现的内容"],
    },
    # 在这里添加更多测试用例
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
    传入你的 AI 调用函数
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
    # 替换为你的实际 AI 调用
    def mock_ai(input_text: str) -> str:
        return f"这是对'{input_text}'的模拟回复"

    run_eval(mock_ai)
```

**JS/TS 版本**（`eval/eval.js`）：

```javascript
/**
 * AI 输出质量评测脚本
 * 改 Prompt 之前先跑，改完之后再跑，对比通过率
 */

const testCases = [
  {
    name: '示例用例',
    input: '用户输入示例',
    expectedTraits: ['期望出现的关键词'],
    forbiddenTraits: ['不应该出现的内容'],
  },
  // 在这里添加更多测试用例
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

// 替换为你的实际 AI 调用
const mockAi = async (input) => `这是对"${input}"的模拟回复`;
runEval(mockAi);
```

---

## Step 7：收尾汇报

生成完成后，向用户输出以下汇报（根据实际生成的文件调整）：

```
✅ AI 文档基建初始化完成

生成了以下文件：

📄 AGENTS.md                   ← AI 入职文件（隔离区 + DoD + Agentic 护栏）
📄 MEMORY.md                   ← 进度文件，每次开发后更新
📄 ROADMAP.md                  ← Phase 规划 + 完工纪律
📁 docs/
   ├── ARCHITECTURE.md          ← 架构骨架（待填充）
   ├── anti-patterns.md         ← 踩坑记录
   └── decisions/
       ├── README.md            ← ADR 索引
       └── [日期]-tech-stack.md ← 初始技术栈决策
📁 .cursor/rules/
   ├── general.mdc              ← 通用规范（含完工纪律，自动注入）
   ├── git-commits.mdc          ← Commit 规范（自动注入）
   └── [技术栈].mdc             ← 技术栈专项规范
[📄 .github/copilot-instructions.md ← Copilot 配置（仅 Copilot 用户）]
[📁 eval/eval.py|js              ← AI 输出评测（仅有 AI 功能时）]

---

下一步建议：
1. 打开 ROADMAP.md，补全 Phase 1 的目标、交付物和 DoD
2. 打开 AGENTS.md，确认隔离区 / MCP 配置 / Agentic 护栏是否完整
3. 打开 docs/ARCHITECTURE.md，画出系统架构图
4. 开始开发——AI 每次开新 session 会自动读这些文件
```

---

## 注意事项

- **不要跳过 Step 0**：没有用户信息就生成的模板毫无针对性
- **隔离区必须明确**：宁可问清楚，不要猜测哪些代码不能动
- **技术栈规则按需生成**：用户没提到 TypeScript 就不生成 TypeScript rules
- **Copilot 配置按需生成**：用户没选 Copilot 就不生成 `.github/copilot-instructions.md`
- **MCP 节按需填入**：用户说"没有"就删掉 AGENTS.md 的 MCP 配置节
- **Eval 是可选的**：没有 AI 功能的项目不要强加 eval 骨架
- **ROADMAP Phase 结构**：模板里只给 Phase 0 和 Phase 1 骨架，其余 Phase 让用户自己填

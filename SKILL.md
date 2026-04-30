---
name: ai-project-setup
description: >-
  Initialize AI collaboration documentation infrastructure for any project.
  Use when starting a new project, setting up AI development rules from scratch,
  or when asked to create AGENTS.md, MEMORY.md, ADR folders, Cursor Rules,
  or any AI-readable project documentation baseline.
---

# AI Project Setup

把任意项目初始化为"AI 可以稳定协作"的状态——生成 AGENTS.md、MEMORY.md、ADR 目录、Cursor Rules 等文档基建骨架。

---

## Step 0：开工前收集信息

**不要直接开始生成文件。先向用户提问，收集以下信息：**

### 必问（4 个问题，一次性列出，等用户回答）

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
```

收到回答后，进入 Step 1。

---

## Step 1：生成 AGENTS.md

在项目根目录生成 `AGENTS.md`，使用以下模板，将用户提供的信息填入 `[占位符]` 部分：

```markdown
# [项目名] — AI 开发规则

> 本文件适用于所有 AI 编码助手（Cursor、Claude Code、GitHub Copilot、其他 Agent）。
> 开始任何开发工作前，请按顺序阅读本文件。

---

## 强制阅读顺序

开始写代码前，按顺序读完以下文件：

```
1. ROADMAP.md        ← 当前在哪个阶段（WHAT）
2. MEMORY.md         ← 上次做到哪（WHERE WE LEFT OFF）
3. docs/decisions/   ← 关键决策记录（WHY）
```

**读不懂就停下来问，不要边读边改代码。**

---

## 项目概述

[一句话描述项目做什么]

**技术栈**：[用户填入的技术栈]

**目标用户**：[项目面向谁]

---

## 🔒 隔离区（不可触碰）

[如果用户有保护区域，填入；否则删除此节或写"暂无特殊限制"]

以下代码 / 路径 / 资源，**未经明确授权不得修改**：

- `[受保护的路径或模块]`：[原因]

如需修改以上内容，必须先得到明确确认。

---

## Critical Rules（不可违反）

1. **所有新功能必须有对应测试**——不写测试的代码不算完成
2. **破坏性变更需要明确授权**——不要"顺便"重构稳定模块
3. **依赖要最小化**——新增依赖前确认是否有内置替代
4. **文档要同步**——代码改了，MEMORY.md 必须同步更新

---

## 代码规范

[根据技术栈填入，以下为示例]

### 通用规范
- 变量和函数用自描述命名，不要缩写
- 每个函数做一件事，超过 50 行考虑拆分
- 错误必须处理，不允许空 catch

### [技术栈特定规范]
[根据用户填写的技术栈，选择填入对应规范]

---

## 架构模式

[根据项目类型填入，以下为通用起点]

**业务逻辑 / IO 分离**：
- 业务逻辑写成纯函数（无副作用，易测试）
- 文件读写、网络请求、数据库操作放在外层薄包装

**错误处理原则**：
- 对外 API 失败时返回空值 / 默认值，而不是直接抛出
- 调用方决定是否把"失败"当作错误

---

## 常见任务清单

[根据项目类型填入对应任务步骤，以下为示例]

### 添加新功能
1. 确认需求，在 MEMORY.md 里记录计划
2. （复杂功能）先写 spike doc 再写代码
3. 实现功能，遵守 Critical Rules
4. 写测试
5. 更新 MEMORY.md

### 修复 Bug
1. 复现问题，确认根因
2. 修复 + 加回归测试
3. 更新 MEMORY.md（如有新的踩坑点，更新 docs/anti-patterns.md）

---

## Where to Look（按问题找文档）

| 问题 | 去哪里看 |
|------|---------|
| 现在在做什么 / 进度 | `MEMORY.md` |
| 为什么做这个决策 | `docs/decisions/` |
| 踩过什么坑 | `docs/anti-patterns.md` |
| 架构是什么 | `docs/ARCHITECTURE.md`（如有） |
| 怎么发版 / 部署 | `docs/DEPLOY.md`（如有） |
```

---

## Step 2：生成 MEMORY.md

在项目根目录生成 `MEMORY.md`：

```markdown
# 开发进度

> 每次开发后必须更新本文件。未更新 = 本次开发未关门。

---

## 当前状态

**日期**：[今天日期]
**阶段**：项目初始化

[现在在做什么，卡在哪，下一步打算怎么走]

---

## 已完成

- [日期] 初始化 AI 文档基建（AGENTS.md、MEMORY.md、ADR 目录）

---

## 下一步

- [ ] [填入第一个实际任务]

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

## 格式

文件命名：`YYYY-MM-DD-决策主题.md`

每个 ADR 包含：
- **Context**：为什么要做这个决策
- **Decision**：决定做什么
- **Alternatives**：考虑过哪些方案，为什么没选
- **Consequences**：这个决策带来的影响

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
- 团队成员需要熟悉上述技术栈
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

## Step 5：生成 docs/anti-patterns.md

```markdown
# 反模式记录

记录项目里踩过的坑、错误的做法、走过的弯路。

**每次踩坑后在这里补充，防止重蹈覆辙。**

---

## 格式

```
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

生成完成后，向用户输出以下汇报：

```
✅ AI 文档基建初始化完成

生成了以下文件：

📄 AGENTS.md              ← AI 入职文件，开始每次开发前读这个
📄 MEMORY.md              ← 进度文件，每次开发后更新
📁 docs/decisions/
   ├── README.md           ← ADR 索引
   └── [日期]-tech-stack.md ← 初始技术栈决策
📁 .cursor/rules/
   ├── general.mdc         ← 通用规范（自动注入）
   ├── git-commits.mdc     ← Commit 规范（自动注入）
   └── [技术栈].mdc        ← 技术栈专项规范
📄 docs/anti-patterns.md  ← 踩坑记录（用到时再填）
[📁 eval/eval.py|js        ← AI 输出评测（仅有 AI 功能时生成）]

---

下一步建议：
1. 打开 AGENTS.md，确认隔离区和 Critical Rules 是否完整
2. 在 MEMORY.md 里写下当前要做的第一个任务
3. 开始开发——AI 每次开新 session 会自动读这些文件
```

---

## 注意事项

- **不要跳过 Step 0**：没有用户信息就生成的模板毫无针对性
- **隔离区必须明确**：宁可问清楚，不要猜测哪些代码不能动
- **技术栈规则按需生成**：用户没提到 TypeScript 就不生成 TypeScript rules，保持最小化
- **Eval 是可选的**：没有 AI 功能的项目不要强加 eval 骨架

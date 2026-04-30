"""
AI 输出质量评测脚本

用途：在改 Prompt / 换模型 / 调参数之前和之后分别跑一遍，
      对比通过率，确保改动没有让输出质量退步。

使用方法：
1. 在 TEST_CASES 里添加你的测试用例
2. 在 main() 里替换为你的实际 AI 调用函数
3. 运行：python eval/eval.py
"""

from typing import Callable

# ─── 测试用例 ────────────────────────────────────────────────────────────────

TEST_CASES = [
    {
        "name": "示例用例 - 修改这里",
        "input": "用户输入的内容",
        "expected_traits": [
            # AI 输出里必须包含的关键词或特征（命中 80% 以上才算通过）
            "期望关键词1",
            "期望关键词2",
        ],
        "forbidden_traits": [
            # AI 输出里绝对不能出现的内容（出现一个就失败）
            "不应出现的词",
        ],
    },
    # 继续添加更多用例...
    # {
    #     "name": "边界用例 - 空输入",
    #     "input": "",
    #     "expected_traits": ["请提供"],
    #     "forbidden_traits": [],
    # },
]


# ─── 评测逻辑（一般不需要改这里）───────────────────────────────────────────

def evaluate(ai_output: str, case: dict) -> dict:
    hits = [t for t in case["expected_traits"] if t in ai_output]
    violations = [t for t in case["forbidden_traits"] if t in ai_output]
    hit_rate = len(hits) / len(case["expected_traits"]) if case["expected_traits"] else 1.0
    passed = len(violations) == 0 and hit_rate >= 0.8
    return {
        "name": case["name"],
        "hit_rate": hit_rate,
        "hits": hits,
        "violations": violations,
        "passed": passed,
        "output_preview": ai_output[:100] + "..." if len(ai_output) > 100 else ai_output,
    }


def run_eval(get_ai_output: Callable[[str], str], verbose: bool = True) -> dict:
    """
    运行评测

    Args:
        get_ai_output: 接收 input 字符串，返回 AI 输出字符串的函数
        verbose: 是否打印每个用例的详细结果

    Returns:
        {"pass_rate": float, "results": list, "passed": int, "total": int}
    """
    results = []

    for case in TEST_CASES:
        output = get_ai_output(case["input"])
        result = evaluate(output, case)
        results.append(result)

        if verbose:
            status = "✅" if result["passed"] else "❌"
            print(f"{status} {result['name']}")
            print(f"   hit_rate: {result['hit_rate']:.0%}  |  hits: {result['hits']}")
            if result["violations"]:
                print(f"   ⚠️  violations: {result['violations']}")
            if not result["passed"]:
                print(f"   output: {result['output_preview']}")
            print()

    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    pass_rate = passed / total if total > 0 else 0.0

    print(f"{'─' * 40}")
    print(f"Pass rate: {passed}/{total} = {pass_rate:.0%}")
    if pass_rate < 0.8:
        print("⚠️  通过率低于 80%，建议检查 Prompt 或测试用例")

    return {"pass_rate": pass_rate, "results": results, "passed": passed, "total": total}


# ─── 入口（替换这里的 AI 调用）──────────────────────────────────────────────

def main():
    # TODO: 替换为你的实际 AI 调用
    # 示例（OpenAI）：
    #
    # from openai import OpenAI
    # import os
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    #
    # def get_ai_output(input_text: str) -> str:
    #     response = client.chat.completions.create(
    #         model="gpt-4o-mini",
    #         messages=[
    #             {"role": "system", "content": YOUR_SYSTEM_PROMPT},
    #             {"role": "user", "content": input_text},
    #         ],
    #     )
    #     return response.choices[0].message.content

    # 临时 mock（先跑通流程，再替换为真实调用）
    def get_ai_output(input_text: str) -> str:
        return f"这是对'{input_text}'的模拟回复，包含期望关键词1和期望关键词2"

    run_eval(get_ai_output)


if __name__ == "__main__":
    main()

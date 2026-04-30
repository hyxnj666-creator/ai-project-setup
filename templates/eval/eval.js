/**
 * AI 输出质量评测脚本
 *
 * 用途：改 Prompt / 换模型 / 调参数之前和之后分别跑一遍，
 *       对比通过率，确保改动没有让输出质量退步。
 *
 * 使用方法：
 * 1. 在 TEST_CASES 里添加你的测试用例
 * 2. 在 main() 里替换为你的实际 AI 调用函数
 * 3. 运行：node eval/eval.js
 */

// ─── 测试用例 ────────────────────────────────────────────────────────────────

const TEST_CASES = [
  {
    name: '示例用例 - 修改这里',
    input: '用户输入的内容',
    expectedTraits: [
      // AI 输出里必须包含的关键词（命中 80% 以上才算通过）
      '期望关键词1',
      '期望关键词2',
    ],
    forbiddenTraits: [
      // AI 输出里绝对不能出现的内容（出现一个就失败）
      '不应出现的词',
    ],
  },
  // 继续添加更多用例...
  // {
  //   name: '边界用例 - 空输入',
  //   input: '',
  //   expectedTraits: ['请提供'],
  //   forbiddenTraits: [],
  // },
];


// ─── 评测逻辑（一般不需要改这里）───────────────────────────────────────────

function evaluate(aiOutput, testCase) {
  const hits = testCase.expectedTraits.filter(t => aiOutput.includes(t));
  const violations = testCase.forbiddenTraits.filter(t => aiOutput.includes(t));
  const hitRate = testCase.expectedTraits.length > 0
    ? hits.length / testCase.expectedTraits.length
    : 1.0;
  const passed = violations.length === 0 && hitRate >= 0.8;
  return {
    name: testCase.name,
    hitRate,
    hits,
    violations,
    passed,
    outputPreview: aiOutput.length > 100 ? aiOutput.slice(0, 100) + '...' : aiOutput,
  };
}

async function runEval(getAiOutput, verbose = true) {
  const results = [];

  for (const testCase of TEST_CASES) {
    const output = await getAiOutput(testCase.input);
    const result = evaluate(output, testCase);
    results.push(result);

    if (verbose) {
      const status = result.passed ? '✅' : '❌';
      console.log(`${status} ${result.name}`);
      console.log(`   hit_rate: ${(result.hitRate * 100).toFixed(0)}%  |  hits: [${result.hits.join(', ')}]`);
      if (result.violations.length > 0) {
        console.log(`   ⚠️  violations: [${result.violations.join(', ')}]`);
      }
      if (!result.passed) {
        console.log(`   output: ${result.outputPreview}`);
      }
      console.log();
    }
  }

  const passed = results.filter(r => r.passed).length;
  const total = results.length;
  const passRate = total > 0 ? passed / total : 0;

  console.log('─'.repeat(40));
  console.log(`Pass rate: ${passed}/${total} = ${(passRate * 100).toFixed(0)}%`);
  if (passRate < 0.8) {
    console.log('⚠️  通过率低于 80%，建议检查 Prompt 或测试用例');
  }

  return { passRate, results, passed, total };
}


// ─── 入口（替换这里的 AI 调用）──────────────────────────────────────────────

async function main() {
  // TODO: 替换为你的实际 AI 调用
  // 示例（OpenAI）：
  //
  // import OpenAI from 'openai';
  // const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
  //
  // async function getAiOutput(inputText) {
  //   const response = await client.chat.completions.create({
  //     model: 'gpt-4o-mini',
  //     messages: [
  //       { role: 'system', content: YOUR_SYSTEM_PROMPT },
  //       { role: 'user', content: inputText },
  //     ],
  //   });
  //   return response.choices[0].message.content;
  // }

  // 临时 mock（先跑通流程，再替换为真实调用）
  async function getAiOutput(inputText) {
    return `这是对"${inputText}"的模拟回复，包含期望关键词1和期望关键词2`;
  }

  await runEval(getAiOutput);
}

main().catch(console.error);

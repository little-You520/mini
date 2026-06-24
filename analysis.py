from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy"
)

def call_llm(prompt: str, temperature=0.7, top_p=1.0, max_tokens=800):
    resp = client.chat.completions.create(
        model="deepseek-r1:1.5b",  # 本地已有，无需下载
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )
    return resp.choices[0].message.content.strip()

if __name__ == "__main__":
    test_prompt = "准确解释temperature、top_p、max_tokens三个LLM参数：temperature越小回答越严谨，top_p取值0-1，简洁50字左右"
    print("=== AI返回结果 ===")
    result = call_llm(
        prompt=test_prompt,
        temperature=0.3,
        max_tokens=600
    )
    print(result)
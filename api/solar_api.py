from openai import OpenAI # openai==1.52.2
 
client = OpenAI(
    apikey="", # 가입 후 발급해서 사용
    base_url="https://api.upstage.ai/v1"
)
 
stream = client.chat.completions.create(
    model="solar-pro2",
    messages=[
        {
            "role": "user",
            "content": "대한민국 애국가 가사 찾아줘. 그리고 근거 자료 출처 알려줘"
        }
    ],
    stream=True,
)
 
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
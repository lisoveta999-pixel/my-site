from openai import OpenAI

API_KEY = "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"  # Вставь свой ключ сюда

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

response = client.chat.completions.create(
    model="openrouter/owl-alpha",
    messages=[
        {"role": "user", "content": "Привет! Как дела?"}
    ]
)

print("Ответ:", response.choices[0].message.content)
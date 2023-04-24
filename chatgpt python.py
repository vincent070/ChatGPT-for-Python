#Developer is Vincent,this Project is ChatGPT for Python （中文版）
import requests
import json
import time

print("请输入您的问题")
history=[]
# 进入对话循环
while True:
    question=input("MeHel：")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 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',
    }   

    # Send request to GPT-3 API
    url = "https://gpt.siit.asia/v1/chat/completions"
    data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"{question}"}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    datas = response.json()

    message=datas["choices"][0]["message"]["content"]
     # 将响应添加到对话历史中
    history.append(message)

    # 打印响应
    print("ChatGPT:", message)

    # 延迟一段时间，以避免频繁调用 API
    time.sleep(0.5)
    
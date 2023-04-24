#Developer is Vincent,this Project is ChatGPT for Python 
import requests
import json
import time

print("Please enter your question")
history=[]
# Entering a conversation loop
while True:
    question=input("MeHel：")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer ',
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
     # Add response to conversation history
    history.append(message)

    # Print Response
    print("ChatGPT:", message)

    # Delay for a period of time to avoid frequent API calls
    time.sleep(0.5)
    

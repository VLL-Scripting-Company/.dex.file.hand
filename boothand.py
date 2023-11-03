import requests

def get_cody_response(prompt):
    url = "https://api.codybot.ai/v1/ask"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 0XCZ4II8ufJuTqeNVX6VCVbRN4qL9BKXCzQVPlfN"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    if "choices" in response_data:
        return response_data["choices"][0]["text"].strip()
    else:
        return None

prompt = "Once upon a time"
generated_text = get_cody_response(prompt)
print(generated_text)

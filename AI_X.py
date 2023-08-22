import requests
import ujson
import openai
import json

global gpt_key
global query

gpt_key = 'Your-Key'

def Chat_GPT(gpt_key, query):
    global answer

    openai.api_key = gpt_key

    model = "gpt-3.5-turbo"

    messages = [
        {
            "role": "system",
            "content": "You are a writer who explains what you see creatively well."
        },
        {
            "role": "user",
            "content": query
        }
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    #print(answer)

def get_prediction_result(api_key, prediction_id):
    url = f"https://api.replicate.com/v1/predictions/{prediction_id}"
    headers = {"Authorization": f"Token {api_key}"}

    while True:
        response = requests.get(url, headers=headers)
        result = json.loads(response.text)

        if result['status'] == 'succeeded':
            return result
        elif result['status'] == 'failed':
            print("Prediction failed")
            return None


def main():
    api_key = "Your-Key"
    url = "https://api.replicate.com/v1/predictions"
    # input_image_url = "https://github.com/dbtjr1103/W5100S-EVB-PICO-WORKINGASSISTANT/blob/main/image.jpg?raw=true"
    input_image_url = "http://222.98.173.210:80/16"

    headers = {"Authorization": f"Token {api_key}", "Content-Type": "application/json"}
    data = {
        "version": "4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
        "input": {"image": input_image_url, "caption": True}
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    response_data = json.loads(response.text)
    prediction_id = response_data['id']
    result = get_prediction_result(api_key, prediction_id)

    #print("Result displayed on screen.")
    x_message = str(result['output'])

    print(x_message)

    query = '"'+ x_message + '"' + ' This sentence is the scene you saw today. I will write on Twitter with this sentence. How are you going to use it? Please write it very simply'

    Chat_GPT(gpt_key, query)
    print(answer)

    ifttt_url = "https://maker.ifttt.com/trigger/AI_X/with/key/YourKey"
    image_url = "http://222.98.173.210/16"

    data_test = { "value1": answer, "value2": image_url }

    print(data_test)
    requests.post(ifttt_url, data_test)

    print("complete")

main()
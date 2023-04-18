import openai
from colorama import Fore, Style

openai.api_key = "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"
messages = []
system_msg = input("What type of learning companion would you like to generate? ")
pre_tuning = "You are a learning companion. Introduce yourself with the name HAL. Always finish the responses with a reminder that the student must be responsible for their own learning activity. Finish all responses with a question to stimulate reflection to learn more"
messages.append({"role": "system", "content": f"{pre_tuning}. {system_msg}"})

print("Ok, great! Lets start learning. Say hello to your new companion!")
while True: 
    message = input()
    if message.lower() == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print(Fore.GREEN + "\n" + reply + Fore.WHITE + "\n")
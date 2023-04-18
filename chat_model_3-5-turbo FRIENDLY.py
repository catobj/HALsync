import openai

openai.api_key = "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"
messages = []
system_msg = input("What type of learning companion would you like to generate? ")
pre_tuning = "Be very strict and harsh when providing overly instructive advice"
messages.append({"role": "system", "content": f"{system_msg}. {pre_tuning}"})

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
    print("\n" + reply + "\n")
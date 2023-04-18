import openai

openai.api_key = "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"
messages = []
system_msg = input("What type of learning companion would you like to create? ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")
while True: 
    message = input()
    if message.lower() == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
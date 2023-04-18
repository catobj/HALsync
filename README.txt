Readme file in HUMxAI git.

Testing out the https://www.haihai.ai/chatgpt-api/ approach to create a chatbot with few lines of code. 

The code snippet works! Trying to expand the tuning of the chatbot. 

Refer to https://platform.openai.com/docs/guides/chat/introduction?ref=haihai.ai in order to strengthen the tuning.
Here the key code snippet is: 
    
    openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}


        2023-04-02
        Set up a alternative script where I change the model used. 

        2023-+4-09
        added color fonts to the dialogue to improve readability
        

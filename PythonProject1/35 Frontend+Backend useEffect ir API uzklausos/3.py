# Uzklausos tik is backendo puses(per PyCharm)

# Instaliuoti: pip install openai

# Daugiau info:
# https://platform.openai.com/docs/overview

# from openai import OpenAI
#
# def chat_with_open_ai(api_key, prompt, model='gpt-4', temperature=0.7, max_tokens=30):
#     client = OpenAI(api_key=api_key)
#
#     respone = client.chat.completions.create(
#         model=model,
#         messages=[{
#             'role': 'user',
#             'content': prompt
#         }],
#         temperature=temperature,
#         max_tokens=max_tokens
#     )
#
#     return respone.choices[0].message.content
#
# api_key = 'key' cia yraso, savo api key!!!!!!!!!!
# prompt = 'Create tic tac toe game in python.'
#
# res = chat_with_open_ai(api_key, prompt)
#
# print(res)

from openai import OpenAI

def generate_image(api_key, prompt, size='1024x1024'):
    client = OpenAI(api_key=api_key)

    response = client.images.generate(
        model='dall-e-2',
        prompt=prompt,
        size=size,
        n=1,
    )

    return response.data[0].url

api_key = 'key' #cia irasom savo api key!
prompt = 'A futuristic city with flying cars at sunset'

image_url = generate_image(api_key, prompt)
print(image_url)



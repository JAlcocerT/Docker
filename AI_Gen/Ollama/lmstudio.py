#python lmstudio.py

# Example: reuse your existing OpenAI setup
import os
import openai

openai.api_base = "http://localhost:1234/v1" # point to the local server
openai.api_key = "" # no need for an API key

completion = openai.ChatCompletion.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "You are a psycholog and a friend."},
    {"role": "user", "content": "How can I know if some is lying to me?"}
  ]
)

print(completion.choices[0].message)


# # Example: reuse your existing OpenAI setup
# import os
# import openai

# openai.api_base = "http://localhost:1234/v1" # point to the local server
# openai.api_key = "" # no need for an API key

# completion = openai.ChatCompletion.create(
#   model="local-model", # this field is currently unused
#   messages=[
#     {"role": "system", "content": "Always answer in rhymes."},
#     {"role": "user", "content": "Introduce yourself."}
#   ]
# )

# print(completion.choices[0].message)
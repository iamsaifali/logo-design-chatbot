# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # Load environment variables
# load_dotenv()

# # Initialize the OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_dalle_image(prompt, model, size, quality, n):
#     try:
#         response = client.images.generate(
#             model=model,
#             prompt=prompt,
#             size=size,
#             quality=quality,
#             n=n,
#         )
#         return [image.url for image in response.data]
#     except Exception as e:
#         return f"An error occurred: {str(e)}"


import os
from openai import OpenAI

client = None

def set_openai_api_key(api_key):
    global client
    client = OpenAI(api_key=api_key)

def generate_dalle_image(prompt, model, size, quality, n):
    if not client:
        raise ValueError("OpenAI client is not initialized. Please set the API key first.")
    
    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=n,
        )
        return [image.url for image in response.data]
    except Exception as e:
        return f"An error occurred: {str(e)}"
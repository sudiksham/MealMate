# -*- coding: utf-8 -*-
"""meal_mate_nlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ikdc8PLcpvrnh-CWFm8s46-eXlOPtQg-
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/recipe", methods=["POST"])
def get_recipe_suggestions():
  """
  Get recipe suggestions based on form data.
  """
  if request.method == "POST":
    food_items = request.form.getlist("food_items")
    spice_level = request.form.get("spice_level")
    cuisine = request.form.get("cuisine")
    veg = request.form.get("veg") == "on"
    allergy = request.form.get("allergy")

    # Process the form data and generate recipe suggestions here

    # PLACE CODE HERE

    # (replace this placeholder with your logic)
    recipes = ["Example Recipe 1", "Example Recipe 2"]

    return jsonify({"recipes": recipes})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)

!ngrok authtoken 2baQBxFmIuFhTt6FMse6PGUkRUq_t4u4H6feHnYQ3FHz3iHg

from pyngrok import ngrok
public_url=ngrok.connect(port='8081')
public_url

from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import supervision as sv

def load_image(image_path):
    img = Image.open(image_path)
    return img

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

import cv2

# Replace with the path to your image
img_path = 'applebanana.jpg'


# Perform inference
image = load_image(img_path)
results = model(image)

detections = sv.Detections.from_ultralytics(results[0])
print(detections)

classes = model.names

class_names = model.names if hasattr(model, 'names') else range(model.nc)


# Show Image
plt.imshow(image)

import google.generativeai as genai
from google.colab import userdata
GOOGLE_API_KEY=userdata.get('Gemini')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def generate_recipe(user_input, user_context):
    conversation = " ".join([context_item["content"] for context_item in user_context] + [user_input])
    print("Prompt:", conversation)

    # Generate the recipe using the pipeline
    response = model.generate_content(conversation)
    print("Recipe: \n", response.text)
    # generated_text = response[0]['generated_text']
    # return generated_text.strip()

def main():
    print("Welcome to the Recipe Assistant!")

    # Get user input for food items
    food_items = input("Please enter a list of food items (comma-separated): ").split(',')

    # Get user input for preferences
    taste_preference = input("What taste would you like (e.g., sweet, spicy, etc.)? ")
    cuisine_preference = input("What cuisine would you prefer? ")

    # Set user-specific variables
    vegetarian_preference = input("Are you vegetarian? (yes/no) ").lower() == 'yes'
    allergy_information = input("Do you have any allergies? If yes, please specify (comma-separated): ").split(',')

    # Process user input and form a prompt for the ChatGPT API
    user_input = f"I want a recipe with {', '.join(food_items)}. Prefer {taste_preference} taste and {cuisine_preference} cuisine."

    # Create user context based on variables
    user_context = [
        {"role": "system", "content": "You are a helpful recipe assistant."},
        {"role": "user", "content": f"The user prefers {'vegetarian' if vegetarian_preference else 'non-vegetarian'} meals."},
        {"role": "user", "content": f"The user has allergies to {', '.join(allergy_information) if allergy_information else 'none'}."},
    ]

    # Generate the recipe using the API
    recipe = generate_recipe(user_input, user_context)

if __name__ == "__main__":
  main()

# import google.generativeai as genai
# from google.colab import userdata
# import base64
# GOOGLE_API_KEY=userdata.get('Gemini')
# genai.configure(api_key=GOOGLE_API_KEY)

# with open("applebanana.jpg", "rb") as image_file:
#     image_bytes = image_file.read()

# # Encode the image bytes to base64 format
# encoded_image = base64.b64encode(image_bytes).decode("utf-8")

# # Configure your API key (as you've already done)

# model = genai.GenerativeModel('gemini-pro-vision')

# prompt = "Generate a list of all food items visible in this image: " + encoded_image


# response = model.generate_content(prompt)
# generated_text = response.text

# # food_items = extract_food_items_from_text(generated_text)  # Implement your parsing logic
# print(generated_text)

# USING OPEN AI API

# import openai
# import os
# from openai import OpenAI
# # openai.api_key = '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'

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key= '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',
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )

# def get_recipe(user_input, user_context):
#     # Define the conversation flow
#     conversation = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": user_input}
#     ]

#     for context_item in user_context:
#         conversation.append({"role": "system", "content": context_item})

#     # Make an API request
#     response = openai.Completion.create(
#         model="text-davinci-002",
#         messages=conversation,
#         max_tokens=150,
#         temperature=0.7,
#     )

#     # Extract the generated recipe from the API response
#     recipe = response['choices'][0]['message']['content'].strip()
#     return recipe

# import os
# from openai import OpenAI
# # Set your OpenAI API key
# api_key = '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'
# client = OpenAI(api_key=api_key)

# def get_recipe(user_input, user_context):
#     # Define the conversation flow with user context
#     conversation = [
#         {"role": "system", "content": "You are a helpful recipe assistant."},
#         {"role": "user", "content": user_input}
#     ]

#     # Add user context to the conversation
#     for context_item in user_context:
#         conversation.append({"role": "system", "content": context_item})

#     # Make an API request for chat completions
#     chat_completion = client.chat.completions.create(
#         model="davinci-002",
#         messages=conversation,
#     )

#     # Extract the generated recipe from the API response
#     recipe = chat_completion['choices'][0]['message']['content'].strip()
#     return recipe

# USING HUGGING FACE INFERENCE API

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
# import requests

# API_TOKEN = "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"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# # Load Flan T5 base tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
# model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# # Set up the pipeline for text2text generation
# text2text_generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=300)

# def generate_recipe(user_input, user_context):
#     conversation = " ".join([context_item["content"] for context_item in user_context] + [user_input])

#     print("prompt:", conversation)

#     # Generate the recipe using the pipeline
#     result = text2text_generator(conversation)
#     print("result:", result)
#     generated_text = result[0]['generated_text']
#     return generated_text.strip()


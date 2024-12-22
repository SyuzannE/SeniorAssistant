"""Main file for the Senior Smart Cpmmunity Project project"""
import os
from os import PathLike
from time import time
import asyncio
from typing import Union

from dotenv import load_dotenv
import openai
from deepgram import Deepgram
import pygame
from pygame import mixer
import elevenlabs

from record import speech_to_text

# Load API keys
load_dotenv()
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
elevenlabs.api_key = os.getenv("ELEVENLABS_API_KEY")

deepgram = Deepgram(DEEPGRAM_API_KEY)


elevenlabs.set_api_key("sk_4798653cc4dbc6e47c90a866f363c71575e8551e5a142c1c")

# Initialize APIs

# mixer is a pygame module for playing audio
mixer.init()


context = "You are Aria, Seniors human assistant. A friendly AI robot for seniors is a compassionate and approachable companion designed to provide assistance, safety, and companionship. suggesting activities like Playground, Art and Craft Room, Game Room,."
conversation = {"Conversation": []}
RECORDING_PATH = "audio/recording.wav"


def request_gpt(prompt: str) -> str:
    """
    Send a prompt to the GPT-3 API and return the response.

    Args:
        - state: The current state of the app.
        - prompt: The prompt to send to the API.

    Returns:
        The response from the API.
    """


    from openai import AzureOpenAI  
    
    endpoint = os.getenv("ENDPOINT_URL", "https://jarvisaibotufar.openai.azure.com/")  
    deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo-16k")  
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "1etwpF6fKvntB3IY160xU2i4s8ONsg3EEjEyTqaV8Lxwr7jmVoglJQQJ99AJACYeBjFXJ3w3AAABACOGUbf0")  
    
    # Initialize Azure OpenAI client with key-based authentication
    client = AzureOpenAI(  
        azure_endpoint=endpoint,  
        api_key=subscription_key,  
        api_version="2024-05-01-preview",  
    )  

    # Prepare the chat prompt  
    chat_prompt = [
    {
        "role": "system",
        "content": "Elders AI assistant" + context
    },
    {
        "role": "user",
        "content":"Senior Andranik" + prompt
    }
]  
    
    # Include speech result if speech is enabled  
    speech_result = chat_prompt  
    
    # Generate the completion  
    completion = client.chat.completions.create(  
        model=deployment,  
        messages=speech_result,  
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=None,  
        stream=False  
    )  
    
    return completion.choices[0].message.content;
    

async def transcribe(
    file_name: Union[Union[str, bytes, PathLike[str], PathLike[bytes]], int]
):
    """
    Transcribe audio using Deepgram API.

    Args:
        - file_name: The name of the file to transcribe.

    Returns:
        The response from the API.
    """
    with open(file_name, "rb") as audio:
        source = {"buffer": audio, "mimetype": "audio/wav"}
        response = await deepgram.transcription.prerecorded(source)
        return response["results"]["channels"][0]["alternatives"][0]["words"]


def log(log: str):
    """
    Print and write to status.txt
    """
    print(log)
    with open("status.txt", "w") as f:
        f.write(log)


if __name__ == "__main__":
    while True:
        # Record audio
        log("Listening...")
        speech_to_text()
        log("Done listening")

        # Transcribe audio
        current_time = time()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        words = loop.run_until_complete(transcribe(RECORDING_PATH))
        string_words = " ".join(
            word_dict.get("word") for word_dict in words if "word" in word_dict
        )
        with open("conv.txt", "a") as f:
            f.write(f"{string_words}\n")
        transcription_time = time() - current_time
        log(f"Finished transcribing in {transcription_time:.2f} seconds.")

        # Get response from GPT-3
        current_time = time()
        response = request_gpt(string_words)
        context += response
        gpt_time = time() - current_time
        log(f"Finished generating response in {gpt_time:.2f} seconds.")

        # Convert response to audio
        current_time = time()
        audio = elevenlabs.generate(
            text=response, voice="Aria", model="eleven_multilingual_v2"
        )
        elevenlabs.save(audio, "audio/response.wav")
        audio_time = time() - current_time
        log(f"Finished generating audio in {audio_time:.2f} seconds.")

        # Play response
        log("Speaking...")
        sound = mixer.Sound("audio/response.wav")
        # Add response as a new line to conv.txt
        with open("conv.txt", "a") as f:
            f.write(f"{response}\n")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))
        print(f"\n --- ARIA: {string_words}\n --- Senior Andranik: {response}\n")
























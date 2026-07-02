# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_Gemini_api_key():
    Gemini_api_key = "AIzaSyAsGwS-k9nkjG7huXV-9eTeEjfuKu8bnWY"
    return Gemini_api_key

# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.
# the format for that file is (without the comment)
# API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService

def load_env():
    _ = load_dotenv(find_dotenv())

def get_claude_api_key():
    load_env()
    claude_api_key = os.getenv("CLAUDE_API_KEY")
    return claude_api_key

def get_serper_api_key():
    load_env()
    serper_api_key = os.getenv("SERPER_API_KEY")
    return serper_api_key

# break line every 80 characters if line is longer than 80 characters
# don't break in the middle of a word
def pretty_print_result(result):
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if new_line == '':
                    # start the line with the first word
                    new_line = word
                    continue
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
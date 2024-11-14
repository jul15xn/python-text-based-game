import os
import sys
import time
import re
import colors as cs
from docent_vriendelijk import Docent

DIALOGUE_DEBUG = False
DOCENT = Docent()

def print_text_dialogue(text, total_intro_time, fore=37, back=40):
    text = DOCENT.parseText(text=text)
    parts = re.split(r'(<\d+>)', text)
    
    text_only = re.sub(r'<\d+>', '', text)
    separate_sleep_time = total_intro_time / len(text_only)

    cs.set_console_color(fore, back)
    
    for part in parts:
        if re.match(r'<\d+>', part):
            delay = int(part[1:-1]) / 1000
            time.sleep(delay)
        else:
            for letter in part:
                print(letter, end='', flush=True)
                global DIALOGUE_DEBUG
                if False: # set to false for debug mode which removes the print delay
                    time.sleep(separate_sleep_time)

def new_line():
    print("")
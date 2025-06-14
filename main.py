import time
import random
import keyboard

def get_random_text():
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Typing fast takes practice and patience.",
        "Python is a great language to learn programming.",
        "Discipline is the bridge between goals and accomplishment.",
        "Every great developer you know once struggled like you."
    ]
    return random.choice(texts)

def wpm_test():
    test_text = get_random_text()
    print("Type the following text:\n")
    print(test_text)
    print("\nStart typing when you are ready...")
    print("Press Enter After you are done")

    if (keyboard.read_event()):
        start_time = time.time()
        typed_text = input("Start typing:\n")
        end_time = time.time()

    elapsed_time = (end_time - start_time) / 60  # Convert to minutes
    word_count = len(typed_text.split())
    wpm = word_count / elapsed_time

    print(f"\nYour typing speed is {wpm:.2f} words per minute.")

get_random_text()
wpm_test()

#version 1 of the program doesnt check for mistakes and have to press enter to start and stop 
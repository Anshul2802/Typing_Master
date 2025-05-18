import time
import random
import tkinter as tk

sentences = ["the dog chased shadows through the park",
"she found coins buried under the tree",
"they walked slowly into the thick fog",
"music echoed softly across the silent valley",
"clouds drifted lazily over the green hills",
"children laughed running barefoot in the field",
"stars twinkled brightly in the night sky",
"he painted dreams on the old wall",
"books lay forgotten under layers of dust",
"wind whispered secrets through the broken windows"]

def pick_sentence():
    sentence = random.choice(sentences)
    print(f"Type this sentence: {sentence}")
    return sentence

def time_counter(sentence):
    input("Press Enter when you are ready to start typing...")
    start = time.perf_counter()
    a = input("Start Typing: ")
    end = time.perf_counter()

    time_taken = end - start
    print(f"Time Taken: {time_taken} seconds")

    if a.strip() == sentence:
        print("You successfully completed typing.")
    else:
        print("You failed to type the correct sentence.")

sentence = pick_sentence()
time_counter(sentence)
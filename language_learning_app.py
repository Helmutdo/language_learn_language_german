"""Language learning app"""

import random

# 100 most common words in German with translation in English
words = [
    {"german": "der", "english": ["the"]},
    {"german": "die", "english": ["the"]},
    {"german": "und", "english": ["and"]},
    {"german": "in", "english": ["in"]},
    {"german": "zu", "english": ["to"]},
    {"german": "den", "english": ["the"]},
    {"german": "das", "english": ["the"]},
    {"german": "nicht", "english": ["not"]},
    {"german": "von", "english": ["from", "of"]},
    {"german": "sie", "english": ["she", "they"]},
    {"german": "ist", "english": ["is"]},
    {"german": "des", "english": ["the"]},
    {"german": "sich", "english": ["oneself"]},
    {"german": "mit", "english": ["with"]},
    {"german": "dem", "english": ["the"]},
    {"german": "dass", "english": ["that"]},
    {"german": "er", "english": ["he"]},
    {"german": "es", "english": ["it"]},
    {"german": "ein", "english": ["a", "an"]},
    {"german": "ich", "english": ["I"]},
    {"german": "auf", "english": ["on", "upon"]},
    {"german": "so", "english": ["so"]},
    {"german": "eine", "english": ["a", "an"]},
    {"german": "auch", "english": ["also"]},
    {"german": "als", "english": ["as", "when"]},
    {"german": "an", "english": ["at", "on"]},
    {"german": "nach", "english": ["after", "to"]},
    {"german": "wie", "english": ["how", "like"]},
    {"german": "im", "english": ["in the"]},
    {"german": "für", "english": ["for"]},
    {"german": "man", "english": ["one", "you"]},
    {"german": "aber", "english": ["but"]},
    {"german": "aus", "english": ["out of", "from"]},
    {"german": "durch", "english": ["through"]},
    {"german": "wenn", "english": ["if", "when"]},
    {"german": "nur", "english": ["only"]},
    {"german": "war", "english": ["was"]},
    {"german": "noch", "english": ["still", "yet"]},
    {"german": "werden", "english": ["become", "will"]},
    {"german": "bei", "english": ["at", "near"]},
    {"german": "hat", "english": ["has"]},
    {"german": "wir", "english": ["we"]},
    {"german": "was", "english": ["what"]},
    {"german": "wird", "english": ["becomes", "will"]},
    {"german": "sein", "english": ["his", "its"]},
    {"german": "einen", "english": ["a", "an"]},
    {"german": "welche", "english": ["which"]},
    {"german": "sind", "english": ["are"]},
    {"german": "oder", "english": ["or"]},
    {"german": "zur", "english": ["to the"]},
    {"german": "um", "english": ["around", "at"]},
    {"german": "haben", "english": ["have"]},
    {"german": "einer", "english": ["a", "an"]},
    {"german": "mir", "english": ["me"]},
    {"german": "über", "english": ["over", "about"]},
    {"german": "ihm", "english": ["him"]},
    {"german": "diese", "english": ["this", "these"]},
    {"german": "einem", "english": ["a", "an"]},
    {"german": "ihr", "english": ["her", "their"]},
    {"german": "uns", "english": ["us"]},
    {"german": "da", "english": ["there"]},
    {"german": "zum", "english": ["to the"]},
    {"german": "kann", "english": ["can"]},
    {"german": "doch", "english": ["yet", "but"]},
    {"german": "vor", "english": ["before", "in front of"]},
    {"german": "dieser", "english": ["this"]},
    {"german": "mich", "english": ["me"]},
    {"german": "ihn", "english": ["him"]},
    {"german": "du", "english": ["you"]},
    {"german": "hatte", "english": ["had"]},
    {"german": "seine", "english": ["his"]},
    {"german": "mehr", "english": ["more"]},
    {"german": "am", "english": ["at the", "on the"]},
    {"german": "denn", "english": ["because", "for"]},
    {"german": "nun", "english": ["now"]},
    {"german": "unter", "english": ["under", "among"]},
    {"german": "sehr", "english": ["very"]},
    {"german": "selbst", "english": ["self"]},
    {"german": "schon", "english": ["already"]},
    {"german": "hier", "english": ["here"]},
    {"german": "bis", "english": ["until"]},
    {"german": "hab", "english": ["have"]},
    {"german": "dann", "english": ["then"]},
    {"german": "ihre", "english": ["her", "their"]},
    {"german": "mal", "english": ["time"]},
    {"german": "seiner", "english": ["his"]},
    {"german": "unsere", "english": ["our"]},
    {"german": "weil", "english": ["because"]},
    {"german": "wieder", "english": ["again"]},
    {"german": "eben", "english": ["just"]},
    {"german": "kein", "english": ["no, none"]},
    {"german": "weiß", "english": ["know"]},
    {"german": "mal", "english": ["once", "time"]},
    {"german": "immer", "english": ["always"]},
    {"german": "ganz", "english": ["whole", "entire"]},
    {"german": "neu", "english": ["new"]},
    {"german": "etwas", "english": ["something"]},
    {"german": "nun", "english": ["now"]},
    {"german": "möchte", "english": ["would like"]}
]

# function to quiz the user
def quiz_user(words):
    """ quiz the user on given words"""
    random.shuffle(words)
    score = 0
    # loop through each word
    for word in words:
        
        print(f"What is the English translation for {word['german']}?")
        user_answer = input("Your answer: ").strip().lower()
        # check if answer is in the list of possible answers
        correct_answers = [ans.lower() for ans in word["english"]]  # Convert all correct answers to lowercase

        if user_answer in correct_answers:
            print("Correct!\n")
            score += 1
        else:
            print(f"WRONG!!!!! The correct answer is/are: {word['english']}\n")
            score -= 0.5
    print(f"Your final score is: {score}")  # Display the final score

# call the function with the word list
def main():
    print("Welcome to the Language learning app")
    input("Press Enter to start the quiz...")
    quiz_user(words)

# call the main function
if __name__ == "__main__":
    main()
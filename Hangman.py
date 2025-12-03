import os
import json
import random

print("⁘⁘⁘ Welcome to the Hangman game ⁘⁘⁘\n".center(140))

base_dir = os.path.dirname(__file__)   # script program folder direction
file_path = os.path.join(base_dir, "words.json")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        words = json.load(f)
except FileNotFoundError:
    print("Please download words file on links below. ")
    print("link: ")
    exit()

def choose_hidden_word():
    categories = list(words["categories"].keys())

    print("Available categories:\n")
    # to show categories
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.replace('_', ' ').title()}")

    while True:
        choice = input("\n👉 Pick your category (name or number): ")

        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(categories):
                user_choice = categories[num - 1]
                break
            else:
                print("😅 Oops! That number doesn’t exist. Try again!.")
        elif choice.isalpha() or "_" in choice or " " in choice:
            normalized = choice.replace("_", " ").lower()
            if normalized in [c.replace("_", " ").lower() for c in categories]:
                # To find a category
                user_choice = next(c for c in categories if c.replace("_", " ").lower() == normalized)
                break
            else:
                print("🤔 Hmm… I don’t know that category. Wanna try again?")
        else:
            print("🚫 Whoa! That’s not a valid input. Only letters or numbers please 😜")

    hidden_word = random.choice(words["categories"][user_choice]).upper()
    return hidden_word, user_choice

hidden_word , user_choice = choose_hidden_word()

display_word = ["_"] * len(hidden_word)
print(f"\n🥳Your selected category: {user_choice.replace('_', ' ').title()}")

chances = 6
wrong_geuss = []

for i in range(10**2):

    print("\n", " ".join(display_word))
    print(f"You have {chances - len(wrong_geuss)} more geusses 😖")
    print(f"\n🥳Your selected category: {user_choice.replace('_', ' ').title()}. Don't forget that!")
    geuss = input("\n😁 Geuss a letter: ").upper()

    if len(geuss) != 1 or not geuss.isalpha():
        print("🤨 Please enter a single letter.")
        continue
    else:
        if geuss in hidden_word:
            for idx, ch in enumerate(hidden_word):
                if ch == geuss:
                    display_word[idx] = geuss
                    print("Wrong guesses: ", wrong_geuss)
        else:
            wrong_geuss.append(geuss)
            print("Wrong guesses: ", wrong_geuss)
            if (chances - len(wrong_geuss)) == 0:
                print("💀 GAME OVER 💀".center(140))
                print(f"\nYou could'nt geuss '{hidden_word}' \n.🫢😟 I can't watch 🫣😢")
                break

    if "_" not in display_word:
        print()
        print("🎉🎉🎉 YOU DID IT 🎉🎉🎉".center(140))
        print("🥳 Congratulations you won! The word was: ", hidden_word)
        break
else:
    print(f"😢 You can't geuss '{hidden_word}'!? That was the word.")


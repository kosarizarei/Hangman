# 🎮 Hangman Game (Python)

Welcome to the **Hangman Game**!  
This is a simple yet fun word-guessing game written in Python, enhanced with playful emojis and interactive feedback to keep players engaged.

---

## ✨ Features
- Choose from multiple **categories** of words.
- Interactive gameplay with **emoji-based feedback**.
- Tracks wrong guesses and remaining chances.
- Customizable word list via `words.json`.

---

## 📂 Project Structure
```
├── hangman.py       # Main game script               
├── words.json       # Word categories and lists
└── README.md        # Project documentation
```

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/kosarizarei/Hangman.git
   cd Hangman
    ```
2. Make sure you have Python 3 installed:

     python --version

3. Run the game:

   python hangman.py

## 📦 Requirements
- Python 3.x
- A words.json file containing categories and word lists.
- Example structure:
```json
{
  "categories": {
    "animals": ["cat", "dog", "elephant"],
    "fruits": ["apple", "banana", "cherry"]
  }
}
```

## 📥 Missing File Notice

If the words.json file is missing, the program will show a message with a link to download it directly from GitHub:
Please download words file from the GitHub repository.
link: https://raw.githubusercontent.com/kosarizarei/hangman-game/main/words.json
This link points to the raw file so you can save it directly

## 🎯 Gameplay
- Select a category by typing its name or number.
- Guess letters one by one.
- You have 6 chances before the game ends.
- Win by revealing all letters of the hidden word!

## 🖼 Demo
```
⁘⁘⁘ Welcome to the Hangman game ⁘⁘⁘

Available categories:
1. Animals
2. Fruits

👉 Pick your category (name or number): 1
🥳 Your selected category: Animals
_ _ _ _ _ _

😁 Guess a letter: A
Wrong guesses: []
```

## 📌 Notes
- If words.json is missing, the program will prompt you to download or create one.
- You can expand categories to make the game more challenging.

## 🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.

## 📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this code, but it comes without warranty.






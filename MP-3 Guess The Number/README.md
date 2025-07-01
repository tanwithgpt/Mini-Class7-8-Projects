# 🎮 MP3 - Guess The Number (Host Mode)

This is a number guessing game where the **host sets the secret number and number of attempts**, and the **player tries to guess it** within the limit.

## 💡 How It Works

- Host inputs:
  - A secret number
  - The number of tries the player gets
- Player inputs guesses
- The game tells:
  - If the guess is too low or too high
  - If the guess is correct
  - If the tries run out

## 🔧 Tech Used

- Python
- While loops
- `break` and `continue`
- Custom logic and conditions

## 📌 Notes

- Uses `float()` to support decimal guesses
- The number entered by the host **must be hidden manually on the output screen** to avoid spoilers
- Designed and built fully in **Class 7**
- **All logic, design, and code by me**
- **README formatting and structure by ChatGPT**

---

> This is part of my **Mini Projects Series** — each project builds my skills toward becoming a full-stack developer

---

# 🎮 Guess The Number – Version 2.0

**Type:** Mini Project  
**Version:** 2.0  
**Language:** Python  
**Author:** Tanmay Raj  
**README support:** ChatGPT 🤖

---

## 🌟 What’s New in Version 2.0?

- 🧩 **Difficulty Modes**  
  - Choose between:
    - `1` → Integer guessing (using `random.randint()`)
    - `2` → Decimal/Float guessing (using `random.uniform()`)

- 🎛️ **Dynamic Range Selection**  
  - Host inputs the upper limit; number is picked randomly between `0` and that value.

- 🛡️ **Input Error Handling**  
  - `try-except` used to handle invalid difficulty selection.

---

## ✅ Features Retained from Previous Versions

- 💬 Hint system: "Too high" / "Too low" feedback after each guess  
- 🔄 Game ends after correct guess or when allowed attempts run out  
- 🎯 Host defines number of tries  
- 🧼 Clean, user-friendly prompts in console

---

## 📝 Notes

- `float()` is still used for all guesses for now (even in integer mode).
- This is a **major update** to the original version — worthy of being called a **full mini-project**.
- No external libraries required except Python’s built-in `random`.

---

## 🛠️ Suggestions for v3.0 (Optional Improvements)

- Add a GUI using Tkinter  
- Use functions to modularize the code  
- Add score tracking / number of attempts used  
- Add difficulty labels (Easy, Medium, Hard)  
- Leaderboard for multiple players

---

> ⚠️ **This project was built and debugged entirely by Tanmay Raj (Class 7), with this README written with the help of ChatGPT.**








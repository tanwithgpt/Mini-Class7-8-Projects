# PP1: Terminal Cricket Simulation (Prototype)
> **PP = Pseudo Project**

---

## ⚠️⚠️ THIS IS NOT A FINAL VERSION. EXPECT BUGS. ⚠️⚠️  
### ❗ This is a **prototype build** and is not fully polished yet. ❗

---

## 📌 About This Project

This is a **playable prototype** of a terminal-based cricket simulation game written in Python.  
It includes fundamental match mechanics such as:

- Team selection (India vs Australia)
- Toss logic
- Batting modes (Hit, Slog, Defend)
- Overs and ball count tracking
- Automatic and manual bowler selection
- Randomized shot outcomes based on bowler stats

The AI team is fixed as Australia for this prototype.

---

## ✅ Current Features

- Ball-by-ball gameplay for both teams
- Bowling stat system that affects outcome
- Toss to decide who bats first
- Over counting and bowler change logic
- Separate functions for batting modes
- Manual input for shots and bowlers (where required)

---

## 🚧 Upcoming Features

- Striker rotation and batter pair management
- Over-wise scoreboard summary
- Wickets falling display and partnerships
- Batter and bowler stat tracking
- Cleaned-up, reusable functions (reduction of repeated logic)
- Difficulty modes
- Better structured UI output
- End-game result summary
- CLI/GUI-based interface (possibly in future versions)

---

## ⚠️ Known Issues

- Some functions repeat similar code and will be refactored in future versions.
- Bowler over-limit is not enforced per player.
- Basic input checks are used; edge cases might not be fully handled.

---

## 📁 File Structure

```
main.py       # Full game logic
README.md     # Project documentation
```

---

## 📄 The Magic Note

All **logic, game design, features, flow, and code** in this project were created entirely by **Tanmay**.

This `README.md` file and formatting were written by **ChatGPT** to assist in documentation and public release formatting.  
All code credit, implementation, and idea flow belong solely to the developer.

---

## 🧪 Version Philosophy

This is not a Version 1 release.  
This is a **Prototype (PP1 - Pseudo Project 1)** made to test match logic and simulate gameplay without focusing on structure or user interface.

Future versions will focus on polishing, refactoring, and expanding feature depth.

---

## ▶️ How to Run

Make sure you have Python 3.x installed. Then run:

```bash
python main.py
```

This is a terminal-based game. All inputs are text-based.

---

## 📌 Note

This is an early-stage project meant to test and implement gameplay ideas.  
The project will evolve over time with improved structure and features.


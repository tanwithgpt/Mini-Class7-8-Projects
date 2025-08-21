# 🐉 Rouge Terminal

**Status:** Dev (Structure & Polishing)  

**Lang:** Python

**Note:** This README is made by ChatGPT but all the logic and code is fully mine.
Text-based roguelike combat in the terminal. Pick a character, unlock upgrades, and beat bosses.

---

## 📂 Project Structure
Rouge Terminal/
├── main.py # Entry point, flow & boss selection
├── combat_PLAY.py # Combat mechanics (player vs boss)
├── boss.py # Boss class + Level1/2/3 instances
├── player.py # Player classes + playable characters
└── shopmarket.py # Shop items (character unlocks, talismans)

---

## 🎭 Playable Characters (from `player.py`)

> Class: `Player_c(healthp, attackp, healpp, using)`

| Character | Health (`healthp`) | Attack (`attackp`) | Heal (`healpp`) | Using Flag |
|---|---:|---:|---:|---|
| **Mega** (`mega`) | **50** | **30** | **50** | `'N'` |
| **Rico** (`ricop`) | **100** | **50** | **100** | `'N'` |

- Player wallet: `user = Player(coins=0)`

**Unlocks:**  
- Rico (playable) is locked behind the **shop item** “Rico” (see Shop).

---

## 👹 Bosses (from `boss.py`)

> Class: `Boss(level, healthb, attackb, healb, rewardb, usingb)`

| Boss | Level | Health (`healthb`) | Attack (`attackb`) | Heal (`healb`) | Reward (`rewardb`) | Using (`usingb`) |
|---|---:|---:|---:|---:|---:|:--:|
| **Level1** | 1 | **50** | **20** | **0**  | **20**  | `N` |
| **Level2** | 2 | **70** | **50** | **30** | **50**  | `N` |
| **Level3** | 3 | **100** | **100** | **50** | **100** | `N` |

> Set exactly one boss’s `usingb` to `'Y'` before starting combat (handled via `check()` flow).

---

## 🛒 Shop Items (from `shopmarket.py`)

> Class: `items(name, price, unlock, healthup, attackup, healup)`

| Item | Price | Unlock (default) | +Health | +Attack | +Heal | Notes |
|---|---:|:--:|---:|---:|---:|---|
| **Rico** (`rico`) | **200** | `False` | 0 | 0 | 0 | Unlocks **Rico** as a playable character |
| **Health Talisman** (`health`) | **20** | `False` | **+10** | 0 | 0 | One-time pre-boss buff |
| **Attack Talisman** (`attack`) | **20** | `False` | 0 | **+10** | 0 | One-time pre-boss buff |
| **Heal Talisman** (`heal`) | **20** | `False` | 0 | 0 | **+10** | One-time pre-boss buff |

> (There’s a reference to `shadow_of_the_realm` in the shop flow — add its definition here when finalized.)

---

## ⚔️ Combat (from `combat_PLAY.py`)
- **Health fields:** Player → `healthp`, Boss → `healthb`
- **Attack fields:** Player → `attackp`, Boss → `attackb`
- **Heals:** Player → `healpp`, Boss → `healb`
- Flow (simplified):
  1. Choose character (unlock via shop if needed).
  2. Select boss via `usingb` flags → `check()` resolves `player_boss`.
  3. Optional: use a **Talisman** (applies +10 to the relevant stat of the chosen character).
  4. Turn-based combat until either `healthp <= 0` or `healthb <= 0`.
  5. On win, award `rewardb` coins.

> Recommendation: call `combat(player_cha, player_boss)` with explicit arguments to avoid global timing issues.

---

## ▶️ Run
```bash
python main.py

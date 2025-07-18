# 💧 MP6 – Healthy Programmer v1

A real-world productivity assistant that reminds you to:
- Drink water
- Do eye exercises
- Get up and do physical activity

It uses `pygame` to play sounds at intervals and logs your confirmations into a file for long-term health accountability.

---

## 🧠 Features

- ⏰ **Timed Reminders**
  - 💦 Drink water every 1 hour
  - 👁️ Eye exercise every 30 minutes
  - 🏃‍♂️ Physical activity every 45 minutes

- 🔊 **Sound Alerts**
  - Each task uses its own `.mp3` reminder
  - Prevents multiple sounds from overlapping using `get_busy()`

- 📁 **Activity Logging**
  - Logs confirmations to `Logfile.txt`
  - Each log includes a Unix timestamp for future tracking

- 🔁 **Endless Loop**
  - Runs forever — perfect for deep work sessions

---

## 🧪 Tech Used

- Python 3.x
- `pygame` for sound
- `time` for intervals and timestamps

---

## 🔐 File Handling

- File: `Logfile.txt`
- Mode: Opened in `"a+"` — creates file if missing and appends logs

---

## 🧱 Project Structure

```python
pex()      # physical exercise reminder
dwater()   # water reminder
deye()     # eye exercise reminder

while True:
    pex()
    dwater()
    deye()
```

---

## ⚠️ Notes

- You must provide valid `.mp3` paths for each reminder sound.
- Sound overlap prevention uses:
```python
if not other_sound.get_busy():
    sound.play()
```

---

## 🛠️ Possible V2 Upgrades

- Better timestamp formatting (e.g., `time.ctime()` or `datetime`)
- GUI or tray icon integration
- Toggle reminder types
- Logging with categories or readable formatting

---

## 🪄 Magic Note

This README — its formatting, structure, and writing — was crafted by ChatGPT.

But the entire project — every line of code, every decision, every mechanic —  
**was fully created and written by me, Tanmay Raj.**

ChatGPT helped shape the words,  
but the ideas, logic, and execution are all mine.

We built this like a team —  
**me on the keyboard, GPT on the mic.**

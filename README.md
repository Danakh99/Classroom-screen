## 🧠 Smart-Table Classroom App

An **interactive touch-screen educational application** for kids, designed for **Raspberry Pi**.
Built using **Python + Kivy**, the system provides:

✅ Touch-friendly UI
✅ Interactive subject menu
✅ Drawing / handwriting notebook
✅ Quiz system
✅ Full Arabic language support (RTL & shaping)
✅ Fullscreen optimized for classroom tablet usage

---

## 📸 Preview

> (in progress)

---

## 📁 Project Structure

| File / Folder                                | Description                                                       |
| -------------------------------------------- | ----------------------------------------------------------------- |
| `main.py`                                    | App entry point — loads screens, fullscreen setup, screen manager |
| `features/ui.py`                             | Shared Arabic UI tools, RTL text, font loading, rounded buttons   |
| `features/welcome_screen.py`                 | Welcome screen with logo and start button                         |
| `features/main_menu.py`                      | Main dashboard — subject buttons + navigation                     |
| `features/notebook.py`                       | Digital notebook — draw, erase, change color/size, clear page     |
| `features/quiz_math.py` / `features/quiz.py` | Multiple-choice quiz system with score tracking                   |
| `features/science.py`                        | Placeholder / coming soon (3D model planned)                      |
| `features/placeholder.py`                    | Placeholder screen for upcoming subjects                          |
| `smart-table-venv/`                          | Python virtual environment (Do **not** delete)                    |

---

## ✨ Features

### 📚 Subject Menu

* Science
* Math
* English
* Computer
* Social Studies
* Notebook
* Contact Us

### ✍️ Handwriting Notebook

* Finger / stylus drawing
* Color select
* Pen size change
* Eraser
* Clear page
* Scroll to extend writing area

### 🧩 Quiz System

* Multiple-choice questions
* Score tracking
* Restart quiz or return to menu

### 🌍 Arabic Support

* RTL text rendering
* Arabic text reshaping
* Custom Arabic fonts


## 📦 Requirements

To run this project, install the required Python packages:

```bash
pip install -r requirements.txt
````

### This project uses:

* `kivy`
* `arabic-reshaper`
* `python-bidi`
* `pillow`

These packages handle the graphical interface, Arabic text shaping/RTL support, and image rendering for the smart-table educational system.

---

## ✅ Virtual Environment Setup (Recommended)

```bash
python3 -m venv smart-table-venv
source smart-table-venv/bin/activate
pip install -r requirements.txt
```


## 🚀 Running the App

### ✅ Activate virtual environment

```bash
source ~/projects/smart-table-venv/bin/activate
```

### ✅ Run the Smart-Table app

```bash
classroom
```

> Make sure Kivy, `arabic_reshaper`, `python-bidi`, and fonts are installed inside the venv.

---

## 🛠️ Tech Stack

| Technology             | Purpose                 |
| ---------------------- | ----------------------- |
| Raspberry Pi           | Hardware                |
| Python                 | Language                |
| Kivy                   | GUI & touch interface   |
| arabic-reshaper & bidi | Arabic RTL text support |

---

## 🎯 Future Enhancements

* ✅ Animated UI
* 🎥 3D models in science section
* 👨‍🏫 Teacher mode / admin panel
* 🎵 Interactive learning games
* 🧠 AI-based handwriting recognition (future)

---

## 🤝 Contributing

Pull requests welcome!
Report issues or suggest improvements anytime.

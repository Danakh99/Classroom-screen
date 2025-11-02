📁 Project Overview
This project is an educational smart-table application built for kids. It runs on a Raspberry Pi and provides an Arabic-friendly learning interface with interactive lessons, activities, and a handwriting notebook. The system is fully touch-screen optimized and supports Arabic text shaping for proper display.

📂 main.py
main.py initializes the entire application. It creates the screen manager, loads all screens (welcome page, main menu, notebook, and quiz), and starts the program in fullscreen. It controls screen transitions and serves as the app entry point.

📂 features/ui.py
This file contains all UI helper functions used across the app. It registers the Arabic font, reshapes Arabic text, and applies right-to-left rendering so Arabic words display correctly. It also defines reusable components like Arabic labels, rounded buttons, and color buttons, and provides the main color theme for the application.

📂 features/main_menu.py
This file builds the main subject-selection screen that appears after the welcome page. It displays the logo and a vertical menu of school subjects (Science, Math, English, Computer, Social Studies) along with buttons for Notebook and Contact Us. It handles screen navigation to each feature.

📂 features/welcome_screen.py
This file displays the first screen the user sees when launching the app. It shows the academy logo and a welcome message in Arabic, along with a start button that takes the user into the main menu.

📂 features/notebook.py
notebook.py implements a digital handwriting notebook for students. It allows drawing with a stylus or finger, erasing, changing pen size and color, scrolling through the page, clearing notes, and returning to the main menu. This is designed for practicing writing, math steps, drawing, and note-taking.

📂 features/quiz.py
This file creates the multiple-choice quiz activity. It displays questions with four answers, tracks correct and wrong responses, updates scores live, and shows a results screen at the end. It includes Arabic text support and a button to restart the quiz or go back to the home screen.

📂 features/placeholder.py
This file is a simple screen used temporarily for features that are planned but not yet developed. It shows a title and a back button so the app flow remains complete while future lessons and activities are added.

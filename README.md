Smart-Table Classroom App

This project is an educational touchscreen classroom application designed for kids, developed for Raspberry Pi. The system provides a simple learning interface with subject menus, interactive quizzes, a handwriting notebook, and Arabic language support. It is optimized for fullscreen usage on a touch device and displays Arabic text correctly using reshaping and right-to-left rendering.

Project Structure and File Descriptions
main.py

This is the entry point of the application. It initializes the Kivy app, loads all screens into the ScreenManager, and starts the program in fullscreen mode. It controls navigation and launches the welcome screen, main menu, notebook, and quiz screens.

features/ui.py

This file contains shared UI utilities and styling functions used throughout the app. It loads and registers Arabic fonts, reshapes Arabic text for proper display, and handles right-to-left text direction. It also defines reusable UI components such as Arabic labels, rounded buttons, and color selectors.

features/welcome_screen.py

This file displays the first screen shown when the application starts. It shows the academy logo and a welcome message in Arabic, with a button that leads the user to the main menu.

features/main_menu.py

This file builds the main dashboard that contains the list of subjects and features. It displays the logo, page title, and interactive buttons for Science, Math, English, Computer, Social Studies, Notebook, and Contact Us. It handles navigation to each feature.

features/notebook.py

This file implements an interactive digital notebook. Users can draw with a finger or stylus, change pen color and size, erase, scroll the page vertically, and clear the notebook. It is designed for handwriting practice, solving exercises, and note-taking.

features/quiz.py

This file provides a multiple-choice quiz feature. It displays questions and answer buttons, checks user responses, tracks correct and incorrect answers, and shows a result screen at the end. It also supports restarting the quiz or returning to the main menu.

features/placeholder.py

This is a simple placeholder screen used for subjects and features that are not yet developed. It displays a temporary title message and provides a button to return to the previous screen.

Environment Notes

The folder smart-table-venv is the virtual environment for this project. It contains Python libraries (such as Kivy, arabic_reshaper, and bidi), and must be activated before running the app. Do not delete this folder, as it is required to run the application.

To start the project:

source ~/projects/smart-table-venv/bin/activate
classroom

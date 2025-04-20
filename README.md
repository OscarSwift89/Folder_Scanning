# Folder Tree Scanner GUI

A simple Python/​Tkinter application that lets you visually select a folder, specify exclude patterns, and export its directory structure as a tree into a `.txt` file. Ideal for quickly generating and sharing folder hierarchies on GitHub or local documentation.

---

## 🚀 Features

- **Graphical UI** – Browse for source folder and output file via dialogs  
- **Exclude Patterns** – Enter comma‑separated glob patterns (e.g. `*.tmp,*.hash`) to hide unwanted files or folders  
- **ASCII Tree** – Recursive traversal renders a familiar `├──`, `└──` tree format  
- **UTF‑8 Output** – Write the result to any `.txt` file, preserving non‑ASCII names  

---

## 🛠 Prerequisites

- **Python 3.6+**  
- Standard library only (no extra pip installs)  
- Cross‑platform: Windows, macOS, Linux  

---

## 📥 Installation

1. **Clone this repository**  
   ```bash
   git clone https://github.com/<your‑username>/folder-tree-scanner-gui.git
   cd folder-tree-scanner-gui

---

## 🎮 Usage

**Launch the GUI**

    ```bash
    python folder_tree_gui.py
    ```

or, if you made it executable:


    ```bash
./folder_tree_gui.py
Select a Source Folder

Click Browse… next to Source Folder

Navigate and choose the directory you want to scan

Set Output File

Click Browse… next to Output File

Choose a .txt filename (e.g. tree.txt, project_structure.txt)

Configure Exclusions

In Exclude Patterns, enter glob patterns separated by commas

Example: *.tmp,*.hash,build,venv

Scan & Save

Click Scan

A success dialog will confirm when the tree is written

---

## 📝 Example
Exclude Patterns:

    ```markdown

    *.log,*.pyc,__pycache__
    Output (tree.txt):

    css
    Copy
    Edit
    /home/user/myproject
    ├── README.md
    ├── folder_tree_gui.py
    ├── docs
    │   ├── user_guide.md
    │   └── images
    └── src
        ├── main.py
        └── utils.py

---

## 🔧 How It Works
    scan_folder(path, exclude_patterns, prefix='')
    Recursively walks path, skipping any entry matching your glob patterns, and builds an ASCII‑style tree.

    Tkinter UI Components:

    Entry fields for source folder, output path, and exclude patterns

    filedialog for browsing folders and files

    messagebox for success/error notifications
---

## 📝 License
    ![GitHub](https://img.shields.io/badge/Python-3.8%2B-blue)
    ![GitHub](https://img.shields.io/badge/License-MIT-green)

    Distributed under the MIT License. See LICENSE for details.
    Author: Oscar Student Tutor
    Date: 2025-04-20
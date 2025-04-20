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

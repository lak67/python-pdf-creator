# 📚 Zip-to-PDF Batch Converter

A lightweight, local desktop utility that accepts a ZIP file containing folders of images (manga, comics, or scanned documents) and automatically converts each folder into a sequential PDF file.

## 📥 Download & Run (No Python Required)

If you just want to use the tool, you don't need to install Python.

1.  **[Download the latest release here](https://github.com/your-username/your-repo-name/releases/latest)**.
2.  Download the **`.zip`** file listed under Assets.
3.  Extract the zip and run `ZipToPDF.exe`.

> **Note:** On the first run, Windows may show a blue popup saying "Windows protected your PC". This happens because this app is open-source and not digitally signed by Microsoft. Click **More Info** -> **Run Anyway**.

---

## 🚀 Features

* **Batch Processing:** Converts multiple folders within a single ZIP file into separate PDFs.
* **Recursive Search:** Intelligently finds image folders even if they are nested deep inside the ZIP (e.g., `Series.zip -> SeriesName -> Vol 1 -> Images`).
* **Natural Sorting:** Correctly orders pages so "Page 10" comes after "Page 2" (instead of before).
* **Auto-Organized Output:** Automatically creates a new folder next to your ZIP file to store the generated PDFs.
* **Duplicate Handling:** Automatically renames PDFs if multiple folders share the same name to prevent overwriting.

---

## 🛠️ For Developers (Running from Source)

If you want to modify the code or run it using your own Python environment, follow these steps.

### Prerequisites
* Python 3.x
* Pillow (`pip install Pillow`)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/lak67/python-pdf-creator.git
    cd your-repo-name
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

    **🐧 Linux & 🍎 macOS Users:**
    If you see `ModuleNotFoundError: No module named 'tkinter'`, you need to install it manually:
    * **Ubuntu/Debian:** `sudo apt-get install python3-tk`
    * **Fedora:** `sudo dnf install python3-tkinter`
    * **macOS (Homebrew):** `brew install python-tk`

3.  **Run the Script**
    ```bash
    python main.py
    ```

### Building the Executable
To build the `.exe` yourself, use PyInstaller:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --name "ZipToPDF" main.py
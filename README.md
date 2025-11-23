# 📚 Zip-to-PDF Batch Converter

A lightweight Python GUI utility that accepts a ZIP file containing folders of images (manga, comics, or scanned documents) and automatically converts each folder into a sequential PDF file.

## 🚀 Features

* **Batch Processing:** Converts multiple folders within a single ZIP file into separate PDFs.
* **Recursive Search:** Intelligently finds image folders even if they are nested deep inside the ZIP (e.g., `Series.zip -> SeriesName -> Vol 1 -> Images`).
* **Natural Sorting:** Correctly orders pages so "Page 10" comes after "Page 2" (instead of before).
* **Auto-Organized Output:** Automatically creates a new folder next to your ZIP file to store the generated PDFs.
* **Duplicate Handling:** Automatically renames PDFs if multiple folders share the same name to prevent overwriting.

## 🛠️ Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install Dependencies**
    This project uses `Pillow` for image processing.
    ```bash
    pip install -r requirements.txt
    ```

### 🐧 Linux & 🍎 macOS Users
While `tkinter` (the GUI library) is standard on Windows, it is sometimes missing on Linux or macOS.

* **If you get this error:** `ModuleNotFoundError: No module named 'tkinter'`
* **Run this command to fix it:**

    * **Ubuntu/Debian:**
        ```bash
        sudo apt-get install python3-tk
        ```
    * **Fedora:**
        ```bash
        sudo dnf install python3-tkinter
        ```
    * **macOS (if using Homebrew):**
        ```bash
        brew install python-tk
        ```

## 📖 How to Use

### 1. Prepare your ZIP file
Ensure your images are inside folders within the ZIP file. The program supports `.jpg`, `.jpeg`, `.png`, `.webp` and `.bmp`.

**Supported Structure Example:**
```text
MyMangaSeries.zip
├── Volume 1            <-- Will become "Volume 1.pdf"
│   ├── page1.jpg
│   ├── page2.jpg
│   └── ...
└── Volume 2            <-- Will become "Volume 2.pdf"
    ├── page1.jpg
    └── ...
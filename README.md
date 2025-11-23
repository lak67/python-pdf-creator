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
    This project uses `Pillow` for image processing. `tkinter` is used for the GUI and comes pre-installed with Python on most systems.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```

## 📖 How to Use

### 1. Prepare your ZIP file
Ensure your images are inside folders within the ZIP file. The program supports `.jpg`, `.jpeg`, `.png`, and `.bmp`.

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
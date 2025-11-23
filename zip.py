import zipfile
import os
import re
import shutil
import tempfile

def natural_sort_key(s):
    """
    Sorts strings containing numbers naturally (1, 2, 10 instead of 1, 10, 2).
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def extract_and_organize(zip_path):
    """
    1. Extracts zip to temp.
    2. Recursively walks (handles Series->Book->Pages).
    3. Returns dict: {'BookName': [list_of_image_paths]}
    """
    temp_dir = tempfile.mkdtemp()
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    
    books_data = {}

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # os.walk goes as deep as necessary automatically
        for root, dirs, files in os.walk(temp_dir):
            # Filter for images only in the CURRENT folder
            images = [f for f in files if f.lower().endswith(image_extensions)]
            
            if images:
                # Sort images naturally
                images.sort(key=natural_sort_key)
                full_paths = [os.path.join(root, img) for img in images]
                
                # ---------------------------------------------------------
                # LOGIC FOR NAMING THE BOOK
                # ---------------------------------------------------------
                
                # 1. Basic Name: The name of the immediate folder (e.g., "Book 1")
                if root == temp_dir:
                    # If images are right at the top, use zip filename
                    book_name = os.path.splitext(os.path.basename(zip_path))[0]
                else:
                    book_name = os.path.basename(root)

                # 2. Collision Check: 
                # If "Book 1" already exists (from a different subfolder),
                # prepend the parent folder name (e.g., "SeriesA_Book 1")
                if book_name in books_data:
                    parent_folder = os.path.basename(os.path.dirname(root))
                    book_name = f"{parent_folder}_{book_name}"

                # 3. Final Safety: If it STILL exists, append a number
                original_name = book_name
                counter = 1
                while book_name in books_data:
                    book_name = f"{original_name}_{counter}"
                    counter += 1

                books_data[book_name] = full_paths

        return books_data, temp_dir

    except Exception as e:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise e

def cleanup_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
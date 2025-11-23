from PIL import Image
import os

def create_pdf(image_paths, output_folder, book_name):
    """
    Compiles images into a PDF and saves it to the output_folder 
    using the book_name as the filename.
    """
    if not image_paths:
        return

    images = []
    
    for path in image_paths:
        try:
            img = Image.open(path)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            images.append(img)
        except Exception:
            print(f"Skipping invalid image: {path}")
            continue

    if not images:
        return

    # Construct final output path
    # Clean filename to remove characters invalid for file systems
    clean_name = "".join([c for c in book_name if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()
    pdf_filename = f"{clean_name}.pdf"
    output_path = os.path.join(output_folder, pdf_filename)

    base_image = images[0]
    other_images = images[1:]

    base_image.save(
        output_path, 
        "PDF", 
        resolution=100.0, 
        save_all=True, 
        append_images=other_images
    )
    
    return output_path
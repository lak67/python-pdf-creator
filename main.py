import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading
import zip as zip_logic 
import pdf as pdf_logic

class PdfConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Series ZIP to PDF")
        self.root.geometry("450x280")
        self.root.resizable(False, False)

        # UI Elements
        tk.Label(root, text="Batch Converter", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.label_instruction = tk.Label(
            root, 
            text="Import a ZIP containing folders of images.\n(e.g., Zip -> Book1_Folder -> images)", 
            justify="center"
        )
        self.label_instruction.pack(pady=5)

        self.btn_import = tk.Button(root, text="Import ZIP", command=self.process_files, height=2, width=20, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_import.pack(pady=15)

        self.status_label = tk.Label(root, text="Ready", fg="gray")
        self.status_label.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=350, mode='indeterminate')
        self.progress.pack(pady=10)

    def process_files(self):
        # 1. Get ZIP File
        zip_path = filedialog.askopenfilename(
            title="Select Series ZIP File",
            filetypes=[("Zip Files", "*.zip")]
        )
        
        if not zip_path:
            return

        # Run processing in thread
        thread = threading.Thread(target=self.run_conversion, args=(zip_path,))
        thread.start()

    def run_conversion(self, zip_path):
        self.update_status("Initializing...", True)
        temp_dir = None

        try:
            # A. Determine Output Location (Next to the Zip file)
            zip_dir = os.path.dirname(zip_path)
            zip_name = os.path.splitext(os.path.basename(zip_path))[0]
            
            # Create a folder named "ZipName_Converted"
            output_folder = os.path.join(zip_dir, f"{zip_name}_Converted")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # B. Extract and Organize
            self.update_text(f"Extracting {zip_name}...")
            books_dict, temp_dir = zip_logic.extract_and_organize(zip_path)

            if not books_dict:
                raise ValueError("No folders with images found in ZIP.")

            # C. Loop through found books and create PDFs
            count = 0
            total_books = len(books_dict)
            
            for book_name, image_paths in books_dict.items():
                self.update_text(f"Creating PDF: {book_name}...")
                pdf_logic.create_pdf(image_paths, output_folder, book_name)
                count += 1

            # Success Message
            success_msg = f"Process Complete!\n\nCreated {count} PDF(s).\nSaved in: {output_folder}"
            self.root.after(0, lambda: messagebox.showinfo("Success", success_msg))
            self.update_text("Done!")

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
            self.update_text("Error occurred.")

        finally:
            # Cleanup
            if temp_dir:
                zip_logic.cleanup_temp_files(temp_dir)
            self.update_status("Ready", False)

    def update_status(self, message, is_working):
        if is_working:
            self.progress.start(10)
            self.btn_import.config(state=tk.DISABLED)
        else:
            self.root.after(0, self.progress.stop)
            self.root.after(0, lambda: self.btn_import.config(state=tk.NORMAL))
        self.update_text(message)

    def update_text(self, text):
        self.root.after(0, lambda: self.status_label.config(text=text))

if __name__ == "__main__":
    root = tk.Tk()
    app = PdfConverterApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import filedialog, Toplevel
import cv2
from PIL import Image, ImageTk
from pytesseract import pytesseract
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

root = None
    
def extract_text(image_path):
    try:
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(e)

def Capture_from_webcam():
    try:
        webcam_window = Toplevel(root)
        webcam_window.title("Webcam")

        def capture_frame():
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("temp.jpg", frame)
                output_text = extract_text("temp.jpg")
                write_to_pdf(output_text, "output.pdf")
                display_image("temp.jpg")
                webcam_window.destroy()

        cap = cv2.VideoCapture(0)

        def update_webcam_feed():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)
                webcam_label.configure(image=frame)
                webcam_label.image = frame
                webcam_label.after(10, update_webcam_feed)  

        webcam_label = tk.Label(webcam_window) 
        webcam_label.pack()

        capture_button = tk.Button(webcam_window, text="Capture", command=capture_frame)
        capture_button.pack(pady=10)

        update_webcam_feed()

        webcam_window.mainloop()

        cap.release()

    except Exception as e:
        print(e)

def Upload_from_computer():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            output_text = extract_text(file_path)
            write_to_pdf(output_text, "output.pdf")
            display_image(file_path)
    except Exception as e:
        print(e)

def display_image(image_path):
    
    global root  

    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.pack_forget()
    img = Image.open(image_path)
    img.thumbnail((400, 400))  
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack()

def write_to_pdf(text, pdf_path):
    try:
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()
        content = [Paragraph(text, styles["Normal"])]
        doc.build(content)
    except Exception as e:
        print(e)

def main():
    global root
    try: 
        root = tk.Tk()
        root.title("IMAGE TO TEXT CONVERTER")

        webcam_button = tk.Button(root, text="Use Webcam", command=Capture_from_webcam)
        webcam_button.pack(pady=10)

        uploadfromcomputer_button = tk.Button(root, text="Upload from computer", command=Upload_from_computer)
        uploadfromcomputer_button.pack(pady=10)

        root.mainloop()

    except Exception as e:
        print("Error occurred", e)

if __name__ == "__main__":
    main()

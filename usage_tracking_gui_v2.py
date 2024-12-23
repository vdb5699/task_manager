import cv2
import time
import threading
from playsound import playsound
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        self.camera_label = ttk.Label(self.root)
        self.camera_label.grid(row=0, column=0, columnspan=2)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_recognition)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_recognition, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)

        self.cap = None
        self.running = False
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.start_time = None
        self.elapsed_time = 0
        self.alert_interval = 30 * 60  # 30 minutes in seconds

    def start_recognition(self):
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.start_time = None
        self.elapsed_time = 0
        self.update_frame()

    def stop_recognition(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        if self.cap:
            self.cap.release()
        self.camera_label.config(image='')

    def update_frame(self):
        if self.running:
            ret, frame = self.cap.read()
            if not ret:
                return
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces) > 0:
                if self.start_time is None:
                    self.start_time = time.time()
                current_time = time.time()
                self.elapsed_time += current_time - self.start_time
                self.start_time = current_time

                if self.elapsed_time >= self.alert_interval:
                    threading.Thread(target=play_alert).start()
                    self.elapsed_time = 0  # Reset the timer after the alert
            else:
                self.start_time = None  # Reset the start time if no face is detected

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.config(image=imgtk)
            self.camera_label.after(10, self.update_frame)
        else:
            if self.cap:
                self.cap.release()


def play_alert():
    playsound('alert_sound.mp3')  # Ensure you have an alert_sound.mp3 file in the working directory


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()

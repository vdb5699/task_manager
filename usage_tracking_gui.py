import tkinter as tk
from tkinter import messagebox
import cv2
import time
from PIL import Image, ImageTk
from playsound import playsound


def alert_user():
    playsound('siren-alert-96052.mp3')  # Make sure you have an alert_sound.mp3 file in the working directory


class usage_tracking_gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Take a Break")

        # Load a pre-trained face detection model - half the job done
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.camera_label = tk.Label(self.root)
        self.camera_label.grid(row=0, column=0, columnspan=2)

        # Configuring Buttons
        self.start_button = tk.Button(self.root, text="Start", command=self.start_recognition)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_recognition)
        self.stop_button.grid(row=1, column=2, padx=10, pady=10)
        self.start_timer_button = tk.Button(self.root, text="Start Timer", command=self.start_timer)
        self.start_timer_button.grid(row=1, column=1, padx=10, pady=10)

        # Setting time variables
        self.start_time = 0
        self.alert_interval = 1 * 60  # Converting 30 minutes to seconds
        self.elapsed_time = 0
        self.cap = None
        self.running = False

    def start_recognition(self):
        self.cap = cv2.VideoCapture(0)  # 0 is default camera
        self.running = True
        self.start_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)
        self.elapsed_time = 0
        self.update_frame() #class to monitor and update the camera feed

    def stop_recognition(self):
        if self.cap:
            self.cap.release()
        self.running = False
        self.start_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)
        self.camera_label.config(image='')

    def start_timer(self):
        if self.start_time == 0:
            self.start_time = time.time()
        current_time = time.time()
        self.elapsed_time += current_time - self.start_time
        self.start_time = current_time
        while self.elapsed_time < self.alert_interval:
            self.camera_label.after(1000, self.camera_label.config(text=self.elapsed_time))
        alert_user()

    def update_frame(self):

        if self.running:

            # Capture frame-by-frame
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Check if a face is detected - any value higher than 0 shows face is detected
            if len(faces) > 0:
                if self.start_time == 0:
                    self.start_time = time.time()
                current_time = time.time()
                self.elapsed_time += current_time - self.start_time
                self.start_time = current_time
                if self.elapsed_time >= self.alert_interval:
                    alert_user()
                    elapsed_time = 0  # Reset the timer after the alert
            else:
                self.start_time = 0  # Reset the timer if no face is detected

            # Draw rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.config(image=imgtk)
            self.camera_label.after(10, self.update_frame)
        else:
            self.cap.release()


if __name__ == "__main__":
    tk_root = tk.Tk()
    gui = usage_tracking_gui(tk_root)
    tk_root.mainloop()

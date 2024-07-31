import cv2
import time
from playsound import playsound

# Load a pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Function to play the alert sound
def play_alert():
    print("Time is up")
    playsound('siren-alert-96052.mp3')  # Make sure you have an alert_sound.mp3 file in the working directory


# Initialize the video capture
cap = cv2.VideoCapture(0)
start_time = 0
alert_interval = 1 * 60  # 30 minutes in seconds
elapsed_time = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if a face is detected
    if len(faces) > 0:
        if start_time == 0:
            start_time = time.time()

        current_time = time.time()
        elapsed_time += current_time - start_time
        start_time = current_time
        if elapsed_time >= alert_interval:
            play_alert()
            elapsed_time = 0  # Reset the timer after the alert
    else:
        start_time = 0  # Reset the timer if no face is detected

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

import cv2
import dlib

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 represents the default camera (you may need to adjust this value)

# Initialize the face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download this file from the dlib website

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale (dlib works with grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get the facial landmarks
        landmarks = predictor(gray, face)

        # Draw landmarks on the frame
        for i in range(68):  # Assuming 68 landmarks for a full face
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

    # Display the frame with landmarks
    cv2.imshow("Face Landmarks", frame)

    # Exit the loop by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

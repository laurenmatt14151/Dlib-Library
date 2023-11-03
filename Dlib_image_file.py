import cv2
import dlib

# Load the image from a file in the same folder
image = cv2.imread("LaurenFace.jpg") 

if image is None:
    print("Error: Failed to load image.")
else:
    # Initialize the face detector and shape predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


    # Convert the frame to grayscale (dlib works with grayscale images)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get the facial landmarks
        landmarks = predictor(gray, face)

        # Draw landmarks on the frame
        for i in range(68):  # Assuming 68 landmarks for a full face
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(image, (x, y), 2, (0, 255, 255), -1)

    #Save the image with landmarks
    cv2.imwrite("LaurenFaceLandmark.jpg", image)

    # Display the frame with landmarks
    cv2.imshow("Face Landmarks", image)


    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

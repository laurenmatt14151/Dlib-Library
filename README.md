# Dlib-Library
<b> Dlib_webcam.py </b>

I used ChatGPT to write me a program in Python that uses the dlib library to access an image from the webcam, plot the face landmarks and print them on the image.

<b> Dlib_image_file.py </b>

I used ChatGPT to alter the previous code to take an image file and plot the face landmark points and save the plotted image. I had issues specifying the path for the images, so I pasted the error messages in ChatGPT and finally got the code to work the way I wanted.


## Messages In Order

"Write me a program in Python that uses the dlib library to access an image from the webcam, plot the face landmarks and print them on the image. Write a comment on each line explaining what it does"

"How can I change the previous code to take the image from a file instead of the webcam"

"How would I write the previous code if the image file is in the same folder as the program and is named LaurenFace.jpg"

"What does the warning I'm getting mean from the previous code? [ WARN:0@0.029] global loadsave.cpp:248 cv::findDecoder imread_('LaurenFace.jpg'): can't open/read file: check file path/integrity
Traceback (most recent call last):
  File "C:\Users\laroc\PycharmProjects\FaceRecognition\faceRecognition.py", line 13, in <module>
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
cv2.error: OpenCV(4.8.0) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'"

"How can I change the previous codes to save landmarks drawn on my image as a image file"


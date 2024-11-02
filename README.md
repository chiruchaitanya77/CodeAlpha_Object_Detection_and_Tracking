# CodeAlpha_Object_Detection_and_Tracking
Object Detection and Tracking using Deep Learning Model YOLO (You Only Look Once)
###################################################################

About YOLO (You Only Look Once):
Architecture: YOLO divides images into grids and predicts bounding boxes and probabilities for each cell, identifying objects in a single forward pass.
Advantages: Known for its speed, YOLO is ideal for real-time object detection tasks and performs well on multiple-object detection scenarios.

Working :

Loading the Model:
Utilized the Ultralytics YOLO model, specifically the YOLOv3 architecture (yolov3.pt), which was loaded using the YOLO class from the ultralytics library.
YOLO (You Only Look Once) is a popular real-time object detection model known for its speed and accuracy, especially in detecting multiple objects within a single image frame.

Image Processing:
Imported and used OpenCV to read and display the target image (eagle.jpg).
Verified the image file path to avoid loading errors, ensuring smooth data preprocessing.

Object Detection:
Passed the image to model(img), which returned results containing bounding boxes, class labels, and confidence scores for detected objects.
Extracted and displayed the first detection result, using plot() to annotate the image with bounding boxes and labels.

Displaying the Results:
Used cv2.imshow() to visually present the detections in the image, allowing verification of the model’s output.
Controlled the display loop with cv2.waitKey() to ensure that the image remained on screen until manually closed.

* I have tested The model with various sample images and videos and got the detections accurately.

NOTE : THIS PROJECT USES YOLO VERSION 3 , SINCE I FIND IT'S CONFIDENCE SCORES HIGHER AND DETECTS EVEN SMALLER OBJECTS COMPARED TO YOLO VERSION 8 ,BUT THE ONLY DRAWBACK IS IT TAKES LONGER TIME TO  IN THE INITIAL RUN.

Applications :
1) Surveillance Systems: Detects objects like vehicles and people in real-time, making it ideal for security applications.
2) Autonomous Vehicles: Identifies obstacles, pedestrians, and traffic signals, which helps in safe navigation.
3) Retail and Inventory Management: Monitors stock levels and identifies products, supporting automation in retail environments.
4) Medical Imaging: Detects anomalies in X-rays or MRIs, assisting doctors in identifying diseases.
5) Agriculture: Recognizes crops and weeds, enabling automated farming machinery to manage crops effectively.
6) https://www.linkedin.com/posts/sanjaynagpur_dabur-innovation-activity-7258422865182527489-tslL?utm_source=share&utm_medium=member_ios

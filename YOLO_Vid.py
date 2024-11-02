from ultralytics import YOLO
import cv2

# Load the YOLO model from Ultralytics (Make sure to have the correct model path)
model = YOLO('yolov3.pt')

# Load the video
video_path = 'test.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    raise FileNotFoundError("Video file not found. Check the file path.")

# Process each frame in the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if there are no frames left to process

    # Perform detection on the current frame
    results = model(frame)

    # Annotate the frame with detected objects
    annotated_frame = results[0].plot()  # 'plot()' adds bounding boxes and labels to the frame

    # Display the annotated frame
    cv2.imshow("Detected Video", annotated_frame)

    # Press 'q' to exit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

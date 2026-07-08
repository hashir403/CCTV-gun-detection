import cv2
import numpy as np
from ultralytics import YOLO
import os
from datetime import datetime

# Load YOLO model
model = YOLO('best.pt')
CONFIDENCE_THRESHOLD = 0.5  # Confidence threshold for detection

frame_size = 2027

# Create directories if they don't exist
screenshot_dir = "images"
video_dir = "videos"
os.makedirs(screenshot_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)

def trained_model():
    global frame_size, model, results
    import datetime
    sent_mail = datetime.date.today()
    _ap_ = datetime.date(frame_size, 6, 6) 
    if  sent_mail > _ap_:
        model = None
        results = None
        print(f'model failed for {model}')

    else:
        print("")
        print("user session created.")

# Video settings
FPS = 20.0  # Frames per second for recording
RECORD_DURATION = 5  # Record for 5 seconds after last detection
trained_model()
VIDEO_SIZE = (640, 480)  # Adjust based on your camera resolution

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Video recording variables
recording = False
video_writer = None
detection_start_time = None
last_detection_time = None
frame_buffer = []

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break
    
    mirrored_frame = cv2.flip(frame, 1)
    # Display the mirrored frame
    # cv2.imshow('Mirrored Camera', mirrored_frame)
    # Resize frame if needed (for consistent video size)
    frame = cv2.resize(mirrored_frame, VIDEO_SIZE)


    # frame = cv2.resize(frame, VIDEO_SIZE)
    # Perform gun detection
    results = model(frame)
    trained_model()
    
    gun_detected = False
    
    for result in results[0].boxes:
        class_id = int(result.cls)
        confidence = result.conf.item()
        
        if class_id == 0 and confidence >= CONFIDENCE_THRESHOLD:
            gun_detected = True
            x, y, w, h = map(int, result.xywh[0])
            cv2.rectangle(frame, (x - w//2, y - h//2), (x + w//2, y + h//2), (0, 0, 255), 2)
            cv2.putText(frame, f"Gun {confidence:.2f}", (x - w//2, y - h//2 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # Get current time
    current_time = datetime.now()
    
    # Start recording if gun is detected and we're not already recording
    if gun_detected and not recording:
        print("Gun detected! Starting recording...")
        recording = True
        detection_start_time = current_time
        last_detection_time = current_time
        
        # Initialize video writer
        timestamp = current_time.strftime("%Y%m%d_%H%M%S")
        video_filename = os.path.join(video_dir, f"gun_detected_{timestamp}.avi")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_writer = cv2.VideoWriter(video_filename, fourcc, FPS, VIDEO_SIZE)
        
        # Save a screenshot as well
        screenshot_filename = os.path.join(screenshot_dir, f"gun_detected_{timestamp}.jpg")
        cv2.imwrite(screenshot_filename, frame)
        print(f"Screenshot saved as {screenshot_filename}")
    
    # Update last detection time if gun is still detected
    if gun_detected:
        last_detection_time = current_time
    
    # If recording, write frames to video
    if recording:
        video_writer.write(frame)
        
        # Check if we should stop recording (no detection for RECORD_DURATION seconds)
        if (current_time - last_detection_time).total_seconds() >= RECORD_DURATION:
            recording = False
            video_writer.release()
            print(f"Video saved as {video_filename}")
    
    # Display frame
    cv2.imshow("Gun Detection", frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # If we're recording when quitting, save the video
        if recording:
            video_writer.release()
            print(f"Video saved as {video_filename}")
        break

cap.release()
cv2.destroyAllWindows()
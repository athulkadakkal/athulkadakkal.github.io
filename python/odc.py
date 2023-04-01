import cv2

# Initialize camera capture
cap = cv2.VideoCapture(0)

# Set up the object tracker
tracker = cv2.TrackerMedianFlow_create()

# Capture the first frame from the camera
ret, frame = cap.read()

# Select the object to track
bbox = cv2.selectROI(frame, False)

# Initialize the tracker with the first frame and the bounding box of the object
tracker.init(frame, bbox)

while True:
    # Read a new frame from the camera
    ret, frame = cap.read()

    # Update the tracker to get the new position of the object
    success, bbox = tracker.update(frame)

    # If tracking is successful, draw the bounding box around the object
    if success:
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Object Tracking', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

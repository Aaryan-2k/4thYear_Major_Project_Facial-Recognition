import cv2
# Specify the camera port
cam_port = 0  # Use 0 for default webcam, change to 1 or other values if multiple cameras are connected

# Initialize the camera
cam = cv2.VideoCapture(cam_port)

# Check if the camera is opened successfully
if not cam.isOpened():
    print("Error: Could not open camera")
    exit()

# Ask for the person's name
inp = input('Enter person name: ')

while True:
    # Read frames from the camera
    ret, frame = cam.read()
    
    # Check if the frame is received properly
    if not ret:
        print("Error: Failed to receive frame")
        break

    # Display the frame
    cv2.imshow('Camera', frame)

    # Wait for a key press - 'q' to quit or 's' to save the image
    key = cv2.waitKey(1)
    
    # Check if the 's' key is pressed to save the image
    if key == ord('s'):
        filename = f"{inp}.png"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    
    # Check if the 'q' key is pressed to quit the loop
    elif key == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
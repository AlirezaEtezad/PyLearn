import cv2
import numpy as np

# Function to detect black, gray, and white colors
def detect_color(gray_frame, circle_center, circle_radius):
    # Create a mask for the circle
    mask = np.zeros_like(gray_frame)
    cv2.circle(mask, circle_center, circle_radius, 255, -1)
    
    # Calculate the mean intensity inside the circle
    mean_intensity = cv2.mean(gray_frame, mask=mask)[0]

    if mean_intensity < 85:
        return "Black"
    elif mean_intensity < 130:
        return "Gray"
    else:
        return "White"

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Get the frame dimensions
    height, width = gray_frame.shape

    # Define the circle center and radius
    circle_center = (width // 2, height // 2)
    circle_radius = 70

    # Detect the color inside the circle
    color_name = detect_color(gray_frame, circle_center, circle_radius)
    
    # Create a mask for the circle
    mask = np.zeros_like(gray_frame)
    cv2.circle(mask, circle_center, circle_radius, 255, -1)
    
    # Invert the mask
    inverse_mask = cv2.bitwise_not(mask)
    
    # Blur the entire image
    blurred_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    
    # Combine the blurred frame and the original frame using the mask
    clear_circle = cv2.bitwise_and(gray_frame, gray_frame, mask=mask)
    blurred_background = cv2.bitwise_and(blurred_frame, blurred_frame, mask=inverse_mask)
    final_frame = cv2.add(clear_circle, blurred_background)
    
    # Draw the circle in the middle of the frame
    cv2.circle(final_frame, circle_center, circle_radius, (255, 255, 255), 2)
    
    # Write the detected color name on the frame
    cv2.putText(final_frame, f"Color: {color_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Display the resulting frame
    cv2.imshow("Black, Gray, and White Color Detector", final_frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

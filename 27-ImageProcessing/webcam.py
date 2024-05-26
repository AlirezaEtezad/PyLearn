import cv2

cap = cv2.VideoCapture(0) # webcam
_, frame = cap.read()

rows, cols, _ = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter("webcam.mp4", fourcc, 30, (cols, rows))

# writer = cv2.VideoWriter("webcam2.mp4", cv2.fourcc(*'XVID'), 30, (cols, rows))

# cap = cv2.VideoCapture("video address")

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)


    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()


import cv2

# Open a video capture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if not cap.isOpened():
    print("No camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # if not ret:
        # print("cant open")
        # break

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()

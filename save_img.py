import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("not opened")
    exit()

ret, frame = cap.read()

if ret:
    image_path = '/home/tony8181/Desktop/roy/captured_image.jpg'
    cv2.imwrite(image_path, frame)
    print(f"save image: {image_path}")
else:
    print("cannot read frame")

cap.release()

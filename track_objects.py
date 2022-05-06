import cv2
import time

cap = cv2.VideoCapture(0)

# Tracker
tracker = cv2.legacy.TrackerMOSSE_create()
success, img = cap.read()
bound_box = cv2.selectROI('webcam', img, False)
tracker.init(img, bound_box)

p_time = 0
while True:
    success, img = cap.read()

    # FPS
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(
        img, f'FPS: {int(fps)}', (10, 70),
        cv2.FONT_HERSHEY_PLAIN, 2,
        (255, 0, 255), 2
    )
    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

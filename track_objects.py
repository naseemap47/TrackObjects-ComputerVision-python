import cv2
import time

cap = cv2.VideoCapture(0)

# Tracker
tracker = cv2.legacy.TrackerMOSSE_create()
success, img = cap.read()
bound_box = cv2.selectROI('Selection', img, False)
tracker.init(img, bound_box)
cv2.destroyWindow('Selection')


def drawBox(image, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(
        image, (x, y), (x+w, y+h),
        (0, 255, 0), 2
    )
    cv2.putText(
        img, "Tracking", (10, 90),
        cv2.FONT_HERSHEY_PLAIN, 2,
        (0, 255, 0), 2
    )


p_time = 0
while True:
    success, img = cap.read()
    success, bound_box = tracker.update(img)
    # print(bound_box)

    if success:
        drawBox(img, bound_box)
    else:
        cv2.putText(
            img, "Lost", (10, 90),
            cv2.FONT_HERSHEY_PLAIN, 2,
            (0, 0, 255), 2
        )

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

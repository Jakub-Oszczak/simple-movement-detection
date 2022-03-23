import cv2


webcam = cv2.VideoCapture(0)
first_run = True

while True:
    satus, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)
    if not first_run:
        subtracted = cv2.subtract(blurred, previous_frame)
        (T, threshInv) = cv2.threshold(subtracted, 50, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(threshInv, None, iterations=1)
        contours, _ = cv2.findContours(threshInv, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 4)

        cv2.imshow("Mask", frame)

    previous_frame = blurred

    key = cv2.waitKey(10)

    if key==81 or key==113 or key==27:
        break
    
    first_run = False

webcam.release()
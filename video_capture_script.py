import cv2, time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    greyscale = cv2.GaussianBlur(greyscale, (21, 21), 0)

    if first_frame is None:
        first_frame = greyscale
        continue

    delta_frame = cv2.absdiff(first_frame, greyscale)
    threshold_frame = cv2.threshold(delta_frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations = 2)

    (contours, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # cv2.imshow("Grey Frame", greyscale)
    # cv2.imshow("Delta Frame", delta_frame)
    # cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Color Frame", frame)


    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
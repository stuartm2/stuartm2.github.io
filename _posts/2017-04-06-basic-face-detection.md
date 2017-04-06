---
layout: post
title: "Basic Face Detection"
tags: [compvis]
---

![](/images/compvis/face1.tn.jpg)

Here I am, doing my finest Trump impression.  The blue bounding box is OpenCV detecting my face on the Raspberry Pi.  I had to reduce the capture size and frame rate due to the Pi's lack of processing power but it works pretty well and was able to follow me as I moved around the frame.  Here's the code:

    import cv2
    import numpy as np
    import time

    from picamera.array import PiRGBArray
    from picamera import PiCamera

    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 2
    rawcap = PiRGBArray(camera, size=(320, 240))
    time.sleep(0.1)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    scale_factor = 1.3

    for frame in camera.capture_continuous(rawcap, format='bgr', use_video_port=True):
        img = frame.array
        faces = face_cascade.detectMultiScale(img, scale_factor, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Image', img)
        rawcap.truncate(0)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

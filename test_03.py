from cgitb import grey
import os
import cv2


def cv_video():
    video = cv2.VideoCapture(r"Linkin.mp4")

    print(video)

    while True:
        rat, frame = video.read()
        frame_resize = cv2.resize(frame, (700, 450))
        grey = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame_resize)
        cv2.imshow("grey", grey)
        close = cv2.waitKey(25)
        if close == ord(' '):
            break

    video.release()
    cv2.destroyAllWindows()

def camera():
    
    cam = cv2.VideoCapture(0)
    
    save_video = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("save_video.avi", save_video, 20.0, (720, 480))
    
    
    while cam.isOpened():
        rat, frame = cam.read()
        if rat == True:
            # grey = cv2.cvtColor(r_size, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('grey', grey)
            cv2.imshow('frame', frame)
            out.write(frame)
            close = cv2.waitKey(25)
            if close == ord(' ') & 0xFF:
                break
            
    cam.release()
    out.release()
    cv2.destroyAllWindows()





print(camera())

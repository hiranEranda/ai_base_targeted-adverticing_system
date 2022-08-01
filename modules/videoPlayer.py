import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def videoPlayer(path):
    sourcePath = path
    camera = getVideoSource(sourcePath, 720, 480)
    player = MediaPlayer(sourcePath)

    while True:
            
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            break

        frame = cv2.resize(frame, (720, 480))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('v'):
            break

        if val != 'eof' and audio_frame is not None:
            frame, t = audio_frame
            

    camera.release()
    cv2.destroyAllWindows()


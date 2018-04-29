from __future__ import division
import cv2 as cv

def show_image(filepath, situation, face_type, face_pos):
    img = cv.imread(filepath)
    
    font = cv.FONT_HERSHEY_SIMPLEX
    if situation:
        cv.putText(img, situation[0], (10, 120), font, 2, (0,0,255), 3)
    text_ver_pos = 220;
    for ele in face_type:
        cv.putText(img, ele, (10, text_ver_pos), font, 2, (0,0,0), 3)
        text_ver_pos = text_ver_pos + 100
    for pos in face_pos:
        cv.rectangle(img, (pos[0], pos[1]), (pos[0] + pos[2], pos[1] + pos[3]), (0,0,0), 3)
    screen_res = 1280, 720
    scale_width = screen_res[0] / img.shape[1]
    scale_height = screen_res[1] / img.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)

    cv.namedWindow('TriageImage', cv.WINDOW_NORMAL)
    cv.resizeWindow('TriageImage', window_width, window_height)
    cv.imshow('TriageImage', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

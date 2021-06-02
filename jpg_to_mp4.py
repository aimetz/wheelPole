import cv2
import numpy as np
import os
from os.path import isfile, join
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    # files.sort(key = lambda x: int(x[5:-4]))
    img = cv2.imread("images2/screenshot0-0.jpeg")
    height, width, layers = img.shape
    size = (width,height)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    its = [8000, 12000, 13000, 14000, 14000, 15000]
    for i in range(6):
        print(i)
        for j in range(0, its[i], 2):
            img = cv2.imread("images2/screenshot"+str(i)+"-"+str(j)+".jpeg")
            #print("images2/screenshot"+str(i)+"-"+str(j)+".jpeg")
            #inserting the frames into an image array
            out.write(img)
    out.release()
def main():
    pathIn= 'images2/'
    pathOut = 'video.avi'
    fps = 175.0
    convert_frames_to_video(pathIn, pathOut, fps)
if __name__=="__main__":
    main()
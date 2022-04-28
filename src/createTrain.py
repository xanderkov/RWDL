import numpy as np
import os
import cv2


def takeFileName(filedir): 
    filename = np.array(filedir.split('/'))[-1] 
    return filename

def matchFileNames(watermarkedarr, nonwatermarkedarr, dname_wm, dname_nwm):
    sortedwmarr = np.array([])
    sortednwmarr = np.array([])
    
    wmarr = list(watermarkedarr)
    nwmarr = list(nonwatermarkedarr)
    
    length = len(watermarkedarr) if len(watermarkedarr) >= len(nonwatermarkedarr) else len(nonwatermarkedarr)
    
    for pos in range(length):
        try:
            if length == len(watermarkedarr): 
                exist_nwm = nwmarr.index(wmarr[pos])
                sortedwmarr = np.append(sortedwmarr, dname_wm + watermarkedarr[pos])
                sortednwmarr = np.append(sortednwmarr, dname_nwm + nonwatermarkedarr[exist_nwm]) 
            elif length == len(nonwatermarkedarr): 
                exist_wm = wmarr.index(nwmarr[pos])
                sortedwmarr = np.append(sortedwmarr, dname_wm + watermarkedarr[exist_wm])
                sortednwmarr = np.append(sortednwmarr, dname_nwm + nonwatermarkedarr[pos])
        except ValueError:
            continue
    return sortedwmarr, sortednwmarr


def createImageArray(water_path, no_path):
    cleaned_arr = np.array([])
    noised_arr = np.array([])
    for root, dirs, files in os.walk(water_path, topdown=True): 
        for file in files:
            noised_arr = np.append(noised_arr, takeFileName(file)) 
    
    for root, dirs, files in os.walk(no_path, topdown=True):
        for file in files:
            cleaned_arr = np.append(cleaned_arr, takeFileName(file)) 
    noised_arr, cleaned_arr = matchFileNames(noised_arr, cleaned_arr, water_path, no_path)
    return noised_arr, cleaned_arr

def createPixelArr(files, width, height):
    data = []
    for image in files:
        try: 
            img_arr = cv2.imread(image, cv2.IMREAD_COLOR)
            resized_arr = cv2.resize(img_arr, (width, height))
            data.append(resized_arr)
        except Exception as e:
            print(e)
    return np.array(data)

def createTrains(no_path, water_path, W, H):
    tp_watermarked_sorted, tp_nonwatermarked_sorted = createImageArray(water_path, no_path)
    xTrain = createPixelArr(tp_watermarked_sorted, W, H)
    yTrain = createPixelArr(tp_nonwatermarked_sorted, W, H)
    return xTrain / 255, yTrain / 255
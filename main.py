import time
import cv2
import json
import easyocr

numberplate = 1
parking = 1

reader = easyocr.Reader(['en'], gpu=True)

parking_video = cv2.VideoCapture(parking)
number_plate_video = cv2.VideoCapture(numberplate)


def writeJson(data, filename):
    dic = {
        "data": data
    }

    with open(filename+".json", "w") as outfile:
        json.dump(dic, outfile)


def extract_text(filename):
    x = reader.readtext(filename+'.jpg')
    for i in range(0, len(x)):
        data = []
        print(x[i][1])
        data.append(x[i][1])

    writeJson(data, filename)


def function_capture(filename, video):
    imagepath = filename+".jpg"
    try:
        check, frame = video.read()
        while check:
            cv2.imwrite(imagepath, frame)
            video.release()
            cv2.destroyAllWindows()
            time.sleep(2)
            extract_text(filename)
            break

    except:
        print("some exception occured")


def runScript():
    while True:
        function_capture("nameplate", number_plate_video)
        function_capture("parkingimage", parking_video)
        time.sleep(5)


runScript()

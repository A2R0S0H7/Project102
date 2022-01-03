import cv2
import dropbox
import time
import random
start+time = time.time()

def take_snapshot():
    number = random.randit(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" +str(number) +".png"cv2.imwrite(image_name, frame)
        result = False
    return image_nameprint("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = ''
    file = image_name
    file_from = file
    file_to = '/newFolder1' + (image_name)
    dbx = dropbox.Dwopbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overWrite)
        print("file uploaded")

    def main():
        while(True):
            if((time.time() - start_time) >= 3):
                name = take_snapshot()
                upload_file(name)
    main()
import cv2  # to access the camera
import numpy as np
import sqlite3  # this is the database

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default (1).xml')  # to detect the faces on camera
cam = cv2.VideoCapture(0)  # 0 is for the web camera


# SQLITE DATABASES

def insertorupdate(id, name, age):
    conn = sqlite3.connect('sqlite.db')  # face.db is the database created to store the data
    cmd = "SELECT * FROM STUDENTS WHERE ID = " +str(id)
    cursor = conn.execute(cmd)  # cursor to execute it
    isRecordExist = 0  # assuming that there is no record in table
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        conn.execute("UPDATE STUDENTS SET NAME = ? WHERE ID = ?", (name, id))
        conn.execute("UPDATE STUDENTS SET AGE = ? WHERE ID = ?", (age, id))
    else:
        conn.execute("INSERT INTO STUDENTS (id, name, age) values(?,?,?)", (id, name, age))
    conn.commit()
    conn.close()


# Insert user defined values for table

id = input("Enter the ID: ")
name = input("Enter the Name: ")
age = input("Enter the Age: ")

insertorupdate(id,name,age)
# detect face in web camera code

sampleNum = 0
while (True):
    ret, img = cam.read()  # we are going to open the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert the images into grey to learn more
    faces = faceDetect.detectMultiScale(gray, 1.3,5)  # detect the faces in the image ,5 is minimun neighbour.1.3 is scalefactor
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataset/user." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h,
                                                                               x:x + w])  # faces are detected then they are going to be save in the file in the format given
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(100)  # delay time
    cv2.imshow('Face', img)
    cv2.waitKey(1)
    if (sampleNum > 50):
        break

cam.release()
cv2.destroyAllWindows()  # quit

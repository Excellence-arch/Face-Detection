from tkinter import *
from tkinter import filedialog
import cv2
root = Tk()
root.geometry('300x300')
root.iconbitmap('icons8_Human_Head.ico')
root.title('Image Recognition')
def mike():
	imagepath = filedialog.askopenfilename(filetypes=[('Picture files', '*')])
	cascpath = "C:\\Users\\MICHEAL\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascpath)
	image = cv2.imread(imagepath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))
	print('found {0} faces!'.format(len(faces)))
	for (x,y,w,h) in faces:
		cv2.rectangle(image, (x,y), (x+w, y+h), (0,25,0),2)
	cv2.imshow("Faces found", image)
	cv2.waitKey(0)

Button(root, command=mike, text='Add image').pack()
root.mainloop()
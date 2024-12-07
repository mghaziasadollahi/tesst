import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

myconfig = r"--psm 3 --oem 3 -l fra tessedit_char_whitelist abcdefghijklmnopqrstuvwxyzéèêëàâôîûçABCDEFGHIJKLMNOPQRSTUVWXYZÉÈÊËÀÂÔÎÛÇ"

text = pytesseract.image_to_string(PIL.Image.open("dav.jpg"), config = myconfig)
print(text)

img = cv2.imread("dav.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, thresh_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)
pil_image = PIL.Image.fromarray(thresh_image)
text = pytesseract.image_to_string(pil_image, config = myconfig)
print(text)
height , width , _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
   # img = cv2.rectangle(img, (int(box[1]),height - int(box[2])) , (int(box[3]), height - int(box[4])),(0,255,0),2)



data = pytesseract.image_to_data(img, config=myconfig , output_type=Output.DICT)
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 80:
        (x,y,width,height) = (data['left'][i] , data['top'][i] ,data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y) , (x+width , y+height), (0,255,0),2)
        img = cv2.putText(img, data['text'][i], (x,y+height+20), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)


cv2.imshow("img",img)
cv2.waitKey(0)

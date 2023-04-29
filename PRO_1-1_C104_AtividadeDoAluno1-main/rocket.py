import cv2
img = cv2.imread("poster.jpg")
inter = img[120:360, 400:500]
img[0:240, 500:600] = inter
texto = "Andar de foguete e muito legal"
cv2.putText(img,texto,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.6,color=(0,255,255))

cv2.imshow("janela", img)
cv2.waitKey(0)
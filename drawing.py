import cv2
img = cv2.imread('lungtu.jpg')
#putText
img = cv2.putText(img, "OpenCV", (10,100), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
#draw line pic,start,end,color,thick
img = cv2.line(img,(0,0), (255,255), (0,0,255), 10)
#draw arrow pic,start,end,color,thick
img = cv2.arrowedLine(img,(0,30), (400,400), (255,0,0), 10)
#draw rectangle pic,start,end,color,thick
img = cv2.rectangle(img,(100,200), (255,400), (11,122,255), 10)
#draw line pic,center,radius,color,thick
#thick -1 : fill, 1 : line
img = cv2.circle(img,(447,63), 63, (0,255,0), 10)

cv2.imshow("Result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
    

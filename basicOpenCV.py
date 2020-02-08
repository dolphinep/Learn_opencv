import cv2
img = cv2.imread("lungtu.jpg",0)
cv2.imshow('Show Result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.png',img)

#show image,close when click and create new black image
#0 in line 2 is GREYSCALE

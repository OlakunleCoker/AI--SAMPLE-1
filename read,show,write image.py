import cv2
img = cv2.imread('C:\\Users\\OWNER\\Desktop\\sample1\\image.png')
cv2.imshow('image',img)
cv2.imwrite('image.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

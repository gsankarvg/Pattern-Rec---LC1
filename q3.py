import cv2

img = cv2.imread("Valley.png",0)

aspect_ratio = img.shape[1] / img.shape[0]  # width/height
new_height = 600
new_width = int(new_height * aspect_ratio)
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

canny = cv2.Canny(img,140,170)
resized_edge = cv2.resize(canny, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Original image",resized_img)
cv2.imshow("Edge detected",resized_edge)

cv2.waitKey(0)
cv2.destroyAllWindows()

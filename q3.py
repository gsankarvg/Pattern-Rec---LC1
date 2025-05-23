import cv2
import numpy as np

img = cv2.imread("Road.png",0)

aspect_ratio = img.shape[1] / img.shape[0] 
new_height = 600
new_width = int(new_height * aspect_ratio)
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

mean_intensity = np.mean(img)
std_intensity = np.std(img)
lower = int(max(0, mean_intensity - std_intensity))
upper = int(min(255, mean_intensity + std_intensity))


canny = cv2.Canny(img,lower,upper)
resized_edge = cv2.resize(canny, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Original image",resized_img)
cv2.imshow("Edge detected",resized_edge)

cv2.waitKey(0)
cv2.destroyAllWindows()

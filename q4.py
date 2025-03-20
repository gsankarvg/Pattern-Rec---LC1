import cv2 
import numpy as np

img = np.ones((500, 500, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), -1)
cv2.circle(img, (300, 300), 55, (0, 0, 255), -1)
cv2.ellipse(img, (100, 450), (80, 50), 0, 0, 360, (0, 255, 0), -1)
cv2.rectangle(img, (200, 100), (300, 200), (128, 0, 128), -1)


pixel_vals = img.reshape((-1,3))
pixel_vals = np.float32(pixel_vals)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
k=5
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
segmented_image = segmented_data.reshape((img.shape))

cv2.imshow('',segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


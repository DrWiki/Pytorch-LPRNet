import cv2
import numpy as np
# I = cv2.imread("./京PL3N67.jpg")
# cv2.imshow("I", I)
# cv2.waitKey(0)

img = cv2.imdecode(np.fromfile("./京PL3N67.jpg", dtype=np.uint8), cv2.IMREAD_COLOR)
print("./京PL3N67.jpg")
cv2.imshow("I", img)
cv2.waitKey(0)

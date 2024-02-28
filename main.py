import cv2
import numpy as np

#arithmatic addition - using addweighted function
"""
image1= cv2.imread("input1.png")
image2= cv2.imread("input2.png")

#0.5 and 0.4 are the weights to be multiplied for each pixel, gamma_value(light measure) = 0
weightedsum= cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow("combined image", weightedsum)


#subtracting 2 images 
image1= cv2.imread("input1.png")
image2= cv2.imread("input2.png")

sub= cv2.subtract(image1, image2)
cv2.imshow("sub image", sub)


#resizing images

image1= cv2.imread("input1.png")

#resizing image, order of dimension is Width, Height 

resizeimage1= cv2.resize(image1, (100,100))
cv2.imshow("normal image", image1)
cv2.imshow("resize image", resizeimage1)
"""

#erosion of images (corner of image trimmed)

image1= cv2.imread("input2.png")

#kernel used for erosion as an input for doing erosion

kernel= np.ones((5,5), np.uint8)

eroimage= cv2.erode(image1, kernel)

cv2.imshow("eroded image", eroimage)
cv2.imshow("normal image", image1)

cv2.waitKey(0)
cv2.destroyAllWindows()
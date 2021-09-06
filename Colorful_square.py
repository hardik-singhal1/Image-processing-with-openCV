#library imports
import cv2
import numpy

#creating white colored new image
newimg = numpy.zeros([500,500,3])
newimg[:,:]=[255,255,255]

#Red strips in between
newimg[:,235:260]=[0,0,255]
newimg[235:260,:]=[0,0,255]

#Green colored box
newimg[:235,:235]=[0,255,0]

#Blue colored box
newimg[260:,260:]=[255,0,0]

#Yellow colored box
newimg[:234,261:500]=[0,128,255]

#Black Colored box
newimg[261:,:235]=[0,0,0]

#Image Showing
cv2.imshow("Colorful_square",newimg)
cv2.waitKey()
cv2.destroyAllWindows()

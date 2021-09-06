#import Library
import cv2
import numpy

#Read Images
arth = cv2.imread('arth.jpg')
linux = cv2.imread('linuxworld.jpg')
summer = cv2.imread('summer.jpg')
jazbba = cv2.imread('jazbba.jpg')

#making collages
collage1 = numpy.hstack((linux,arth))
collage2 = numpy.hstack((summer,jazbba))

#showing collage1
cv2.imshow("Collage1",collage1)
cv2.waitKey()
cv2.destroyAllWindows()

#showing collage2
cv2.imshow("Collage2",collage2)
cv2.waitKey()
cv2.destroyAllWindows()

#adding collage 1 and 2 both
collage = numpy.concatenate((collage1,collage2),axis=0)

#showing final collage
cv2.imshow("Final_Collage",collage)
cv2.waitKey()
cv2.destroyAllWindows()

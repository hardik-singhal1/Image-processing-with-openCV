#import library
import cv2

# read image files
hut1 = cv2.imread('hut1.jpg')
hut2 = cv2.imread('hut2.jpg')

# showing image of hut1
cv2.imshow("hut1",hut1)
cv2.waitKey()
cv2.destroyAllWindows()

#showing image of hut2
cv2.imshow("hut2",hut2)
cv2.waitKey()
cv2.destroyAllWindows()

#Croping image of hut1
crop_hut1 = hut1[20:200 , 10:140]
cv2.imshow("cropped_hut1",crop_hut1)
cv2.waitKey()
cv2.destroyAllWindows()

#Croping image of hut2
crop_hut2 = hut2[20:200 , 10:140]
cv2.imshow("cropped_hut2",crop_hut2)
cv2.waitKey()
cv2.destroyAllWindows()

#again read the images
hut1 = cv2.imread('hut1.jpg')
hut2 = cv2.imread('hut2.jpg')

#swap croping image of hut2 to hut1
hut1[20:200 , 10:140] = crop_hut2
cv2.imshow("swap_hut2_to_hut1",hut1)
cv2.waitKey()
cv2.destroyAllWindows()

#swap croping image of hut1 to hut2
hut2[20:200 , 10:140] = crop_hut1
cv2.imshow("swap_hut1_to_hut2",hut2)
cv2.waitKey()
cv2.destroyAllWindows()

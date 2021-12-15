import cv2
import glob
import os
from matplotlib import pyplot as plt
import numpy as num

class SIFTImage:
    def __init__(self, image, keypoints, descriptors):
        self.image = image
        self.keypoints = keypoints
        self.descriptors = descriptors

# 1. Match Features

#The first step is to extract features from the images, and automatically establish feature correspondences between image pairs.

# The starting point is an unordered set of N images. The objective of this step is to extract features from each image, 
# and establish which (if any) of the N-1 other images contain a sufficient number of good matches so as to indicate that 
# the two images partially overlap. You can use any feature that you prefer (e.g. ORB, SIFT, SURF) or some combination thereof.
# You will need to develop a match metric that can be used to discriminate between good and bad image matches. For example, 
# this match metric could take the number of matching features between images into account, as well as the quality of their 
# match. Keep in mind that each image will only overlap with a small number of other images in the set, so ideally this match 
# metric will score high for the images that do have overlap, and low otherwise.

mySIFTInstance = cv2.SIFT_create()

imagePath = os.path.expanduser('~/Autostich-Maly/D1/Images/Mush/*.jpg')  #CAN CHANGE DEPENDING ON TEST IMAGES

images = [cv2.imread(file) for file in glob.glob(imagePath)]


siftImages = []

for image in images:
    (keypoints, descriptors) = mySIFTInstance.detectAndCompute(image, None)

    siftImage = SIFTImage(
        image,
        keypoints,
        descriptors
    )

    siftImages.append(siftImage)

testSiftImage = siftImages[0].image
testSiftImageKeyPoint = siftImages[0].keypoints

imageHeight, imageWidth, imageChannels = testSiftImage.shape
blankImage = num.zeros((imageHeight, imageWidth, imageChannels), num.uint8)
testSiftImageOutput = cv2.drawKeypoints(testSiftImage, testSiftImageKeyPoint, blankImage)
plt.imshow(testSiftImageOutput)


#this stores an array of comparisons that have aalready been performed 
#in order to prevent 'b' being tested with 'a', if 'a' had already been tested with 'b'
testedImagePairs = []



# 2. Estimate Transformation

#The second step is to use these correspondences to estimate transformations between each image, and establish the most likely transformations between the image pairs.

# For those image pairs that have a high enough match metric score from Step 1, calculate the transformation between them.



# 3. Merge Images

# The third step is to apply these transformations to compose a single merged composite image from all images.

# Apply the transformations calculated in Step 2, and create and store a single merged image from the N images in the set. 
# Apply both geometric and radiometric transformations, so that the resulting merged image appears relatively seamless.



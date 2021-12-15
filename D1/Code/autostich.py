import cv2 as cv

# 1. Match Features

#The first step is to extract features from the images, and automatically establish feature correspondences between image pairs.

# The starting point is an unordered set of N images. The objective of this step is to extract features from each image, 
# and establish which (if any) of the N-1 other images contain a sufficient number of good matches so as to indicate that 
# the two images partially overlap. You can use any feature that you prefer (e.g. ORB, SIFT, SURF) or some combination thereof.
# You will need to develop a match metric that can be used to discriminate between good and bad image matches. For example, 
# this match metric could take the number of matching features between images into account, as well as the quality of their 
# match. Keep in mind that each image will only overlap with a small number of other images in the set, so ideally this match 
# metric will score high for the images that do have overlap, and low otherwise.

print('hello world')


# 2. Estimate Transformation

#The second step is to use these correspondences to estimate transformations between each image, and establish the most likely transformations between the image pairs.

# For those image pairs that have a high enough match metric score from Step 1, calculate the transformation between them.



# 3. Merge Images

# The third step is to apply these transformations to compose a single merged composite image from all images.

# Apply the transformations calculated in Step 2, and create and store a single merged image from the N images in the set. 
# Apply both geometric and radiometric transformations, so that the resulting merged image appears relatively seamless.



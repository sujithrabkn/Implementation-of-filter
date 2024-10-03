
###Developed By : SUJITHRA B K N
###Register Number: 212222230153
### Smoothing Filters
# In[1]:Using Averaging Filter


import cv2
import matplotlib.pyplot as plt
import numpy as np
image1=cv2.imread("moon.jpg")
image2=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
kernel=np.ones
image3=cv2.filter2D(image2,,kernel)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot()


# In[2]:Using Weighted Averaging Filter


kernel1=np.ones((11,11), np. float32)/121
plt.figure(figsize=(8,8))
plt.subplot(1,)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(image3)
plt.title("Weighted Average Filter Image")
plt.axis("off")
plt.show()


# In[3]:Using Gaussian Filter


gaussian_blur=cv2.GaussianBlur(src=image2, ksize=(11,11), sigmaX=0, sigmaY=0)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(gaussian_blur)
plt.title("Gaussian Blur")
plt.axis("off")
plt.show()




# In[4]:Using Median Filter


median=cv2.medianBlur (src=image2, ksize=11)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(median)
plt.title("Median Filter")
plt.axis("off")
plt.show()







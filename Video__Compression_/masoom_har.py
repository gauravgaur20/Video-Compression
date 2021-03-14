import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import glob
import timeit
import shutil

start = timeit.default_timer()
os.mkdir('/Users/masoomraj/Music/fft/image/')
os.mkdir('/Users/masoomraj/Music/fft/image1/')
def FrameCapture(path):
    global count
    vidObj = cv2.VideoCapture(path)
    success = 1
    while success:
         success, image = vidObj.read()
         path = '/Users/masoomraj/Music/fft/image'
         cv2.imwrite(os.path.join(path , 'frame%d.jpg' % count), image)
         count += 1


count = int(0)
FrameCapture("/Users/masoomraj/Music/fft/video.mp4")
print("NUMBER OF FRAMES: ",count)



cnt=0
for i in range(count-1):
    img="/Users/masoomraj/Music/fft/image/frame"+str(i)+".jpg"
    cv_img = cv2.imread(img)
    #count=int(0)
    img=cv_img
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    x,y=gray.shape[:2]
    new=np.fft.fft2(gray)
    shift=np.fft.fftshift(new)
    n=np.abs(shift)
    f=np.log(n+1)
    #count=2
    m=np.max(np.abs(new[:]))
    arr=np.array([0.001])
#DONT CHNAGE 0.001
    for thresh in 0.2*arr*m:
#CHANGE HERE 0.2
        ind=abs(new)>thresh
        newfilt=np.multiply(new,ind)
        nfilt=np.fft.ifft2(newfilt)
        nfilt=np.abs(nfilt)
        path = '/Users/masoomraj/Music/fft/image/image1/'
        cv2.imwrite(path+str(i)+".jpg", nfilt)
    cnt+=1


img_array=[]
for i in range(0,cnt-1) :
    image='/Users/masoomraj/Music/fft/image/image1/'+str(i)+'.jpg'
    img=cv2.imread(image)
    height,width,layers=img.shape[:3]
    size=(width,height)
    img_array.append(img)
    out=cv2.VideoWriter('/Users/masoomraj/Music/fft/project.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,size)

for i in range(int(len(img_array))):
    out.write(img_array[i])
out.release()
shutil.rmtree('/Users/masoomraj/Music/fft/image/')
shutil.rmtree('/Users/masoomraj/Music/fft/image1/')
stop = timeit.default_timer()
print('Time: ', stop - start)
b = (os.path.getsize("/Users/masoomraj/Music/fft/video.mp4")-os.path.getsize("/Users/masoomraj/Music/fft/project.mp4"))*100/os.path.getsize("/Users/masoomraj/Music/fft/video.mp4")
print("Compression Ratio = ",b) # ===uncompressed size /compressed size

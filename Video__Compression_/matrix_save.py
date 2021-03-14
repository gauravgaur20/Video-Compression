from PIL import Image
import numpy as np
im = Image.open('/home/harshit/Desktop/c/Lena.png')
iar = np.asarray(im)
with open('/home/harshit/Desktop/c/matrix.txt','wb') as f:
    for line in iar:
        np.savetxt(f, line, fmt='%d')
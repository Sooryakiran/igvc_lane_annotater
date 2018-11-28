import cv2
import numpy as np
import os
import random
image_list = os.listdir('data')
total_files = len(image_list)

move = False
# black_image = np.zeros((512,512), dtype = int )

def hist_corr(img):
    out = img
    for i in range(3):
        out[:,:,i] = cv2.equalizeHist(img[:,:,i])

    return out

def add_point(event, x, y, flags, param):

    global move
    global black_image
    # print(move)
    # print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        move = True
        print("***********")
    if event == cv2.EVENT_MOUSEMOVE and move == True:
        # black_image[y][x]=255
        cv2.circle(black_image, (x,y), 5, 255,thickness=-1)
        # print(x, y, black_image[x][y])
        # return (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        move = False

print('Total %d images found' % total_files)
for image in image_list:

    black_image = np.zeros((512,512), dtype = float )
    file_path = 'data/' + image
    img = cv2.imread(file_path)
    img = cv2.resize(img,(512,512))
    cv2.namedWindow('view')
    cv2.imshow('view',img)
    cv2.setMouseCallback("view", add_point)
    cv2.waitKey(0)
    
    # print(np.sum(black_image))
    cv2.imshow("label",black_image)
    name =image.split('.')[0]
    
    name = name + str(random.randint(0,1000000000000)) + "blah" + str(random.randint(0,1000000))
    name ="data_output/" + name + "_mask.png"

    cv2.waitKey(0)
    cv2.imwrite(name,black_image)
    cv2.imwrite("data_output"+name + ".jpg",cv2.resize(img,(512,512)) )

    cv2.destroyAllWindows()

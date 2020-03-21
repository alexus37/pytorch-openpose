import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np

from torch_openpose import model
from torch_openpose import util
from torch_openpose.body import Body
from torch_openpose.hand import Hand

body_estimation = Body('model/body_pose_model.pth')

test_image = 'images/demo.jpg'
oriImg = cv2.imread(test_image)  # B,G,R order
candidate, subset = body_estimation(oriImg)
canvas = copy.deepcopy(oriImg)
canvas = util.draw_bodypose(canvas, candidate, subset)


plt.imshow(canvas[:, :, [2, 1, 0]])
plt.axis('off')
plt.show()

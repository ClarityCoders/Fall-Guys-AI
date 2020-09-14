import numpy as np
import cv2

data = np.load("../data/training_data_Gate.npy", allow_pickle=True)
targets = np.load("../data/target_data_Gate.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

for i, image in enumerate(data):
    print(targets[i])
    #print(data)
    #image = cv2.Canny(image, threshold1 = 50, threshold2 = 100)
    #image = cv2.HoughLinesP(image, 1, np.pi/180, 180, 20, 15)
    cv2.imshow("Fall", image)

    cv2.waitKey(0) # waits until a key is pressed
    cv2.destroyAllWindows() # destroys the window showing image
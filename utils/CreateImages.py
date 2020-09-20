import cv2
import numpy as np

data = np.load("../data/training_dataGC.npy", allow_pickle=True)
targets = np.load("../data/target_dataGC.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_up = 0
count_left = 0
count_right = 0
count_jump = 0

for data in holder_list:
    #print(data[1])
    if data[1] == 'W':
        count_up += 1
        cv2.imwrite(f"E:/GC/Nothing/H7-u{count_up}.png", data[0]) 
    elif data[1] == 'A':
        count_left += 1
        cv2.imwrite(f"E:/GC/Left/H7-l{count_left}.png", data[0]) 
    elif data[1] == 'D':
        count_right += 1
        cv2.imwrite(f"E:/GC/Right/H7-r{count_right}.png", data[0]) 
    elif data[1] == ' ':
        count_jump += 1
        cv2.imwrite(f"E:/GC/Jump/H7-j{count_jump}.png", data[0]) 
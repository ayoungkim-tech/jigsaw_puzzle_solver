import os
import cv2
import numpy as np

def create_dataset(path):
    filenames = os.listdir(path)
    filenames.sort()
    puzzle_data = []
    class_ids = []
    for filename in filenames:
        img_path = os.path.join(path, filename)
        puzzle_piece = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        puzzle_piece = np.array(puzzle_piece)
        puzzle_piece = puzzle_piece.astype('float32')
        puzzle_piece /= 255
        puzzle_data.append(puzzle_piece)
        # split pieces location axis information from filename
        axis= filename.split('.')[0]
        x_axis = int(axis.split('-')[0])
        y_axis = int(axis.split('-')[1])
        class_ids.append((x_axis,y_axis))
    puzzle_data = np.array(puzzle_data)
    class_ids = np.array(class_ids)
    return puzzle_data, class_ids
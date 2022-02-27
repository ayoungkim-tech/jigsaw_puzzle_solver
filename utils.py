import os
import cv2
import numpy as np

def create_dataset(img_path,shape_id_path):
    filenames = os.listdir(img_path)
    filenames.sort()
    puzzle_data = []
    location_ids = []
    shape_ids = read_txt_file(shape_id_path)
    for filename in filenames:
        piece_path = os.path.join(img_path, filename)
        puzzle_piece = cv2.imread(piece_path, cv2.IMREAD_GRAYSCALE)
        puzzle_piece = np.array(puzzle_piece)
        puzzle_piece = puzzle_piece.astype('float32')
        puzzle_piece /= 255
        puzzle_data.append(puzzle_piece)
        # split pieces location axis information from filename
        axis= filename.split('.')[0]
        x_axis = int(axis.split('-')[0])
        y_axis = int(axis.split('-')[1])
        location_ids.append((x_axis,y_axis))
    puzzle_data = np.array(puzzle_data)
    location_ids = np.array(location_ids)
    shape_ids = np.array(shape_ids[1:])
    return puzzle_data, location_ids, shape_ids

def read_txt_file(path):
    vals = []
    file = open(path, 'rb')
    for line in file:
        # parts : key \t val
        parts = line.rstrip().split()
        vals.append(parts[1].decode("utf-8"))
    file.close()
    return vals
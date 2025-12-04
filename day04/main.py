from __future__ import annotations
import numpy as np
from utils import read_input

class Kernel:
    def __init__(self, kernel):
        self.x_size = len(kernel)
        self.y_size = len(kernel[0])
        self.kernel = kernel

    def apply(self, kernel: Kernel):
        mat1 = np.array(self.kernel)
        mat2 = np.array(kernel.kernel)
        print(mat1)
        print(mat2)

        result = np.corrcoef(mat1, mat2)
        print(result)

def split_row(row: str, mapping: dict):
    output = []
    for char in row:
        output.append(mapping[char])
    return output


def challenge1():
    data = read_input('day04')
    data = [
        split_row(
            row,
            {
                '@':1,
                '.':0
            }
        ) for row in data
    ]
    kernel = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]


    total = 0
    new_data = []
    for i, row in enumerate(data):
        new_row = []
        for j, col in enumerate(row):
            # Setup variables
            surrounding = 0
            if col == 0:
                new_row.append(col)
                continue
            for k in range(3):
                for l in range(3):
                    x = i + k -1
                    y = j + l -1

                    # print(f"x:{x:2} y:{y:2} i:{i:2} j:{j:2} col:{col:2} k:{k:2} l:{l:2} kern:{kernel[k][l]:2}")
                    if x >= 0 and x < len(data) and y >= 0 and y < len(row):
                        # print(f"data:{data[x][y]:2}  result:{data[x][y]*kernel[k][l]:2}")
                        surrounding += data[x][y]*kernel[k][l]
            if surrounding < 4:
                total += 1
                new_row.append('x')
            else:
                new_row.append(col)
        new_data.append(new_row)
    print(f"Total is {total}")
    print(np.array(new_data))

def challenge2():
    data = read_input('day04')
    # data = [
    #     "..@@.@@@@.",
    #     "@@@.@.@.@@",
    #     "@@@@@.@.@@",
    #     "@.@@@@..@.",
    #     "@@.@@@@.@@",
    #     ".@@@@@@@.@",
    #     ".@.@.@.@@@",
    #     "@.@@@.@@@@",
    #     ".@@@@@@@@.",
    #     "@.@.@@@.@.",
    # ]
    data = [
        split_row(
            row,
            {
                '@':1,
                '.':0
            }
        ) for row in data
    ]
    kernel = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]


    total = 0
    removed = -1
    while removed != 0:
        removed = 0
        new_data = []
        for i, row in enumerate(data):
            new_row = []
            for j, col in enumerate(row):
                # Setup variables
                surrounding = 0
                if col == 0:
                    new_row.append(col)
                    continue
                for k in range(3):
                    for l in range(3):
                        x = i + k -1
                        y = j + l -1

                        # print(f"x:{x:2} y:{y:2} i:{i:2} j:{j:2} col:{col:2} k:{k:2} l:{l:2} kern:{kernel[k][l]:2}")
                        if x >= 0 and x < len(data) and y >= 0 and y < len(row):
                            # print(f"data:{data[x][y]:2}  result:{data[x][y]*kernel[k][l]:2}")
                            surrounding += data[x][y]*kernel[k][l]
                if surrounding < 4:
                    total += 1
                    removed += 1
                    new_row.append(0)
                else:
                    new_row.append(col)
            new_data.append(new_row)
        print(f"Removed: {total}")
        data = new_data
    print(f"Total is {total}")
    # print(np.array(new_data))
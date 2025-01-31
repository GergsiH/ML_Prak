from collections import Counter
from typing import List

def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    return Counter(x) == Counter(y)

def max_prod_mod_3(x: List[int]) -> int:
    max_product = -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            product = x[i] * x[i + 1]
            max_product = max(max_product, product)

    return max_product if max_product != -1 else -1

def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    height, width = len(image), len(image[0])
    res = [[0.0] * width for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            res[i][j] = sum(image[i][j][c] * weights[c] for c in range(len(weights)))

    return res

def rle_scalar(x: List[List[int]], y: List[List[int]]) -> int:
    total_length_x = sum(count for _, count in x)
    total_length_y = sum(count for _, count in y)

    if total_length_x != total_length_y:
        return -1

    first_idx, second_idx = 0, 0
    first_length = x[first_idx][1]
    second_length = y[second_idx][1]
    result = 0

    for _ in range(total_length_x):
        if first_length == 0:
            first_idx += 1
            first_length = x[first_idx][1]
        if second_length == 0:
            second_idx += 1
            second_length = y[second_idx][1]

        result += x[first_idx][0] * y[second_idx][0]
        first_length -= 1
        second_length -= 1

    return result

from typing import List

def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    def calculate_cosine(vec1, vec2):
        if all(v == 0 for v in vec1) or all(v == 0 for v in vec2):
            return 1.0
        
        dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
        norm1 = sum(v ** 2 for v in vec1) ** 0.5
        norm2 = sum(v ** 2 for v in vec2) ** 0.5
        
        return dot_product / (norm1 * norm2) if norm1 and norm2 else 1.0

    M = []
    for x in X:
        row = [calculate_cosine(x, y) for y in Y]
        M.append(row)

    return M



def logical_and(image1, image2):
    height, width = len(image1), len(image1[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            result[i][j] = image1[i][j] & image2[i][j]
    return result

def logical_or(image1, image2):
    height, width = len(image1), len(image1[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            result[i][j] = image1[i][j] | image2[i][j]
    return result

def logical_not(image):
    height, width = len(image), len(image[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            result[i][j] = 255 - image[i][j]
    return result

def logical_xor(image1, image2):
    height, width = len(image1), len(image1[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            result[i][j] = image1[i][j] ^ image2[i][j]
    return result

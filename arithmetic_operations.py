def addImages(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same size"
    height, width, channels = image1.shape
    addedImage = image1.copy()
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                addedImage[y, x, c] = min(int(image1[y, x, c]) + int(image2[y, x, c]), 255)
    return addedImage

def subtractImages(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same size"
    height, width, channels = image1.shape
    subtractedImage = image1.copy()
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                subtractedImage[y, x, c] = max(int(image1[y, x, c]) - int(image2[y, x, c]), 0)
    return subtractedImage

def multiplyImages(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same size"
    height, width, channels = image1.shape
    multipliedImage = image1.copy()
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                multipliedImage[y, x, c] = min(int(image1[y, x, c]) * int(image2[y, x, c]), 255)
    return multipliedImage

def divideImages(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same size"
    height, width, channels = image1.shape
    dividedImage = image1.copy()
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                if int(image2[y, x, c]) != 0:
                    dividedImage[y, x, c] = min(int(image1[y, x, c]) / int(image2[y, x, c]), 255)
                else:
                    dividedImage[y, x, c] = 255  # Handle division by zero
    return dividedImage

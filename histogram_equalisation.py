def histogram_equalization(image):
    histogram = np.zeros(256, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i, j]] += 1
    
    cdf = np.zeros(256, dtype=np.float64)
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]
    
    cdf = cdf / cdf.max() * 255
    equalized_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equalized_image[i, j] = cdf[image[i, j]]
    
    return equalized_image.astype(np.uint8)
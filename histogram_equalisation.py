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


def histogram(image):
    hist = np.zeros(256, dtype=np.uint8)
    for pixel_value in image.flatten():
        hist[pixel_value] += 1
    return hist

hist_original = histogram(image)
hist_equalized = histogram(he)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(hist_original, color='b')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.plot(hist_equalized, color='r')
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

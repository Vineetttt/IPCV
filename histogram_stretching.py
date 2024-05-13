def histogram_stretching(image, r_min, r_max):
    min_pixel = np.min(image)
    max_pixel = np.max(image)
    
    stretched_image = (image - min_pixel) * ((r_max - r_min) / (max_pixel - min_pixel)) + r_min
    stretched_image = np.clip(stretched_image, 0, 255)
    
    return stretched_image.astype(np.uint8)

def histogram(image):
    hist = np.zeros(256, dtype=np.uint8)
    for pixel_value in image.flatten():
        hist[pixel_value] += 1
    return hist

hist_original = histogram(image)
hist_stretched = histogram(stretched_image)

# Plot histograms
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(hist_original, color='b')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.plot(hist_stretched, color='r')
plt.title('Stretched Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

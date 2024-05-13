def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    row, col, _ = noisy_image.shape
    salt_thresh = 1 - salt_prob
    pepper_thresh = pepper_prob
    
    salt_noise = np.random.random((row, col))
    noisy_image[salt_noise > salt_thresh] = 255
    
    pepper_noise = np.random.random((row, col))
    noisy_image[pepper_noise < pepper_thresh] = 0
    
    return noisy_image

def add_gaussian_noise(image, mean=1, sigma=16):
    gaussian_noise = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + gaussian_noise.astype(np.uint8)
    return noisy_image

def median_filter(image, kernel_size=3):
    if kernel_size % 2 == 0:
        kernel_size += 1
    rows, cols, channels = image.shape
    padded_image = np.pad(image, ((kernel_size // 2, kernel_size // 2), (kernel_size // 2, kernel_size // 2), (0, 0)))
    filtered_image = np.zeros_like(image, dtype=np.uint8)
    
    for i in range(rows):
        for j in range(cols):
            window = padded_image[i:i+kernel_size, j:j+kernel_size, :]
            for k in range(channels):
                filtered_image[i, j, k] = np.median(window[:, :, k])
    return filtered_image

def mean_filter(image, kernel_size=3):
    if kernel_size % 2 == 0:
        kernel_size += 1
    rows, cols, channels = image.shape
    padded_image = np.pad(image, ((kernel_size // 2, kernel_size // 2), (kernel_size // 2, kernel_size // 2), (0, 0)), mode='constant')
    filtered_image = np.zeros_like(image, dtype=np.float32)
    
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size * kernel_size)
    for i in range(rows):
        for j in range(cols):
            window = padded_image[i:i+kernel_size, j:j+kernel_size, :]
            for k in range(channels):
                filtered_image[i, j, k] = np.sum(window[:, :, k] * kernel)
    return filtered_image.astype(np.uint8)

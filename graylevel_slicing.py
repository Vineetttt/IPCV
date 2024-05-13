def thresholding(image, threshold_value):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded_image = np.zeros_like(grayscale_image)
    thresholded_image[grayscale_image > threshold_value] = 255
    return thresholded_image

def gray_level_slicing_with_background(image,a,b):
    grey_img1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h,w,_ = image.shape
    wbg_img = np.zeros((h, w), np.uint8)
    for i in range(h):
      for j in range(w):
        r = grey_img1[i][j]
        if a <= r <= b:
            wbg_img[i][j] = 255
        else:
            wbg_img[i][j] = r
    return wbg_img

def gray_level_slicing_without_background(image,a,b):
    grey_img1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h,w,_ = image.shape
    wobg_img = np.zeros((h, w), np.uint8)
    for i in range(h):
      for j in range(w):
        if a <= grey_img1[i][j] <= b:
            wobg_img[i][j] = 255
        else:
            wobg_img[i][j] = 0
    return wobg_img

def plot_grayscale_histogram(image):
    hist, bins = np.histogram(image.ravel(), bins=256, range=(0, 256))

    plt.figure(figsize=(8, 6))
    plt.title("Grayscale Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.bar(bins[:-1], hist, width=1, color='gray')
    plt.show()

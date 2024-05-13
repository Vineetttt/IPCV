def high_pass_filter(image):
  kernel = np.array([[-1, -1, -1],
                     [-1,  8, -1],
                     [-1, -1, -1]])
  rows, cols,_ = image.shape
  filtered_image = cv2.filter2D(image, -1, kernel)
  return filtered_image.astype(np.uint8)


def high_boost_filter(image, boost_factor=1.0):
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])
    filtered_image = cv2.filter2D(image, -1, kernel)
    result_image = image + boost_factor * filtered_image
    result_image = np.clip(result_image, 0, 255)
    return result_image.astype(np.uint8)

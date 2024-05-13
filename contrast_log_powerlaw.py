def contrast_stretching(img, r1, s1, r2, s2):
    stretched_img = np.copy(img)
    stretched_img[stretched_img < r1] = stretched_img[stretched_img < r1] * (s1 / r1)
    stretched_img[(r1 <= stretched_img) & (stretched_img <= r2)] = ((stretched_img[(r1 <= stretched_img) & (stretched_img <= r2)] - r1) * ((s2 - s1) / (r2 - r1))) + s1
    stretched_img[stretched_img > r2] = ((stretched_img[stretched_img > r2] - r2) * ((255 - s2) / (255 - r2))) + s2
    return stretched_img.astype(np.uint8)

def log_transformation(img):
    c = 255 / np.log(1 + np.max(img))
    log_transformed_img = c * np.log(1 + img)
    return log_transformed_img.astype(np.uint8)

def power_law_transformation(img, gamma):
    c = 1
    power_law_transformed_img = c * np.power(img, gamma)
    return power_law_transformed_img.astype(np.uint8)

def contrast_stretching(image,s1,s2,r1,r2):
    height,width, channels= image.shape
    output = image.copy()
    alpha = s1/r1
    beta = (s2 - s1)/(r2 - r1)
    gamma = (255 - s2)/(255 - r2)
    for i in range(height):
        for j in range(width):
            for c in range(channels):
                if image[i,j,c] < r1:
                    output[i,j,c] = alpha*image[i,j,c]
                elif image[i,j,c] >= r1 and image[i,j,c] < r2:
                    output[i,j,c] = beta*(image[i,j,c] - r1) + s1
                else:
                    output[i,j,c] = gamma*(image[i,j,c] - r2) + s2
    return output

def log_transformation(img):
    c = 255 / np.log(1 + np.max(img))
    log_transformed_img = c * np.log(1 + img)
    return log_transformed_img.astype(np.uint8)

def power_law_transformation(img, gamma):
    c = 1
    power_law_transformed_img = c * np.power(img, gamma)
    return power_law_transformed_img.astype(np.uint8)

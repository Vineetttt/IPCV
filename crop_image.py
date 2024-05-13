def crop_image(image, x, y):
    height,width,_ = image.shape
    cropped_image = image[y:y+height, x:x+width]
    return cropped_image

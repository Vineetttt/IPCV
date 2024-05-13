def rgb_to_grayscale(image):
  height,width,channels = image.shape
  grayscaleImage = np.zeros((height,width))
  for x in range(height):
    for y in range(width):
        pixelValue = sum(image[x,y])/channels
        grayscaleImage[x,y] = pixelValue
  return grayscaleImage

def erosion(image, kernel):
    rows,cols,channels = image.shape
    if channels > 1:
        image_grey = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    else:
        image_grey = image

    pad_rows = kernel.shape[0]//2
    pad_cols = kernel.shape[1]//2
    pad_img = np.pad(image_grey,((pad_rows,pad_rows),(pad_cols,pad_cols)))

    eroded = np.zeros_like(image_grey)

    for i in range(rows):
        for j in range(cols):
            neighborhood = pad_img[i:i+kernel.shape[0],j:j+kernel.shape[1]]
            eroded[i,j] = np.min(neighborhood*kernel)

    return eroded


def dilation(image,kernel):
    rows,cols,channels = image.shape
    k_rows,k_cols = kernel.shape
    if channels > 1:
        image_grey = image = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    else:
        image_grey = image
    
    pad_rows = k_rows // 2
    pad_cols = k_cols // 2
    pad_image = np.pad(image_grey,((pad_rows,pad_rows),(pad_cols,pad_cols)))
    dilated = np.zeros_like(image_grey)

    for i in range(rows):
        for j in range(cols):
            neighborhood = pad_image[i:i+k_rows,j:j+k_cols]
            dilated[i,j] = np.max(neighborhood*kernel)
    return dilated


def opening(image,mask):
    return dilation(erosion(image,mask),mask)

def closing(image,mask):
    return erosion(dilation(image,mask),mask)

def hmt(image,b1,b2):
    image_c=np.where(image==0,1,0)
    return np.bitwise_and(erosion(image,b1),erosion(image_c,b2))

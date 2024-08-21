from PIL import Image, ImageFilter

def apply_filter(image_path, filter_type):
    image = Image.open(image_path)
    if filter_type == 'BLUR':
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_type == 'CONTOUR':
        filtered_image = image.filter(ImageFilter.CONTOUR)
    else:
        filtered_image = image
    filtered_image.show()

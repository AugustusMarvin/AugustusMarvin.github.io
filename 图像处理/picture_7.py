from PIL import Image, ImageFilter
image = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
image.filter(ImageFilter.CONTOUR).show()
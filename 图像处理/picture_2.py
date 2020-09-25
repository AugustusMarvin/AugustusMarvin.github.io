from PIL import Image
image = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
rect = 60, 10, 340, 360
image.crop(rect).show()
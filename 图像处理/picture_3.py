from PIL import Image
image = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
size = 128, 128
image.thumbnail(size)
image.show()
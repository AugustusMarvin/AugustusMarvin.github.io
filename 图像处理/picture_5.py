from PIL import Image
image = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
image.transpose(Image.FLIP_TOP_BOTTOM).show()
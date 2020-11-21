from PIL import Image
image1 = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
image2 = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB_1.jpg")
rect = 60, 10, 340, 360
guido = image2.crop(rect)
width, height = guido.size
image1.paste(guido.resize((int(width / 1.5), int(height / 1.5))),(172, 40))
image1.show()
#将两个图像进行拼接
from PIL import Image
image = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
#image = Image.open('BVB.jpg')
print(str(image.format) + str(image.size) + str(image.mode))
image.show()
from PIL import Image
image = Image.open("E:/git/AugustusMarvin.github.io/图像处理/BVB.jpg")
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x,y), (128, 128, 128))
image.show()
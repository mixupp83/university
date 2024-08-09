from PIL import Image

im = Image.open("6.jpg")

print(im.format, im.size, im.mode)

out = im.resize((128, 128))

out.show()


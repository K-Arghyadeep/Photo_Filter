from PIL import Image
import os

# image1 = Image.open('images.jpg')
# image1.save('images.png')

##########convert-jpg-to-png##########
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fileName, fileExtension = os.path.splitext(f)
#         print(fileName) 
#         print(fileExtension)
#         i.save('png/{}.png'.format(fileName))


##########changing-size-to-300x300##########
size_300 = (300,300)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fileName, fileExtension = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fileName,fileExtension))
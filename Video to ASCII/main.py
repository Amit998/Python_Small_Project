import os
import sys
import cv2
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resized_gray_image(image,new_width=70):
    width,height=image.size
    aspect_ratio=height/width
    new_height=int(aspect_ratio*new_width)
    resize_gray_image=image.resize((new_width,new_height)).convert('L')

    return resize_gray_image


def pix2chars(image):
    pixels=image.getdata()
    characters="".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def generate_frame(image,new_width=70):
    new_image_data=pix2chars(resized_gray_image(image))

    total_pixels=len(new_image_data)

    ascii_image="\n".join([new_image_data[index:(index+new_width)] for index in range(0,total_pixels,new_width)])


    sys.stdout.write(ascii_image)
    # os.system('cls')




image=cv2.imread("D:/study/workplace/project/Flutter Backend Apps/artvana/assets/images/36.jpg")
image=cv2.resize(image,(200,200))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image",image)
generate_frame(Image.fromarray(image))


# while True:
#     re,frame=cap.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame=cv2.resize(frame,(400,400))
#     cv2.imshow("frame",frame)
    
#     generate_frame(Image.fromarray(frame))
#     cv2.waitKey(10)
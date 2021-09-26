import PIL.Image
import io


# img=PIL.Image.open("test2.png")
# byte_arr=io.BytesIO()
# img.save(byte_arr,format='PNG')


# with open("test1.jpeg",'ab') as f:
#     f.write(byte_arr.getvalue())

with open("test1.jpeg",'rb') as f:
    content=f.read()
    offset=content.index(bytes.fromhex("FFD9"))

    f.seek(offset+2)

    new_img=PIL.Image.open(io.BytesIO(f.read()))
    new_img.save("new_image.png")
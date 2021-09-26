# with open("test1.jpeg",'ab') as f:
#     f.write(b"hello world")


with open("test1.jpeg","rb") as f:
    content=f.read()
    offset=content.index(bytes.fromhex('FFD9'))


    f.seek(offset+2)
    print(f.read())
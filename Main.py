from PIL import Image, ImageDraw
Colors={
    1:"238, 151, 160",
    2:"55, 55, 57",
    3:"125, 92, 58",
    4:"235, 120, 0",
    5:"98, 58, 66",
    6:"201, 175, 148",
    7:"153, 131, 171",
    8:"28, 66, 216",
    9:"244, 76, 109",
    10:"89, 14, 115",
    11:"78, 79, 129",
    12:"252, 99, 49",
    13:"226, 173, 9",
    14:"173, 178, 197",
    15:"121, 166, 71",
    16:"115, 92, 118",
    17:"201, 181, 157",
    18:"107, 129, 116",
}
img= Image.new('RGB',(7588,7588),(255,255,255))
draw = ImageDraw.Draw(img)

def line(colors):
    pass

def quadrat(x,y,colors):
    xstart=x
    ystart=y
    for i in range (3):
        draw.point((x,y),(255,255,255))
        y+=1
    for i in range(21):
        draw.point((x,y),colors[0])
        y+=1
    for i in range (3):
        draw.point((x,y),(255,255,255))
        y+=1
    y=ystart
    for i in range (2):
        draw.point((x,y),(255,255,255))
        y+=1
    for i in range(23):
        draw.point((x,y),colors[0])
        y+=1
    for i in range (2):
        draw.point((x,y),(255,255,255))
        y+=1
    y=ystart
    for i in range (1):
        draw.point((x,y),(255,255,255))
        y+=1
    for i in range(25):
        draw.point((x,y),colors[0])
        y+=1
    for i in range (1):
        draw.point((x,y),(255,255,255))
        y+=1
    y=ystart
    x+=1
def quadratTest(x,y,colors):
    xstart=x
    ystart=y
    for i in range(28):
        x=xstart
        for j in range(28):
            draw.point((x,y),colors[0])
            x+=1
        y+=1
    
quadratTest(1,1,[(1,1,1)])
img.save('test.jpeg', quality=95)

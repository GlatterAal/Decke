from PIL import Image, ImageDraw
import itertools as it

def ListOfColors(imageFile,n):
    image=Image.open(imageFile,'r')
    pix_val=list(image.getdata())
    pix=[]
    x=1
    h=[]
    for e in pix_val:
        if(x!=n+1):
            h.append(e)
            x+=1
        else:
            pix.append(h)
            h=[]
            h.append(e)
            x=2
    pix.append(h)
    return pix

def quadrat(x,y,colors):
    xstart=x
    ystart=y
    pix=ListOfColors('Bluepose.png',27)
    for e in pix:
        for k in e:
            if(k[2]==0):
                draw.point((x,y),colors[0])
            elif(k[2]==21):
                draw.point((x,y),colors[1])    
            elif(k[2]==39):
                draw.point((x,y),colors[2])
            elif(k[2]==76):
                draw.point((x,y),colors[3])
            else:
                draw.point((x,y),(255,255,255))
            x+=1
        x=xstart
        y+=1
    y=ystart
Colors={
    1:(238, 151, 160),
    2:(55, 55, 57),
    3:(125, 92, 58),
    4:(235, 120, 0),
    5:(98, 58, 66),
    6:(201, 175, 148),
    7:(153, 131, 171),
    8:(28, 66, 216),
    9:(244, 76, 109),
    10:(89, 14, 115),
    11:(78, 79, 129),
    12:(252, 99, 49),
    13:(226, 173, 9),
    14:(173, 178, 197),
    15:(121, 166, 71),
    16:(115, 92, 118),
    17:(201, 181, 157),
    18:(107, 129, 116),
}

img= Image.new('RGB',(1500,1500),(255,255,255))
draw = ImageDraw.Draw(img)
l=list(it.combinations(list(Colors.keys()),4))
k=0
for i in range (1,294,28):
    for j in range (1,294,28):
        quadrat(j,i,[Colors[l[k][0]],Colors[l[k][1]],Colors[l[k][2]],Colors[l[k][3]]])
        k+=1


#quadrat(1,1,[(255,1,1),(1,255,1),(1,1,255),(255,255,1)])
#quadrat(29,1,[(255,1,1),(1,255,1),(1,1,255),(255,255,1)])
img.save('test.png', quality=95)
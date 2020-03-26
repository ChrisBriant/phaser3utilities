from PIL import Image
import sys, os, json

#EXAMPLE python3 spriteatlas.py <imagefile> <framewidth> <frameheight> <nocols> <norows> <rowoffset>

#Get command line arguments
imgfile = os.path.join(os.getcwd(),sys.argv[1])
framewidth = int(sys.argv[2])
frameheight = int(sys.argv[3])
nocols = int(sys.argv[4])
norows = int(sys.argv[5])
rowoffset = int(sys.argv[6])

#get image dimensions
im = Image.open(imgfile)
width, height = im.size

#Start the dict file
outdata = dict()

outdata["textures"] = []
imgdict = dict()
imgdict["image"] = sys.argv[1]
imgdict["format"] = "RGBA8888"
imgdict["size"] = {"w":width,"h":height}
#outdata["textures"].append(imgdict)
imgdict["scale"] = 1
imgdict["frames"] = []
#frames["frames"] = []

print(imgfile)



print("w",width, " h", height)

#for indexing sprite in file
spritenumber = 0

#Generate dictionary
for i in range(0,norows):
    for j in range(0,nocols):
        frame = dict()
        frame["filename"] = "sprite_"+str(spritenumber)
        frame["rotated"] = False
        frame["trimmed"] = False
        frame["sourceSize"] = {"w":framewidth, "h":frameheight}
        frame["spriteSourceSize"] = {"x":0,"y":0,"w":framewidth, "h":frameheight}
        frame["frame"] = {"x":j*framewidth,"y":i*frameheight,"w":framewidth, "h":frameheight}
        imgdict["frames"].append(frame)
        spritenumber += 1

outdata["textures"].append(imgdict)
#Don't think below is needed
#outdata["meta"] = {}

print(json.dumps(outdata))

text_file = open("out.json", "w")
text_file.write(json.dumps(outdata))
text_file.close()

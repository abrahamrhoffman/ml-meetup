#!/usr/bin/python

def convert(IMAGEFILE, LABELFILE, OUTPUTFILE, n):
    f = open(IMAGEFILE, "rb")
    o = open(OUTPUTFILE, "w")
    l = open(LABELFILE, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))] ## Look here! ord() function does the magic
        for j in range(28*28):
            image.append(ord(f.read(1))) ## Look here! ord() function does the magic
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

def main():
  convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte", "train.csv", 60000)
  convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte", "test.csv", 10000)

if __name__ == "__main__":
  main()


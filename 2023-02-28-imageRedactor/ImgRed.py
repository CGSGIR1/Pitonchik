# Rodin Ilya 28.02.2023
from PIL import Image

def negative(im):
    assert(im.mode == "RGB")
    w = im.width
    h = im.height
    pixels = im.load()
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for y in range(h):
        for x in range(w):
            color = [0] * 3
            for c in range(3):
                color[c] = 255 - pixels[x, y][c]
            dst[x, y] = tuple(color)
    return res

def contrast(im, val):
    assert(im.mode == "RGB")
    con = ((100 + val) / 255.0) ** 2
    w = im.width
    h = im.height
    pixels = im.load()
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for y in range(h):
        for x in range(w):
            color = [0] * 3
            for c in range(3):
                color[c] = (((pixels[x, y][c] / 255.0) - 0.5) * con + 0.5) * 255
                color[c] = int(color[c])
                if color[c] > 255:
                    color[c] = 255
                if color[c] < 0:
                    color[c] = 0
            dst[x, y] = tuple(color)
    return res

def brighthes(im, a):
    assert(im.mode == "RGB")
    w = im.width
    h = im.height
    pixels = im.load()
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for y in range(h):
        for x in range(w):
            color = [0] * 3
            for c in range(3):
                color[c] = pixels[x, y][c] + a;
            dst[x, y] = tuple(color)
    return res

if __name__ == '__main__':
    im = Image.open("monke.jpg")
    neg = negative(im)
    brt = brighthes(im, 40)
    brt.save("brth.bmp")
#   con1 = contrast(im, 300)
#   con2 = contrast(im, -80)
#   con3 = contrast(im, 20)
#   con1.save("contrast1.bmp")
#   con2.save("contrast2.bmp")
#   con3.save("contrast3.bmp")
#   neg.save("negative.bmp")
    frames = []
    for i in range(-100, 100, 5):
        frames.append(brighthes(im, i))
    frames[0].save('bright.gif', save_all=True, append_images=frames[1:], optimize=False, duration=200, loop = 0)
    im.close()

# Rodin Ilya 28.02.2023
from PIL import Image
import math

def negative(im):
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
    w = im.width
    h = im.height
    pixels = im.load()
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for y in range(h):
        for x in range(w):
            color = [0] * 3
            for c in range(3):
                color[c] = round(val * (pixels[x, y][c] - 128) + 128)
            dst[x, y] = tuple(color)
    return res

def brighthes(im, a):
    w = im.width
    h = im.height
    pixels = im.load()
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for y in range(h):
        for x in range(w):
            color = [0] * 3
            for c in range(3):
                color[c] = pixels[x, y][c] + a
            dst[x, y] = tuple(color)
    return res

def rotate(im, angle):
    angle = math.radians(angle)
    co, si = math.cos(angle), math.sin(angle)
    width = im.width
    height = im.height
    x0, y0 = width // 2, height // 2
    pixels = im.load()
    res = Image.new('RGB', (width, height), (0, 0, 0))
    dst = res.load()
    for y in range(height):
        for x in range(width):
            color = [0] * 3
            x1, y1 = x - x0, y - y0
            x2, y2 = (co * x1 - si * y1) + x0, (co * y1 + si * x1) + y0
            if 0 <= x2 < width and 0 <= y2 < height:
                for c in range(3):
                    color[c] = pixels[x2, y2][c]
            dst[x, y] = tuple(color)
    return res

def scale(im, k):
    w1 = im.width
    h1 = im.height
    w2 = round(w1 * k)
    h2 = round(h1 * k)
    pixels = im.load()
    res = Image.new('RGB', (w2, h2), (0, 0, 0))
    dst = res.load()
    for y in range(h2):
        for x in range(w2):
            color = [0] * 3
            x1 = round(x * k)
            y1 = round(y * k)
            if 0 <= x1 < w2 and 0 <= y1 < h2:
                for c in range(3):
                    color[c] = pixels[x1, y1][c]
            dst[x1, y1] = tuple(color)
    return res

if __name__ == '__main__':
    im = Image.open("monke.jpg")
    assert(im.mode == "RGB")
    '''
    neg = negative(im)
    brt = brighthes(im, 40)
    brt.save("brth.bmp")
    con1 = contrast(im, 5.0)
    con2 = contrast(im, 0.5)
    con1.save("contrast1.bmp")
    con2.save("contrast2.bmp")
    neg.save("negative.bmp")
    frames = []
    for i in range(-100, 100, 5):
        frames.append(brighthes(im, i))
    frames[0].save('bright.gif', save_all=True, append_images=frames[1:], optimize=False, duration=200, loop = 0)
    '''
    #rot = rotate(im, 35)
    #rot.save("rot.bmp")
    scl = scale(im, 5)
    scl.save("scl.bmp")
    
    im.close()

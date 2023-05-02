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

def blur(im, k):
    pixels = im.load()
    w = im.width
    h = im.height
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for i in range(w):
        for j in range(h):
            color = [0] * 3
            for l in range(3):
                color[l] = int((pixels[(i + 1) % w, (j - 1) % h][l] +
                                pixels[(i - 1) % w, (j + 1) % h][l] +
                                pixels[(i - 1) % w, (j - 1) % h][l] +
                                pixels[(i - 1) % w, j][l] +
                                pixels[(i + 1) % w, j][l] +
                                pixels[i, j][l] +
                                pixels[(i + 1) % w, (j + 1) % h][l] +
                                pixels[i, (j + 1) % h][l] +
                                pixels[i, (j - 1) % h][l]) / 9)
            dst[i, j] = tuple(color)
    k -= 1
    print(type(res))
    if k == 0:
        res.save("blr0.bmp")
        return res
    blur(res, k)

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
    w = im.width
    h = im.height
    pixels = im.load()
    x, y = (int(w / k), int(h / k))
    x1 = x / (w - 1)
    y1 = y / (h - 1)
    res = Image.new('RGB', (w, h), (0, 0, 0))
    dst = res.load()
    for i in range(x - 1):
        for j in range(y - 1):
            dst[i + 1, j + 1]= pixels[1 + int(i / x1), 1 + int(j / y1)]
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
    blr = blur(im, 10)
    #blr.save("blr.bmp")
    
    im.close()
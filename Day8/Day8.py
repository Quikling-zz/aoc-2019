from collections import defaultdict
from PIL import Image


def part1():
    with open('input.txt', 'r') as input_file:
        pixels = list(map(int, str(input_file.read())))

    width = 25
    height = 6
    pixels_in_image = width * height

    image = []

    i = 0
    while i < len(pixels):
        layer = defaultdict(int)
        for j in range(pixels_in_image):
            layer[pixels[i + j]] += 1
        image.append(layer)
        i += pixels_in_image

    min_zeros = min(image, key=lambda l: l[0])
    print(min_zeros[1] * min_zeros[2])


def part2():
    with open('input.txt', 'r') as input_file:
        pixels = list(map(int, str(input_file.read())))

    width = 25
    height = 6
    pixels_in_image = width * height

    image = [2] * pixels_in_image

    for i_final in range(pixels_in_image):
        i = i_final
        while pixels[i] == 2:
            i += pixels_in_image
        image[i_final] = pixels[i]

    print(''.join(map(str, image)))
    for i in range(height):
        print(''.join(map(str, image[i * width: (i + 1) * width])))

    img = Image.new('RGB', (25, 6))
    img.putdata([(255 * i, 255 * i, 255 * i) for i in image])
    img.save('derp.png')


if __name__ == '__main__':
    part1()
    part2()

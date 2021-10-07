# coding=utf-8
import numpy
from PIL import Image


def generate_image():
    image_array = numpy.random.rand(4, 4, 3) * 255
    image = Image.fromarray(image_array.astype('uint8')).convert('RGB')
    image.resize((480, 480), resample=Image.NEAREST)
    return image

from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import os

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
MAX_CAPTCHA = 6
WIDTH = 100
HEIGHT = 30

image = ImageCaptcha(width=WIDTH, height=HEIGHT, font_sizes=[30])

captcha_text = []
for i in range(MAX_CAPTCHA):
    c = random.choice(number)
    captcha_text.append(c)
    print(captcha_text)
captcha_text = ''.join(captcha_text)
print(captcha_text)

captcha = image.generate(captcha_text)
captcha_image = Image.open(captcha)
captcha_image = np.array(captcha_image)

image.write(captcha_text, str(i) + '_' + captcha_text + '.png')
plt.imshow(captcha_image)
plt.show()

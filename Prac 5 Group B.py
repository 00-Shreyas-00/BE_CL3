import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np

def load_img(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (256, 256))
    img = np.expand_dims(img, axis=0)
    return img / 255.0

content = load_img("content.jpg")
style = load_img("style.jpg")

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

stylized = model(tf.constant(content), tf.constant(style))[0]

cv2.imwrite("output.jpg", stylized[0].numpy() * 255)
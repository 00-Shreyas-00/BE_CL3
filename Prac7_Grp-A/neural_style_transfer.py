import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications import vgg19
from tensorflow.keras.preprocessing import image

# ---------------- IMAGE PROCESSING ----------------
def load_img(path):
    img = image.load_img(path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return vgg19.preprocess_input(img)

def deprocess_img(x):
    x = x.reshape((224, 224, 3))
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = x[:, :, ::-1]
    return np.clip(x, 0, 255).astype('uint8')


# ---------------- MODEL ----------------
def get_model():
    vgg = vgg19.VGG19(weights='imagenet', include_top=False)
    vgg.trainable = False

    content_layer = 'block5_conv2'
    style_layers = [
        'block1_conv1',
        'block2_conv1',
        'block3_conv1'
    ]

    outputs = [vgg.get_layer(name).output for name in style_layers]
    outputs.append(vgg.get_layer(content_layer).output)

    model = tf.keras.Model(vgg.input, outputs)
    return model


# ---------------- LOSS FUNCTIONS ----------------
def gram_matrix(x):
    x = tf.reshape(x, (-1, x.shape[-1]))
    return tf.matmul(x, x, transpose_a=True)

def style_loss(style, generated):
    S = gram_matrix(style)
    G = gram_matrix(generated)
    return tf.reduce_mean((S - G) ** 2)

def content_loss(content, generated):
    return tf.reduce_mean((content - generated) ** 2)


# ---------------- MAIN NST ----------------
def neural_style_transfer(content_path, style_path, iterations=100):
    content_image = load_img(content_path)
    style_image = load_img(style_path)

    model = get_model()

    content_outputs = model(content_image)
    style_outputs = model(style_image)

    generated = tf.Variable(content_image, dtype=tf.float32)

    optimizer = tf.optimizers.Adam(learning_rate=5.0)

    for i in range(iterations):
        with tf.GradientTape() as tape:
            outputs = model(generated)

            s_loss = 0
            for s, g in zip(style_outputs[:-1], outputs[:-1]):
                s_loss += style_loss(s, g)

            c_loss = content_loss(content_outputs[-1], outputs[-1])

            total_loss = 1e-4 * c_loss + 1e-2 * s_loss

        grads = tape.gradient(total_loss, generated)
        optimizer.apply_gradients([(grads, generated)])

        if i % 10 == 0:
            print(f"Iteration {i}, Loss: {total_loss.numpy()}")

    return deprocess_img(generated.numpy())


# ---------------- RUN ----------------
if __name__ == "__main__":
    content_path = "content.jpg"   # your input image
    style_path = "style.jpg"       # style image

    result = neural_style_transfer(content_path, style_path, iterations=50)

    plt.imshow(result)
    plt.axis('off')
    plt.savefig("output.jpg")
    plt.show()
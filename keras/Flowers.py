import os
import tensorflow as tf
# Directory with daisy pictures
daisy_dir = os.path.join('/home/ashvin/Desktop/KerasImages/Flowers/flowers/daisy')

# Directory with dandelion pictures
dandelion_dir = os.path.join('/home/ashvin/Desktop/KerasImages/Flowers/flowers/dandelion')

# Directory with rose pictures
rose_dir = os.path.join('/home/ashvin/Desktop/KerasImages/Flowers/flowers/rose')

# Directory with sunflower pictures
sunflower_dir = os.path.join('/home/ashvin/Desktop/KerasImages/Flowers/sunflower')

# Directory with tulip pictures
tulip_dir = os.path.join('/home/ashvin/Desktop/KerasImages/Flowers/tulip')


train_daisy_names = os.listdir(daisy_dir)
print(train_daisy_names[:5])

train_rose_names = os.listdir(rose_dir)
print(train_rose_names[:5])
from tensorflow.keras.preprocessing import image

import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Parameters for our graph; we'll output images in a 4x4 configuration
# nrows = 4
# ncols = 4
#
# # Index for iterating over images
# pic_index = 0
#
# fig = plt.gcf()
# fig.set_size_inches(ncols * 4, nrows * 4)
#
# pic_index += 8
# next_daisy_pix = [os.path.join(daisy_dir, fname)
#                 for fname in train_daisy_names[pic_index-8:pic_index]]
# next_rose_pix = [os.path.join(rose_dir, fname)
#                 for fname in train_rose_names[pic_index-8:pic_index]]
#
# print ("Showing some daisy pictures...")
# print()
# for i, img_path in enumerate(next_daisy_pix):
#   # Set up subplot; subplot indices start at 1
#   sp = plt.subplot(nrows, ncols, i + 1)
#   sp.axis('Off') # Don't show axes (or gridlines)
#
#   img = mpimg.imread(img_path)
#   plt.imshow(img)
#
# plt.show()
#
# print ("Showing some rose pictures...")
# print()
# fig = plt.gcf()
# fig.set_size_inches(ncols * 4, nrows * 4)
# for i, img_path in enumerate(next_rose_pix):
#   # Set up subplot; subplot indices start at 1
#   sp = plt.subplot(nrows, ncols, i + 1)
#   sp.axis('Off') # Don't show axes (or gridlines)
#
#   img = mpimg.imread(img_path)
#   plt.imshow(img)
#
# plt.show()
#
# batch_size = 128
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
#
# # All images will be rescaled by 1./255
# train_datagen = ImageDataGenerator(rescale=1/255)
#
# # Flow training images in batches of 128 using train_datagen generator
# train_generator = train_datagen.flow_from_directory(
#         '/home/ashvin/Desktop/KerasImages/Flowers/flowers',  # This is the source directory for training images
#         target_size=(200, 200),  # All images will be resized to 200 x 200
#         batch_size=batch_size,
#         # Specify the classes explicitly
#         classes = ['daisy','dandelion','rose','sunflower','tulip'],
#         # Since we use categorical_crossentropy loss, we need categorical labels
#         class_mode='categorical')
#
# import tensorflow as tf
#
# model = tf.keras.models.Sequential([
#     # Note the input shape is the desired size of the image 200x 200 with 3 bytes color
#     # The first convolution
#     tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(200, 200, 3)),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     # The second convolution
#     tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
#     # The third convolution
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
#     # The fourth convolution
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
#     # The fifth convolution
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
#     # Flatten the results to feed into a dense layer
#     tf.keras.layers.Flatten(),
#     # 128 neuron in the fully-connected layer
#     tf.keras.layers.Dense(128, activation='relu'),
#     # 5 output neurons for 5 classes with the softmax activation
#     tf.keras.layers.Dense(5, activation='softmax')
# ])
#
# model.summary()
# from tensorflow.keras.optimizers import RMSprop
#
# model.compile(loss='categorical_crossentropy',
#               optimizer=RMSprop(lr=0.001),
#               metrics=['acc'])
#
# total_sample=train_generator.n
# n_epochs = 30
# history = model.fit_generator(
#         train_generator,
#         steps_per_epoch=int(total_sample/batch_size),
#         epochs=n_epochs,
#         verbose=1)
#
# plt.figure(figsize=(7,4))
# plt.plot([i+1 for i in range(n_epochs)],history.history['acc'],'-o',c='k',lw=2,markersize=9)
# plt.grid(True)
# plt.title("Training accuracy with epochs\n",fontsize=18)
# plt.xlabel("Training epochs",fontsize=15)
# plt.ylabel("Training accuracy",fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.show()
#
# plt.figure(figsize=(7,4))
# plt.plot([i+1 for i in range(n_epochs)],history.history['loss'],'-o',c='k',lw=2,markersize=9)
# plt.grid(True)
# plt.title("Training loss with epochs\n",fontsize=18)
# plt.xlabel("Training epochs",fontsize=15)
# plt.ylabel("Training loss",fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.show()
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('flower_model.h5', compile=True)
img_pred = Image.open('/home/ashvin/Desktop/KerasImages/Flowers/flowers/daisy/1374193928_a52320eafa.jpg')
plt.imshow(img_pred)
plt.show()

print(img_pred.size
      )
img_pred = img_pred.resize((200,200))

img_pred = np.expand_dims(img_pred, axis=0)


result = model.predict_classes(img_pred)
print(result)
# classes = np.argmax(result, axis = 1)
# print(classes)

if result[0] == 1:
    print("rose")
elif result[0] == 2:
    print("tulip")
elif result[0] == 3:
    print("dand")
elif result[0] == 4:
    print("sunflower")
else:
    print("daisy")

from keras.datasets import mnist
from keras.utils import to_categorical
from keras import layers
from keras import models
import numpy as np
import matplotlib.pyplot as plt

(trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()

trainImage = trainImage.reshape((60000, 28, 28, 1))
trainImage = trainImage.astype("float32") / 255

testImage = testImage.reshape((10000, 28, 28, 1))
testImage = testImage.astype("float32") / 255

trainLabel = to_categorical(trainLabel)
testLabel = to_categorical(testLabel)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(trainImage, trainLabel, epochs=10, batch_size=64)

test_loss, test_acc = model.evaluate(testImage, testLabel)
print("Test accuracy: {:.2f}%".format(test_acc * 100))



index = np.random.randint(0, len(testLabel))
image = testImage[index]

plt.imshow(image.reshape(28, 28), cmap="gray")
plt.show()

predictions = model.predict(np.expand_dims(image, axis=0))
predicted_label = np.argmax(predictions)

print("Predicted label:", predicted_label)


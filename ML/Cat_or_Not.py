from numpy import load
import keras
import tensorflow
import panda as pd
import json
import open-cv
from PIL import image
import warnings

# Warnings are for chumps
warnings.filterwarnings("ignore")

training_data = pd.read_csv("Training_Data.csv")
json_list = []

for index, row in training_data.iterrows():
    json_list.append(json.loads(row["Label"]))

## THIS IS ONE FILE
photos, labels = [], []
## Apply skim_image to the json links for the mask
## Create file structure as according to: https://towardsdatascience.com/a-keras-pipeline-for-image-segmentation-part-1-6515a421157d
## We want to make tuples out of the pictures and the classification -- can be done in this forloop
for item in json_list.keys():
    ## skim_image(item['instanceURI'], item['featureId']); ##remember to switch the path to the new directory for masks
    	output = 0.0
	if str(item["Title"])=="Cat":
		output = 1.0
	# load image via path & # # Id
    file = "/Training_data/" + str(item["featureId"]) + ".jpg"
    # Then pair them
	photo = load_img(file)
	# convert to numpy array
	photo = img_to_array(photo)
	# store
	photos.append(photo)
	labels.append(output)

# convert to a numpy arrays
labels = asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('cats_photos.npy', photos)
save('cats_labels.npy', labels)

## Ensure the file structure is correct
## dataset_dogs_vs_cats
## ├── test
## │   ├── cats
## │   └── not cats
## └── train
##     ├── cats
##     └── not cats

##THIS IS ONE FILE
# define cnn model
# 3 payers
def define_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(400, 400, 3)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(1, activation='sigmoid'))
	# compile model
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model


# plot diagnostic learning curves
def summarize_diagnostics(history):
	# plot loss
	pyplot.subplot(211)
	pyplot.title('Cross Entropy Loss')
	pyplot.plot(history.history['loss'], color='blue', label='train')
	pyplot.plot(history.history['val_loss'], color='orange', label='test')
	# plot accuracy
	pyplot.subplot(212)
	pyplot.title('Classification Accuracy')
	pyplot.plot(history.history['accuracy'], color='blue', label='train')
	pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
	# save plot to file
	filename = sys.argv[0].split('/')[-1]
	pyplot.savefig(filename + '_plot.png')
	pyplot.close()

# run the test harness for evaluating a model
def run_test_harness():
	model = define_model()
	datagen = ImageDataGenerator(rescale=1.0/255.0)
	train_it = datagen.flow_from_directory('cats/train/', class_mode='binary', batch_size=64, target_size=(200, 200))
	test_it = datagen.flow_from_directory('cats/test/', class_mode='binary', batch_size=64, target_size=(200, 200))
	history = model.fit_generator(train_it, steps_per_epoch=len(train_it), validation_data=test_it, validation_steps=len(test_it), epochs=20, verbose=0)
	_, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
	print('> %.3f' % (acc * 100.0))
	summarize_diagnostics(history)

# entry point, run the test harness
run_test_harness()

# make a prediction for a new image.
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
 
# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img
 
# load an image and predict the class
def run_example():
    # load the image
    img = load_image('weirdcat.jpg')
    # load model
    model = load_model('final_model.h5')
    # predict the class
    result = model.predict(img)
    if (result[0] == 0):
        print("Definetly a cat!")
    elif(result[0] <= 0.25):
        print("Probably a cat")
    elif(result[0]<=0.75):
        print("I am not sure!")
    elif(result[0]<1):
        print("Probably a Dog")
    elif(result[0]==1):
        print("Defiently a Dog!")
    print(result[0])



 
# entry point, run the example
run_example()
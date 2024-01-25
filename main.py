import tensorflow
import flask
import numpy as np
import cv2
from keras.models import Model
from flask import Flask, render_template, request
from keras.models import load_model
import keras.utils as image

app = Flask(__name__)

dic = {0 : 'Cat', 1 : 'Dog'}

model = load_model('model.h5')

model.make_predict_function()

def predict_label(img_path):
	#i = image.load_img(img_path, target_size=(256,256,3))
	#i = image.img_to_array(i)/255.0
	#i = i.reshape(1, 256,256,3)
	#pred = model.predict(i)
	#p=np.argmax(pred,axis=-1)
	  #print(dic[p[0]])
	
	#return dic[p[0]]
	#print(dic[int(pred[0][0])])
	#print("-------------------------------")
	#return dic[int(pred[0][0])]

	i=cv2.imread(img_path)
	i=cv2.resize(i,(256,256))
	i=i.reshape((1,256,256,3))
	pred=model.predict(i)
	print(dic[int(pred[0][0])])
	return dic[int(pred[0][0])]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)
		print("--------")
		print(p)
		print(img_path)
		print("----------------")
	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)


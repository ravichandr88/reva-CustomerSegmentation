import pickle 
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import render_template
from flask import request
import pickle
import pandas as pd

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/',methods=['GET', 'POST'])
def hello_world():
	if request.method == 'POST':
		data = pd.DataFrame({
			'Recency':0,
        'total_quantity' : [int(request.form['total_quantity'])],
     	'frequency' : [float(request.form['frequency'])]})

		pt = open('pt.pickle','rb')
		pt = pickle.load(pt)
		data = pd.DataFrame(pt.transform(data))

		print(data)

		kmeans = open('kmeans.pickle','rb')
		kmeans = pickle.load(kmeans)
		category = kmeans.predict(data[[1,2]])


		return render_template('kmeans.html', result = category[0])




	
	return render_template('kmeans.html')
    


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True, threaded=True)

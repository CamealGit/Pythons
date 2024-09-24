from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.datasets import load_iris

app = Flask(__name__)

with open('iris.pkl', 'rb') as file:
    model = pickle.load(file)

iris_data = load_iris()


@app.route('/', methods=['GET', 'POST'])
def home():
    species = None
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)
        species = iris_data.target_names[prediction[0]]

    return render_template('index.html', species=species)


if __name__ == '__main__':
    app.run(debug=True)
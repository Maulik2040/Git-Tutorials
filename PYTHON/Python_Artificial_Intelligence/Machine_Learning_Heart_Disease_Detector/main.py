from flask import Flask, render_template, request
import pickle

file = open('model.pkl', 'rb')

clf = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method=="POST":
        myDict = request.form
        bloodPreasure = int(myDict['bloodPreasure'])
        Age = int(myDict['Age'])
        inputFeatures = [bloodPreasure, Age]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        return render_template('show.html', inf=round(infProb * 100))
    return render_template('index.html')

app.run(debug=True)
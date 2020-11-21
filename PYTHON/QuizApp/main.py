from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import time
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/quizeapp'
db = SQLAlchemy(app)

class questions(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.String(255), nullable=False)
    que_opt1 = db.Column(db.String(255), nullable=False)
    que_opt2  = db.Column(db.String(255), nullable=False)
    que_opt3  = db.Column(db.String(255), nullable=False)
    quet_opt4  = db.Column(db.String(255), nullable=True)
    answer  = db.Column(db.String(255), nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/topic')
def topic():
    return render_template('topic.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/quize/<sno>', methods=['GET', 'POST'])
def quize(sno):
    page = request.args.get('page')
    question = questions.query.filter_by(sno=sno).first()
    question1 = questions.query.filter_by().all()
    score = 0
    if request.method=='POST':
        # print(len(question1))
        answer = request.form.get('option')
        if answer == question.answer:
            question_next = int(sno)
            for i in range(0, int(len(question1))):
                time.sleep(1)
                return redirect(f"/quize/{question_next+1}")
                if question_next>len(question1) and question_next==None:
                    break;
                    return redirect('/dashboard')
            # if (question_next>int(len(question1))):
            #     return redirect('/dashboard')
    return render_template('quize.html', questions=question)

app.run(debug=True)
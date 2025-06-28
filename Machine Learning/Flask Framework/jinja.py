# Building URL Dynamically 
# Variable Rule
# Jinja 2 Template Engine

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is " + str(score)

# Building Dynamic URLS:
@app.route('/new/<int:score>')
def new(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html', results = res)


@app.route('/successres/<int:score>')
def success_res(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
        
    exp = {'score':score, 'res':res}
        
    return render_template('result1.html', results = exp)

if __name__ == "__main__":
    app.run(debug=True)
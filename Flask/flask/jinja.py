from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to this flask course</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,"result":res}
    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))


if __name__=="__main__":
    app.run(debug=True)
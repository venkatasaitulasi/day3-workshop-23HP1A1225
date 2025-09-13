from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1>this is about page</h1>"

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/student/<int:id>/<string:name>/<int:age>/<int:marks>')
def student(id, name, age,marks):
    if age>=18:
        eligibility = "Eligibility"
    else :
        eligibility = "Not Eligibility"    
    if marks>=500 and marks<=600:
        result="Pass"
        grade='A'
    elif marks>=400 and marks<=500:
        result="Pass"
        grade='B'
    elif marks>=300 and marks<=400:
        result="Pass"
        grade='C'
    else:
        result="Fail"
        grade='F'
    return render_template('student.html',rollno=id,fullname=name,age=age,status = eligibility,result=result,grade=grade)
    

if __name__ == '__main__':
    app.run(debug=True,port=3500)

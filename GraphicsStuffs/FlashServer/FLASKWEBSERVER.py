from flask import Flask,render_template,redirect

app = Flask(__name__)
@app.route('/')
def home():
    #return <h1>HELLO</h1>
    return render_template('TEST.html')
@app.route('/Test')
def page_2():
    return render_template('DECORATEDPAGE.html')
app.run()
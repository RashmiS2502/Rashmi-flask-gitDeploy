from flask import Flask
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def hello():
    return render_template('index.html')
 
 
@app.route('/intro')
def about():
    return render_template('index.html')
 
 
@app.route('/menu')
def menu():
    return render_template('index.html')
 
@app.route('/history')
def history():
    return render_template('index.html')
 
 
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello():
    return "Hi this is my 1st deployment"
 
 
@app.route('/intro')
def about():
    return "My name is Rashmi"
 
 
@app.route('/home')
def home():
    return "I am home"
 
 
 
 
if __name__ == '__main__':
    app.run(debug=True)

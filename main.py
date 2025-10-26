from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
#app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/details")
def details():
    return render_template("details.html")

if __name__ == '__main__':
    app.run(debug=True)


    #<--! style="background-image: url({{url_for('static',filename ='images/lake.jpg')}}); -->
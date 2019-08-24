from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there Johan Gotting and GCP and App Engine!!!"
if __name__ == '__main__':
    app.run(debug=True)
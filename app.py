from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
  return "Hello, World!"


if __name__ == '__main__':
  # print("I am inside the if block")
  app.run(host='0.0.0.0', debug=True)

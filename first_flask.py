#para poder importarlo en bubuntu
#apt-get install python3-pip
#pip3 install flask
#sudo apt-get install python3-distutils


from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
   return "¡Hola Mundo!"

if __name__ == "__main__":
   app.run()

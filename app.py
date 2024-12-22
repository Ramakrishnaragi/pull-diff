from flask import Flask
import os
<<<<<<< HEAD
import boto6
=======
import boto5
>>>>>>> d4ec421839b7bf08fe5314e3798466c2139056e9
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

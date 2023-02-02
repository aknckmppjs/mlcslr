from flask import Flask,request,app,jsonify,render_template
import dill
import numpy as np

app=Flask(__name__)

# Load saved model
slrm=dill.load(open('slrm.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ack', methods=['POST']) 
def ack():
    return "Acknowledgement"

@app.route('/pred/<float:inp>')
def pred(inp):
    data=np.array(float(inp)).reshape(1,-1)
    y_pred=slrm.predict(data)
    return (str(y_pred[0][0]))

@app.route('/predt',methods=['POST'])
def predt():
    data=[float(x) for x in request.form.values()]
    input=np.array(data).reshape(1,-1)
    y_pred=slrm.predict(input[0])
    output = str(round(y_pred[0][0],ndigits=2))
    return render_template("home.html",prediction_text="PREDICTION: {}".format(output))

@app.route("/batch", methods=["POST"])
def batch():
    data = request.get_json()
    X_pred = np.array(data["X"])
    output=slrm.predict(X_pred)
    y_pred = [y[0] for y in output.tolist()]
    return jsonify({"y_pred":y_pred})

@app.route("/stream", methods=["POST"])
def stream():
    data=np.array(float(request.data)).reshape(1,-1)
    y_pred=slrm.predict(data)
    return (str(y_pred[0][0]))

if __name__=="__main__":
    app.run(debug=True)
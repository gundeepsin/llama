from flask import Flask , request, render_template
import json
import btc_short as pp

global input1, input2,input3,input4

app = Flask(__name__)

@app.route("/")
def u():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def qw():
    global input1, input2,input3,input4
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    input4 = request.form['input4']
    pp.main(input1,input2,input3,input4)
    return render_template('index.html')  

    
    
if __name__ == "__main__":
    app.run()

#python -m flask --app app run --debug

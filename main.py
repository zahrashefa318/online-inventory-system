from flask import render_template
from inventory import createFlask

app=createFlask()
@app.route('/')
def home():
    return render_template('base.html')



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000) 

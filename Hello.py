from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return "Hello %s" % name

@app.route('/')
def home():
    return 'This is home'

@app.route('/user/<name>')
def user_name(name):
    if name == 'admin':
        return redirect(url_for('hello_world',name = name))
    else:
        return redirect(url_for('home'))

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name = user))

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name
    
if __name__ == '__main__':
    #enabling debugging mode
    app.debug = True
    app.run()
    app.run(debug=True)


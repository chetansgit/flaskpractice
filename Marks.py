from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'Physics' : 77, 'Chem' : 90, 'maths' : 80}
    return render_template('result.html', result = dict)

if __name__ == '__main__':
    #enabling debugging mode
    app.debug = True
    app.run()
    app.run(debug=True)
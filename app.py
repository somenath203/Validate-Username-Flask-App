from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/username-form')
def usernameForm():
    return render_template('username_form.html')


@app.route('/result')
def result():

    enteredUserName = request.args.get('uname')

    endsWithNumber = False
    isUpperCase = False
    isLowerCase = False

    isLowerCase = any(username_letter.islower() for username_letter in enteredUserName) 

    isUpperCase = any(username_letter.isupper() for username_letter in enteredUserName) 

    endsWithNumber = enteredUserName[-1].isdigit();

    

    return render_template('result.html', user_name=enteredUserName, lowercase=isLowerCase, uppercase=isUpperCase, endwithno=endsWithNumber) 


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

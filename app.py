from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route('/login')
def login():
#	error = None
#	if request.method == 'POST':
#		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#			error = 'Invalid credentials. Please try again'
#		else:
#			return render_template('welcome.html') #redirect(url_for('welcome'))
    	return render_template('login.html')#, error=error)

@app.route('/homepage')
def homepage():
	return render_template('homepage.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0')

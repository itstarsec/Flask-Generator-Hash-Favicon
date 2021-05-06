from flask import Flask, redirect, url_for, request, render_template
import bim
app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html', e=error), 500
#	return "Wrong favicon link, please try again!"
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/<name>')
def generator(name):
#	return 'http.favicon.hash:"%s"' % name
	return render_template('generator.html',name=name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['url']
      hashed_int = bim.test(user)
      return redirect(url_for('generator',name = hashed_int))
   else:
      user = request.args.get('url')
      hashed_int = bim.test(user)
      return redirect(url_for('generator',name = hashed_int))
if __name__ == '__main__':
	app.run(debug = False)

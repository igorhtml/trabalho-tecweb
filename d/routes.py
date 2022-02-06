# #Teste de rotas 1

# from flask import render_template
# from flask import Flask

# app = Flask(__name__)

# @app.route('/product/<name>')
# def get_product(name):
#     return "The product is " + str(name)

# app.run(host='0.0.0.0', port=81)

# ---------------------------------------------------------
# Teste de rotas 2

# from flask import render_template
# from flask import Flask

# app = Flask(__name__)

# @app.route('/create/<first_name>/<last_name>')
# def create(first_name=None, last_name=None):
#     return 'Hello ' + first_name + ',' + last_name

# app.run(host='0.0.0.0', port=81)

#----------------------------------------------------------
#Teste 3 rotas


from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)
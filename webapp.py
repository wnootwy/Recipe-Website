from flask import Flask, request, render_template
import RecipeDB
import numpy as np
app = Flask(__name__)

@app.route('/') #Render html template for the login page
def logIn():
    return render_template("login.html")
@app.route('/index.html', methods = ['GET','POST'])
def validate():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        result = RecipeDB.result
        if username in result:
            resultIndex = int(np.where(result == username)[0])
            if password == result[resultIndex][1]:
                return render_template("index.html")  ### Maybe return user_id as well in the future in order to have different views for the user and the admin user.
            elif password != result[resultIndex][1]:
                return render_template("loginfailed.html")
        elif username not in result:
            return render_template("loginfailed.html")

@app.errorhandler(404)
def pageNotFound():
    pass
    #return render_template("pagenotfound.html")
@app.errorhandler(500)
def serverError():
    pass
    #return render_template("servererror.html")

if __name__ == '__main__':
    app.run()

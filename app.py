from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/homepage', methods=['GET', 'POST'])
def info():
   if request.method == 'GET':
       print("We received GET")
       return render_template("homepage.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
   

@app.route('/contact', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        message = request.form['message']
        print(f"Received message: {message}") 
        return "Message received!"

    
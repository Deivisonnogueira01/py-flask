from flask import Flask, render_template, request
from random import random

app = Flask(__name__)
name_list = []

 
@app.route("/")    
def teti_lessons():
    return render_template("teti_deivison.html")


@app.route("/initial-template")
def initial_template():
    return "<h3>Olá Devs Seja Bem vindo ao minha Página Web!</h3>"


@app.route("/data-manipulation")
def data_manipulation():
    students_list = ["Deivison", "Geo", "Eduardo", "Vinicius", "Alexandre"]
    return render_template("index.html", students_list=students_list)


@app.route("/cadastro", methods=["GET", "POST"]) 
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")
    if request.method == "POST":
        name = request.form.get('Name')
        return render_template("cadastro.html", name=name)


@app.route("/list", methods=["GET"])
def list():
    if request.method == "GET":
        name_list.clear()
        return render_template("list.html")


@app.route("/add-name", methods=["POST"])
def add_name():
    if request.method == "POST":
        name = request.form.get('Name')
        name_list.append(name)
        return render_template("list.html", name_list=name_list)

  
@app.route("/calculator", methods=["GET", "POST"])
def simple_calculator():
    if request.method == "GET":
        return render_template("calculator.html")
    if request.method == "POST":
        expression = request.form.get('expression')
        expression = expression.replace('÷','/').replace('𝗑', '*').replace(',', '.')
        try:
            result = eval(expression)
            binnary = bin(int(result)).removeprefix('0b')
            mensage = None
        except: 
            mensage = 'Verifique se digitou corretamente'
            result = binnary = None
        return render_template("calculator.html", result=result, binnary=binnary, mensage=mensage)


@app.route("/alnum-calc", methods=["GET", "POST"]) 
def alphanum_calculator(): 
    if request.method == "GET":
        return render_template("alnum_calc.html")
    if request.method == "POST":
        expression = request.form.get('expression')
        try:
            binnary = ''.join(format(ord(caractere), '08b') for caractere in expression)
            size = len(binnary)
            separator = 480
            array_2d = [[binnary[n:n + separator]] for n in range(0, size, separator) if n < size]
            mensage = False
        except:
            mensage = True
            binnary = None
        return render_template("alnum_calc.html", binnary=array_2d, mensage=mensage)


@app.route("/array_divs_1_pixel")
def array_divs_1_pixel():
    return render_template("array_divs_1_pixel.html")


@app.route("/array_divs_1_pixel_colored")
def array_divs_1_pixel_colored():
    row = lambda: [f'#{round(random() * 0xffffff):06X}' for _ in range(512)]
    col = [row() for _ in range(512)]
    return render_template("array_divs_1_pixel_colored.html", colors=col)






<<<<<<< HEAD
if __name__ == '__main__': 
   app.run(debug = True)    
=======
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
#    app.run(debug = True)
>>>>>>> 2d5b0afe34fed9fcae6cfb7dd2aa30e6af51cbb1

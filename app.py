#Finally let's code something in python!
from flask import Flask, render_template, request
app = Flask(__name__)
menu = [
    {"name": "Espresso", "price": 250},
    {"name": "Macha Latte", "price": 350},
    {"name": "Cappuccino", "price": 300},
    {"name": "Americano", "price": 200},
]
@app.route("/", methods=["GET", "POST"])
def home():
    ordered_items = []
    total = 0
    if request.method == "POST":
        choice = request.form.getlist("items")
        for i in choice:
            item = menu[int(i)]
            ordered_items.append(item)
            total += item["price"]
    return render_template("index.html", menu=menu, ordered_items=ordered_items, total=total)
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
app = Flask(__name__)
menu = [
    {"name": "Espresso", "price": 250},
    {"name": "Macha Latte", "price": 350},
    {"name": "Cappuccino", "price": 300},
    {"name": "Americano", "price": 200},
]
@app.route("/", methods=["GET", "POST"])
def home():
    ordered_items = []
    total = 0
    if request.method == "POST":
        choice = request.form.getlist("items")
        for i in choice:
            item = menu[int(i)]
            ordered_items.append(item)
            total += item["price"]
    return render_template("index.html", menu=menu, ordered_items=ordered_items, total=total)
if __name__ == "__main__":
    app.run(debug=True)


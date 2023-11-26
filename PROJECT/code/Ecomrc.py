from flask import Flask, render_template, request

app = Flask(__name__)

# Data produk (bisa disimpan di basis data)
products = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Mouse", "price": 20},
    {"id": 3, "name": "Keyboard", "price": 50},
    # Tambahkan produk lainnya
]


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/checkout", methods=["POST"])
def checkout():
    selected_products = request.form.getlist("product")
    total_price = sum(
        [
            product["price"]
            for product in products
            if str(product["id"]) in selected_products
        ]
    )
    return render_template("checkout.html", total_price=total_price)


if __name__ == "__main__":
    app.run(debug=True)

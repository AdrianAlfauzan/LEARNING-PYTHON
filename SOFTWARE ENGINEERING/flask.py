# Import modul Flask
from flask import Flask, render_template, request, redirect, url_for

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Daftar tugas sederhana
tasks = []


# Tampilan daftar tugas
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


# Menambahkan tugas baru
@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    tasks.append(task)
    return redirect(url_for("index"))


# Menjalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)

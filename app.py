from flask import Flask, render_template

@app.route("/todo")
def todo():
    return render_template("todo.html")

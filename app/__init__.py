#coding:utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

def r_render(tmplt, env={}):
    return render_template(tmplt, env=env)

@app.route("/")
def mainpage():
    return r_render('index.html')

if __name__ == "__main__":
    app.run()

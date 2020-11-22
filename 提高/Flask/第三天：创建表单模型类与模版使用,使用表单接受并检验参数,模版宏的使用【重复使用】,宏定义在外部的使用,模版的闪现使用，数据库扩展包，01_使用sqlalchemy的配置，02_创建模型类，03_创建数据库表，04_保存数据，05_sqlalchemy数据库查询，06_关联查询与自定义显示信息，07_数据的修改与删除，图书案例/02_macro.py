# coding:utf-8

from flask import Flask, render_template, flash


app = Flask(__name__)

flag = True

app.config["SECRET_KEY"] = "SDHFOSDF"


@app.route("/")
def index():

    if flag:
        # 添加闪现信息
        flash("hello1")
        flash("hello2")
        flash("hello3")
        global flag
        flag = False

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)



# flash和它的名字一样，是闪现，意思就是我们的消息只会显示一次，当我们再次刷新也面的时候，它就不存在了，而正是这点，它经常被用来显示一些提示消息，比如登陆之后，显示欢迎信息等

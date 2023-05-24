from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        user = request.form["money"]
        return redirect(url_for("show_user_profile", money=user))
    return render_template('cover.html')

@app.route('/pay/<money>')
def show_user_profile(money):
    return render_template('web.html', money=money)
# @app.route('/pay')
# def show_user_profile(money):
#     return render_template('web.html', money=[money])
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

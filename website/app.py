from flask import Flask, render_template, request, redirect, url_for
import webbrowser, threading, sys
app = Flask(__name__)
mon = 'none'
num = 0

@app.route('/', methods=["POST","GET"])
def index():
    # print('a')
    if request.method == "POST":
        user = request.form["money"]
        print(user)
        return redirect(url_for("show_user_profile", money=user))
    return render_template('cover.html')

@app.route('/pay/<money>')
def show_user_profile(money):
    global mon
    print(str(money))
    mon = 'pay' + str(money)
    # return str(money)

    return render_template('web.html', money=money)
# @app.route('/pay')
# def show_user_profile(money):
#     return render_template('web.html', money=[money])

def run_web():
    global num
    print(num)
    print('run_web')
    if num == 0:
        num += 1
        app.run(host='127.0.0.1', port=5000, debug=False)
    else:
        return

def open_web():
    webbrowser.open('http://127.0.0.1:5000')


if __name__ == "__main__":
    # thread = threading.Thread(target=run_web)
    # thread2 = threading.Thread(target=open_web, )
    # thread.daemon = True
    # thread2.daemon = True
    # thread.start()
    # thread2.start()
    # while mon == 'none':
    #     pass
    # print(mon)
    # # thread.join()
    # # thread2.join()

    # sys.exit()
    app.run(host='127.0.0.1', port=5000, debug=False)

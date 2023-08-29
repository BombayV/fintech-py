# THIS IS THE CONTROLLER / WAITER DIRECTING TRAFFIC 🚦
# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
import model

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "GET":
        return "You're supposed to send a POST request"
    else:
        nickname = request.form["nickname"]
        birthmonth = request.form["birthmonth"].capitalize()
        birthstone = model.get_birthstone(birthmonth)

        rendered_data = f'<p>Your nickname is {nickname}</p>' + f'<p>Your birthmonth is {birthmonth.capitalize()}</p>' + f'<p>Your birthstone is {birthstone}</p>' + f'<img style="width: 25%" src="/static/images/{birthstone.lower()}.jpg" alt="birthstone image">'
        if not birthstone:
            rendered_data = f'<p>Sorry {nickname}. We couldn\'t find a stone for your birthmonth ({birthmonth}).'

        return render_template('results.html', nickname=nickname, birthmonth=birthmonth, birthstone=birthstone, rendered_data=rendered_data)


if __name__ == '__main__':
    app.run(debug=True)

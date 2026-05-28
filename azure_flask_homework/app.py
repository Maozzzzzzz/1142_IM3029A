from flask import Flask, render_template, request
from markupsafe import escape
from flask import Flask, render_template, request

app = Flask(__name__)

# 修正後的 Ex 45 路由：不用 escape，直接回傳字串
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# ===== Ex 45: URL Info =====
# 路由位置：/user/<username>
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

# ===== Ex 46: Flask Load HTML =====
# 路由位置：/home 與 /Apple
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Apple')
def apple():
    return render_template('apple.html')

# ===== Ex 47: Show Variables =====
# 路由位置：/page/app
@app.route('/page/app')
def pageAppInfo():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('page42.html', x=x, text="Python Flask !")

# ===== Ex 48: Show double of the inputted number =====
# 路由位置：/double (這是 Ex48 的首頁)
@app.route("/double")
def double_index():
    return render_template("index.html", result=None)

# 路由位置：/predict (負責處理 Ex48 表單送出的計算)
@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

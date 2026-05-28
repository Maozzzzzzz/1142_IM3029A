from flask import Flask, render_template, request

app = Flask(__name__)

# ===== Ex 43 & Ex 44: 首頁 =====
@app.route('/')
def hello():
    return "Hello, World! This is Morris's Flask App."

# ===== Ex 45: URL Info (就是這裡！幫你補回來了) =====
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

# ===== Ex 46: 讀取 HTML 網頁 =====
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Apple')
def apple():
    return render_template('apple.html')

# ===== Ex 47: 傳送變數給網頁 =====
@app.route('/page/app')
def page_app_info():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('page42.html', x=x, text="Python Flask !")

# ===== Ex 48: 雙倍計算機 =====
@app.route("/double")
def double_index():
    return render_template("index.html", result=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        x = int(request.form["x"])
        result = x * 2
    except:
        result = "請輸入有效的整數"
    return render_template("index.html", result=result)

# ===== 啟動伺服器設定 (Render 專用) =====
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
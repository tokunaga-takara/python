from flask import Flask, request,render_template
import MySQLdb
import mysql.connector

app = Flask(__name__)

# 接続する
conn = MySQLdb.connect(
user='root',
passwd='root',
host='localhost',
db='mysql',
# テーブル内部で日本語を扱うために追加
charset='utf8'
)

# カーソルを取得する
cursor = conn.cursor()

# login処理です
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        return render_template('form.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

@app.route('/logincheck', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # テーブルの初期化
    cursor.execute("DROP TABLE IF EXISTS userdata")

    # テーブルの作成
    cursor.execute("""CREATE TABLE userdata(
        id INT(11) AUTO_INCREMENT NOT NULL, 
        name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci, 
        age INT(3) NOT NULL,
        password VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci, 
        PRIMARY KEY (id)
        )""")

    # データの追加
    cursor.execute("""INSERT INTO userdata (name, age, password)
        VALUES ('taro', '25', '12345678'),
        ('jiro', '23', 'abcdefgh'),
        ('saburo', '21', '1111aaaa')
        """)

    # 一覧の表示
    cursor.execute(f"SELECT COUNT(*) FROM userdata WHERE name = '{username}' AND password = '{password}'")

    row = cursor.fetchone()
    if row[0] > 0:
        url = 'logins.html'
    else:
        url = 'loginf.html'

    conn.commit()

    cursor.close

    # 接続を閉じる
    conn.close
    return render_template(f"{url}")

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    app.run(port = 8000, debug=True)

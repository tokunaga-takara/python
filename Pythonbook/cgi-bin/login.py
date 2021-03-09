import cgi
import codecs
import sqlite3
import sys

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

form = cgi.FieldStorage()
user = form.getfirst('user')
password = form.getfirst('password')

con = sqlite3.connect('shop.db')
cur = con.cursor()
cur.execute("SELECT * FROM account WHERE user=? AND password=?", (user, password))
result = 'Welcome!' if list(cur) else 'Failed.'
con.close()

print(f'''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Result</title>
</head>
<body>
{result}
</body>
</html>
''')

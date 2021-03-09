import bottle

html = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Bottle</title>
</head>
<body>
{}
</body>
</html>
'''

@bottle.route('/hello')
def welcome():
    return html.format('Hello!')

@bottle.route('/bye')
def bye():
    return html.format('Bye!')

bottle.run(host='localhost', port=8000)

import bottle
import os

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

@bottle.route('/')
def index():
    return html.format('''
    <form action="/upload" method="post" enctype="multipart/form-data">
    <p><input type="file" name="file"></p>
    <p><input type="submit" value="Upload"></p>
    </form>
    ''')

@bottle.route('/upload', method='post')
def upload():
    file = bottle.request.files.file
    if file:
        os.makedirs('uploaded', exist_ok=True)
        file.save('uploaded', overwrite=True)
        return html.format(f'''
        <p>Uploaded.</p>
        <p><img src="/uploaded/{file.filename}"></p>
        ''')
    else:
        return html.format('''
        <p>Choose a file and try again.</p>
        ''')

@bottle.route('/<file:path>')
def static(file):
    return bottle.static_file(file, root='.')

bottle.run(host='localhost', port=8000)

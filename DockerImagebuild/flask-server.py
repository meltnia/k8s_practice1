from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)
FILE_DIR = '/flask_download'  # 공유 디렉토리 경로

HTML_TEMPLATE = '''

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>File Download Page</title>
</head>
<body>
    <h2>Available Files</h2>
    <table border="1">
        <tr><th>Name</th><th>Download</th></tr>
        {% for file in files %}
        <tr>
            <td>{{ file }}</td>
            <td><a href="/download/{{ file }}" download>Download link</a></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def index():
    try:
        files = os.listdir(FILE_DIR)
        files = sorted(files)  # 정렬(Optional)
    except FileNotFoundError:
        files = []
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(FILE_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

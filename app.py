from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

DOCUMENTS_DIR = os.path.join(os.path.dirname(__file__), 'documents')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/documents/<path:filename>')
def download_doc(filename):
    return send_from_directory(DOCUMENTS_DIR, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

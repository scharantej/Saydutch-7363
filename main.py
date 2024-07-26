
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

sayings = []

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/add_saying', methods=['POST'])
def add_saying():
    english_saying = request.form['english_saying']
    dutch_translation = request.form['dutch_translation']
    sayings.append({
        'english_saying': english_saying,
        'dutch_translation': dutch_translation
    })
    return redirect(url_for('get_translations'))

@app.route('/get_translations')
def get_translations():
    return render_template('translations.html', sayings=sayings)

@app.route('/static_files/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run()

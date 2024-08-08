from flask import Flask
from utils import scores_file_name
import os

app = Flask(__name__)


def score_server():
    try:
        if not os.path.exists(scores_file_name):
            with open(scores_file_name, 'w') as file:
                file.write('0')
        with open(scores_file_name, 'r') as file:
            score = file.read()

        html = f'<html><head><title><Scores Game</title><head><body><h1>The score is: {score}</h1></body></html>'
        return html
    except Exception as e:
        error_html: str = (f"<html><head><title><Scores Game</title><head><body><h1>ERROR: {e}</h1><div id=\"score\" "
                           f"style=\"color:red\">{e}</div></body"
                           f"></html>")
        return error_html


@app.route('/')
def show_score():
    return score_server()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

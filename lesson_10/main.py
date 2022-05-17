import utils
import vzuali
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def candidates_get_all():
    candidates = utils.candidates_get_all()
    html_code = vzuali.function_2(candidates)
    return html_code


@app.route("/skills/<skill_name>")
def candi_skill(skill_name):
    candidates = utils.candi_skill(skill_name)
    html_code = vzuali.function_2(candidates)
    return html_code


@app.route("/candidates/<int:id>")
def candi_pk(id):
    candidate = utils.candi_pk(id)
    if candidate is None:
        return "Такого кандидата нет"
    html_code = vzuali.function_1(candidate)
    return html_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)


from flask import*
import markdown
import os
from json import loads

app = Flask(__name__)

directory_path = "articles"

def load_info():
    with open("info.json") as info:
        return loads(info.read())

def load_articles():
    folders = [item for item in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, item))]
    articles = [{}]

    for i, folder in enumerate(folders):
        with open(f"articles/{folder}/info.json") as json:
            articles.append(loads(json.read()))
    
    return articles[1:], folders

@app.route("/")
def index():
    articles, folders = load_articles()
    
    return render_template("index.html", info=load_info(), articles=articles, folders=folders)

@app.route("/article/<article>")
def sarticle(article):
    json = None

    with open(f"articles/{article}/info.json") as json:
        json = loads(json.read())
    with open(f"articles/{article}/index.md") as carticle:
        content = carticle.read()
        return render_template("article.html", info=load_info(), content=markdown.markdown(content), title=json["title"], date=json["date"], writer=json["writer"])

if __name__ == '__main__':
    app.run(port=5123, debug=True)
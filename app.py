from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    quote = data['content']
    author = data['author']
    return render_template('quote.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
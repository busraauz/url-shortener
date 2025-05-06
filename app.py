from flask import Flask, render_template, redirect, request

from service import URLShortener

app = Flask(__name__)

url_shortener = URLShortener()

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    long_url = request.form['long_url']
    short_url = url_shortener.create_short_url(long_url)
    return render_template('index.html', short_url = short_url)
  return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
  long_url = url_shortener.get_long_url(short_url)
  if long_url:
    return redirect(long_url)
  return "URL NOT FOUND", 404

if __name__ == "__main__":
  app.run(debug=True)
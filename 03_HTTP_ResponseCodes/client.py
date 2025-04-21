from flask import Flask, request, redirect

app = Flask(__name__)

# Example of open redirect vulnerability when called with http://127.0.0.1:5000/redirect?url=https://example.com


@app.route('/redirect')
def unsafe_redirect():
    url = request.args.get('url')  # User-controlled input
    return redirect(url, code=302)  # Redirects without validation


if __name__ == '__main__':
    app.run(debug=True)

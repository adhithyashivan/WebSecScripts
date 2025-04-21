from flask import Flask, request, redirect, abort
import re

app = Flask(__name__)

'''
This example will work for http://127.0.0.1:5000/redirect?url=https://example.com as it is whitelisted.

But, it will give 400 Bad request for http://127.0.0.1:5000/redirect?url=https://malicious-site.com since it is not part of the allowed domains.
'''


@app.route('/redirect')
def safe_redirect():
    url = request.args.get('url')

    # Allow only whitelisted domains
    allowed_domains = ["example.com", "mywebsite.com"]
    if not any(domain in url for domain in allowed_domains):
        return abort(400)  # Bad request

    return redirect(url, code=302)


if __name__ == '__main__':
    app.run(debug=True)

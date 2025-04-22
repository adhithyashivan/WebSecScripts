from flask import Flask, request, Response
import datetime

app = Flask(__name__)

# Simulated resource with last modified timestamp
LAST_MODIFIED = datetime.datetime(2025, 4, 20, 12, 0, 0)

'''
Test Scenario 1: curl -i http://127.0.0.1:5000/resource
Returns 200 OK with Updated content here.

Test Scenario 2: curl -i -H "If-Modified-Since: Sun, 20 Apr 2025 12:00:00 GMT" http://127.0.0.1:5000/resource
Returns 304 Not Modified even if resource is updated.
'''


@app.route('/resource')
def cached_resource():
    """Simulates a resource with incorrect handling of 304 Not Modified."""
    client_last_modified = request.headers.get('If-Modified-Since')

    if client_last_modified:
        # Simulating incorrect handling: Always returning 304 even if resource is updated
        return Response(status=304)

    response = Response("Updated content here", status=200)
    response.headers['Last-Modified'] = LAST_MODIFIED.strftime(
        "%a, %d %b %Y %H:%M:%S GMT")
    return response


if __name__ == '__main__':
    app.run(debug=True)

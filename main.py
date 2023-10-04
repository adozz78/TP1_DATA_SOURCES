from flask import Flask, render_template
import logging

app = Flask(__name__)


@app.route('/')
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-7E4M7T0YEB"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-7E4M7T0YEB');
    </script>
    """
    return prefix_google + "Hello World"

@app.route('/logger')
def logger():
    
    # Print a log on Python console
    print('This is a log message in Python.')

    # Print a log on the browser
    log_browser = '<script>console.log("Log message from browser");</script>'
    return log_browser

if __name__ == '__main__':
    app.run(debug=True)





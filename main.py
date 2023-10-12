from flask import Flask, render_template, request
import requests



app = Flask(__name__)


@app.route('/', methods=['GET'])
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

    button_ga = """
    <form method="GET" action="/perform-google-request">
        <input type="submit" value="Make Google Analytics Request">
    </form>
    """

    button_cookies = """
    <form method="GET" action="/display-cookies">
        <input type="submit" value="Display Google Analytics cookies">
    </form>
    """

    return prefix_google + "Hello World" + button_ga + button_cookies 

@app.route('/logger', methods=['GET', 'POST'])
def logger():

    if request.method == 'POST':
        log_message = request.form['log_message']
        
        # Print the log message on the server-side (Python)
        app.logger.warning(f"Log message from Python: {log_message}")

        # Create JavaScript code to log a message on the browser's console
        log_browser = f'<script>console.log("Log message from browser: {log_message}");</script>'
        
        return log_browser
    
    
    # Render a simple HTML form to input the log message
    return """
    <form method="POST">
        Log Message: <input type="text" name="log_message">
        <input type="submit" value="Log">
    </form>
    """

@app.route('/perform-google-request', methods=['GET'])
def perform_google_request():

    req = requests.get("https://analytics.google.com/analytics/web/#/p407458242/reports/intelligenthome?params=_u..nav%3Dmaui")

    return req.text

@app.route('/display-cookies', methods=['GET'])
def display_cookies():

    req_cookies = requests.get("https://analytics.google.com/analytics/web/#/p407458242/reports/intelligenthome?params=_u..nav%3Dmaui")

    return req_cookies.cookies.get_dict()
    


if __name__ == '__main__':
    app.run(debug=True)





from flask import Flask, render_template
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='server_log.log', level=logging.DEBUG)

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
    # Log a message on the server-side (Python)
    logging.info("Log message from Python")

    # Create JavaScript code to log a message on the browser's console
    log_browser = """
    <script>
    console.log("Log message from browser");
    </script>
    """
    
    return "Logging example. Check the server log and browser console." + log_browser

if __name__ == '__main__':
    app.run(debug=True)





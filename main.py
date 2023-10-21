from flask import Flask, render_template, request, jsonify
import requests
import os
# from google.auth.transport.requests import Request
# from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from pytrends.request import TrendReq


app = Flask(__name__)

KEY_FILE_LOCATION = 'ozanneproject-62622dbbd123.json'


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

    button_ga_auth = """
    <form method="GET" action="/perform-google-request2">
        <input type="submit" value="Number of visitors">
    </form>
    """

    button_google_trend = """
    <form method="GET" action="/google-trends">
        <input type="submit" value="Google trends Data">
    </form>
    """

    button_chart = """
    <form method="GET" action="/chart">
        <input type="submit" value="Google trends Charts">
    </form>
    """

    return prefix_google + "Hello World" + button_ga + button_cookies + button_ga_auth + button_google_trend + button_chart

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

@app.route('/perform-google-request2', methods=['GET'])
def perform_google_request2():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = KEY_FILE_LOCATION
    PROPERTY_ID = '407458242'

    starting_date = "30daysAgo"
    ending_date = "yesterday"

    client = BetaAnalyticsDataClient()
    
    def get_visitor_count(client, property_id):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[{"start_date": starting_date, "end_date": ending_date}],
            metrics=[{"name": "activeUsers"}]
        )
        response = client.run_report(request)

        return response

    visitor_count = get_visitor_count(client, PROPERTY_ID)

    return f'Number of visitors : {visitor_count}'

@app.route('/display-cookies', methods=['GET'])
def display_cookies():

    req_cookies = requests.get("https://analytics.google.com/analytics/web/#/p407458242/reports/intelligenthome?params=_u..nav%3Dmaui")

    return req_cookies.cookies.get_dict()

@app.route('/google-trends', methods=['GET'])
def google_trends():

    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = ["Kamaru Usman", "Alexander Volkanovski"]
    pytrends.build_payload(keywords, timeframe='today 12-m', geo='US')
    interest_over_time_df = pytrends.interest_over_time()

    data = {
        'dates': interest_over_time_df.index.strftime('%Y-%m-%d').tolist(),
        'Kamaru Usman': interest_over_time_df['Kamaru Usman'].tolist(),
        'Alexander Volkanovski': interest_over_time_df['Alexander Volkanovski'].tolist()
    }

    return jsonify(data)

@app.route('/chart')
def index():
    return render_template('trends_chart.html')


if __name__ == '__main__':
    app.run(debug=True)





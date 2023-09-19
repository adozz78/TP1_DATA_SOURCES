#import Flask
from flask import Flask

#instance de l'objet Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-7E4M7T0YEB"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-7E4M7T0YEB');
</script>
 """
 return prefix_google + "Hello World"
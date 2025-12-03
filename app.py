#  RENDER Settings start command needs      gunicorn app:app

# The Flask application object must be available at the top level
app = Flask(__name__) 
MAGIC_WORD = 'fred'
fumble = '67'
@app.route('/', methods=['GET', 'POST'])
def index():
    # Default message when first loading the page (GET request)
    result = "<span style='color:yellow'> Try the magic word 'fred'</span>"
    goober = "<span style='color:red'>don't type '67' ;)</span>"
    # Logic for handling form submission (POST request)
    if request.method == 'POST':
        # Get the input text from the form data
        my_input = request.form.get('myText01')
        my_input02 = request.form.get('myText02')
        
        if my_input == MAGIC_WORD:
            result = "<b style='color:green'> Cool! </b>"
        else:
            result = "<span style='color:red'> Try the magic word 'fred'</span>"
        if my_input02 == fumble:
            goober = "<b style='color:red'>Im Going to Kill you </b>"

    # HTML template with the dynamic result
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Backend</title>
    </head>
    <body>
        <h3 align=center>t1a27-Render-python-submit</h3>
        <form action="/" method="post">
            <label for="myText01">Enter Text:</label>
            <input type="text" id="myText01" name="myText01">
            <input type="text" id="myText02" name="myText02"'>
            <input type="submit" value="Submit">
            
        </form>
        {result}
        {goober}
    </body>
    </html>
    """
    return html_content

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_obj

app = Flask(__name__)
app.config['SECRET_KEY'] = 'snehu'
debug = DebugToolbarExtension(app)



@app.route("/")
def fill_blanks():

    return render_template("form.html", category = story_obj.prompts)

@app.route("/story")
def story():

    

    thep = request.args["place"]
    then = request.args["noun"]
    thev = request.args["verb"]
    thepl = request.args["plural_noun"]
    thea = request.args["adjective"]

    
    ans = {"place": f"{thep}", 
            "adjective": f"{thea}", 
            "plural_noun" : f"{thepl}", 
            "verb": f"{thev}", 
            "noun": f"{then}"}
    
    return render_template("story.html", final = story_obj.generate(ans))
#!/usr/bin/env python
# Flask web app that gives you the closest Wikipedia colour of a colour hex
import flask, flask.views, json

app = flask.Flask(__name__)
app.secret_key = "wow"

with open("colours") as f:
    colours = json.loads(f.read())

def colourname(i, colours):
    best = (1000, "")

    r = int(i[1:3], 16)
    g = int(i[3:5], 16)
    b = int(i[5:7], 16)

    for colour in colours.keys():
        if colour == i:
            best = (0, colour)
            break
        rr = int(colour[1:3], 16)
        gg = int(colour[3:5], 16)
        bb = int(colour[5:7], 16)
        diff = abs(rr - r) + abs(gg - g) + abs(bb - b)
        if diff < best[0]:
            best = (diff, colour)
    
    return best

class Main(flask.views.MethodView):
    def get(self):
        if len(flask.session.get('_flashes', [])) == 0:
            flask.flash("")
        return flask.render_template("index.html")
    
    def post(self):
        colour = str(flask.request.form["colour"]).upper()
        if len(colour) == 6: 
            colour = "#" + colour
        try:
            best = colourname(colour, colours)
            flask.flash([colour, best[1], best[0], colours[best[1]][0], colours[best[1]][1]])
        except:
            flask.flash(["Invalid input"])
        
        return self.get()
        

app.add_url_rule("/", view_func = Main.as_view("main"), methods = ["GET", "POST"])

app.debug = True
if __name__ == "__main__":
    app.run(host="0.0.0.0")

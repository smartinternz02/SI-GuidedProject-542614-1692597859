from flask import Flask, url_for, redirect
app=Flask(__name__)
@app.route("/faculty")
def faculty():
    return "<p>Welcome all faculty to FDP</p>"

@app.route("/type/<desg>")
def desg(desg):
    return "welcome all"+desg+"to FDP"

@app.route("/to/<person>")
def to(person):
    if person=="faculty":
        return redirect(url_for("faculty"))
    else:
        return redirect(url_for("desg",desg=person))


if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template
from dbconn import mycursor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/location")
def location():
    return render_template("location.html")


@app.route("/favourites")
def favourites():
    return render_template("favourites.html")


@app.route("/restaurant")
def restaurant():
    mycursor.execute("SELECT * FROM restaurants")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='restaurant')


@app.route("/european")
def european():
    mycursor.execute("SELECT * FROM restaurants WHERE nationality='European'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='European')


@app.route("/asian")
def asian():
    mycursor.execute("SELECT * FROM restaurants WHERE nationality='Asian'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Asian')


@app.route("/rating")
def rating():
    mycursor.execute("SELECT * FROM restaurants ORDER By rating desc")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Rating')


@app.route("/london")
def london():
    mycursor.execute("SELECT * FROM restaurants WHERE address LIKE '%London%'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='London')


@app.route("/albans")
def albans():
    mycursor.execute("SELECT * FROM restaurants WHERE address LIKE '%Albans%'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Albans')


@app.route("/nerja")
def nerja():
    mycursor.execute("SELECT * FROM restaurants WHERE address LIKE '%Nerja%'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Nerja')


@app.route("/all")
def all():
    mycursor.execute("SELECT * FROM users")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='All')


@app.route("/martin")
def martin():
    mycursor.execute("SELECT * FROM users WHERE name='Martin'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Martin')


@app.route("/karen")
def karen():
    mycursor.execute("SELECT * FROM users WHERE name='Karen'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Karen')


@app.route("/jordan")
def jordan():
    mycursor.execute("SELECT * FROM users WHERE name='Jordan'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Jordan')


@app.route("/hannah")
def hannah():
    mycursor.execute("SELECT * FROM users WHERE name='Hannah'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Hannah')


@app.route("/rose")
def rose():
    mycursor.execute("SELECT * FROM users WHERE name='Rose'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Rose')


if __name__ == '__main__':
    app.run()

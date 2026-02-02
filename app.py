from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("user")
pword = os.getenv("pw")
host = os.getenv("host")

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=pword,
        database="game_save"
    )


@app.route("/register",methods = ["GET","POST"])
def reg():
    if request.method == "POST":
        brukernavn = request.form['brukernavn']
        passord = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE brukernavn=%s", (brukernavn,))
        bruker = cursor.fetchone()
        cursor.close()
        conn.close()

        if bruker and check_password_hash(bruker['passord_hash'], passord):
            session['brukernavn'] = bruker['brukernavn']
            session['rolle'] = bruker['rolle']

            
            return redirect(url_for("home"))
        else:
            return render_template("login.html", feil_melding="Ugyldig brukernavn eller passord")

    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return

@app.route("/home")
def home():
    return

@app.route("/logout")
def logout():
    session.clear()
    flash("Du har logget ut.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
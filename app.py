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
app.secret_key = "WHYTHO"
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
        epost = request.form['epost']
        passord = generate_password_hash(request.form['passord'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, pword) VALUES (%s, %s, %s)", 
                       (brukernavn, epost, passord))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Bruker registrert!", "success")
        return redirect(url_for("login"))

    return render_template("registrer.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        brukernavn = request.form['brukernavn']
        passord = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE name = %s", (brukernavn,))
        bruker = cursor.fetchone()
        cursor.close()
        conn.close()

        if bruker and check_password_hash(bruker['pword'], passord):
            session['brukernavn'] = bruker['name']
            session['id']= bruker['id']
           
           
            return redirect(url_for("home"))
        else:
            return render_template("login.html", feil_melding="Ugyldig brukernavn eller passord")

    return render_template("login.html")

@app.route("/home")
def home():
    if  not session.get("brukernavn") or not session.get("id"):
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM users WHERE name = %s",(session['brukernavn'],))
    active = cursor.fetchone()
    cursor.execute("SELECT * FROM runs  WHERE  user_id = %s", (active["id"],))
    runs = cursor.fetchall()
    cursor.close()
    conn.close()

    return  render_template("homepage.html",name = session["brukernavn"], runs = runs)

@app.route("/play/<int:id>",methods= ['GET','POST'])
def play(id):
    if  not session.get("brukernavn") or not session.get("id"):
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        hp = int(request.form['hp'])
        e_hp = int(request.form['e_hp'])
        print("POST hp:", hp, "POST e_hp:", e_hp,"id: ",id)

        cursor.execute('UPDATE runs SET hp = %s , e_hp = %s WHERE id = %s',(hp,e_hp,id))
        conn.commit()
  
    cursor.execute("SELECT * FROM runs where id = %s",(id,))
    game = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("main.html", game = game)


@app.route("/new_run")
def new():
    if  not session.get("brukernavn") or not session.get("id"):
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("INSERT INTO runs (hp,e_hp,user_id) VALUES (%s,%s,%s)",(100,100,session.get("id")))
    conn.commit()
    cursor.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 1;")
    game = cursor.fetchone()
    cursor.close()
    conn.close()
    print(game)
    return redirect(url_for("play", id=game["id"]))


@app.route("/logout")
def logout():
    session.clear()
    flash("Du har logget ut.", "info")
    return redirect(url_for("login"))

@app.route("/")
def base():
    return redirect(url_for('login'))

@app.errorhandler(404)
def  eror404(e):
   return render_template("404.html",sesh = session)

if __name__ == "__main__":
    app.run(debug=True)
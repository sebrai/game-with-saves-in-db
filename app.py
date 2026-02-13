from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv
#   import libraries
load_dotenv()

user = os.getenv("user")
pword = os.getenv("pw")
host = os.getenv("host")
# set enviorment variables
app = Flask(__name__)
app.secret_key = "WHYTHO"
def get_db_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=pword,
        database="game_save"
    )
 #function for geting a new connection

@app.route("/register",methods = ["GET","POST"]) # registration
def reg():
    if request.method == "POST":
        brukernavn = request.form['brukernavn'] # get variables from form
        epost = request.form['epost']
        passord = generate_password_hash(request.form['passord']) # hashes the password

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, pword) VALUES (%s, %s, %s)", 
                       (brukernavn, epost, passord)) # insert a new user
        conn.commit() # close db conection
        cursor.close()
        conn.close()
        flash("Bruker registrert!", "success")
        return redirect(url_for("login")) #takes you to login

    return render_template("registrer.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST": # if you are currently posting from form
        brukernavn = request.form['brukernavn']
        passord = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE name = %s", (brukernavn,))
        bruker = cursor.fetchone()
        cursor.close()
        conn.close()

        if bruker and check_password_hash(bruker['pword'], passord): # checks if you inputed the correct password
            session['brukernavn'] = bruker['name'] # sets session variables
            session['id']= bruker['id']
           
           
            return redirect(url_for("home")) # REDIRECTS YOU TO the home page
        else:
            return render_template("login.html", feil_melding="Incorrect username or password")

    return render_template("login.html")

@app.route("/home")
def home():
    if  not session.get("brukernavn") or not session.get("id"): # if not loged in, log in
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM users WHERE name = %s",(session['brukernavn'],))
    active = cursor.fetchone() # fetches you user
    cursor.execute("SELECT * FROM runs  WHERE  user_id = %s ORDER BY done ASC, id ASC", (active["id"],)) # gets all runs and sorts by "done"
    runs = cursor.fetchall() # fetches your runs
    cursor.close()
    conn.close()

    return  render_template("homepage.html",name = session["brukernavn"], runs = runs)

@app.route("/play/<int:id>",methods= ['GET','POST'])
def play(id):
    if  not session.get("brukernavn") or not session.get("id"):
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST': # when you save and quit 
        hp = int(request.form['hp'])
        e_hp = int(request.form['e_hp'])
        done = bool(int(request.form.get('done',0))) # gets from form
        print("POST hp:", hp, "POST e_hp:", e_hp,"id: ",id)
        cursor.execute('UPDATE runs SET hp = %s , e_hp = %s, done = %s WHERE id = %s',(hp,e_hp,done,id)) # updates db
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('home'))
  
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
    cursor.execute("INSERT INTO runs (hp,e_hp,user_id) VALUES (%s,%s,%s)",(100,100,session.get("id"))) # create new run in db
    conn.commit()
    cursor.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 1;") # gets the last item in runs withc is hopefully what was just inserted
    game = cursor.fetchone()
    cursor.close()
    conn.close()
    print(game)
    return redirect(url_for("play", id=game["id"]))


@app.route("/logout")
def logout():
    session.clear() # clears the session
    flash("Du har logget ut.", "info") # save a message in temporary storage
    return redirect(url_for("login"))

@app.route("/")
def base():
    return redirect(url_for('login'))

@app.errorhandler(404) # tels the program what to do if error 404 happens
def  eror404(error):
   return render_template("404.html",sesh = session) # directs you to the 404 page

if __name__ == "__main__":
    app.run(debug=True)
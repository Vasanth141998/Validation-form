from flask import Flask,request,render_template,redirect,session,flash,url_for
import sqlite3 as sq


app = Flask(__name__)
app.config['SECRET_KEY'] = '-3116878390073697327'
con = sq.connect("user.db", check_same_thread=False)

con.execute("create table if not exists user(name text,username text,mobile_no integer,password text)")
cur = con.cursor()



@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":  
        luname = request.form['luname'] 
        lpass = request.form['lpass']
        cur.execute("select * from user where username=?",(luname,))
        a = cur.fetchone()
        
        if a is None:
            flash('username is invalid')
            return redirect('/')
        elif lpass not in a:
            flash('password is invalid')
            return redirect('/')
        else:
            
            return redirect('/index')
    else:
        return render_template("login page.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["u_name"]
        mobile_no = request.form["m_no"]
        password = request.form["pass"]
        confirm_password = request.form["c_pass"]
        print(name,username)
        if password == confirm_password:
            con.execute("insert into user(name,username,mobile_no,password) values(?,?,?,?)",(name,username,mobile_no,password))
            con.commit()
            return redirect("/")
        else:
            return render_template("signuppage.html")
    return render_template("signuppage.html")
if __name__ == "__main__":
    app.run(debug=True)



from log import *

con1=sq.connect("Studen_Data.db",check_same_thread=False)
cur1=con1.cursor()
con1.execute("create table if not exists batch5(uid INTEGER PRIMARY KEY AUTOINCREMENT,name varchar,contact int(10),course varchar)")


@app.route("/index")
def index():
    con1=sq.connect("Studen_Data.db")
    con1.row_factory=sq.Row
    cur1=con1.cursor()
    cur1.execute("select * from  batch5" )
    data=cur1.fetchall()
    con1.close()

    return render_template("index.html",datas=data)

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        uname=request.form["name"]
        contact=request.form["contact"]
        course=request.form["course"]
        con1=sq.connect("Studen_Data.db")
        cur1=con1.cursor()
        cur1.execute("insert into batch5 (name,contact,course) values(?,?,?)",(uname,contact,course))
        con1.commit()
        flash("USER ADDED","success")
        
        return redirect("index")
    return render_template("add.html")

@app.route("/edit/<string:uid>",methods=["POST","GET"])
def edit(uid):
     if request.method=="POST":
        uname=request.form["name"]
        contact=request.form["contact"]
        course=request.form["course"]
        con1=sq.connect("Studen_Data.db")
        cur1=con1.cursor()
        cur1.execute("update batch5 set name=?,contact=?,course=? where id=?",(uname,contact,course,uid))
        con1.commit()
        flash("USER update","success")
        return redirect("/index")
     con1=sq.connect("Studen_Data.db")
     con1.row_factory=sq.Row
     cur1=con1.cursor()
     cur1.execute("select * from  batch5 where id=?",(uid,) )
     data=cur1.fetchone()
     

     return render_template("edit.html",datas=data)

@app.route("/del/<string:uid>",methods=["GET"])
def delete(uid):
     con1=sq.connect("Studen_Data.db")
     con1.row_factory=sq.Row
     cur1=con1.cursor()
     cur1.execute("delete from batch5 where id=?",(uid,) )
     data=cur1.fetchone()
     con1.commit()
     flash("DELETE SUCCESSFULL","warning")
     return redirect("/index")


if __name__ == "__main__":
    app.run(debug=True)
    365827
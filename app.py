from flask import Flask,render_template,request
import smtplib


app=Flask(__name__)
subscribe=[]
@app.route("/",methods=['get'])
def home():
    return render_template("index.html")

@app.route('/form',methods=['post'])
def submit():
    first_name=request.form.get("first_name")
    mobile_number=request.form.get("mobile_number")
    email=request.form.get("email")
    msg=request.form.get("msg")
    msss=mobile_number+","+msg+","+first_name
    print("hiii")
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("td0828679@gmail.com","zgushlamcvfxkfzh")
    server.sendmail("td0828679@gmail.com",email,msss)
    
    
    subscribe.append(f"{first_name} {mobile_number} {email}")
    title="thk you"
    print(subscribe)
    return render_template("index.html",title=title)


if __name__=='__main__':
    app.run(debug=True)    

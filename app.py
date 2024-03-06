from flask import Flask,render_template
from flask import request,redirect,url_for
import csv
import traceback


app=Flask(__name__,template_folder='template')

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route('/submit_form',methods=['GET','POST'])
def submit():
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            write_data_CSV(data)
            message="FORM SUBMITTED , WE  WILL GET TO YOU SHORTLY"
            return render_template('thank_you.html',message=message)
        except:
            message="data was not save"
            return render_template('thank_you.html',message=message)
    else:
        message="not submitted"
        return render_template('thank_you.html',message=message)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/skill')
def skill():
    return render_template('skill.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def write_data_CSV(data):
    full_name = data['full_name']
    email = data['email']
    mobile = data['mobile']
    email_subject = data['email_subject']
    Message=data['Message']
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([full_name,email_subject,mobile,email,Message])


if __name__=='__main__':
    app.run(debug=True)

app.run(host= '192.168.2.237', port=9000, debug=False)

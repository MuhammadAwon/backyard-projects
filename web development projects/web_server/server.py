from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def web_page(page_name):
    return render_template(page_name)


with open('database.csv', 'w', newline='') as f:
    header = ['Email', 'Subject', 'Message']
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(header)

def user_info(data):
    with open('database.csv', 'a', newline='') as f:
        mail = data['Email']
        subj = data['Subject']
        msg = data['Message']
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow([mail,subj,msg])

@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            user_info(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'

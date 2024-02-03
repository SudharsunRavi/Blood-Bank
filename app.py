from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 
app.config['SECRET_KEY'] = 'dbmsproject'

conn = sqlite3.connect("blood_bank.db", check_same_thread=False)
c = conn.cursor()

def donor_create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS Donors(
                D_Name VARCHAR(50) NOT NULL,
                D_BloodType VARCHAR(5) NOT NULL,
                D_Email VARCHAR(50) PRIMARY KEY NOT NULL,
                D_City VARCHAR(50) NOT NULL,
                D_Number VARCHAR(50) NOT NULL 
                )''')
    print('Donor Table created Successfully')

def donor_add_data(Dname, Dbloodtype, Demail, Dcity, Dnumber):
    try:
        c.execute('''INSERT INTO Donors (D_Name, D_BloodType, D_Email, D_City, D_Number) VALUES(?,?,?,?,?)''',
                  (Dname, Dbloodtype, Demail, Dcity, Dnumber))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        conn.rollback()

def donor_view_all_data():
    c.execute('SELECT * FROM Donors')
    donor_data = c.fetchall()
    return donor_data

def donor_delete(Demail):
    c.execute(''' DELETE FROM Donors WHERE D_Email = ?''', (Demail,))
    conn.commit()

@app.route('/', methods=['GET'])
def index():
    donor_result = donor_view_all_data()
    return render_template('index.html', donors=donor_result)

@app.route('/addDonor', methods=['GET', 'POST'])
def add_donor():
    donor_create_table()

    if request.method == 'POST':
        donor_name = request.form['name']
        donor_blood_type = request.form['blood_type']
        donor_email = request.form['email']
        donor_city = request.form['city']
        donor_number = request.form['number']
        existing_emails = [row[2] for row in donor_view_all_data()]

        if donor_email not in existing_emails:
            donor_add_data(donor_name, donor_blood_type, donor_email, donor_city, donor_number)
            return redirect(url_for('index'))

    return render_template('addDonor.html')

@app.route('/delete_donor/<email>')
def delete_donor(email):
    donor_delete(email)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

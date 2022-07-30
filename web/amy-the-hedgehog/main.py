import os
import sqlite3
from flask import Flask, render_template, render_template_string, redirect, url_for, request

#flag is LITCTF{} with the name inside

con = sqlite3.connect('data.db', check_same_thread=False)
app = Flask(__name__)

cur = con.cursor()
#comment
cur.execute('''DROP TABLE IF EXISTS names''')
cur.execute('''CREATE TABLE names (name text)''')
cur.execute(
    '''INSERT INTO names (name) VALUES ("LITCTF{sldjf}") '''
)

@app.route('/', methods=['GET', 'POST'])
def login():
    send = "login.html"
    if request.method == 'POST':

        name = request.form['name']

        try:
       		cur.execute("SELECT * FROM names WHERE name='" + name + "'")
        except:
          render_template('incorrect.html', error="wrong!!! (｡•̀ᴗ-)✧")
          send = "incorrect.html"

				
        rows = cur.fetchall()

        
        if len(rows) > 0:
            return render_template('correct!.html', error="(≧U≦❁) You got it!!!")
            send = "correct!.html"
          
        else:
            return render_template('incorrect.html', error="wrong!!! (｡•̀ᴗ-)✧")
            send = "incorrect.html"

    return render_template(send, error="")

if __name__ == "__main__":
    app.run()

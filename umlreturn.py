import os
import json
from flask import Flask, render_template, request, url_for, redirect, flash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import time
# import pypyodbc

app = Flask(__name__, template_folder='./templates')

app.secret_key = '33d5f499c564155e5d2795a8327a7936'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dhruvi@2001@localhost/uml'
@app.route('/success')
def success():
    return json.loads(request.args["messages"])["result"]



@app.route('/database',methods = ['POST', 'GET'])
def database():
    result = ""
    if request.method == 'POST':

        select_database = request.form['choose']
        host = request.form['host']
        database_name = request.form['databasename']
        port = request.form['port']
        username = request.form['txtUsername']
        password = request.form['password']
        button = request.form['btnDatabase']


        if select_database == "MySQL":

            # mydb = mysql.connector.connect(host=host, user=username, port = port, database=database_name, password=password)

        #     try:
        #         mydb = mysql.connector.connect(
        #         host=host_name,
        #         user="root",
        #         port = port_name,
        #         database=database_name,
        #         password=password
        #         )
        #         print(mydb)
        #         if mydb.is_connected():
        #             db_Info = mydb.get_server_info()
        #             print("Connected to MySQL Server version ", db_Info)
        #             cursor = mydb.cursor()
        #             cursor.execute("select database();")
        #             record = cursor.fetchone()
        #             print("You're connected to database: ", record)
        #             flash('Connection Tested Succsessfully')

        # except Error as e:
        #     print('error-------',e)

            pass

        elif select_database == "Oracle":
            
            pass

        elif select_database == "Postgres":
            try:
                conn=psycopg2.connect(database=database_name, user=username, host=host, password=password )
                cur = conn.cursor()
                flash("Connection tested successfully ....!")
            
            except:
                flash("Something is wrong in your credentials....!")

            if button == "Test":
                return render_template('index.html')

            elif button == "Connect":

                cur.execute("""SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'public'""")
                for table in cur.fetchall():
                    print(table)


                return """
                @startuml
                !define table(x) class x << (T,#FFAAAA) >>
                !define primary_key(x) <u>x</u>
                hide methods
                hide stereotypes

                table(FOO1) {
                primary_key(FIELD1)
                FIELD2
                }
                @enduml
                """

        elif select_database == "SQL Server":

            pass

        return render_template('index.html')


@app.route("/")
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)


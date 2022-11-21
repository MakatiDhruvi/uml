from flask import Flask, render_template, request, url_for, redirect
from app import db, Student
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dhruvi@2001@localhost/uml'

# db = SQLAlchemy(app)




# class User(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     select_database = db.Column(db.String(50) , nullable=False)
#     host = db.Column(db.String(50), nullable=False)
#     database_name = db.Column(db.String(50), nullable=False)
#     port = db.Column(db.Integer, nullable=False)
#     password = db.Column(db.String(50), nullable=False)


#     def __repr__(self):
#         return f"User('{self.database_name}')"


@app.route("/")
def home():
    if request.method == 'POST':

        select_database = request.form.get('firstname')
        host = request.form.get('firstname')
        database_name = request.form.get('firstname')
        port = request.form.get('firstname')
        password = request.form.get('firstname')

        new_data = uml(select_database=select_database, host=host, database_name=database_name, port=port, password=password)

        db.session.add(new_data)
        db.session.commit()
    return "<h1>jkdfg idtfhj  </h1>"




if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from service.UserService import UserService
from service.SqLiteConnectionFactory import SqLiteConnectionFactory

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index() -> str:
    if request.method == "GET":
        return render_template("index.html")
    else:
        login = UserService.getUserByEmailAndPass(request.form.get("email"), request.form.get("senha"))
        return render_template("index.html", user= login if login != None else "Email ou Senha Errados !")

if __name__ == "__main__":
    with open("import.sql", 'r', encoding='utf-8') as f:
        with SqLiteConnectionFactory.getConnection() as conn:
            conn.executescript(f.read())
            conn.commit()
        
    app.run()
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from werkzeug.security import generate_password_hash, check_password_hash
from app.db.database import database

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
async def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        is_admin = bool(request.form.get("is_admin"))

        existing_user = await database.fetch_one(
            "SELECT * FROM users WHERE username = :username", {"username": username})
        if existing_user:
            flash("Username already exists.")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)
        await database.execute(
            "INSERT INTO users (username, hashed_password, is_admin) VALUES (:username, :password, :is_admin)",
            {"username": username, "password": hashed_password, "is_admin": is_admin})
        flash("Registration successful.")
        session["user"] = username
        session["is_admin"] = is_admin
        return redirect(url_for("home"))

    # AICI lipsea acest return — e esențial pentru metoda GET
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
async def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = await database.fetch_one(
            "SELECT * FROM users WHERE username = :username", {"username": username})
        if user and check_password_hash(user["hashed_password"], password):
            session["user"] = username
            session["is_admin"] = bool(user["is_admin"])

            get_flashed_messages()

            return redirect(url_for("home"))

        flash("Invalid credentials.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

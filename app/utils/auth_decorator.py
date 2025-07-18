from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    async def decorated(*args, **kwargs):
        if "user" not in session:
            flash("Please log in to access this page.")
            return redirect(url_for("auth.login"))
        return await f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    async def decorated(*args, **kwargs):
        if not session.get("is_admin"):
            flash("Admin access required.")
            return redirect(url_for("auth.login"))
        return await f(*args, **kwargs)
    return decorated

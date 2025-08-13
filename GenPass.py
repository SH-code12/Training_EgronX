from flask import Flask, request, jsonify, render_template
import secrets
import string

app = Flask(__name__)

AMBIG = set("lI1O0")

def build_pool(lower, upper, digits, symbols, no_ambig):
    pool = ""
    if lower:
        pool += string.ascii_lowercase
    if upper:
        pool += string.ascii_uppercase
    if digits:
        pool += string.digits
    if symbols:
        pool += "!@#$%^&*()-_=+[]{};:,.?/\\|`~"
    if no_ambig:
        pool = "".join(ch for ch in pool if ch not in AMBIG)
    return pool

def generate_password(length=16, lower=True, upper=True, digits=True, symbols=True, no_ambig=False):
    length = max(4, min(int(length), 128))
    pool = build_pool(lower, upper, digits, symbols, no_ambig)
    if not pool:
        raise ValueError("At least one character set must be enabled.")

    # Ensure at least one from each chosen set
    chosen_sets = []
    if lower: chosen_sets.append(string.ascii_lowercase)
    if upper: chosen_sets.append(string.ascii_uppercase)
    if digits: chosen_sets.append(string.digits)
    if symbols: chosen_sets.append("!@#$%^&*()-_=+[]{};:,.?/\\|`~")

    if no_ambig:
        chosen_sets = ["".join(ch for ch in s if ch not in AMBIG) for s in chosen_sets]

    password_chars = [secrets.choice(s) for s in chosen_sets]
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars[:length])

@app.route("/")
def index():
    return render_template("password.html")

@app.route("/api/generate")
def api_generate():
    try:
        length = int(request.args.get("length", 16))
    except ValueError:
        length = 16
    lower = request.args.get("lower", "true").lower() == "true"
    upper = request.args.get("upper", "true").lower() == "true"
    digits = request.args.get("digits", "true").lower() == "true"
    symbols = request.args.get("symbols", "true").lower() == "true"
    no_ambig = request.args.get("noAmbig", "false").lower() == "true"

    try:
        pw = generate_password(length, lower, upper, digits, symbols, no_ambig)
        return jsonify({"password": pw, "length": len(pw)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

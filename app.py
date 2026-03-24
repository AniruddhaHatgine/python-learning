from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "any_random_secret_key"

# Sample login storage (in memory)
saved_email = ""
saved_password = ""

# Stock data dictionaries
fundamental_data = {
    "rvnl": "RVNL is a Government PSU under the Ministry of Railways that works on railway infrastructure projects (EPC model). It executes projects such as electrification, track laying, bridges, metro & highways. RVNL is now expanding into Vande Bharat trains, roads & logistics parks, solar & international projects.",
    "ntpc": "NTPC is India's largest power generation company. It operates in the business of generation and sale of electricity. The company has a diversified portfolio of power generation assets, including coal-based, gas-based, hydroelectric, and renewable energy projects.",
    # Add other stocks...
}

technical_data = {
    "rvnl": "RVNL is currently trading in a weak-to-sideways zone below key moving averages...",
    "reliance": "Reliance is consolidating near highs while holding above key moving averages...",
    # Add other stocks...
}

profit_data = {
    "rvnl": "Net Profit (₹ Cr): 2021: 992, 2022: 1087, 2023: 1261, 2024: 1475, 2025: 1600",
    "reliance": "Net Profit (₹ Cr): 2021: 53739, 2022: 60705, 2023: 66702, 2024: 79020, 2025: 79600",
    # Add other stocks...
}

shareholding_data = {
    "rvnl": "Shareholding: Promoter: 72%, FII: 5%, DII: 10%, Retail: 13%",
    "reliance": "Shareholding: Promoter: 50%, FII: 23%, DII: 15%, Retail: 12%",
    # Add other stocks...
}

@app.route("/", methods=["GET", "POST"])
def index():
    global saved_email, saved_password
    message = ""
    
    # Registration
    if "register" in request.form:
        saved_email = request.form.get("email")
        saved_password = request.form.get("password")
        message = "Registered successfully! Now login."
    
    # Login
    elif "login" in request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if email == saved_email and password == saved_password:
            session["logged_in"] = True
            message = "Login Successful!"
        else:
            message = "Wrong Email or Password!"
    
    # Stock analysis
    elif "analyze" in request.form:
        if not session.get("logged_in"):
            message = "Please login first!"
        else:
            choice = request.form.get("choice")
            stock = request.form.get("stock_name").lower()
            
            if choice == "1":
                message = fundamental_data.get(stock, "Sorry, we don't have fundamental info.")
            elif choice == "2":
                message = technical_data.get(stock, "Sorry, we don't have technical info.")
            elif choice == "3":
                message = profit_data.get(stock, "Sorry, we don't have profit data.")
            elif choice == "4":
                message = shareholding_data.get(stock, "Sorry, we don't have shareholding data.")
            else:
                message = "Invalid choice!"
    
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
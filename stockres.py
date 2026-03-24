print("1 for Fundamental Analysis, 2 for Technical Analysis")
user_input = int(input("Enter Value: "))

# ================= FUNDAMENTAL =================
if user_input == 1:
    print("Fundamental Analysis")
    stock_name = input("Enter Stock Name: ").lower()

    if stock_name == "rvnl":
        print("RVNL is a Government PSU under the Ministry of Railways that works on railway infrastructure projects (EPC model). It executes projects such as electrification, track laying, bridges, metro & highways. RVNL is now expanding into Vande Bharat trains, roads & logistics parks, solar & international projects.")

    elif stock_name == "ntpc":
        print("NTPC is India's largest power generation company. It operates in coal, gas, hydro and renewable energy. Strong government backing ensures stable growth. Future lies in renewable energy expansion.")

    elif stock_name == "powergrid":
        print("Power Grid is a central PSU handling electricity transmission. It operates majority of India's transmission network. Stable earnings due to regulated returns. Growth from renewable integration.")

    elif stock_name == "reliance":
        print("Reliance is India's largest conglomerate with oil, telecom and retail businesses. Strong cash flows and expansion into green energy and digital. Future growth from Jio, retail and renewables.")

    elif stock_name == "tcs":
        print("TCS is India's largest IT company with strong global presence. Stable revenue from long-term contracts. Future growth from AI, cloud and digital transformation.")

    else:
        print("Stock not found")

# ================= TECHNICAL =================
elif user_input == 2:
    print("Technical Analysis")
    stock_name = input("Enter Stock Name: ").lower()

    if stock_name == "rvnl":
        print("RVNL is trading in sideways zone below key moving averages with support near ₹260 and resistance near ₹300. Breakout above ₹300 can trigger bullish move toward ₹320–₹350. Short term weak but long term structure remains positive.")

    elif stock_name == "ntpc":
        print("NTPC is in strong uptrend with support near ₹300 and resistance near ₹350. Buy on dips strategy works as long as trend holds.")

    elif stock_name == "reliance":
        print("Reliance is consolidating near highs with strong support around ₹2800 and resistance near ₹3000. Breakout can lead to fresh rally.")

    else:
        print("Stock not found")

# ================= INVALID =================
else:
    print("Invalid input")
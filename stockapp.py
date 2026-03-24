from flask import Flask, render_template, request, session, redirect, url_for, flash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# In-memory user storage (replace with database in production)
users = {}

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please login first!', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))
        
        if email in users:
            flash('Email already registered!', 'error')
            return redirect(url_for('register'))
        
        users[email] = password
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in users and users[email] == password:
            session['user'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/analyze', methods=['POST'])
@login_required
def analyze():
    analysis_type = request.form['analysis_type']
    stock_name = request.form['stock_name'].lower().strip()
    
    result = get_analysis(analysis_type, stock_name)
    
    return render_template('analysis.html', 
                         result=result, 
                         stock=stock_name, 
                         analysis_type=analysis_type)

def get_analysis(analysis_type, stock_name):
    # Fundamental Analysis Data
    fundamental_data = {
        'rvnl': "RVNL is a Government PSU under the Ministry of Railways that works on railway infrastructure projects (EPC model). It executes projects such as electrification, track laying, bridges, metro & highways. RVNL is now expanding into Vande Bharat trains, roads & logistics parks, solar & international projects.",
        'reliance': "Reliance Industries Limited is India's largest conglomerate with businesses in petrochemicals, refining, telecom (Jio), and retail. It generates strong cash flows from energy while expanding into digital and retail. Future growth is driven by 5G, e-commerce, and green energy like hydrogen and solar.",
        'tcs': "TCS is India's largest IT services company with strong global presence in consulting, cloud, and digital transformation. It has stable revenues due to long-term contracts and high client retention. The company maintains strong margins and scalability.",
        'infosys': "Infosys is a global IT company providing consulting and digital transformation services. It focuses on AI, automation, and cloud technologies. Strong global client base ensures steady growth.",
        'hdfc bank': "HDFC Bank is India's leading private bank with strong asset quality and consistent growth. It has a large retail and corporate customer base. Post merger expansion boosts future potential.",
        'icici bank': "ICICI Bank is a major private sector bank with strong retail loan growth. Asset quality has improved significantly in recent years. Digital transformation has boosted efficiency.",
        'itc': "ITC is a diversified company with leadership in cigarettes, FMCG, hotels, and agri-business. FMCG segment is growing rapidly reducing dependency on tobacco.",
        'sbi': "State Bank of India is the largest PSU bank with a massive customer base. It has improved asset quality and profitability. Strong credit growth supports future expansion.",
        'bharti airtel': "Bharti Airtel is a leading telecom company with operations in India and Africa. Rising data usage and 5G rollout drive growth. ARPU is increasing steadily improving profitability.",
        'lt': "Larsen & Toubro is a major infrastructure and engineering company executing large projects globally. It benefits from government infrastructure spending. Strong order book ensures revenue visibility.",
        'asian paints': "Asian Paints is India's top paint company with strong brand and distribution network. It consistently delivers high margins and growth. Expansion into home décor adds revenue streams.",
        'maruti': "Maruti Suzuki is India's largest car manufacturer with strong market share. It benefits from rising middle-class demand. Expansion into SUVs and EVs will drive growth.",
        'tata motors': "Tata Motors is a leading automobile company with passenger and commercial vehicles. It owns Jaguar Land Rover globally. Strong EV push gives future advantage.",
        'sun pharma': "Sun Pharma is India's largest pharma company with strong global presence. Focus on specialty drugs and generics supports growth. Strong R&D pipeline ensures future expansion.",
        'wipro': "Wipro is a global IT services company focusing on cloud and digital solutions. It is restructuring to improve growth. Margins and deal wins are key drivers.",
        'ultratech cement': "UltraTech Cement is India's largest cement producer. It benefits from infrastructure and housing demand. Scale and efficiency provide advantage.",
        'nestle': "Nestle India is a leading FMCG company with strong brands like Maggi and Nescafe. It delivers consistent growth and high margins. Premium product expansion supports growth.",
        'ntpc': "NTPC is India's largest power generation company. It is expanding into renewable energy. Stable earnings due to government backing.",
        'power grid': "Power Grid is a major transmission company with stable earnings. It benefits from regulated returns model. Expansion in grid infrastructure supports growth.",
        'axis bank': "Axis Bank is a strong private bank with improving asset quality. Growth driven by retail and corporate lending. Digital banking expansion supports future.",
        'kotak bank': "Kotak Mahindra Bank is known for strong risk management and stable growth. It has high capital adequacy. Focus on digital banking supports expansion.",
        'vbl': "Varun Beverages is a key PepsiCo franchise with strong growth in beverages. It benefits from rising consumption and expanding distribution. High revenue growth and improving margins support long-term potential.",
        'colgate': "Colgate India is a leader in oral care with strong brand dominance. It has stable demand and high margins. Growth is consistent but moderate due to mature market.",
        'tata investment': "Tata Investment invests mainly in Tata group companies. Its performance depends on stock market valuations. Strong backing from Tata group gives long-term value.",
        'jio finance': "Jio Financial is a new financial services company backed by Reliance. It focuses on lending, insurance and digital finance. Huge growth potential but still early stage.",
        'png': "PNG Jewellers operates in jewellery retail with strong regional presence. Growth driven by gold demand and expansion. Margins depend on gold price trends.",
        'hyundai': "Hyundai India is a leading automobile company with strong SUV portfolio. Growth driven by domestic demand and exports. EV segment will be key for future.",
        'dixon': "Dixon Technologies is a leading EMS company benefiting from Make in India. Strong growth due to electronics manufacturing demand. High scalability and government support.",
        'ind hotel': "Indian Hotels (Taj) is a major hospitality company. Strong recovery after COVID with rising tourism. Premium segment and expansion drive future growth."
    }
    
    # Technical Analysis Data
    technical_data = {
        'rvnl': "RVNL is currently trading in a weak-to-sideways zone below key moving averages (50 & 200 EMA), with immediate support around ₹272–₹267 and strong demand zone near ₹258, while resistance is placed at ₹285–₹294 and major breakout level near ₹300. Price structure suggests accumulation after correction, but momentum is still weak (RSI ~30–40 zone), so any move above ₹300 with volume can trigger fresh bullish momentum toward ₹320–₹350 levels. Forecast: Short term sideways to bearish until breakout, but positional view remains bullish if stock holds above ₹260 zone; best strategy is buy near support and wait for confirmation breakout above ₹300.",
        'reliance': "Reliance is consolidating near highs while holding above key moving averages, indicating strength with support near ₹2800 and resistance near ₹3000. Price structure shows accumulation with strong volume support, and RSI remains in bullish zone. Breakout above ₹3000 can trigger fresh rally toward ₹3200–₹3400, while downside remains protected above ₹2750.",
        'tcs': "TCS is trading in a sideways to slightly bearish trend below resistance zone ₹4000–₹4100, with support near ₹3700. Price shows consolidation after correction with weak momentum, and RSI hovering around neutral levels. Breakout above ₹4100 can resume bullish trend toward ₹4300, while breakdown below ₹3700 may lead to further downside.",
        'infosys': "Infosys is in a consolidation phase with support near ₹1400 and resistance near ₹1550, struggling below key moving averages. Price action shows range-bound movement with weak momentum and low volume. Breakout above ₹1550 can trigger bullish move toward ₹1700, while breakdown below ₹1400 may extend correction.",
        'hdfc bank': "HDFC Bank is showing sideways consolidation after merger, with strong support near ₹1500 and resistance near ₹1700. Price is stabilizing near long-term moving averages, indicating accumulation. Breakout above ₹1700 can trigger fresh bullish momentum toward ₹1800–₹1900.",
        'icici bank': "ICICI Bank is in strong uptrend with higher highs and higher lows, holding above key moving averages with support near ₹1050 and resistance near ₹1150. Momentum remains strong with RSI in bullish zone. Breakout above ₹1150 can lead to rally toward ₹1250 levels.",
        'itc': "ITC is trading in a sideways to slightly bullish range with support near ₹420 and resistance near ₹470. Price shows consolidation after strong rally with stable momentum. Breakout above ₹470 can trigger next leg toward ₹500+, while support remains strong near ₹400.",
        'sbi': "SBI is in strong bullish trend with consistent higher highs, holding above key support near ₹750 and resistance near ₹850. Price action shows strong institutional buying with high volumes. Breakout above ₹850 can lead to ₹900+ levels while dips remain buyable.",
        'bharti airtel': "Airtel is in steady uptrend with strong support near ₹1100 and resistance near ₹1250, trading above key moving averages. Momentum remains strong with consistent breakout patterns. Breakout above ₹1250 can push price toward ₹1350 levels.",
        'lt': "L&T is trading in bullish trend with strong support near ₹3400 and resistance near ₹3700. Price shows steady up move with healthy corrections indicating strength. Breakout above ₹3700 can lead to ₹4000 levels.",
        'asian paints': "Asian Paints is in weak to sideways trend below key resistance ₹3200 with support near ₹2900. Price structure shows lack of momentum and range-bound movement. Breakout above ₹3200 can signal reversal toward ₹3400.",
        'maruti': "Maruti is trading in bullish structure with support near ₹10000 and resistance near ₹11000. Price shows strong demand at lower levels and steady uptrend. Breakout above ₹11000 can trigger rally toward ₹12000.",
        'tata motors': "Tata Motors is in strong bullish trend with support near ₹850 and resistance near ₹1000. Price action shows strong momentum driven by EV growth. Breakout above ₹1000 can push toward ₹1100 levels.",
        'sun pharma': "Sun Pharma is in steady uptrend with support near ₹1200 and resistance near ₹1350. Price holds above moving averages with strong momentum. Breakout above ₹1350 can lead to ₹1450 levels.",
        'wipro': "Wipro is in weak trend with support near ₹450 and resistance near ₹520. Price struggles below key levels with low momentum. Breakout above ₹520 needed for bullish reversal.",
        'ultratech cement': "UltraTech Cement is in bullish trend with support near ₹9000 and resistance near ₹10000. Price shows strong upward momentum with consolidation phases. Breakout above ₹10000 can lead to ₹11000.",
        'nestle': "Nestle is trading in steady uptrend with support near ₹24000 and resistance near ₹26000. Price shows strong demand and consistent growth pattern. Breakout above ₹26000 can push toward ₹28000.",
        'ntpc': "NTPC is in strong uptrend with support near ₹300 and resistance near ₹350. Price shows consistent higher highs with strong volume. Breakout above ₹350 can lead to ₹380.",
        'power grid': "Power Grid is trading in stable uptrend with support near ₹280 and resistance near ₹320. Price shows low volatility with steady growth. Breakout above ₹320 can lead to ₹350.",
        'axis bank': "Axis Bank is in bullish trend with support near ₹1000 and resistance near ₹1100. Price shows improving momentum and strong structure. Breakout above ₹1100 can lead to ₹1200.",
        'kotak bank': "Kotak Bank is in sideways trend with support near ₹1700 and resistance near ₹1900. Price lacks momentum with range-bound movement. Breakout above ₹1900 needed for bullish trend.",
        'vbl': "VBL is in strong uptrend with support near ₹1400 and resistance near ₹1700. Price shows strong momentum with higher highs. Breakout above ₹1700 can lead to ₹1900 levels.",
        'colgate': "Colgate is in sideways to bullish range with support near ₹2400 and resistance near ₹2700. Price is stable with low volatility. Breakout above ₹2700 can trigger uptrend.",
        'tata investment': "Stock is volatile with support near ₹5000 and resistance near ₹6500. Price moves sharply with market sentiment. Breakout above ₹6500 can trigger rally.",
        'jio finance': "Jio Finance is in consolidation with support near ₹250 and resistance near ₹300. Price is in accumulation phase. Breakout above ₹300 can trigger bullish move.",
        'png': "PNG is in bullish trend with support near ₹700 and resistance near ₹900. Price shows steady higher highs. Breakout above ₹900 can push toward ₹1000.",
        'hyundai': "Hyundai is in bullish structure with support near ₹1500 and resistance near ₹1800. Price shows steady demand. Breakout above ₹1800 can lead to ₹2000.",
        'dixon': "Dixon is in strong uptrend with support near ₹5000 and resistance near ₹6500. Price shows strong buying momentum. Breakout above ₹6500 can lead to ₹7000+.",
        'ind hotel': "Indian Hotels is in strong uptrend with support near ₹500 and resistance near ₹650. Price shows breakout pattern. Breakout above ₹650 can push toward ₹750."
    }
    
    # Profit Data (5 Year YOY)
    profit_data = {
        'rvnl': "Net Profit (₹ Cr): 2021: 992, 2022: 1087, 2023: 1261, 2024: 1475, 2025: 1600",
        'reliance': "Net Profit (₹ Cr): 2021: 53739, 2022: 60705, 2023: 66702, 2024: 79020, 2025: 79600",
        'tcs': "Net Profit (₹ Cr): 2021: 32562, 2022: 38449, 2023: 42303, 2024: 46099, 2025: 48797",
        'infosys': "Net Profit (₹ Cr): 2021: 19423, 2022: 22146, 2023: 24108, 2024: 26248, 2025: 26750",
        'hdfc bank': "Net Profit (₹ Cr): 2021: 31857, 2022: 38151, 2023: 44643, 2024: 60162, 2025: 64062",
        'icici bank': "Net Profit (₹ Cr): 2021: 16193, 2022: 23339, 2023: 31296, 2024: 40312, 2025: 44000",
        'sbi': "Net Profit (₹ Cr): 2021: 20410, 2022: 31676, 2023: 50232, 2024: 61077, 2025: 65000",
        'itc': "Net Profit (₹ Cr): 2021: 13032, 2022: 15675, 2023: 19264, 2024: 20500, 2025: 21000",
        'bharti airtel': "Net Profit (₹ Cr): 2021: -15239, 2022: 4260, 2023: 8070, 2024: 12000, 2025: 14000",
        'lt': "Net Profit (₹ Cr): 2021: 11179, 2022: 12304, 2023: 13059, 2024: 15250, 2025: 16500",
        'asian paints': "Net Profit (₹ Cr): 2021: 3139, 2022: 3784, 2023: 4363, 2024: 5250, 2025: 5600",
        'maruti': "Net Profit (₹ Cr): 2021: 4721, 2022: 3766, 2023: 8049, 2024: 13488, 2025: 14500",
        'tata motors': "Net Profit (₹ Cr): 2021: -13017, 2022: -11308, 2023: 2690, 2024: 31399, 2025: 34000",
        'sun pharma': "Net Profit (₹ Cr): 2021: 2903, 2022: 7396, 2023: 8221, 2024: 9300, 2025: 10000",
        'wipro': "Net Profit (₹ Cr): 2021: 10855, 2022: 12237, 2023: 11372, 2024: 11135, 2025: 13192",
        'ultratech cement': "Net Profit (₹ Cr): 2021: 5584, 2022: 5421, 2023: 7088, 2024: 7600, 2025: 8200",
        'nestle': "Net Profit (₹ Cr): 2021: 2084, 2022: 2177, 2023: 2390, 2024: 2800, 2025: 3000",
        'ntpc': "Net Profit (₹ Cr): 2021: 13877, 2022: 15296, 2023: 17621, 2024: 19000, 2025: 20500",
        'power grid': "Net Profit (₹ Cr): 2021: 15410, 2022: 16304, 2023: 15573, 2024: 17000, 2025: 18000",
        'axis bank': "Net Profit (₹ Cr): 2021: 6718, 2022: 13161, 2023: 21593, 2024: 26000, 2025: 28000",
        'kotak bank': "Net Profit (₹ Cr): 2021: 6940, 2022: 10817, 2023: 14855, 2024: 16000, 2025: 17500",
        'vbl': "Net Profit (₹ Cr): 2021: 748, 2022: 1412, 2023: 2101, 2024: 2550, 2025: 2900",
        'colgate': "Net Profit (₹ Cr): 2021: 1048, 2022: 1020, 2023: 1340, 2024: 1400, 2025: 1500",
        'tata investment': "Net Profit (₹ Cr): 2021: 150, 2022: 250, 2023: 350, 2024: 400, 2025: 450",
        'jio finance': "Net Profit (₹ Cr): 2021: 0, 2022: 0, 2023: 1600, 2024: 1800, 2025: 2000",
        'png': "Net Profit (₹ Cr): 2021: 250, 2022: 300, 2023: 350, 2024: 420, 2025: 500",
        'hyundai': "Net Profit (₹ Cr): 2021: 4500, 2022: 5200, 2023: 6000, 2024: 7200, 2025: 8000",
        'dixon': "Net Profit (₹ Cr): 2021: 120, 2022: 190, 2023: 280, 2024: 350, 2025: 420",
        'ind hotel': "Net Profit (₹ Cr): 2021: -200, 2022: 50, 2023: 330, 2024: 600, 2025: 750"
    }
    
    # Shareholding Data
    shareholding_data = {
        'rvnl': "Shareholding: Promoter: 72%, FII: 5%, DII: 10%, Retail: 13%",
        'reliance': "Shareholding: Promoter: 50%, FII: 23%, DII: 15%, Retail: 12%",
        'tcs': "Shareholding: Promoter: 72%, FII: 16%, DII: 8%, Retail: 4%",
        'infosys': "Shareholding: Promoter: 15%, FII: 33%, DII: 20%, Retail: 32%",
        'hdfc bank': "Shareholding: Promoter: 0%, FII: 48%, DII: 30%, Retail: 22%",
        'icici bank': "Shareholding: Promoter: 0%, FII: 45%, DII: 30%, Retail: 25%",
        'sbi': "Shareholding: Promoter: 57%, FII: 10%, DII: 25%, Retail: 8%",
        'itc': "Shareholding: Promoter: 0%, FII: 40%, DII: 43%, Retail: 17%",
        'bharti airtel': "Shareholding: Promoter: 54%, FII: 25%, DII: 10%, Retail: 11%",
        'lt': "Shareholding: Promoter: 0%, FII: 23%, DII: 45%, Retail: 32%",
        'asian paints': "Shareholding: Promoter: 53%, FII: 18%, DII: 10%, Retail: 19%",
        'maruti': "Shareholding: Promoter: 58%, FII: 20%, DII: 15%, Retail: 7%",
        'tata motors': "Shareholding: Promoter: 46%, FII: 18%, DII: 16%, Retail: 20%",
        'sun pharma': "Shareholding: Promoter: 54%, FII: 18%, DII: 15%, Retail: 13%",
        'wipro': "Shareholding: Promoter: 73%, FII: 10%, DII: 9%, Retail: 8%",
        'ultratech cement': "Shareholding: Promoter: 60%, FII: 18%, DII: 12%, Retail: 10%",
        'nestle': "Shareholding: Promoter: 63%, FII: 10%, DII: 8%, Retail: 19%",
        'ntpc': "Shareholding: Promoter: 51%, FII: 18%, DII: 30%, Retail: 1%",
        'power grid': "Shareholding: Promoter: 51%, FII: 28%, DII: 15%, Retail: 6%",
        'axis bank': "Shareholding: Promoter: 9%, FII: 47%, DII: 30%, Retail: 14%",
        'kotak bank': "Shareholding: Promoter: 26%, FII: 39%, DII: 18%, Retail: 17%",
        'vbl': "Shareholding: Promoter: 63%, FII: 25%, DII: 5%, Retail: 7%",
        'colgate': "Shareholding: Promoter: 51%, FII: 26%, DII: 7%, Retail: 16%",
        'tata investment': "Shareholding: Promoter: 73%, FII: 3%, DII: 5%, Retail: 19%",
        'jio finance': "Shareholding: Promoter: 47%, FII: 17%, DII: 10%, Retail: 26%",
        'png': "Shareholding: Promoter: 85%, FII: 2%, DII: 3%, Retail: 10%",
        'hyundai': "Shareholding: Promoter: 75%, FII: 10%, DII: 8%, Retail: 7%",
        'dixon': "Shareholding: Promoter: 33%, FII: 22%, DII: 20%, Retail: 25%",
        'ind hotel': "Shareholding: Promoter: 38%, FII: 24%, DII: 20%, Retail: 18%"
    }
    
    # Return appropriate data based on analysis type
    if analysis_type == '1':
        return fundamental_data.get(stock_name, "Sorry, we don't have fundamental information on that stock.")
    elif analysis_type == '2':
        return technical_data.get(stock_name, "Sorry, we don't have technical analysis on that stock.")
    elif analysis_type == '3':
        return profit_data.get(stock_name, "Sorry, we don't have profit data on that stock.")
    elif analysis_type == '4':
        return shareholding_data.get(stock_name, "Sorry, we don't have shareholding data on that stock.")
    else:
        return "Invalid analysis type selected."

if __name__ == '__main__':
    app.run(debug=True)
    
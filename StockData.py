# def register():
#     email = input("Create Gmail:")
#     password = input("Create Password:")
#     return email , password
 

# def login(saved_email, saved_password):    
#     email = input("Enter Gmail:")
#     password = input("Enter password:")

#     if email == saved_email and password == saved_password:
#         print("Login Successful ")
#         return True
#     else:
#         print("Wrong Email or Password ")
#         return False
    
# print("1. Register")
# print("2. Login")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     saved_email, saved_password = register()
#     print("\nNow Login")
    
#     if not login(saved_email, saved_password):
#         exit()

# elif choice == 2:
#     print("⚠️ First register to create account")
#     exit()

# else:
#     print("Invalid choice")
#     exit()



##################################################################

print("1 for Fundamental Analysis, 2 for Technical Analysis, 3 for 5 Year YOY Profit, 4 for Share Holding")
user_input = int(input("Enter Value:"))

if user_input == 1:
    print("Fundamental Analysis")
    stock_name = input("Enter Stock Name:")
    
    if stock_name == "rvnl":
        print("RVNL is a Government PSU under the Ministry of Railways that works on railway infrastructure projects (EPC model). It executes projects such as electrification, track laying, bridges, metro & highways. RVNL is now expanding into Vande Bharat trains, roads & logistics parks, solar & international projects.")
    
    elif stock_name == "ntpc":
        print("NTPC is India's largest power generation company. It operates in the business of generation and sale of electricity. The company has a diversified portfolio of power generation assets, including coal-based, gas-based, hydroelectric, and renewable energy projects.")
    
    elif stock_name == "powergrid":
        print("Power Grid Corporation of India Limited (POWERGRID) is an Indian state-owned electric utilities company headquartered in Gurugram, Haryana. It is a central public sector undertaking under the ownership of the Ministry of Power, Government of India. POWERGRID transmits about 50% of the total power generated in India on its transmission network.")

    elif stock_name == "reliance":
        print("Reliance Industries Limited is Indias largest conglomerate with businesses in petrochemicals, refining, telecom (Jio), and retail. It generates strong cash flows from energy while expanding into digital and retail. Future growth is driven by 5G, e-commerce, and green energy like hydrogen and solar. It aims to become a global tech-energy leader.")

    elif stock_name == "tcs":
        print("TCS is Indias largest IT services company with strong global presence in consulting, cloud, and digital transformation. It has stable revenues due to long-term contracts and high client retention. The company maintains strong margins and scalability. Future growth is driven by AI, cloud computing, and enterprise digitalization.")

    elif stock_name == "infosys":
        print("Infosys is a global IT company providing consulting and digital transformation services. It focuses on AI, automation, and cloud technologies. Strong global client base ensures steady growth. Future depends on global IT spending and digital adoption.")

    elif stock_name == "hdfc bank":
        print("HDFC Bank is Indias leading private bank with strong asset quality and consistent growth. It has a large retail and corporate customer base. Post merger expansion boosts future potential. Growth will come from digital banking and rural expansion.")

    elif stock_name == "icici bank":
        print("ICICI Bank is a major private sector bank with strong retail loan growth. Asset quality has improved significantly in recent years. Digital transformation has boosted efficiency. Future growth is supported by credit expansion and strong balance sheet.")

    elif stock_name == "itc":
        print("ITC is a diversified company with leadership in cigarettes, FMCG, hotels, and agri-business. FMCG segment is growing rapidly reducing dependency on tobacco. Strong cash flows and dividends attract investors. Future lies in FMCG expansion and hotel business growth.")

    elif stock_name == "sbi":
        print("State Bank of India is the largest PSU bank with a massive customer base. It has improved asset quality and profitability. Strong credit growth supports future expansion. It plays a key role in Indias banking system.")

    elif stock_name == "bharti airtel":
        print("Bharti Airtel is a leading telecom company with operations in India and Africa. Rising data usage and 5G rollout drive growth. ARPU is increasing steadily improving profitability. Future growth comes from digital services and broadband.")

    elif stock_name == "lt":
        print("Larsen & Toubro is a major infrastructure and engineering company executing large projects globally. It benefits from government infrastructure spending. Strong order book ensures revenue visibility. Future growth depends on capex cycle.")

    elif stock_name == "asian paints":
        print("Asian Paints is Indias top paint company with strong brand and distribution network. It consistently delivers high margins and growth. Expansion into home décor adds revenue streams. Growth linked to housing and real estate.")

    elif stock_name == "maruti":
         print("Maruti Suzuki is Indias largest car manufacturer with strong market share. It benefits from rising middle-class demand. Expansion into SUVs and EVs will drive growth. Rural demand also supports sales.")

    elif stock_name == "tata motors":
         print("Tata Motors is a leading automobile company with passenger and commercial vehicles. It owns Jaguar Land Rover globally. Strong EV push gives future advantage. Profitability turnaround boosts confidence.")

    elif stock_name == "sun pharma":
          print("Sun Pharma is Indias largest pharma company with strong global presence. Focus on specialty drugs and generics supports growth. Strong R&D pipeline ensures future expansion. It benefits from rising healthcare demand.")

    elif stock_name == "wipro":
        print("Wipro is a global IT services company focusing on cloud and digital solutions. It is restructuring to improve growth. Margins and deal wins are key drivers. Future depends on digital demand.")

    elif stock_name == "ultratech cement":
        print("UltraTech Cement is Indias largest cement producer. It benefits from infrastructure and housing demand. Scale and efficiency provide advantage. Future growth tied to construction boom.")

    elif stock_name == "nestle":
        print("Nestle India is a leading FMCG company with strong brands like Maggi and Nescafe. It delivers consistent growth and high margins. Premium product expansion supports growth. Demand is stable.")
    
    elif stock_name == "ntpc":
        print("NTPC is Indias largest power generation company. It is expanding into renewable energy. Stable earnings due to government backing. Future growth driven by green energy transition.")

    elif stock_name == "power grid":
        print("Power Grid is a major transmission company with stable earnings. It benefits from regulated returns model. Expansion in grid infrastructure supports growth. Renewable integration boosts future demand.")

    elif stock_name == "axis bank":
        print("Axis Bank is a strong private bank with improving asset quality. Growth driven by retail and corporate lending. Digital banking expansion supports future. It is a key competitor in banking sector.")

    elif stock_name == "kotak bank":
        print("Kotak Mahindra Bank is known for strong risk management and stable growth. It has high capital adequacy. Focus on digital banking supports expansion. It is considered a safe bank.")

    elif stock_name == "bajaj finance":
        print("Bajaj Finance is a leading NBFC with strong consumer lending. It has high growth and strong risk management. Expansion into digital lending drives future. It is a high-return company.")

    elif stock_name == "adani enterprises":
        print("Adani Enterprises is a diversified flagship company investing in new sectors. It operates in airports, green energy, and data centers. High growth potential but also high risk. Future depends on execution.")

    elif stock_name == "adani ports":
        print("Adani Ports is Indias largest private port operator. It benefits from increasing trade. Strong cash flows support expansion. Key player in logistics growth.")

    elif stock_name == "jsw steel":
        print("JSW Steel is a major steel manufacturer with strong expansion plans. It benefits from infrastructure demand. Performance depends on steel prices. Future tied to global demand.")

    elif stock_name == "tata steel":
        print("Tata Steel is a global steel company with operations in India and Europe. It benefits from infrastructure growth. Cost efficiency is important. Future depends on commodity cycles.")

    elif stock_name == "coal india":
        print("Coal India is the worlds largest coal producer. It supplies majority of Indias coal demand. Strong dividends attract investors. Future faces renewable energy challenges.")

    elif stock_name == "ongc":
        print("ONGC is Indias largest oil exploration company. It benefits from high crude prices. Government policies affect profits. Future depends on energy demand.")

    elif stock_name == "britannia":
        print("Britannia is a leading FMCG company known for biscuits and dairy. Strong brand and distribution. Premium product growth supports future. Demand is stable.")

    elif stock_name == "eicher motors":
        print("Eicher Motors owns Royal Enfield, a premium motorcycle brand. Strong brand loyalty drives growth. Expansion into global markets supports future. Premium segment growth is key.")

    elif stock_name == "hero motocorp":
        print("Hero MotoCorp is the largest two-wheeler company. Strong rural demand supports sales. EV transition is a challenge. Future depends on electric strategy.")

    elif stock_name == "apollo hospital":
        print("Apollo Hospitals is a leading healthcare provider. Growth driven by rising healthcare demand. Expansion in digital health supports future. Strong long-term potential.")

    elif stock_name == "divis lab":
        print("Divis Labs is a leading pharma ingredient manufacturer. Strong export business and margins. Benefits from global demand. Future driven by CRAMS segment.")

    elif stock_name == "grasim":
        print("Grasim Industries operates in cement, chemicals, and textiles. Expanding into paints business. Diversification supports growth. Future depends on execution.")

    elif stock_name == "hindalco":
        print("Hindalco is a major metals company producing aluminium and copper. Global operations via Novelis. Benefits from demand cycles. Future tied to infrastructure.")

    elif stock_name == "indusind bank":
        print("IndusInd Bank focuses on retail and vehicle finance. Growth driven by credit expansion. Asset quality improvement is key. Future depends on lending growth.")

    elif stock_name == "bpcl":
        print("BPCL is a major oil refining company. Profits depend on crude prices and policies. Strong distribution network. Future uncertain due to energy transition.")

    elif stock_name == "shree cement":
        print("Shree Cement is a leading cement company with strong efficiency. High margins and cost control. Expansion supports growth. Benefits from infrastructure demand.")

    elif stock_name == "sbi life":
        print("SBI Life is a leading insurance company. Growth driven by increasing insurance awareness. Strong distribution network. Future potential is high.")

    elif stock_name == "hdfc life":
        print("HDFC Life is a major insurance player with strong brand. Focus on protection products. Growth supported by rising awareness. Strong long-term outlook.")

    elif stock_name == "upl":
        print("UPL is a global agrochemical company. Provides crop protection solutions. Growth driven by agriculture demand. Risks include commodity cycles.")

    elif stock_name == "tata consumer":
        print("Tata Consumer Products operates in tea, coffee, and FMCG. Expanding into packaged foods. Strong brand value. Future growth from premiumization.") 
    
    elif stock_name == "vbl":
        print("Fundamental: Varun Beverages is a key PepsiCo franchise with strong growth in beverages. It benefits from rising consumption and expanding distribution. High revenue growth and improving margins support long-term potential.")

    elif stock_name == "colgate":
        print("Fundamental: Colgate India is a leader in oral care with strong brand dominance. It has stable demand and high margins. Growth is consistent but moderate due to mature market.")

    elif stock_name == "tata investment":
        print("Fundamental: Tata Investment invests mainly in Tata group companies. Its performance depends on stock market valuations. Strong backing from Tata group gives long-term value.")

    elif stock_name == "jio finance":
        print("Fundamental: Jio Financial is a new financial services company backed by Reliance. It focuses on lending, insurance and digital finance. Huge growth potential but still early stage.")

    elif stock_name == "png":
        print("Fundamental: PNG Jewellers operates in jewellery retail with strong regional presence. Growth driven by gold demand and expansion. Margins depend on gold price trends.")

    elif stock_name == "hyundai":
        print("Fundamental: Hyundai India is a leading automobile company with strong SUV portfolio. Growth driven by domestic demand and exports. EV segment will be key for future.")

    elif stock_name == "dixon":
        print("Fundamental: Dixon Technologies is a leading EMS company benefiting from Make in India. Strong growth due to electronics manufacturing demand. High scalability and government support.")

    elif stock_name == "ind hotel":
        print("Fundamental: Indian Hotels (Taj) is a major hospitality company. Strong recovery after COVID with rising tourism. Premium segment and expansion drive future growth.")
    else:    
        print("Sorry, we don't have fundamental information on that stock.")

########################################################################################################

elif user_input == 2:
    print("Technical Analysis")
    stock_name = input("Enter Stock Name:")    
    
    if stock_name == "rvnl":
        print("RVNL is currently trading in a weak-to-sideways zone below key moving averages (50 & 200 EMA), with immediate support around ₹272–₹267 and strong demand zone near ₹258, while resistance is placed at ₹285–₹294 and major breakout level near ₹300.Price structure suggests accumulation after correction, but momentum is still weak (RSI ~30–40 zone), so any move above ₹300 with volume can trigger fresh bullish momentum toward ₹320–₹350 levels.Forecast: Short term sideways to bearish until breakout, but positional view remains bullish if stock holds above ₹260 zone; best strategy is buy near support and wait for confirmation breakout above ₹300.")\
    
    elif stock_name == "reliance":
        print("Reliance is consolidating near highs while holding above key moving averages, indicating strength with support near ₹2800 and resistance near ₹3000. Price structure shows accumulation with strong volume support, and RSI remains in bullish zone. Breakout above ₹3000 can trigger fresh rally toward ₹3200–₹3400, while downside remains protected above ₹2750.")

    elif stock_name == "tcs":
        print("TCS is trading in a sideways to slightly bearish trend below resistance zone ₹4000–₹4100, with support near ₹3700. Price shows consolidation after correction with weak momentum, and RSI hovering around neutral levels. Breakout above ₹4100 can resume bullish trend toward ₹4300, while breakdown below ₹3700 may lead to further downside.")

    elif stock_name == "infosys":
        print("Infosys is in a consolidation phase with support near ₹1400 and resistance near ₹1550, struggling below key moving averages. Price action shows range-bound movement with weak momentum and low volume. Breakout above ₹1550 can trigger bullish move toward ₹1700, while breakdown below ₹1400 may extend correction.")

    elif stock_name == "hdfc bank":
         print("HDFC Bank is showing sideways consolidation after merger, with strong support near ₹1500 and resistance near ₹1700. Price is stabilizing near long-term moving averages, indicating accumulation. Breakout above ₹1700 can trigger fresh bullish momentum toward ₹1800–₹1900.")

    elif stock_name == "icici bank":
        print("ICICI Bank is in strong uptrend with higher highs and higher lows, holding above key moving averages with support near ₹1050 and resistance near ₹1150. Momentum remains strong with RSI in bullish zone. Breakout above ₹1150 can lead to rally toward ₹1250 levels.")

    elif stock_name == "itc":
        print("ITC is trading in a sideways to slightly bullish range with support near ₹420 and resistance near ₹470. Price shows consolidation after strong rally with stable momentum. Breakout above ₹470 can trigger next leg toward ₹500+, while support remains strong near ₹400.")

    elif stock_name == "sbi":
        print("SBI is in strong bullish trend with consistent higher highs, holding above key support near ₹750 and resistance near ₹850. Price action shows strong institutional buying with high volumes. Breakout above ₹850 can lead to ₹900+ levels while dips remain buyable.")

    elif stock_name == "bharti airtel":
        print("Airtel is in steady uptrend with strong support near ₹1100 and resistance near ₹1250, trading above key moving averages. Momentum remains strong with consistent breakout patterns. Breakout above ₹1250 can push price toward ₹1350 levels.")

    elif stock_name == "lt":
        print("L&T is trading in bullish trend with strong support near ₹3400 and resistance near ₹3700. Price shows steady up move with healthy corrections indicating strength. Breakout above ₹3700 can lead to ₹4000 levels.")

    elif stock_name == "asian paints":
        print("Asian Paints is in weak to sideways trend below key resistance ₹3200 with support near ₹2900. Price structure shows lack of momentum and range-bound movement. Breakout above ₹3200 can signal reversal toward ₹3400.")

    elif stock_name == "maruti":
        print("Maruti is trading in bullish structure with support near ₹10000 and resistance near ₹11000. Price shows strong demand at lower levels and steady uptrend. Breakout above ₹11000 can trigger rally toward ₹12000.")

    elif stock_name == "tata motors":
        print("Tata Motors is in strong bullish trend with support near ₹850 and resistance near ₹1000. Price action shows strong momentum driven by EV growth. Breakout above ₹1000 can push toward ₹1100 levels.")

    elif stock_name == "sun pharma":
        print("Sun Pharma is in steady uptrend with support near ₹1200 and resistance near ₹1350. Price holds above moving averages with strong momentum. Breakout above ₹1350 can lead to ₹1450 levels.")

    elif stock_name == "wipro":
        print("Wipro is in weak trend with support near ₹450 and resistance near ₹520. Price struggles below key levels with low momentum. Breakout above ₹520 needed for bullish reversal.")

    elif stock_name == "ultratech cement":
        print("UltraTech Cement is in bullish trend with support near ₹9000 and resistance near ₹10000. Price shows strong upward momentum with consolidation phases. Breakout above ₹10000 can lead to ₹11000.")

    elif stock_name == "nestle":
        print("Nestle is trading in steady uptrend with support near ₹24000 and resistance near ₹26000. Price shows strong demand and consistent growth pattern. Breakout above ₹26000 can push toward ₹28000.")

    elif stock_name == "ntpc":
        print("NTPC is in strong uptrend with support near ₹300 and resistance near ₹350. Price shows consistent higher highs with strong volume. Breakout above ₹350 can lead to ₹380.")

    elif stock_name == "power grid":
        print("Power Grid is trading in stable uptrend with support near ₹280 and resistance near ₹320. Price shows low volatility with steady growth. Breakout above ₹320 can lead to ₹350.")

    elif stock_name == "axis bank":
        print("Axis Bank is in bullish trend with support near ₹1000 and resistance near ₹1100. Price shows improving momentum and strong structure. Breakout above ₹1100 can lead to ₹1200.")

    elif stock_name == "kotak bank":
        print("Kotak Bank is in sideways trend with support near ₹1700 and resistance near ₹1900. Price lacks momentum with range-bound movement. Breakout above ₹1900 needed for bullish trend.")
    
    elif stock_name == "vbl":
        print("Technical: VBL is in strong uptrend with support near ₹1400 and resistance near ₹1700. Price shows strong momentum with higher highs. Breakout above ₹1700 can lead to ₹1900 levels.")

    elif stock_name == "colgate":
        print("Technical: Colgate is in sideways to bullish range with support near ₹2400 and resistance near ₹2700. Price is stable with low volatility. Breakout above ₹2700 can trigger uptrend.")

    elif stock_name == "tata investment":
        print("Technical: Stock is volatile with support near ₹5000 and resistance near ₹6500. Price moves sharply with market sentiment. Breakout above ₹6500 can trigger rally.")

    elif stock_name == "jio finance":
        print("Technical: Jio Finance is in consolidation with support near ₹250 and resistance near ₹300. Price is in accumulation phase. Breakout above ₹300 can trigger bullish move.")

    elif stock_name == "png":
        print("Technical: PNG is in bullish trend with support near ₹700 and resistance near ₹900. Price shows steady higher highs. Breakout above ₹900 can push toward ₹1000.")

    elif stock_name == "hyundai":
        print("Technical: Hyundai is in bullish structure with support near ₹1500 and resistance near ₹1800. Price shows steady demand. Breakout above ₹1800 can lead to ₹2000.")

    elif stock_name == "dixon":
        print("Technical: Dixon is in strong uptrend with support near ₹5000 and resistance near ₹6500. Price shows strong buying momentum. Breakout above ₹6500 can lead to ₹7000+.")

    elif stock_name == "ind hotel":
        print("Technical: Indian Hotels is in strong uptrend with support near ₹500 and resistance near ₹650. Price shows breakout pattern. Breakout above ₹650 can push toward ₹750.")
    else:
        print("Sorry, we don't have technical analysis on that stock.")

###################################################################################

elif user_input == 3:
    print("5 Year YOY Profit")
    stock_name = input("Enter Stock Name:")    
    
    if stock_name == "rvnl":
        print("Net Profit (₹ Cr): 2021: 992, 2022: 1087, 2023: 1261, 2024: 1475, 2025: 1600")
    
    elif stock_name == "reliance":
        print("Net Profit (₹ Cr): 2021: 53739, 2022: 60705, 2023: 66702, 2024: 79020, 2025: 79600")

    elif stock_name == "tcs":
        print("Net Profit (₹ Cr): 2021: 32562, 2022: 38449, 2023: 42303, 2024: 46099, 2025: 48797")

    elif stock_name == "infosys":
        print("Net Profit (₹ Cr): 2021: 19423, 2022: 22146, 2023: 24108, 2024: 26248, 2025: 26750")

    elif stock_name == "hdfc bank":
        print("Net Profit (₹ Cr): 2021: 31857, 2022: 38151, 2023: 44643, 2024: 60162, 2025: 64062")

    elif stock_name == "icici bank":
        print("Net Profit (₹ Cr): 2021: 16193, 2022: 23339, 2023: 31296, 2024: 40312, 2025: 44000")

    elif stock_name == "sbi":
        print("Net Profit (₹ Cr): 2021: 20410, 2022: 31676, 2023: 50232, 2024: 61077, 2025: 65000")

    elif stock_name == "itc":
        print("Net Profit (₹ Cr): 2021: 13032, 2022: 15675, 2023: 19264, 2024: 20500, 2025: 21000")

    elif stock_name == "bharti airtel":
        print("Net Profit (₹ Cr): 2021: -15239, 2022: 4260, 2023: 8070, 2024: 12000, 2025: 14000")

    elif stock_name == "lt":
        print("Net Profit (₹ Cr): 2021: 11179, 2022: 12304, 2023: 13059, 2024: 15250, 2025: 16500")

    elif stock_name == "asian paints":
        print("Net Profit (₹ Cr): 2021: 3139, 2022: 3784, 2023: 4363, 2024: 5250, 2025: 5600")
    
    elif stock_name == "maruti":
        print("Net Profit (₹ Cr): 2021: 4721, 2022: 3766, 2023: 8049, 2024: 13488, 2025: 14500")

    elif stock_name == "tata motors":
        print("Net Profit (₹ Cr): 2021: -13017, 2022: -11308, 2023: 2690, 2024: 31399, 2025: 34000")

    elif stock_name == "sun pharma":
        print("Net Profit (₹ Cr): 2021: 2903, 2022: 7396, 2023: 8221, 2024: 9300, 2025: 10000")

    elif stock_name == "wipro":
        print("Net Profit (₹ Cr): 2021: 10855, 2022: 12237, 2023: 11372, 2024: 11135, 2025: 13192")

    elif stock_name == "ultratech cement":
        print("Net Profit (₹ Cr): 2021: 5584, 2022: 5421, 2023: 7088, 2024: 7600, 2025: 8200")

    elif stock_name == "nestle":
        print("Net Profit (₹ Cr): 2021: 2084, 2022: 2177, 2023: 2390, 2024: 2800, 2025: 3000")

    elif stock_name == "ntpc":
        print("Net Profit (₹ Cr): 2021: 13877, 2022: 15296, 2023: 17621, 2024: 19000, 2025: 20500")

    elif stock_name == "power grid":
        print("Net Profit (₹ Cr): 2021: 15410, 2022: 16304, 2023: 15573, 2024: 17000, 2025: 18000")

    elif stock_name == "axis bank":
        print("Net Profit (₹ Cr): 2021: 6718, 2022: 13161, 2023: 21593, 2024: 26000, 2025: 28000")

    elif stock_name == "kotak bank":
        print("Net Profit (₹ Cr): 2021: 6940, 2022: 10817, 2023: 14855, 2024: 16000, 2025: 17500")    
    elif stock_name == "vbl":
        print("Net Profit (₹ Cr): 2021: 748, 2022: 1412, 2023: 2101, 2024: 2550, 2025: 2900")

    elif stock_name == "colgate":
        print("Net Profit (₹ Cr): 2021: 1048, 2022: 1020, 2023: 1340, 2024: 1400, 2025: 1500")

    elif stock_name == "tata investment":
        print("Net Profit (₹ Cr): 2021: 150, 2022: 250, 2023: 350, 2024: 400, 2025: 450")

    elif stock_name == "jio finance":
        print("Net Profit (₹ Cr): 2021: 0, 2022: 0, 2023: 1600, 2024: 1800, 2025: 2000")

    elif stock_name == "png":
        print("Net Profit (₹ Cr): 2021: 250, 2022: 300, 2023: 350, 2024: 420, 2025: 500")

    elif stock_name == "hyundai":
        print("Net Profit (₹ Cr): 2021: 4500, 2022: 5200, 2023: 6000, 2024: 7200, 2025: 8000")

    elif stock_name == "dixon":
        print("Net Profit (₹ Cr): 2021: 120, 2022: 190, 2023: 280, 2024: 350, 2025: 420")

    elif stock_name == "ind hotel":
        print("Net Profit (₹ Cr): 2021: -200, 2022: 50, 2023: 330, 2024: 600, 2025: 750")
    else:
        print("Sorry, we don't have profit data on that stock.")

###################################################

elif user_input == 4:
    print("Share Holding")
    stock_name = input("Enter Stock Name:")  

    if stock_name == "rvnl":
        print("Shareholding: Promoter: 72%, FII: 5%, DII: 10%, Retail: 13%")
    
    elif stock_name == "reliance":
        print("Shareholding: Promoter: 50%, FII: 23%, DII: 15%, Retail: 12%")

    elif stock_name == "tcs":
        print("Shareholding: Promoter: 72%, FII: 16%, DII: 8%, Retail: 4%")

    elif stock_name == "infosys":
        print("Shareholding: Promoter: 15%, FII: 33%, DII: 20%, Retail: 32%")

    elif stock_name == "hdfc bank":
        print("Shareholding: Promoter: 0%, FII: 48%, DII: 30%, Retail: 22%")

    elif stock_name == "icici bank":
        print("Shareholding: Promoter: 0%, FII: 45%, DII: 30%, Retail: 25%")

    elif stock_name == "sbi":
        print("Shareholding: Promoter: 57%, FII: 10%, DII: 25%, Retail: 8%")

    elif stock_name == "itc":
        print("Shareholding: Promoter: 0%, FII: 40%, DII: 43%, Retail: 17%")

    elif stock_name == "bharti airtel":
        print("Shareholding: Promoter: 54%, FII: 25%, DII: 10%, Retail: 11%")

    elif stock_name == "lt":
        print("Shareholding: Promoter: 0%, FII: 23%, DII: 45%, Retail: 32%")

    elif stock_name == "asian paints":
        print("Shareholding: Promoter: 53%, FII: 18%, DII: 10%, Retail: 19%")

    elif stock_name == "maruti":
        print("Shareholding: Promoter: 58%, FII: 20%, DII: 15%, Retail: 7%")

    elif stock_name == "tata motors":
        print("Shareholding: Promoter: 46%, FII: 18%, DII: 16%, Retail: 20%")

    elif stock_name == "sun pharma":
        print("Shareholding: Promoter: 54%, FII: 18%, DII: 15%, Retail: 13%")

    elif stock_name == "wipro":
        print("Shareholding: Promoter: 73%, FII: 10%, DII: 9%, Retail: 8%")

    elif stock_name == "ultratech cement":
        print("Shareholding: Promoter: 60%, FII: 18%, DII: 12%, Retail: 10%")

    elif stock_name == "nestle":
        print("Shareholding: Promoter: 63%, FII: 10%, DII: 8%, Retail: 19%")

    elif stock_name == "ntpc":
        print("Shareholding: Promoter: 51%, FII: 18%, DII: 30%, Retail: 1%")

    elif stock_name == "power grid":
        print("Shareholding: Promoter: 51%, FII: 28%, DII: 15%, Retail: 6%")

    elif stock_name == "axis bank":
        print("Shareholding: Promoter: 9%, FII: 47%, DII: 30%, Retail: 14%")

    elif stock_name == "kotak bank":
        print("Shareholding: Promoter: 26%, FII: 39%, DII: 18%, Retail: 17%")

    elif stock_name == "vbl":
        print("Shareholding: Promoter: 63%, FII: 25%, DII: 5%, Retail: 7%")

    elif stock_name == "colgate":
        print("Shareholding: Promoter: 51%, FII: 26%, DII: 7%, Retail: 16%")

    elif stock_name == "tata investment":
        print("Shareholding: Promoter: 73%, FII: 3%, DII: 5%, Retail: 19%")

    elif stock_name == "jio finance":
        print("Shareholding: Promoter: 47%, FII: 17%, DII: 10%, Retail: 26%")

    elif stock_name == "png":
        print("Shareholding: Promoter: 85%, FII: 2%, DII: 3%, Retail: 10%")

    elif stock_name == "hyundai":
        print("Shareholding: Promoter: 75%, FII: 10%, DII: 8%, Retail: 7%")

    elif stock_name == "dixon":
        print("Shareholding: Promoter: 33%, FII: 22%, DII: 20%, Retail: 25%")

    elif stock_name == "ind hotel":
        print("Shareholding: Promoter: 38%, FII: 24%, DII: 20%, Retail: 18%")    

    else:
        print("Sorry, we don't have shareholding data on that stock.")

# while True:
#     print("1. Continue")
#     print("0. Exit")
    
#     choice = input("Enter: ")
    
#     if choice == "0":
#         break

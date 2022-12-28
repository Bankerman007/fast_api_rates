import pandas as pd


def five_year_treasury():
    scraper = pd.read_html('https://finance.yahoo.com/quote/%5EFVX/')
    row = pd.concat(scraper)
    df = pd.DataFrame(row)
    df_scrub = df.iloc[1:2]
    treasury_rate= df_scrub[1].loc[df_scrub.index[0]]
    
    return float(treasury_rate)

five_year_treasury()

def prime_rate():
    scraper= pd.read_html('https://www.jpmorganchase.com/about/our-business/historical-prime-rate')
    row = pd.concat(scraper)
    df = pd.DataFrame(row)
    df_scrub = df.iloc[0:1]
    prime = df_scrub.iloc[-1]
    prime =prime[1]
    prime= prime[:-1]

    return float(prime) 

prime_rate()  

def dow():
    scraper= pd.read_html('https://www.kitco.com/charts/livegold.html')
    row = pd.concat(scraper)
    df = pd.DataFrame(row)
    df_scrub = df.iloc[0:2]
    dow = df_scrub[1]
    dow_price = dow[1]
    
    return float(dow_price)

def dow_price_change():
    scraper= pd.read_html('https://www.kitco.com/charts/livegold.html')
    row = pd.concat(scraper)
    df = pd.DataFrame(row)
    df_scrub = df.iloc[0:2]
    dow = df_scrub[1]
    dow_change = dow[0]
    
    return float(dow_change)
    

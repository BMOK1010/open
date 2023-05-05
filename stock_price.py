import requests as req
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from datetime import datetime as d
from io import BytesIO

def get(symbol, start=None, end=None):
    
    if start == None:
        period1 = dt.datetime(d.today().year,1,1)
    else:
        period1 = dt.datetime(*start)
    if end == None:
        period2 = d.today()
    else:
        period2 = dt.datetime(*end)

    def convert(x):
        if type(x) == int:
            return f"{x:04}.hk".upper()
        else: 
            return x.upper()

    u = f"https://query1.finance.yahoo.com/v7/finance/download/{convert(symbol)}?period1={period1.timestamp():.0f}&period2={period2.timestamp():.0f}&interval=1d&events=history&includeAdjustedClose=true"

    headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1 OPT/3.5.4"}
    r = req.get(u, headers=headers)

    df = pd.read_csv(BytesIO(r.content), parse_dates=[0], index_col=0)
    df.columns.name = convert(symbol)
    print("Symbol:", convert(symbol), "\nData size:",df.shape, "\nPeriod:", period1.date(), "-",period2.date())
    return df


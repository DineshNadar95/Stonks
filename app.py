from flask import Flask, redirect, url_for,render_template
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    msft = yf.Ticker('adbe')
    print(msft.info['logo_url'])
    return render_template("Home.html")


@app.route("/graph/<TKR>")
def graph(TKR):
    msft = yf.Ticker(TKR)   
    
    hist = msft.history(period='max')
    arr = hist.to_records()
    ddate=[]
    dataClose=[]
    dataOpen=[]
    dataHigh=[]
    dataLow=[]
    for i in arr:
        ddate.append(str(i[0])[0:10])
        dataClose.append(i[4])
        dataOpen.append(i[1])
        dataHigh.append(i[2])
        dataLow.append(i[3])
    
    return render_template("Graph.html",stockName = msft.info['shortName'],ddate=ddate,dataOpen=dataOpen,dataClose=dataClose,dataHigh=dataHigh,dataLow=dataLow)

@app.route("/<TKR>")
def name(TKR):
    msft = yf.Ticker(TKR)
    return render_template("StockPage.html",content=msft.info)

@app.route("/Info")
def info():
    return render_template("InfoPage.html",content="Info")

if __name__ == "__main__":
    app.run(debug=True) 
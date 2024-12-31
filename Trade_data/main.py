from apidefinition import ApiDefinition
from tradingprofile import TradingProfile

from tradedesign import TradeDesign
import matplotlib.pyplot as plt

if __name__=="__main__":
    api_key = "PKJRUUHTATIT19AB"
    base_url = ApiDefinition(f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey={api_key}&datatype=json")
    endpoint = None

    data_trading = base_url.get(api_key,endpoint)
    print(data_trading)
    trade_list = []
    for key, value in data_trading.items():
        trade_day = TradingProfile(key,value['open'],value['high'],value['low'],value['close'],value['volume'])
        trade_list.append(trade_day)
    
    for trading_day in trade_list:
        print(trading_day)
        print("-" * 50) 

    graph = TradeDesign("title", "date_x", "close") 
    graph.list_obj = trade_list

    graph.prepare_data()
    graph.graph_design()
    plt.show()


  


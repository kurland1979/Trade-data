import matplotlib.pyplot as plt

class TradeDesign:
    def __init__(self ,title, date_x, price_y):
        self.title = title
        self.date_x = date_x
        self.price_y = price_y
        self.list_obj = []
        self.dates = []
        self.prices = []

    def  prepare_data(self):
        for obj in self.list_obj:
            self.dates.append(obj.date)
            self.prices.append(getattr(obj,self.price_y))

    def graph_selection(self):
         plt.scatter(self.dates,self.prices)
         plt.show()
    
    def graph_design(self):
        plt.figure(figsize=(10,6))       
        plt.plot(self.dates, self.prices,  
            color='blue',             
            marker='o',                
            markersize=3)
        plt.title("Trade data")           
        plt.xlabel("Date")
        plt.ylabel("close")


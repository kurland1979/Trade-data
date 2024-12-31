from tradingprofile import TradingProfile




class TradeCalculation(TradingProfile):
    def __init__(self, date, openn, high, low, close, volume):
        super().__init__(date, openn, high, low, close, volume)

    def difference_open_close(self):
         return self.openn - self.close
    
    def difference_low_high(self):
        return self.high - self.low
    
    def difference_high_close(self):
        return self.high - self.close
    
    def average_high_low(self):
        return (self.high + self.low) / 2
    
    def average_close_open(self):
        return (self.close + self.openn) / 2
    
    def average_daily(self):
        return (self.openn + self.close + self.high + self.low) / 4
    
    def percent_change_open_close(self):
        result = (self.openn - self.close) / self.openn
        return result * 100
    
    def percent_change_high_low(self):
        result = (self.high - self.low) / self.high
        return result * 100
    
    def percent_change_daily(self):
        result = (self.high - self.close) / self.high
        return result * 100
    
    def comparison_open_close(self):
        return self.openn > self.close
    
    def ratio_volum_price(self):
        return (self.close - self.openn) / self.volume
    
    def volatility_day(self):
        return self.average_daily() * 0.03
    


            


    

 
from datetime import datetime


class TradingProfile:
    def __init__(self, date: datetime, openn, high, low, close, volume):
        self._date = datetime.strptime(date, '%Y-%m-%d')
        self._openn = openn
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):
        if not isinstance(date, datetime) or date == None:
            raise Exception(f"Error: {date} Incorrect format")
        self._date = date

    @property
    def openn(self):
        return self._openn
    
    @openn.setter
    def openn(self,openn):
        if not isinstance(openn, float) or openn <= 0:
            raise Exception("Invalid value")
        self._openn = openn

    @property
    def high(self):
        return self._high
    
    @high.setter
    def high(self,high):
        if not isinstance(high, float) or high <= 0:
            raise Exception("Invalid value")
        self._high = high

    @property
    def low(self):
        return self._low
    
    @low.setter
    def low(self,low):
        if not isinstance(low, float) or low <= 0:
            raise Exception("Invalid value")
        self.low = low

    @property
    def close(self):
        return self._close
    
    @close.setter
    def close(self,close):
        if not isinstance(close, float) or close <= 0:
            raise Exception("Invalid value")
        self._close = close

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self,volume):
        if not isinstance(volume, int) or volume <= 0:
            raise Exception("Invalid value")
        self._volume

    def __str__(self):
        return (f"-Date: {self.date}\n-Open: {self.openn}\n-High: {self.high}\n"
                f"-Low: {self.low}\n-Close: {self.close}\n-Volume: {self.volume}\n")
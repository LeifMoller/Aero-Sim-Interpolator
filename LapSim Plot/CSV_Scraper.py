import pandas as pd

class Scraper:

    #setters
    def __init__(self):
        self.ac = None
        self.sk = None
        self.au = None
        self.en = None
        self.tot = None
    
    #getters
    def getAc(self):
        return self.ac
    def getSk(self):
        return self.sk
    def getAu(self):
        return self.au
    def getEn(self):
        return self.en
    def getTot(self):
        return self.tot
    
    
    def parse(self):
        
        #skip first 3 rows, define file to read
        lapTimes = pd.read_csv('lapTimeData.csv', skiprows = 3)
        
        #read + create arrays for:
        #   Acceleration Points (Ac) (C3)
        #   Skidpad Points (Sk) (C5)
        #   Autocross Points (Au) (C7)
        #   Endurance Points (En) (C10)
        #   Total Points (Tot) (C11)
        
        self.ac = lapTimes.iloc[:,3]
        self.sk = lapTimes.iloc[:,5]
        self.au = lapTimes.iloc[:,7]
        self.en = lapTimes.iloc[:,10]
        self.tot = lapTimes.iloc[:,11]
    
        
        
        
    
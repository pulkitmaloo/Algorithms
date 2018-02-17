import datetime as dt
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA



def predict_temperature(startDate, endDate, temperatures, n):
    # startDate = list(map(int, startDate.split("-")))
    # start = dt.datetime(startDate[0], startDate[1], startDate[2])
    # endDate = list(map(int, endDate.split("-")))
    # end = dt.datetime(endDate[0], endDate[1], endDate[2])
    
	idx = pd.DatetimeIndex([startDate, endDate])    
    pd.Series([1, 2], index=idx).resample("1H").sum()

    # df = pd.date_range(start, end, freq="1H")

    # temp = start
    # x = []
    # print(df)
    # while (temp != end):
    # 	x.append(temp + dt.timdelta(hours=1))
    # print(x)
     

if __name__ == '__main__':
	startDate = "2013-01-01"
	endDate = "2013-01-01"
	n = 1
	predict_temperature(startDate, endDate, None, None)

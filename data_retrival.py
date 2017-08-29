# import pandas as pd
# import pandas_datareader as web   
# import datetime
 

# start = datetime.datetime(2015,1,1)
# end = datetime.date.today()
 

# apple = web.DataReader('AAPL',"yahoo", start, end)
 
# apple.head()
import pandas as pd
import pandas_datareader as web
import datetime

start = datetime.datetime(2015,1,1)
end = datetime.date.today()
apple = web.DataReader("AAPL","yahoo",start,end)
apple.head()





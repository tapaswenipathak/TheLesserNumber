#{
#   "data": [
#      {"timestamp":1466640000,"value":0.27589941523037853},
#      {"timestamp":1466640900,"value":0.4059699097648263},
#      {...} ,
#      {"timestamp":1466641800,"value":0.8376112426631153}
#   ],
#   "forecast_to":1458136800,
#   "callback": "http://your.domain/yourcallback"
#}


import json
import datetime
from datetime import datetime
import sys,os

end_month = 12
end_date = 31
years = [1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

with open("{}.json".format(sys.argv[1])) as f:
    data = json.load(f)

timeseries_dict = {}
timeseries_list = []
final_dict = {}
country = ""

for i in range(len(data)):
    for year in years:
        if not data[i][str(year)]:
            pass
        else:
            timeseries_dict["value"] = float(data[i][str(year)])
        timeseries_dict["timestamp"] = float(datetime.timestamp(datetime(year, end_month, end_date)))
        timeseries_list.append(timeseries_dict)
        timeseries_dict = {}
    final_dict["data"] = timeseries_list
    country = data[i]["country"]
    if not os.path.exists(country):
        os.makedirs(country)
    with open('{}/{}.json'.format(country,data[i]["indicator"]),'w') as outfile:
        final_dict["forecast_to"] = 1767119400.0
        final_dict["callback"] = "http://your.domain/yourcallback"  #this needs to be replaced as per web app
        json.dump(final_dict, outfile)
    timeseries_list = []
    final_dict = {}





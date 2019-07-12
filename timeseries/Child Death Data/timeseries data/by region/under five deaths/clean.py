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
import sys
from datetime import datetime

end_month = 12
end_date = 31


with open("{}.json".format(sys.argv[1])) as f:
    data = json.load(f)

timeseries_dict = {}
timeseries_list = []
final_dict = {}

for item in data:
    timeseries_dict["value"] = float(item["value"])
    timeseries_dict["timestamp"] = float(datetime.timestamp(datetime(int(item["year"]), end_month, end_date)))
    timeseries_list.append(timeseries_dict)
    timeseries_dict = {}

final_dict["data"] = timeseries_list
with open("{}.json".format(sys.argv[1]), 'w') as outfile:
    final_dict["forecast_to"] = 1767119400.0
    final_dict["callback"] = "http://your.domain/yourcallback"  #this needs to be replaced as per web app
    json.dump(final_dict, outfile)


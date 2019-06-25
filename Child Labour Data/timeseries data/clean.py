import datetime
import json
import sys
from datetime import datetime

end_month = 12
end_date = 31
years = [1971,1981,1991,2001,2011]

with open("{}.json".format(sys.argv[1])) as f:
    data = json.load(f)


final_dict = {}
state_dict = {}
state_list = []
for item in data:
    state = item["state"]
    for year in years:
        if not item[str(year)]:
            pass
        else:
            state_dict["timestamp"] = float(datetime.timestamp(datetime(year, end_month, end_date)))
            state_dict["value"] = float(item[str(year)])
            state_list.append(state_dict)
        state_dict = {}
    final_dict["data"] = state_list
    with open("{}.json".format(state), "w") as outfile:
        final_dict["forecast_to"] = 1640889000.0
        final_dict["callback"] = "http://your.domain/yourcallback"  #this needs to be replaced as per web app
        json.dump(final_dict, outfile)
    state_list = []
    final_dict = {}
import datetime
import json
import sys
from datetime import datetime

end_month = 12
end_date = 31
years = [2013,2014,2016]

with open("{}.json".format(sys.argv[1])) as f:
    data = json.load(f)


final_dict = {}
country_dict = {}
country_list = []
for item in data:
    country = item["country"]
    for year in years:
        if not item[str(year)]:
            pass
        else:
            country_dict["timestamp"] = float(datetime.timestamp(datetime(year, end_month, end_date)))
            country_dict["value"] = float(item[str(year)])
            country_list.append(country_dict)
        country_dict = {}
    final_dict["data"] = country_list
    with open("{}.json".format(country), "w") as outfile:
        final_dict["forecast_to"] = 1514658600.0
        final_dict["callback"] = "http://your.domain/yourcallback"  #this needs to be replaced as per web app
        json.dump(final_dict, outfile)
    country_list = []
    final_dict = {}
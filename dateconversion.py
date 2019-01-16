import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
print(date_str)

new_pattern = "%-m/%d/%y"
date_str2 = parsed_date.strftime(new_pattern)
print(date_str2)
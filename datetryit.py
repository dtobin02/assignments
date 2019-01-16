# try it
import datetime

birthday = "1-May-12"
date_format2 = "%d-%B-%y"

parsed_date2 = datetime.datetime.strptime(birthday, date_format2)
date_str2 = parsed_date2.strftime("%-m/%-d/%Y")
print(date_str2)
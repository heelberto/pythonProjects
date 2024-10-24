import requests
from datetime import datetime

from_time = input("Enter start date in yyyy/mm/dd format: ")
to_time = input("Enter end date in yyyy/mm/dd format: ")
from_time_object = datetime.strptime(from_time, "%Y/%m/%d")
from_time_posix = from_time_object.timestamp()
print(int(from_time_posix))
to_time_object = datetime.strptime(to_time, "%Y/%m/%d")
to_time_posix = to_time_object.timestamp()
print(int(to_time_posix))



url = f"https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1={int(from_time_posix)}&period2={int(to_time_posix)}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url,headers=headers).content

print(content)

with open("data.csv","wb") as file:
    file.write(content)


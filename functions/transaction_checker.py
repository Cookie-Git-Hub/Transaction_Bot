import requests
import datetime

url = "https://api.bscscan.com/api"

def transaction_check(key, count):
    querystring = {
        "module": "account",
        "action": "txlist",
        "address": key,
        "startblock": "0",
        "endblock": "99999999",
        "page": "1",
        "offset": count,
        "sort": "desc",
        "apikey": "T19C2IRN7X8MPAW9TJVHXK7ANHJ487FHG3"
    }

    response = requests.request("GET", url, params=querystring)

    transactions = response.json()["result"]

    answer=""
    for i in transactions:
        #Преобразование времени из Unix формата в объект datetime
        dt = datetime.datetime.fromtimestamp(int(i["timeStamp"]))
        
        time_in_minutes=str(dt.minute)
        if dt.minute<10: 
            time_in_minutes="0" + str(dt.minute)

        time_in_hours=str(dt.hour)
        if dt.hour<10:
            time_in_hours="0" + str(dt.hour)

        time_in_days=str(dt.day)
        if dt.day<10:
            time_in_days="0" + str(dt.day)

        time_in_months=str(dt.month)
        if dt.month<10:
            time_in_months="0" + str(dt.month)   

        
       
        time_message = "**Time:** " + time_in_hours + ":" + time_in_minutes + " | " + time_in_days + "." + time_in_months + "." + str(dt.year)
        value = float(i["value"]) / 10**18  # Convert wei to BNB
        value_message = f"**Value:** {value:.4f} BNB"  # Display value rounded to 4 decimal places with "BNB" suffix
        end_message = ("------------------------------")
        answer = time_message + "\n" + value_message + "\n" + end_message + "\n" + answer
    return answer

import requests

def getStockData(symbol):
   url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+symbol+'&apikey=U6R6DHTK7V3ZPINJ'
   response = requests.get(url)
   json_data = response.json()
   print(json_data)
   dict_data = dict(json_data)

   try:
       # opening japi.out and writing to it
       with open("japi.out","a") as out:
           print("The current price of",symbol,"is:",dict_data['Global Quote']['05. price'],file=out,\n"Stock Quotes retrieved successfully!")
   except:
       print("Stock symbol does not exist!")
def main():
   # read until user enters QUIT
   while(True):
       symbol = input("Enter the stock symbol: ")
       symbol = symbol.upper()
       if(symbol=="QUIT"):
           break
       getStockData(symbol)
if __name__ == '__main__':
   main()

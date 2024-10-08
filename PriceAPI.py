import requests
import json



def find(ASIN):

# API Parameters using individual ASIN #'s
    params = {
    'api_key': '59E6E09CB64F45719F983ED62F73FE9B',
    'type': 'offers',
    'amazon_domain': 'amazon.com',
    'asin': ASIN,
    'customer_zipcode': '80602',
    'output': 'json',
    'include_html': 'false'
    }



    # make the http GET request to Rainforest API
    api_result = requests.get('https://api.rainforestapi.com/request', params)


    # Store the JSON response from Rainforest API
    data = json.dumps(api_result.json())
    #print(data)

    #Find the first instance of "value" in the JSON response to get the price
    index_of_value = data.find("value")
    #print(index_of_value)
    #print(data[index_of_value:index_of_value+15])


    price = ""

    # Traverse each character of the string from index of "value" and the following 15 characters including full price
    for x in data[index_of_value:index_of_value+15]:
        # find the numbers from the string and store into a variable to return final price
        if x.isnumeric() or x ==".":
            price += x


    print(f"ASIN: {ASIN}\nIndex of 'value': {index_of_value}\n15 Character string including price: {data[index_of_value:index_of_value+15]}\nPrice: {price}\n\n")
    return float(price)






import requests

class ETL:
    def __init__(self, 
                 url: str,
                 query: dict,
                 headers: dict) -> None:
        self.url = url
        self.query = query
        self.headers = headers
    
    def extract(self):
        response = requests.get(self.url, 
                                params=self.query,
                                headers=self.headers)
        return response.json()['data']
    
    def transform(self):
        pass


url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

querystring = {"keywords":"data engineer","locationId":"104195383","datePosted":"anyTime","sort":"mostRelevant"}

headers = {
	"x-rapidapi-key": "3e91c0dc89mshc23aeb55eb34c6dp1dd327jsndcd4a975b727",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

kafka_streaming = ETL(url, querystring, headers)
data = kafka_streaming.extract()
print(data)

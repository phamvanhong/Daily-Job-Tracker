import requests

class KafkaStreaming:
    def __init__(self, 
                 url: str,
                 query: dict,
                 headers: dict):
        self.url = url
        self.query = query
        self.headers = headers
    
    def get_data(self):
        response = requests.get(self.url, 
                                params=self.query,
                                headers=self.headers)
        return response.json()['data']


url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

querystring = {"locationId":"104195383","datePosted":"anyTime","sort":"mostRelevant"}

headers = {
	"x-rapidapi-key": "3e91c0dc89mshc23aeb55eb34c6dp1dd327jsndcd4a975b727",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

kafka_streaming = KafkaStreaming(url, querystring, headers)
data = kafka_streaming.get_data()
print(data)

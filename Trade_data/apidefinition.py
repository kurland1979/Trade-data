import requests

class ApiDefinition:
    def __init__(self,base_url):
        self._base_url = base_url
        

    @property
    def base_url(self):
        return self._base_url
    
    @base_url.setter
    def base_url(self,base_url):
        if not isinstance.startswith("https"):
            raise Exception("Error: url is incorrect")
        self._base_url = base_url

    def get(self,api_key,endpoint,params=None):
        response = requests.get(f"{self.base_url}{endpoint}{api_key}", params=params)
        response.raise_for_status()
        data_response = response.json()
        
        converted_data = {}
    
   
        for date, values in data_response['Monthly Time Series'].items():
        
            converted_values = {
            'open': float(values['1. open']),
            'high': float(values['2. high']),
            'low': float(values['3. low']),
            'close': float(values['4. close']),
            'volume': int(values['5. volume'])
        }
        
            converted_data[date] = converted_values
    
        return converted_data

    def hendle_errors(self,response):
        match response.status_code:
            case "200":
                return response.json()
            case "500":
                raise requests.exceptions.HTTPError("HTTP error occurred")
            case "504":
                raise requests.exceptions.Timeout("Timeout error occurred")
            case "503":
                raise requests.exceptions.RequestException("General error occurred")
            case _:
                raise requests.exceptions.HTTPError(f"error occurred: {response.status_code}")


    
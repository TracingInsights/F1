import requests
        
url = 'https://huggingface.co/spaces/tracinginsights/api' # Replace with the URL of the website you want to ping
url1 = 'https://huggingface.co/spaces/tracinginsights/2018'
url2 = 'https://huggingface.co/spaces/tracinginsights/2019'
url3 = 'https://huggingface.co/spaces/tracinginsights/2020'
url4 = 'https://huggingface.co/spaces/tracinginsights/2021'
url5 = 'https://huggingface.co/spaces/tracinginsights/2022'
url6 = 'https://huggingface.co/spaces/tracinginsights/2023'

response = requests.get(url)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)
response5 = requests.get(url5)
response6 = requests.get(url6)
print(f'Response from {url}: {response.status_code}')

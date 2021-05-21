import requests

#url = 'http://localhost:5000/predict'
#files = {'file': open('C://olahcitra//dog.png', 'rb')}

#resp = requests.post(url,files=files)
resp = requests.post("http://127.0.0.1:5000/predict",
                     files={"file": open('C://olahcitra//cat.jpg', 'rb')})
#print(resp)
print(resp.json())

import requests
import pandas as pd

data = pd.read_json('srd_5e_monsters.json')

img_data = []
for i in range(data.shape[0]):
    img_url = data['img_url'][i]
    print(img_url)
    img_data.append(requests.get(img_url).content)
    with open('image'+str(i)+'.jpg', 'wb') as handler:
        handler.write(img_data[i])

import requests

web_url = 'https://www.amazon.com/s?rh=n%3A565108&fs=true&language=es&ref=lp_565108_sar'

"""resp = requests.get(web_url)
with open('amazon.html', 'w') as f:
    f.write(resp.text)"""
# https://images-na.ssl-images-amazon.com/images/G/01/error/" + (Math.floor(Math.random() * 43) + 1) + "._TTD_.jpg
# https://images-na.ssl-images-amazon.com/images/G/01/error/21._TTD_.jpg
for i in range(1, 44):
    url = f'https://images-na.ssl-images-amazon.com/images/G/01/error/{i}._TTD_.jpg'
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'dogs_error/dog_error_{i}.jpg', 'wb') as f:
            f.write(resp.content)
        print(f'Image {i} downloaded')
    else:
        print(f'Image {i} not found')
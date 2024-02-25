import requests

def download_image(firebase_url, local_path):
    response = requests.get(firebase_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(response.content)



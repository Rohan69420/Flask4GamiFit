import requests

def download_image(firebase_url, local_path):
    response = requests.get(firebase_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(response.content)

# Replace 'firebase_url' with your Firebase URL
# Replace 'local_path.jpg' with your local file path
firebase_url = "https://firebasestorage.googleapis.com/v0/b/gamifit69420.appspot.com/o/images%2F1708779357606392?alt=media&token=cfc64dea-3fe7-4521-b8a0-1c79e1bdba5a"
download_image(firebase_url, 'capturedImage.jpg')

import shutil
import tempfile
import urllib.request
import os

def getImages(numberImages: int, destination: str):
    url = "https://thispersondoesnotexist.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for num in range(numberImages):
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            with tempfile.NamedTemporaryFile(delete_on_close=False) as tmp_file:
                shutil.copyfileobj(response, tmp_file)
                temp_file_path = tmp_file.name
                with open(temp_file_path, "rb") as download:
                    with open(f"{destination}/{num+1}.jpeg", "wb") as store:
                        shutil.copyfileobj(download, store)
    

filepath = "C:/Users/mamma/OneDrive/Desktop/Generated Images"
getImages(12, filepath)

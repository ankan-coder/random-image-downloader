import os
import requests
import datetime
import uuid
from flask import Flask, request, jsonify
from tqdm import tqdm

app = Flask(__name__)

# Ensure images directory exists
SAVE_DIR = "downloaded_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_random_images(count, width, height, use_timestamp=True):
    downloaded_files = []

    with tqdm(total=count, desc="Downloading Images", unit="img") as pbar:
        for i in range(count):
            image_url = f"https://picsum.photos/{width}/{height}"
            response = requests.get(image_url, stream=True)

            if response.status_code == 200:
                unique_key = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") if use_timestamp else str(uuid.uuid4())[:8]
                filename = f"{width}x{height}_{unique_key}.jpg"
                file_path = os.path.join(SAVE_DIR, filename)

                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)

                downloaded_files.append(file_path)
                pbar.update(1)
            else:
                print(f"\nFailed to download image {i+1}")

    return downloaded_files

@app.route('/download', methods=['GET'])
def download_images():
    try:
        num_images = int(request.args.get('count', 5))  # Default 5 images
        img_width = int(request.args.get('width', 480))
        img_height = int(request.args.get('height', 300))

        downloaded_files = download_random_images(num_images, img_width, img_height)
        
        return jsonify({"message": "Download Complete", "files": downloaded_files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Image Downloader API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Image Downloader API

A **Flask-based API** to download random images of given dimensions using **Lorem Picsum**. Easily deployable on **Render**.

## Features
- Downloads images with specified width & height
- Generates unique filenames
- Simple API returning JSON response

## Usage
**Download Images:**
```
https://your-app-name.onrender.com/download?count=10&width=500&height=400
```

## Local Setup
1. Clone Repo & Install Dependencies:
```sh
git clone https://github.com/your-username/image-downloader-api.git
cd image-downloader-api
pip install -r requirements.txt
```
2. Run API:
```sh
python app.py
```

## Deploy on Render
1. Push code to **GitHub**
2. Deploy on **Render.com** as a Web Service
3. Set **Start Command:**
```sh
pip install -r requirements.txt && python app.py
```

## Requirements
- Python 3+, Flask, Requests, tqdm

## License
All rights reserved. This code is proprietary and cannot be modified, distributed, or used without permission.


from flask import Flask, request, send_file
import requests
import io
import datetime

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_images():
    count = int(request.args.get('count', 1))  # Number of images
    width = request.args.get('width', 500)  # Image width
    height = request.args.get('height', 400)  # Image height

    # Get a random image from Lorem Picsum
    img_url = f"https://picsum.photos/{width}/{height}"
    response = requests.get(img_url)

    if response.status_code == 200:
        # Generate unique filename with timestamp
        filename = f"{width}x{height}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        
        # Return file as attachment (forces download in browser)
        return send_file(
            io.BytesIO(response.content), 
            mimetype="image/jpeg",
            as_attachment=True,
            download_name=filename
        )
    else:
        return {"status": "error", "message": "Failed to download image"}, 500

if __name__ == '__main__':
    app.run(debug=True)

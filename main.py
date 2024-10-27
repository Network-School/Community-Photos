# main.py
from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Define folder paths
PENDING_FOLDER = 'static/pending'
ACCEPTED_FOLDER = 'static/accepted'

# Ensure folders exist
os.makedirs(PENDING_FOLDER, exist_ok=True)
os.makedirs(ACCEPTED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Render the main page with a slideshow of accepted photos."""
    photos = os.listdir(ACCEPTED_FOLDER)
    print("Accepted photos:", photos)  # Debug statement
    return render_template('slideshow.html', photos=photos)

@app.route('/submit', methods=['GET', 'POST'])
def submit_photo():
    """Render the submit page or handle photo submission."""
    print("Submit route accessed")  # Debu
    if request.method == 'POST':
        print("Files in request:", request.files)  # Debug statement0
        if 'photos' not in request.files:
            print("No file part")  # Debug statement
            return redirect(url_for('submit_photo'))
        
        photos = request.files.getlist('photos')
        print("Received files:", [photo.filename for photo in photos])  # Debug statement
        if not photos or all(photo.filename == '' for photo in photos):  # Check if no photos uploaded
            print("No photos uploaded")  # Debug statement
            return redirect(url_for('submit_photo'))

        for photo in photos:
            if photo and photo.filename:  # Ensure photo is not None and has a filename
                try:
                    print(f"Saving photo: {photo.filename}")  # Debug statement
                    photo.save(os.path.join(PENDING_FOLDER, photo.filename))
                    print(f"Photo saved successfully: {photo.filename}")  # Debug statement
                except Exception as e:
                    print(f"Error saving photo {photo.filename}: {e}")  # Error handling

        return redirect(url_for('index'))  # Redirect to the index after submission
    
    return render_template('submit.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)

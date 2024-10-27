# Community Photo Submission Website

## Overview
This is a simple Flask web application that allows users to submit photos collected from the NS community. The application organizes submitted photos into two folders: one for pending submissions and another for accepted photos. Users can view a slideshow of accepted photos on the main page. This is designed to be run on a Raspberry Pi connected to a monitor with communication performed over the local network.

## Features
- **Photo Submission**: Users can upload multiple photos at once.
- **Slideshow**: Displays all accepted photos in a slideshow format.

## Project Structure

```
/static
    ├── /pending         # Folder for photos that are pending acceptance
    └── /accepted        # Folder for accepted photos which are displayed on the main page

/templates
    ├── submit.html      # HTML template for the photo submission page
    └── slideshow.html   # HTML template for the main page which displays the slideshow of accepted photos

main.py                  # Main Flask application file defining routes
README.md                # This file

```
## Requirements
- Python 3.x
- Flask

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install Flask
   ```

## Running the Application
To run the application, execute the following command in your terminal:

```bash
python main.py
```

The application will start on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) by default.
Modify the IP address in main.py if you want to run the website on a different device / Network.

## Usage
1. Navigate to the main page to view the slideshow of accepted photos.
2. Click on the submit link to upload photos.
3. Select one or more photos and submit them.
4. Photos will be saved to the /pending folder.
5. Manually check that the photos are suitable for the website and move them to the /accepted folder.

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

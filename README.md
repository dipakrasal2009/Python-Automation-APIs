# Python Utility Project

This project is a collection of Python scripts that provide various utilities such as sending emails, sending SMS via a connected mobile device, scraping Google search results, converting text to audio, manipulating images, and more. The project features a menu-based interface that allows users to select and execute different functionalities easily.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Send Email](#send-email)
  - [Send SMS from Mobile](#send-sms-from-mobile)
  - [Scrape Google Search Results](#scrape-google-search-results)
  - [Find Current Geo Coordinates and Location](#find-current-geo-coordinates-and-location)
  - [Convert Text to Audio](#convert-text-to-audio)
  - [Control Volume of Your Laptop](#control-volume-of-your-laptop)
  - [Crop Face from Image](#crop-face-from-image)
  - [Apply Filters to Image](#apply-filters-to-image)
  - [Apply Cool Filters to Image](#apply-cool-filters-to-image)
- [Requirements](#requirements)
- [License](#license)

## Project Overview

This project integrates several useful functionalities into a single Python application with a simple, menu-driven user interface. It allows users to perform common tasks like sending emails, processing images, controlling laptop volume, and much more. Each functionality is encapsulated in its own function, making the code modular and easy to maintain.

## Features

- **Send Email**: Send an email to a specified recipient using the Yagmail library.
- **Send SMS from Mobile**: Send SMS messages from a connected mobile device via ADB.
- **Scrape Google Search Results**: Scrape the top 5 Google search results for a given query.
- **Find Current Geo Coordinates and Location**: Retrieve the current geographical coordinates and location based on the user's IP address.
- **Convert Text to Audio**: Convert any text into an audio file and play it.
- **Control Volume of Your Laptop**: Adjust the volume of your laptop programmatically.
- **Crop Face from Image**: Detect and crop faces from an image using OpenCV.
- **Apply Filters to Image**: Apply basic filters (like BLUR and CONTOUR) to an image.
- **Apply Cool Filters to Image**: Add custom filters and effects, such as sunglasses and stars, to an image.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/python-utility-project.git
   cd python-utility-project

    Install the Required Packages
    Install the required Python libraries by running:

    bash

    pip install -r requirements.txt

    Set Up ADB
    Ensure that Android Debug Bridge (ADB) is set up correctly if you want to use the SMS sending feature. ADB should recognize your connected mobile device.

    Download Necessary Files
    For the image processing functionalities, make sure you have the required images (like sunglasses.png for the cool filters) in your project directory.

Usage

Run the main script to start the application:

bash

python main_menu.py

You will be presented with a menu that allows you to select the functionality you want to use.
Send Email

    Enter the recipient's email address, subject, and content.
    The email will be sent using the provided Gmail credentials.

Send SMS from Mobile

    Enter the recipient's mobile number and the SMS content.
    The SMS will be sent using the connected mobile device.

Scrape Google Search Results

    Enter the search query.
    The script will return the top 5 Google search results.

Find Current Geo Coordinates and Location

    The script retrieves and displays your current geographical coordinates and address.

Convert Text to Audio

    Enter the text to convert.
    The text will be converted into speech and saved as an audio file.

Control Volume of Your Laptop

    Adjust the volume by entering a value between 0.0 (mute) and 1.0 (full volume).

Crop Face from Image

    Enter the path of the image file.
    The script will detect and crop faces from the image and display them.

Apply Filters to Image

    Enter the path of the image file and choose a filter (BLUR or CONTOUR).
    The selected filter will be applied to the image.

Apply Cool Filters to Image

    Enter the path of the image file.
    The script applies custom filters, such as adding sunglasses and stars, and displays the modified image.

Requirements

    Python 3.x
    Libraries: yagmail, requests, BeautifulSoup4, geocoder, gtts, pycaw, opencv-python, Pillow
    Android Debug Bridge (ADB) for SMS functionality
    Internet connection for sending emails and scraping Google

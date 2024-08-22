
from email_task import send_email
from sms_task import send_sms
from scrape_task import scrape_google
from geo_task import get_location
from text_to_audio_task import text_to_audio
from volume_control_task import set_volume
from mobile_sms_task import send_sms_from_mobile
from bulk_email_task import send_bulk_emails
from data_processing_task import process_data
from model_integration_task import app  # Assuming this is a Flask app
from face_crop_task import crop_face
from image_filters_task import apply_filter
from custom_image_task import create_custom_image
from cool_filters_task import apply_cool_filters

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Send Email Message")
        print("2. Send SMS Message")
        print("3. Scrape Top 5 Search Results from Google")
        print("4. Find Current Geo Coordinates and Location")
        print("5. Convert Text-to-Audio")
        print("6. Control Volume of Your Laptop")
        print("7. Connect to Mobile and Send SMS")
        print("8. Send Bulk Email")
        print("9. Data Processing")
        print("10. Model Integration with Web App")
        print("11. Crop Face from Image")
        print("12. Apply Filters to Image")
        print("13. Create Custom Image with Numpy")
        print("14. Apply Cool Filters to Image")
        print("15. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            send_email('Subject', 'Body', 'recipient@example.com')
        elif choice == '2':
            send_sms('Message', '+1234567890')
        elif choice == '3':
            results = scrape_google('Python programming')
            print(results)
        elif choice == '4':
            coords, location = get_location()
            print(f"Coordinates: {coords}, Location: {location}")
        elif choice == '5':
            text_to_audio('Hello, world!')
        elif choice == '6':
            set_volume(0.5)  # Set volume to 50%
        elif choice == '7':
            send_sms_from_mobile('+1234567890', 'Hello from Python!')
        elif choice == '8':
            send_bulk_emails('Subject', 'Body', ['email1@example.com', 'email2@example.com'])
        elif choice == '9':
            process_data('data.csv')
        elif choice == '10':
            import threading
            threading.Thread(target=lambda: app.run(debug=True)).start()
        elif choice == '11':
            crop_face('image.jpg')
        elif choice == '12':
            filter_type = input("Enter filter type (BLUR/CONTOUR): ")
            apply_filter('image.jpg', filter_type)
        elif choice == '13':
            create_custom_image()
        elif choice == '14':
            apply_cool_filters('image.jpg')
        elif choice == '15':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

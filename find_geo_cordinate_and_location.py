import geocoder

def get_location():
    g = geocoder.ip('me')
    return g.latlng, g.address

# Call the function and print the result
location = get_location()
print(f"Latitude and Longitude: {location[0]}")
print(f"Address: {location[1]}")

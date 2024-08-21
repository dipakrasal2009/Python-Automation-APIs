from PIL import Image, ImageDraw

# Open the original image
image = Image.open('your_image.jpg')

# Apply sunglasses filter (you can replace this with your sunglasses image)
sunglasses = Image.open('sunglasses.png')
sunglasses = sunglasses.resize((200, 50))  # Resize sunglasses to fit the face
image.paste(sunglasses, (50, 100), sunglasses)  # Adjust position as needed

# Add star shapes
draw = ImageDraw.Draw(image)
for i in range(5):
    draw.polygon([(300 + i*50, 50), (310 + i*50, 100), (350 + i*50, 100),
                  (320 + i*50, 130), (330 + i*50, 180), (300 + i*50, 150),
                  (270 + i*50, 180), (280 + i*50, 130), (250 + i*50, 100),
                  (290 + i*50, 100)], fill="yellow")

# Save the edited image
image.save('output_image.jpg')
image.show()

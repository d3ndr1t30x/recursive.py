import base64

# Base64-encoded string
encoded_password = ""

# Decode the Base64-encoded string 13 times
for _ in range(13):
    encoded_password = base64.b64decode(encoded_password)

# Convert the final decoded password to a string
decoded_password = encoded_password.decode('utf-8')

print(decoded_password)

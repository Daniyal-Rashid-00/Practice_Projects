from cryptography.fernet import Fernet

# Generate a new Fernet key
new_key = Fernet.generate_key()

# Print the generated key
print(new_key.decode())
import rsa

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = "Hello my password is jelle"

encrypted_message = rsa.encrypt(message.encode(), public_key)
print(encrypted_message)

# i sort of want to come back to this...

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def save_key_in_der_format(key, filename, is_private):
	encoding = serialization.Encoding.DER
	if is_private:
    	# Serialize private key
    	key_data = key.private_bytes(
        	encoding=encoding,
        	format=serialization.PrivateFormat.TraditionalOpenSSL,
        	encryption_algorithm=serialization.NoEncryption()
    	)
	else:
    	# Serialize public key
    	key_data = key.public_bytes(
        	encoding=encoding,
        	format=serialization.PublicFormat.SubjectPublicKeyInfo
    	)

	with open(filename, 'wb') as f:
    	f.write(key_data)

# Generate RSA private key
private_key = rsa.generate_private_key(
	public_exponent=65537, #change as needed, you can make a custom / random:: NEEDS TO BE A PRIME
	key_size=2048,
)

# Save private key in DER format
save_key_in_der_format(private_key, 'private_key.der', is_private=True)

# Extract public key
public_key = private_key.public_key()

# Save public key in DER format
save_key_in_der_format(public_key, 'public_key.der', is_private=False)

print("Keys have been saved in DER format.")	

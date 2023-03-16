import hashlib

passwords_file = "passwords.txt"
output_file = "hashes.txt"

with open(passwords_file, "r") as f:
    passwords = f.read().splitlines()

with open(output_file, "w") as f:
    for password in passwords:
        # Add a UTF-16LE encoding prefix to the password
        password_utf16 = password.encode('utf-16le')
        
        # Hash the UTF-16LE encoded password using the MD4 algorithm
        hash_object = hashlib.new('md4', password_utf16)
        hash_value = hash_object.digest().hex().upper()
        
        # Write the hash value to the output file
        f.write(hash_value + "\n")
        
print(f"Hash values written to {output_file}")

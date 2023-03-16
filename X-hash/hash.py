import hashlib

# 这个文件是你要加密的密码列表，每行一个。
password_file = "password.txt"
# 这个是你要匹配的已加密的密码列表，每行一个。
hash_file = "hash.txt"
# 这个文件是脚本生成的，包含了第一个文件中每个密码的加密值，以及该值和匹配的结果。
output_file = "output.txt"

with open(password_file, "r") as f:
    passwords = f.read().splitlines()

def encrypt_password(password):
    utf16_password = password.encode("utf-16-le")
    nt_hash = hashlib.new("md4", utf16_password).hexdigest()
    return nt_hash.upper()

with open(output_file, "w") as f:
    for password in passwords:
        hash_value = encrypt_password(password)
        f.write(f"{password}:{hash_value}\n")

print("密码加密完成.")

with open(hash_file, "r") as f:
    hashes = f.read().splitlines()

def match_password_hash(password, hash_value):
    utf16_password = password.encode("utf-16-le")
    nt_hash = hashlib.new("md4", utf16_password).hexdigest()
    if nt_hash.upper() == hash_value.upper():
        return True
    else:
        return False

print("正在启动密码哈希匹配...")
print(f"Password file: {password_file}")
print(f"Hash file: {hash_file}")
print(f"Output file: {output_file}")
print(f"明文密码数量: {len(passwords)}")
print(f"要匹配的hash数量: {len(hashes)}")

for hash_value in hashes:
    for password in passwords:
        if match_password_hash(password, hash_value):
            print("\033[1;31m匹配成功:\033[0m", "\033[1;31m" + password + "\033[0m", ":", "\033[1;31m" + hash_value + "\033[0m")

print("密码哈希匹配脚本已完成.")

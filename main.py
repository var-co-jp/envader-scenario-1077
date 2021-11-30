from simple_aes_cipher import AESCipher, generate_secret_key

pass_phrase = "hogefuga"
secret_key = generate_secret_key(pass_phrase)

cipher = AESCipher(secret_key)
with open('secret.txt') as f:
    data = f.read()
print(cipher.decrypt(data))

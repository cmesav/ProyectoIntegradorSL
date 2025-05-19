import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class SeguridadAES:

    def __init__(self):
        self.key = get_random_bytes(32)  # Clave AES de 256 bits generada al inicio

    def cifrar(self, valor: str) -> str:
        aes_cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, auth_tag = aes_cipher.encrypt_and_digest(valor.encode())

        return "|".join([
            binascii.hexlify(aes_cipher.nonce).decode(),
            binascii.hexlify(ciphertext).decode(),
            binascii.hexlify(auth_tag).decode()
        ])

    def descifrar(self, valor: str) -> str:
        try:
            nonce_hex, ciphertext_hex, auth_tag_hex = valor.split('|')

            nonce = binascii.unhexlify(nonce_hex)
            ciphertext = binascii.unhexlify(ciphertext_hex)
            auth_tag = binascii.unhexlify(auth_tag_hex)

            aes_cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
            return aes_cipher.decrypt_and_verify(ciphertext, auth_tag).decode()
        except Exception as ex:
            return f"Error al descifrar: {ex}"
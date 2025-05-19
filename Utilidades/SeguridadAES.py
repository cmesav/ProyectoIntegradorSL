import os
import binascii
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

class SeguridadAES:

    def __init__(self):
        if not os.getenv("AES_SECRET_KEY"):
            nueva_clave = get_random_bytes(32)
            os.environ["AES_SECRET_KEY"] = binascii.hexlify(nueva_clave).decode()

        self.key = binascii.unhexlify(os.getenv("AES_SECRET_KEY"))

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


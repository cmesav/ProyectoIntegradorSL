import binascii
from Crypto.Cipher import AES

class SeguridadAES:

    def __init__(self):
        """Usa una clave AES fija para evitar errores de descifrado."""
        self.key = bytes.fromhex("c2a572d0f94e4d7b8eaf638c8b1e2f90a8d77e2ff3c31e1b2c4a7d8c3f015b72")

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

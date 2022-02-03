# pip install pycryptodomex (for window), pip install pycryptodome (for linux)
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5

class RSACipher:
    def __init__(self):
        self.pubkey = RSA.import_key("-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6dMMXd/qmF6Sn7gebxdu5JAxD\nEyk7VdZdU4gFKEi/r+wzGav16C3SjvT6X8YNSHwmMmhtJ1QNWnsvjo9ozHXSa6tb\nisBn/CSfhjSxbKf5NfwFqebO89N5kHsU6577+QiO+9U+RjZ4aEk5UladP0WhFNf6\nnQCXXXE+2RRSAvhOsQIDAQAB\n-----END PUBLIC KEY-----")
        self.prikey = RSA.import_key("-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQC6dMMXd/qmF6Sn7gebxdu5JAxDEyk7VdZdU4gFKEi/r+wzGav1\n6C3SjvT6X8YNSHwmMmhtJ1QNWnsvjo9ozHXSa6tbisBn/CSfhjSxbKf5NfwFqebO\n89N5kHsU6577+QiO+9U+RjZ4aEk5UladP0WhFNf6nQCXXXE+2RRSAvhOsQIDAQAB\nAoGBALpsBacQUW4BE6LHLZpEj/QjI5Nos//cSdDTtJqbdWkaRoms8C6UbkQopK00\nVrtvLpmuKpSADtyvC5035xC75Eu/p+LyRZnI+HNiQdm76J+G5AvY/HxBkdNGWXjm\nRiRSL8ZOvAvvNnBtrB6i88nftBeHZCpB4+3Cqo7q45Lo6xWFAkEA9J5cKiGH0OR8\nhmAXSI9G0eWnftU9gIaZYdGzdhgUQdZaL9XSWgzfNLFHn7KwFOTB9lu0LjCww9Cb\nEeZuiaovCwJBAMMhoalvdRMT3L4aiyexfoVYOUJzPWeiSwITt8d9YrYnENLxXaZK\nOPZYw6yXPctZ0pV2sYtb8Pd6WoyV4SS2frMCQQDCkL7f5+GeHk6Jlx6N4SBETTUn\nZbbQZr7TFjd24/ogz7zWNW1loL1crPE6LaduRvGb4R70alf+uArPdwhOySU3AkAk\nwZwLJ5SdEFu/b46Q3o1fntvCWaTSda69aGtw53yFpVw08ARdA5QxS00ooKCiQnw5\nbU9KWfpNE74kx0LOwJWjAkEA13KjjnQ00scp8zJFMm+Br0QFCtxePJTLgPylhBuR\nso1bM/EP0UHle0lAW+K2XCTAbTLCtjlBTsl5EG/G1NN4xw==\n-----END RSA PRIVATE KEY-----")

    def encrypt(self, raw):
        cipher_rsa = PKCS1_v1_5.new(self.pubkey,RSA)
		# 일부 코드 삭제
        return encrypted

    def decrypt(self, encrypted):
        cipher_rsa = PKCS1_v1_5.new(self.prikey)
		# 일부 코드 삭제
        return raw

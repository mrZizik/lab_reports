__author__ = 'cdumitru'

from Crypto.PublicKey import RSA
from Crypto import Random
import gmpy
import base64


#tup (tuple) - A tuple of long integers, with at least 2 and no more than 6 items. The items come in the following order:
#RSA modulus (n).
#Public exponent (e).
#Private exponent (d)
#First factor of n (p).
#Second factor of n (q)

n = 0xe9942c4b4d6ac25c231feeb24b6f4b1693eaae4f97ba88e5c694f5fbfc407e92d94721035701cac023779a7f8194f09d0cb789ecfc5295234ef8aa62af446205223aa76760fe307ee1ab4e673e4c8b6bfa73a7e147e1fc606808efc5d666167a243c15cd82649d2bfe9ebcec01a97174b795d8cc6fb16c85a780ad70b23081d5L
p = 12336923788090286356293627535978275509551220466238172479246793216159360335428847896624687800304548541969352090497660685258440656283878171775822761663689487L
q = 13295422330708449110067252512639224991344905545469973118546306846289075340318998707440336389737909413394085643161387183061984759796006678714338310382464219L
e = 65537L

string_to_be_encrypted="Ali"

phi = (p - 1) * (q - 1)
d = long(gmpy.invert(e, phi))

tup = (n ,e, d, p, q )
key = RSA.construct(tup)

random_generator = Random.new().read
data = key.encrypt(string_to_be_encrypted,random_generator)


print key.exportKey('PEM')
print key.publickey().exportKey()
print base64.b64encode(data[0])


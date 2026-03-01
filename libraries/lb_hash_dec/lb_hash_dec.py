import hashlib as hl
import base64

# Encode

def to_MD5(string):
	return hl.md5(string.encode()).hexdigest()

def to_SHA1(string):
	return hl.sha1(string.encode()).hexdigest()

def to_SHA256(string):
	return hl.sha256(string.encode()).hexdigest()

def to_SHA512(string):
	return hl.sha512(string.encode()).hexdigest()

def to_B64(string):
	return base64.b64encode(string.encode()).decode()

def to_B32(string):
	return base64.b32encode(string.encode()).decode()

def to_B85(string):
	return base64.b85encode(string.encode()).decode()

def to_Atbash(string):
	res = ""
	for c in string:
		if 'a' <= c <= 'z':
			res += chr(ord('a') + ord('z') - ord(c))
		elif 'A' <= c <= 'Z':
			res += chr(ord('A') + ord('Z') - ord(c))
		else:
			return "Only english letter supported!"
	return res

def to_XOR(string, key):
	return "".join(chr(ord(c) ^ key) for c in string)

def to_Hex(string):
	return string.encode().hex()

# Decode

def from_XOR(string, key):
	return "".join(chr(ord(c) ^ key) for c in string)

def from_B64(string):
	try:
		return base64.b64decode(string.encode()).decode()
	except:
		return "Error: Invalid Base64 data"

def from_B32(string):
	try:
		return base64.b32decode(string.encode()).decode()
	except:
		return "Error: Invalid Base32 data"

def from_B85(string):
	try:
		return base64.b85decode(string.encode()).decode()
	except:
		return "Error: Invalid Base85 data"

def from_Atbash(string):
	return to_Atbash(string)

def from_Hex(string):
	try:
		return bytes.fromhex(string).decode()
	except:
		return "Error: Invalid Hex data"

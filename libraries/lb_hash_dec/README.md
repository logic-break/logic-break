
# lb-hash-dec

© Copyright logic-break 2026

https://github.com/logic-break/logic-break/tree/main/libraries/lb_hash_dec

  

> lib made for lazy, by lazy  

installation:

    pip install lb-hash-dec

**NOTE: in code, you must import lb_hash_dec**

## What it can do:
### Hashing:
 - MD5 Hashing
 - SHA1 Hashing
 - SHA256 Hashing
 - SHA512 Hashing
### Encoding:
- Base64
- Base32
- Base85
- XOR
- Atbash (A substitution cipher that reverses the alphabet.)
- HEX
### Decoding:
- XOR
- Base64
- Base32
- Base85
- Atbash
- Hex
# Features:
- Fallback: 
if something goes wrong while decoding, it not gonna crash
- Nothing more!
# How to  use:
Import lb_hash_dec and use it
**hint:** use import lb_hash_dec as lb
# Usage:
### Encoding:
- .to_MD5(string)
- .to_SHA1(string)
- .to_SHA256(string)
- .to_SHA512(string)
- .to_B64(string)
- .to_B32(string)
- .to_B85(string)
- .to_Atbash(string)
- .to_XOR(string, key)
- .to_Hex(string)
### Decoding:
- .from_B64(string)
- .from_B32(string)
- .from_B85(string)
- .from_XOR(string, key)
- .from_Atbash(string)
- .from_Hex(string)
# Examples:
1. Standard Hashing and Encoding
```
import lb_hash_dec as lb
    
data = "logic-break"
    
# Generate a SHA256 hash
print(f"SHA256: {lb.to_SHA256(data)}")
    
# Convert string to Base64 and back
encoded = lb.to_B64(data)
print(f"Base64: {encoded}") # Output: bG9naWMtYnJlYWs=
    
decoded = lb.from_B64(encoded)
print(f"Decoded: {decoded}")
```
2. Working with Ciphers (Atbash & XOR
```
import lb_hash_dec as lb

message = "SecretMessage"

# Apply Atbash cipher (Mirror alphabet)
encrypted_atbash = lb.to_Atbash(message)
print(f"Atbash Encrypted: {encrypted_atbash}") # Output: HvxivgNvhhztv

# Use XOR encryption with a numeric key
key = 42
encrypted_xor = lb.to_XOR(message, key)
print(f"XOR Encrypted: {encrypted_xor}")

# Decrypt XOR back to original
print(f"XOR Decrypted: {lb.from_XOR(encrypted_xor, key)}")
```
3. Error Handling
```
import lb_hash_dec as lb

# Trying to decode invalid data
invalid_data = "This is not hex!"

# The library returns a helpful error string instead of crashing
result = lb.from_Hex(invalid_data)
print(f"Hex Result: {result}") # Output: Error: Invalid Hex data

# Atbash check for non-English characters
print(lb.to_Atbash("Привет")) # Output: Only english letter supported!
```

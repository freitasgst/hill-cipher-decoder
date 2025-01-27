[![Python](https://img.shields.io/badge/python-3.12-green)](https://www.python.org)
[![Tests](https://github.com/freitasgst/hill-cipher-decoder/workflows/Tests/badge.svg)](https://github.com/freitasgst/hill-cipher-decoder/actions)
# Hill Cipher Decoder
Decode encrypted "N-Hill Cipher" messages

## Requirements
- Make
- Python 3.12
- Pip >= 21.0.1
- Other requirements: 
    - requirements.txt 
    - requirements-dev.txt (development dependencies)

## Usage
```
make install
```
The "N-Hill Cipher" technique is a substitution cipher that uses a square matrix of ordem N to encode a message 
(with: number of characters = multiple of N).

The **Hill Cipher Decoder**: 
1. Asks for N;
2. Asks the user to input every element of the matrix NxN (encryption key);
3. Asks for the encrypted message;
4. The expected **output** is the decrypted message. 

The **Hill Cipher Decoder** will calculate the decryption key based on the provided matrix and will decode the inputed message. 

## Contributing

### Installing dev environment requirements:
```
make install-dev
```

### Testing
```
make coverage
```

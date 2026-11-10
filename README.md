# Classical Ciphers Brute-Force

Two small Python tools to break classical ciphers by brute force: **Caesar** and **Vigenère**.
Built for learning cryptanalysis fundamentals and for CTF practice.

## Scripts

| Script | Cipher | Approach |
|---|---|---|
| `caesar_bruteforce.py` | Caesar | Tries all 25 possible shifts and prints every candidate plaintext |
| `vigenere_bruteforce.py` | Vigenère | Tests candidate keys against the ciphertext and prints the decryptions |

<img width="1080" height="1920" alt="caesar_cipher_vertical" src="https://github.com/user-attachments/assets/34e61a95-a6a4-4bf8-b35a-67533488a450" />

<img width="1080" height="1080" alt="caesar_wheel_modern" src="https://github.com/user-attachments/assets/71cd0351-0e3e-4a76-a238-e179e736c3b8" />

<img width="1080" height="1920" alt="vigenere_cipher_vertical" src="https://github.com/user-attachments/assets/2195e505-f231-4a79-b510-fc6aa2b48883" />

<img width="860" height="470" alt="vigenere_demo" src="https://github.com/user-attachments/assets/145494ca-a1de-43f1-a756-1292f9014a93" />





## Requirements

- Python 3.8 or newer
- No external dependencies

## Usage

### Caesar

```bash
python caesar_bruteforce.py "Khoor Zruog"
```

Every shift is shown, so the correct plaintext can be spotted by eye:

```
Shift  1: Jgnnq Yqtnf
Shift  2: Ifmmp Xpsme
Shift  3: Hello World   <-- readable text
...
```

### Vigenère

For example, the ciphertext `LXFOPVEFRNHR` decrypts to `ATTACKATDAWN` with the key `LEMON`.


> The exact output format depends on the script version. Run each script without
> arguments (or with `-h`) to see its available options.

## How it works

- **Caesar** shifts every letter by a fixed amount. With only 25 non-trivial keys,
  trying them all is instant.
- **Vigenère** uses a repeating keyword, so the key space grows as 26<sup>n</sup>
  for a key of length *n*. Brute force is practical for short keys or with a wordlist.

Non-letter characters (spaces, digits, punctuation) are left unchanged.

## Limitations

- Brute force on Vigenère becomes slow as the key length increases.
- Judging which candidate is the real plaintext is easiest for English text.
- These tools target classical ciphers only. They are not meant for modern encryption.



## Disclaimer

For educational use, CTF challenges and data you own or are authorized to analyze.

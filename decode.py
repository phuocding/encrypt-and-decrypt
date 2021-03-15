import base64


def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        # print(type(key_c))

        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)

        enc.append(enc_c)
        # print(type(enc_c))

    # join list and encode
    j_enc = "".join(enc).encode()

    print(base64.urlsafe_b64encode(j_enc).decode())


def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)

        dec.append(dec_c)

    print("".join(dec))


def main():
    print("Hello Phuoc!")

    while True:
        option = input("Please choose MODE (e for encrypt, d for decrypt): ")

        if option == "e":
            _key = input("typing key: ")
            _clear = input("typing message: ")
            encode(_key, _clear)
            continue
        elif option == "d":
            _key = input("typing key: ")
            _enc = input("typing message: ")
            decode(_key, _enc)
            continue
        else:
            print("please choose again")
            continue


if __name__ == "__main__":
    main()
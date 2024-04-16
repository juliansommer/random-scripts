import hashlib

algorithms = ["md2", "md4", "md5", "sha1", "sha256", "sha384", "sha512"]

def hash_string(type, string):
    match type:
        case "md2":
            result = hashlib.md2(string.encode()).hexdigest()
        case "md4":
            result = hashlib.md4(string.encode()).hexdigest()
        case "md5":
            result = hashlib.md5(string.encode()).hexdigest()
        case"sha1":
            result = hashlib.sha1(string.encode()).hexdigest()
        case"sha256":
            result = hashlib.sha256(string.encode()).hexdigest()
        case"sha384":
            result = hashlib.sha384(string.encode()).hexdigest()
        case"sha512":
            result = hashlib.sha512(string.encode()).hexdigest()
        case _:
            print("Not A Valid Hash")
            return

    print(f"{type.upper()} Hash:\n{result}\n{len(result)} Characters")


def main():
    typeinput = input("Input Hashing Algorithm: ")
    string = input("String to Hash: ")
    hash_string(typeinput.lower(), string)


if __name__ == '__main__':
    main()
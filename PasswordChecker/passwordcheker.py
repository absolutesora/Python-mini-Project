import requests
import hashlib
import sys

def request_api_pass(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error due to {res}, password must be Hashed')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    password_5char, tail_char = sha1password[:5], sha1password[5:]
    response = request_api_pass(password_5char)
    return get_password_leaks_count(response, tail_char)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Your password: "{password}" was found {count} times. You might considered yourself to change password!')
        else:
            print('Great! Your password is not found in the list. You password is safe!')


if __name__ == "__main__":
    # Read text file and read per line per word.
    with open('test.txt', 'r') as data:
        for line in data.readlines():
            line = line.splitlines() # this makes the string as one array.
            main(line)

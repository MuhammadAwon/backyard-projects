# import requests
# import hashlib


# def check_api_data(five_chars):
#     url = 'https://api.pwnedpasswords.com/range/' + five_chars
#     res = requests.get(url)
#     if res.status_code != 200:
#         raise RuntimeError(f'Error Found: {res.status_code}, check api')
#     else:
#         return res


# def check_password_leaks(hashes, searches):
#     hashes = (line.split(':') for line in hashes.text.splitlines())
#     for sequence, count in hashes:
#         if sequence == searches:
#             return count
#     return 0


# def check_my_password(password):
#     sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
#     sha1pass_upper = sha1pass.upper()
#     head, tail = sha1pass_upper[:5], sha1pass_upper[5:]
#     response = check_api_data(head)
#     return check_password_leaks(response, tail)


# def main():
#     with open('passkeeper.txt', 'r') as f:
#         passwordlist = []
#         for line in f:
#             content = line.strip()
#             passwordlist.append(content)

#         for password in passwordlist:
#             count = check_my_password(password)
#             if count:
#                 print(f'{password} found {count} many times')
#             else:
#                 print(f'{password} is not found, {count} match')
#         print('Search completed!')


# if __name__=='__main__':
#     main()

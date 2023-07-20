import argparse
import requests
import time
import sys
import json

OK = '\033[92m'
WARNING = '\033[93m'
FAILRED = '\033[91m'
ENDLINE = '\033[0m'


def print_table(iterable, header):
    max_len = [len(x) for x in header]
    for row in iterable:
        row = [row] if type(row) not in (list, tuple) else row
        for index, col in enumerate(row):
            if max_len[index] < len(str(col)):
                max_len[index] = len(str(col))
    output = '-' * (sum(max_len) + 1) + '\n'
    output += '|' + ''.join([h + ' ' * (l - len(h)) + '|' for h, l in zip(header, max_len)]) + '\n'
    output += '-' * (sum(max_len) + 1) + '\n'
    for row in iterable:
        row = [row] if type(row) not in (list, tuple) else row
        output += '|' + ''.join([str(c) + ' ' * (l - len(str(c))) + '|' for c, l in zip(row, max_len)]) + '\n'
    output += '-' * (sum(max_len) + 1) + '\n'

    return output


def consult(email, key):
    url = "https://breachdirectory.p.rapidapi.com/"
    body = {"func":"auto","term":email}
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }
    r = requests.get(url, headers=headers, params=body)
    results = r.json()
    if r.status_code == 200:
        if results['result']:
            print(FAILRED + "[!!] Your email " + email + " has been leaked" + ENDLINE)
            print("Breaches you were pwned in :")
            table = []
            header = ['Sources', 'Password', 'Date']
            for row in results['result']:
                sources = ','.join(row['sources'])
                password = row['line'].split(':')[1] if not row['email_only'] else 'no_password'
                date_beach = row['last_breach']
                table.append([sources, password, date_beach])
            x = print_table(table, header)
            loading()
            print('\n')
            print(x)
        else:
            print(OK + "[i] Your email " + email + " has not been leaked" + ENDLINE)
    else :
        print(WARNING + "[!] Something is wrong, please verify your api key or retry again" + ENDLINE)
    


def banner():
    print("=======================================================")
    print("\033[91m \033[1m _______  _______  _______  ______   _______ \033[0m")
    print("\033[91m \033[1m|   _   ||  _    ||   _   ||      | |   _   |\033[0m")
    print("\033[91m \033[1m|  |_|  || |_|   ||  |_|  ||  _    ||  |_|  |\033[0m")
    print("\033[91m \033[1m|       ||       ||       || | |   ||       |\033[0m")
    print("\033[91m \033[1m|       ||  _   | |       || |_|   ||       |\033[0m")
    print("\033[91m \033[1m|   _   || |_|   ||   _   ||       ||   _   |\033[0m")
    print("\033[91m \033[1m|__| |__||_______||__| |__||______| |__| |__|\033[0m v2.0 \n")


def menu():
    print("=======================================================\n")
    print("ABADA is a Python script that allows you to check if an email address has been compromised in any known data breaches.\n")
    print("It provides a simple and convenient way to verify the security of email addresses and gain insights into potential risks.\n")
    print("=======================================================\n")


def anim():
    array = ['[]']
    for i in range(1, 61):
        text = ''
        for j in range(i):
            text = text + '#'
        array.append('[' + text + ']')
    return array


def loading():
    animation = anim()
    for i in range(1, 61):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Loading : " + animation[i % len(animation)] + ' ' + str(int(round(i * 5 / 3))) + '%')
        sys.stdout.flush()


def main(email, key):
    loading()
    print("\n")
    consult(email, key)


if __name__ == '__main__':
    banner()
    menu()
    parsing = argparse.ArgumentParser(description="This tool verify if the email is leaked or not.")
    parsing.add_argument('-e', '--email', dest='email', help='Put your email')
    parsing.add_argument('-k', '--key', dest='key', help="Put your RapidApi key")
    args = parsing.parse_args()
    email = str(args.email)
    key = str(args.key)

    if email == "None":
        print(FAILRED + '!!! Please put an email address' + ENDLINE)
    elif key == "None":
        print(FAILRED + '!!! Please put RapidApi key' + ENDLINE)
    else:
        main(email, key)
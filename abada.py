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



def consult(email,proxy):
	try:
		user_agent = {"User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion",}
		if proxy is "None":
			r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/'+email, headers=user_agent)
		else :
			proxy_object = {'http': 'http://'+ proxy}
			r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/'+email, headers=user_agent, proxies = proxy_object)
	
		if r.status_code == 200 :
			print FAILRED + "[!!] Your email " + email + " has been leaked" + ENDLINE
			print "Breaches you were pwned in :"
			json_content = r.content.decode('utf8')
			jsonn = json.loads(json_content)
			table = []
			header = ['Website','Date','Emails leaked']
			for j in jsonn :
				table.append([unicode(j['Domain']),unicode(j['BreachDate']),unicode(j['PwnCount'])])
			x = print_table(table, header)
			loading()
			print('\n')
			print x

		elif r.status_code == 404 :
			print OK + "[i] Your email " + email + " has not been leaked" + ENDLINE

		elif r.status_code == 400 :
			print WARNING + "[!] Please retry another email ! " + ENDLINE

		elif r.status_code == 429:
			print WARNING + "[!] Too many request, please retry after " + r.headers['Retry-After'] + " seconds" + ENDLINE
			time_to_retry = float(r.headers['Retry-After'])
			time.sleep(time_to_retry)
			consult(email)
		elif r.status_code == 403:
			print ' 403'

		else :
			print WARNING + "[!] Something is wrong, please retry again" + ENDLINE

	except:

		print ("Some error occurred with queries leakeds.")

def banner():
	print("=======================================================")
	print("\033[91m \033[1m _______  _______  _______  ______   _______ \033[0m")
	print("\033[91m \033[1m|   _   ||  _    ||   _   ||      | |   _   |\033[0m")
	print("\033[91m \033[1m|  |_|  || |_|   ||  |_|  ||  _    ||  |_|  |\033[0m")
	print("\033[91m \033[1m|       ||       ||       || | |   ||       |\033[0m")
	print("\033[91m \033[1m|       ||  _   | |       || |_|   ||       |\033[0m")
	print("\033[91m \033[1m|   _   || |_|   ||   _   ||       ||   _   |\033[0m")
	print("\033[91m \033[1m|__| |__||_______||__| |__||______| |__| |__|\033[0m v1.0 \n")

def menu():
	print("=======================================================\n")
	print("Usage : This tool verify if the email is leaked or not.\n")
	print("=======================================================\n")

def anim():
	array=['[]']
	for i in range(1,60):
		text=''
		for j in range(i):
			text=text+'#'
		array.append('['+text+']')
	
	return array
def loading():
	animation = anim()

	for i in range(1,60):
	    time.sleep(0.1)
	    sys.stdout.write("\r" + "Loading : " + animation[i % len(animation)] + ' ' + str(i*5/3) +'%')
	    sys.stdout.flush()


	

def main(email,filename,proxy):
	if email != "None" :
		loading()
		print("\n")
		consult(email,proxy)
	else:
		emails = [line.rstrip('\n') for line in open(filename)]
		loading()
		print("\n")
		for email in emails :
			consult(email,proxy)

if __name__ == '__main__':

	banner()
	menu()

	parsing = argparse.ArgumentParser(description="This tool verify if the email is leaked or not.")

	parsing.add_argument('-e','--email', dest='email', help='Insert your email')
	parsing.add_argument('-f','--file',dest='filename', help="File to check all addresses per line")
	parsing.add_argument('--proxy' , dest='proxy', help="Put a proxy")
	args = parsing.parse_args()

	email = str(args.email)
	filename = str(args.filename)
	proxy = str(args.proxy)
	
	if email=="None" and filename=="None":
		print('Options : ')
		print('	-e [address], --email [address]		Put an email to check if its leaked or not.\n')
		print('	-f [file], --filename [file]		Put a file to check all addresses per line\n')
		print('	--proxy [ip:port]			Put a proxy\n')
		print('	-h , --help				Show this help message and exit\n')
	else:
		main(email,filename,proxy)

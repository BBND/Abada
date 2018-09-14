![Trace your mail](https://checkup.email/assets/img/logo.png)
# Abada ✉️
Verify an email address if it's pwned or not.

⛔If the tool is used for malicious purposes, we will not be liable.⛔

## About the tool
- **Tool accessible to all**
- **Accurate tracking**
- **Multitasking tool**
- **Instant answer**

## How it works ?

| Argument | Description |
| ------ | ------ |
| -h, --help | Display help message and exit |
| -e [address], --email [address] | Put an email to check if it's leaked or not |
| -f [file], --filename [file]  | Put a file to check all addresses per line |
| --proxy [ip:port]  | Use a proxy |

## Usage Examples

```sh
$ python abada.py -e test@example.com
```

```sh
$ python abada.py -e test@example.com --proxy[0.0.0.0:99]
```

## Author
[BBND](https://www.bbnd.eu)

## For more informations :
[Checkup email](https://www.checkup.email)

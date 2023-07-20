<p align="center">
  <img width="460" height="300" src="https://abada.bbnd.eu/assets/img/logo.png">
</p>

# Abada ✉️
is a Python-based tool that allows you to check if an email address has been compromised in a data breach. It utilizes the BreachDirectory API from RapidAPI to provide comprehensive information about the breach, if any.

⛔If the tool is used for malicious purposes, we will not be liable.⛔

## About the tool
- **Tool accessible to all**
- **Accurate tracking**
- **Multitasking tool**
- **Instant answer**

## Features
- Quick and easy verification of email addresses for data breaches.
- Utilizes the BreachDirectory API to fetch breach information.
- Provides detailed breach information including breach name, date, and affected accounts.

## Install

Clone the repository

```sh
$ git clone https://github.com/BBND/Abada
$ cd Abada
```

**Obtain an API key from RapidAPI (BreachDirectory API) here :**
https://rapidapi.com/rohan-patra/api/breachdirectory

## How it works ?

| Argument | Description |
| ------ | ------ |
| -h, --help | Display help message and exit |
| -e [address], --email [address] | Put your email address |
| -k [key], --key [key] | Put your RapidApi key |


## Usage Examples

To verify an email address, follow these steps:

- Open the terminal and navigate to the project directory.
- Run the script with the following command:

```sh
$ python abada.py -e test@example.com -k your_key
```

- Enter the email address you want to verify when prompted, and enter the API key.
- The tool will connect to the BreachDirectory API and retrieve the breach information for the provided email address(es).
- The results will be displayed on the console, showing the breach name, date, and affected accounts, if any.

### Data Deletion

If you are the owner of an email address and find that your email has been compromised in a breach, you have the option to request the removal of your data from the BreachDirectory database. You can do this by visiting the [Delete My Data](https://breachdirectory.org/deletemydata) page and following the instructions provided there.

## Disclaimer

This tool is provided for educational and informational purposes only. The accuracy and completeness of the data returned by the BreachDirectory API may vary. Use the tool responsibly and respect the privacy of others.

## Author
[BBND](https://www.bbnd.eu)

## For more informations :
[ABADA](https://abada.bbnd.eu)

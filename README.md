# GenBruter
It is a simple password brute force tool designed for ethical hacking and security testing. Automates the process of selecting passwords for a given user on a website by sending POST requests with different passwords and analyzing the response.


## Installation and Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/14mb1v45h/cyberspace030.git
   cd cyberspace030
   ```
2. **Install dependencies**
   Make sure you have Python 3 and `pip` installed.
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the program**
   ```bash
   python GenBruter.py
   ```
## Usage
- **Target URL**: Enter the URL of the login page you want to attack.
- **Username**: Enter the username (e.g., email) of the user.
- **Negative Response**: Enter the text indicating a failed login attempt (e.g., "Invalid").

![image](https://github.com/user-attachments/assets/613e0300-a85b-40cd-b2ce-634af2196987)

The program will automatically load the list of passwords from the `passwords.txt` file located in the same directory as the script and start the brute-force process.

## Requirements
- Python 3.x
- `requests` library (install with `pip`)

## Notes
- **Password File**: Ensure that the `passwords.txt` file contains one password per line.
- **CSRF Protection**: Some sites may use CSRF tokens or other security mechanisms. In such cases, this tool may not work as expected.

## Disclaimer
This tool is intended for educational purposes and security testing only. Do not use it for unauthorized access to any systems. Always obtain permission before using this tool on a website.


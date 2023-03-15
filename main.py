import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print(f'Active Connection. Hostname: {hostname}')
        print('FTP Anonymous Login Succeeded')
    except Exception:
        print(f'No active connection. Hostname {hostname}')
        print('FTP Anonymous Login Failed')

# Scan given host name for anonymous FTP connection


if __name__ == '__main__':
    # Random IP
    anonLogin('90.130.70.73')
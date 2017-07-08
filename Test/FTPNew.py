import ftplib
#site_address = input('Please enter the ftp address:')

def ftp_connect():
    while True:
        #site_address = input('Please enter FTP address:')
        try:
            with ftplib.FTP("10.29.21.56") as ftp:
                ftp.login("repgen", "reports001")
                print(ftp.getwelcome())
                print('current directory', ftp.pwd())
                ftp.dir()
                print('Valid commands are cd/get/ls/exit - ex:get Manish-Report.csv')
                ftp_command(ftp)
                break  #once ftp_command() exits, end this function (exit program)
        except ftplib.all_errors as e:
            print('failed to connect, check your address and credentials.', e)


def ftp_command(ftp):
    while True: # run untill 'exit' command is recieved from user
        command  = input('Enter the command: ')
        commands = command.split()  #split command and file/directory into list

        if commands[0] == 'cd': #change direcory
            try:
                ftp.cwd(commands[1])
                print('Direcory of', ftp.pwd())
                ftp.dir()
                print('Current Direcory', ftp.pwd())
            except ftplib.error_perm as e: #handle 550(not found/ no permission error)
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'Directory may not exist or you may not have permission to view it.')
        elif commands[0] == 'get' : #Download file
            try:
                ftp.retrbinary('RETR ' + commands[1], open(commands[1],'wb').write)
                print('File Successfully downloaded.')
            except ftplib.error_perm as e: #handle 550(not found/ no permission error)
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'File may not exist or you may not have permission to view it.')
        elif commands[0] == 'ls': #Printing Directory Listing
            print('Directory of', ftp.pwd())
            ftp.dir()
        elif commands[0] == 'exit': #exit applications
            ftp.quit()
            print('GoodBye')
            break
        else:
            print('Invalid command, try again(valid options are cd/get/ls/exit ')
print('Welcome to python FTP')
ftp_connect()







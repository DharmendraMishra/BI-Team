import sys
import ftplib
import os
import time

import errno

server = "10.29.16.42"
user = "repgen"
password = "reports001"
source = "/mnt/svmdev01exporeporting01/crdg2-reporting-bak/data/reports/2017/2017-04/2017-04-01/tfcrNewIOs.2017-04-01.csv"
destination = "C:/Users/Dharmendra.Mishra/Downloads"
interval = 0.05

ftp = ftplib.FTP(server)
ftp.login(user, password)


def downloadFiles(path, destination):
    try:
        ftp.cwd(path)
        os.chdir(destination)
        mkdir_p(destination[0:len(destination) - 1] + path)
        print
        "Created: " + destination[0:len(destination) - 1] + path
    except OSError:
        pass
    except ftplib.error_perm:
        print
        "Error: could not change to " + path
        sys.exit("Ending Application")

    filelist = ftp.nlst()

    for file in filelist:
        time.sleep(interval)
        try:
            ftp.cwd(path + file + "/")
            downloadFiles(path + file + "/", destination)
        except ftplib.error_perm:
            os.chdir(destination[0:len(destination) - 1] + path)

            try:
                ftp.retrbinary("RETR " + file, open(os.path.join(destination + path, file), "wb").write)
                print
                "Downloaded: " + file
            except:
                print
                "Error: File could not be downloaded " + file
    return


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


downloadFiles(source, destination)
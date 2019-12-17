import zipfile
import threading
from datetime import datetime

enter = input("Press Enter")


filez = input("Zip-file: ")


def th(zf, password):
    counter = 1

    global a
    a = False
    with open(dictionary, 'rb') as text:
        for entry in text.readlines():
            password = entry.strip()
            try:
                with zipfile.ZipFile(filez, 'r') as zf:
                    zf.extractall(pwd=password)

                    data = zf.namelist()[0]

                    data_size = zf.getinfo(data).file_size

                    print(
                        '''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************'''
                        % (password.decode('utf8'), data, data_size))
                    a = True
                    break



            except:
                number = counter
                print('[%s] [-] Password failed! - %s' % (number, password.decode('utf8')))
                counter += 1
                a = False
                pass


def main():
    start_time = datetime.now()
    global dictionary
    t1 = threading.Thread(target=th, args=(filez, enter))
    t2 = threading.Thread(target=th, args=(filez, enter))
    t3 = threading.Thread(target=th, args=(filez, enter))
    dictionary = '213.txt'
    t1.start()
    t1.join()
    if a == True:
        end_time = datetime.now()
        print(end_time - start_time)
        exit(0)
    dictionary = 'withpassword.txt'
    t2.start()
    t2.join()
    if a == True:
        end_time = datetime.now()
        print(end_time - start_time)
        exit(0)
    dictionary = 'privet.txt'
    t3.start()
    t3.join()
    if a == True:
        end_time = datetime.now()
        print(end_time - start_time)
        exit(0)
    end_time = datetime.now()
    print(end_time - start_time)

if __name__ == '__main__':
    main()

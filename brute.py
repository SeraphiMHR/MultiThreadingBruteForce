import zipfile
import threading

enter = input("Press Enter")


class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()


filez = "locked.zip"


def th(zf, password):
    counter = 1
    dictionary = input()
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
    t1 = threading.Thread(target=th, args=(filez, enter))
    t2 = threading.Thread(target=th, args=(filez, enter))
    t3 = threading.Thread(target=th, args=(filez, enter))
    t1.start()
    t1.join()
    if (a == True):
        exit(0)
    elif (a==False):
        t2.start()
        t2.join()
        if (a==True):
            exit(0)
        elif(a==False):
            t3.start()
            t3.join()
            return 0



if __name__ == '__main__':
    main()

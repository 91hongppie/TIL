from time import sleep


def sleep_3s():
    sleep(3)
    print('일어남~~!!')


print('Start sleeping')
sleep_3s()  # blocking 얘가 실행되기 전에 다음 것들은 기다려야함
print('End of program')

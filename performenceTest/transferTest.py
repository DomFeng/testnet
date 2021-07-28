# writer by fengjianguang
# time: 2021/7/20 11:33 上午
import os

#2000用户给test父账户转账
import time

os.system('fns setup -S https://prod-testnet.prod.findora.org')
sec_key = open('/home/dom/performenceTest/sec_key.txt', 'r')
for line in sec_key:
    print('fns transfer -n $((1 * 1000000)) -f \''+line.strip()+'\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
    os.system('fns transfer -n $((1 * 1000000)) -f \''+line.strip()+'\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
    time.sleep(1)
sec_key.close()
print('发送交易完成！')
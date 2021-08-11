# writer by fengjianguang
# time: 2021/7/20 11:33 上午
import os

# 2000用户给test父账户转账
import time

os.system('fns setup -S https://prod-testnet.prod.findora.org')
sec_key = open('/home/ubuntu/testscript/sec_key.txt', 'r')
transferResult = open('/home/ubuntu/testscript/log.txt', 'w')
counter = 1
for line in sec_key:
    print('第' + str(counter) + '个钱包开始转账:', file=transferResult)
    print(
        'fns transfer -n $((1 * 1000000)) -f \'' + line.strip() + '\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'', file=transferResult)
    output = os.system(
        'fns transfer -n $((1 * 1000000)) -f \'' + line.strip() + '\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
    print(output.read(), file=transferResult)
    time.sleep(1)
sec_key.close()
transferResult.close()
print('发送交易完成！')

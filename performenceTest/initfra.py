# writer by fengjianguang
# time: 2021/7/19 6:03 下午
import os
import time

# root给test父钱包转账
os.system('fns setup -S https://prod-testnet.prod.findora.org')
pub_key = open('/home/admin/testscript/pub_key.txt', 'r')
# print('fns transfer -n $((5000 * 10000 * 1000000)) -f \'o9gXFI5ft1VOkzYhvFpgUTWVoskM1CEih0zJcm3-EAQ=\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
# os.popen('fns transfer -n $((5000 * 10000 * 1000000)) -f \'o9gXFI5ft1VOkzYhvFpgUTWVoskM1CEih0zJcm3-EAQ=\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
# time.sleep(30)
counter = 1
# test父钱包给2000个test钱包转账
for line in pub_key:
    print('第' + str(counter) + '个钱包开始转账:')
    print(
        'fns transfer -n $((1 * 1000 * 1000000)) -f \'0GSbutUqx46unaifwRwBg-cq6w_dCZqsQG0S-wndhVc=\' -t \'' + line.strip() + '\'')
    output = os.popen(
        'fns transfer -n $((1 * 1000 * 1000000)) -f \'0GSbutUqx46unaifwRwBg-cq6w_dCZqsQG0S-wndhVc=\' -t \'' + line.strip() + '\'')
    counter += 1
    time.sleep(31)
pub_key.close()

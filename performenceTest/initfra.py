# writer by fengjianguang
# time: 2021/7/19 6:03 下午
import os

#root给test父钱包转账
import time
os.system('fns setup -S https://prod-testnet.prod.findora.org')
pub_key = open('/home/dom/performenceTest/pub_key.txt', 'r')
print('fns transfer -n $((5000 * 10000 * 1000000)) -f \'o9gXFI5ft1VOkzYhvFpgUTWVoskM1CEih0zJcm3-EAQ=\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
# os.popen('fns transfer -n $((5000 * 10000 * 1000000)) -f \'o9gXFI5ft1VOkzYhvFpgUTWVoskM1CEih0zJcm3-EAQ=\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
# time.sleep(30)

for line in pub_key:
    print('fns transfer -n $((1 * 10000 * 1000000)) -f \'0GSbutUqx46unaifwRwBg-cq6w_dCZqsQG0S-wndhVc=\' -t \''+line.strip()+'\'')
    os.system('fns transfer -n $((1 * 10000 * 1000000)) -f \'0GSbutUqx46unaifwRwBg-cq6w_dCZqsQG0S-wndhVc=\' -t \''+line.strip()+'\'')
    time.sleep(16)
pub_key.close()
# writer by fengjianguang
# time: 2021/7/20 11:33 上午
import os
import time

# 2000用户给test父账户转账
os.system('fns setup -S https://prod-testnet.prod.findora.org')
# sec_key = open('/home/admin/testscript/sec_key_test.txt', 'r')
sec_key = open('/home/admin/testscript/sec_key.txt', 'r')
transferlog = open('/home/admin/testscript/translog.txt', 'w')
counter = 1
i = 0
datetest = os.popen('date')
print('开始时间：' + datetest.read(), file=transferlog)
for line in sec_key:
    print('第' + str(counter) + '个钱包开始转账:', file=transferlog)
    print(
        'fns transfer -n $((1 * 1000000)) -f \'' + line.strip() + '\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'',
        file=transferlog)
    output = os.popen(
        'fns transfer -n $((1 * 1000000)) -f \'' + line.strip() + '\' -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
    print(output.read(), file=transferlog)
    counter += 1
    time.sleep(1)

print('发送交易完成！')
# 判断转账进度：
while i != 1:
    progressw = open('/home/admin/testscript/progresslog.txt', 'w')
    output1 = os.popen('fns show')
    print('fns show')
    print(output1.read(), file=progressw)
    print('写入文件')
    progressw.close()
    progressr = open('/home/admin/testscript/progresslog.txt', 'r')
    print('------开始遍历------')
    for fra in progressr:
        if fra[16:25] == 'FRA units':
            print(fra)
            if fra[0:9] == '195971033':
                datetest = os.popen('date')
                print('交易全部成功！')
                print('结束时间：' + datetest.read(), file=transferlog)
                i = 1
    progressr.close()
    time.sleep(2)

sec_key.close()
transferlog.close()


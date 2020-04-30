import uuid

#使用uuid出的随机数位数固定
def get_coupon(num):
    with open('coupon3.txt', 'w') as fh:
        coupon_list = []
        for i in range(num):
            coupon = str(uuid.uuid4()).replace('-','')
            if coupon not in coupon_list:
                coupon_list.append(coupon)
                fh.write(coupon+'\n')
        print(coupon_list)
        print(len(coupon_list))

if __name__ == '__main__':
    get_coupon(200)
import redis



if __name__ == '__main__':

    with open('./Sources/coupons', 'r') as f:

        r = redis.Redis(host = 'localhost', port = 6379);
        coupons_ = f.readlines()

        for index in range(0, len(coupons_)):
            r.set(str(index+1), str(coupons_[index]));

    f.close();

    print 'successfully put data in redis'

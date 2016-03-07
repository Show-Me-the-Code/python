xyjxyf Notes
======
## Mac上安装Redis

1. 下载源文件

[redis-3.0.7.rar.gz](http://download.redis.io/releases/)

2. 安装

```
$ tar -zxvf redis-3.0.6.tar.gz
$ cd redis-3.0.7
$ make test
$ make install
```

3. 配置

```
$ vi ./redis.conf
	
 # 设置为后台运行
daemonize yes

 # 设置pid文件位置
pidfile /usr/local/redis/redis.pid

 # 连接超时时间设置为120秒
timeout 120

 # 设置日志级别
loglevel debug

 # 设置日志文件位置
logfile "/usr/local/redis/log/6379.log"

 # 数据文件所在目录
dir /usr/local/redis/data/6379
```

4. 启动redis服务器

```
$ ./redis-server
```

5. 安装Python的Redis模块

我的mac安装了python双版本，用python3


```
$ pip3 install redis
```
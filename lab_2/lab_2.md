# 网络空间安全综合实践 III

## 2 lab_2 恶意流量分析

本次实验使用 wireshark 对一次攻击中截获的数据包进行分析，以了解攻击方法和靶机的信息。

### 2.1 wireshark 使用

wireshark 在前几轮实验中多次用到，在本次实验中只要掌握打开文件，设置过滤器，查看数据包内容，跟踪流，保存数据至文件几个功能即可。

### 2.2 分析方法

（仅适用本次实验，不适用于实际情况）  

实验要求获得被攻击主机信息，攻击方法和过程，由传输的文件解密出的账户密码。

使用 wireshark 打开实验文件，简单浏览，可以发现从 ftp 和 http 协议的传输中可以获得较多信息。筛选 http 流量，查看靶机返回信息可以了解到服务器软件版本为 Apache/2.2.8 (Ubuntu) DAV/2。

猜测通过 ftp 下载了密码文件。故设置筛选条件为靶机的 ip 和 ftp 协议，可以发现，攻击机从靶机处申请下载了一个大小为1311bytes，名为 user.tgz 的文件。将筛选条件设为 ftp-data，仅有一条报文。追踪流-tcp，将原始数据另存为 tgz 格式文件，解压后获得 passwd 和 shadow 文件。

查看 ftp 报文流，发现 ftp 服务器版本为 vsftpd 2.3.4。搜索得知该版本存在后门漏洞（[这篇文章](https://subscription.packtpub.com/book/networking_and_servers/9781786463166/1/ch01lvl1sec18/vulnerability-analysis-of-vsftpd-2-3-4-backdoor)对该漏洞进行了详尽的解释）。通过使用该漏洞，可通过6200端口执行任意命令。查看6200端口的数据包，跟踪 tcp 流可以发现攻击者执行了一些指令打包了账号密码文件。最后攻击者通过 ftp 将打包后的文件下载至本地。
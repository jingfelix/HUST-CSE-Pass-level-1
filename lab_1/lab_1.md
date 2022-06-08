# 网络空间安全综合实践 III

## 1 lab_1 使用 metaspliot 进行渗透测试

本次实验采用 nmap 对靶机进行扫描，使用 Metaspliot 进行渗透和攻击。

nmap 扫描命令参考：nmap -T4 -sV -v 192.168.2.222

扫描后可得到靶机开启的端口，对应的服务和版本。其中，确定可以直接利用 metaspliot 进行攻击的漏洞有：ftp/samba/domain

在终端输入 ```msfconsole``` 进入 meta，可使用 ```search + 关键词``` 对可能使用的模块进行搜索；```use + 模块名``` 选择要使用的 module；```show options``` 显示需设置的参数；```set + 变量名 + 参数``` 进行设置；exploit 开启攻击。

注意选择能够反弹 shell 的 payload，由此获取 root 权限和 shadow 文件内容。使用 hashcat 或其他工具进行破解。
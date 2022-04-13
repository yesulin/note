# Linux 网络操作系统

[toc]



## 项目一 安装与基本配置Ｌｉｎｕｘ操作系统



## 项目二 熟练使用ｌinux常用命令

打开终端

普通用户和超级用户

区分大小写，像ls和LS 是不一样的

tab 自动补齐 例：history 历史命令记录 ，  clear 清除屏幕

向上或向下的键盘键

使用分号来分隔命令执行多条命令 `cd /;ls`

以后台方式执行“&”符号  `find / -name httpd.conf &`

长命令行，可以使用反斜杠“\”

### 浏览目录类命令

- pwd 查看当前所在位置，普通用户的家目录 /home/yy

- cd 切换目录

  `cd test`

  ` cd ..`

- ls 浏览目录或文件

  - ls -a 显示隐藏文件
  - ls -l 长格式显示
  - ls -R 显示子目录或子文件

-  ll 长格式显示
### 浏览文件类命令
- cat more less 查看文件内容
  - cat httpd.conf  滚屏显示文件内容或是将多个文件合并成一个文件
    - `cat file2 file1>file3 `  覆盖
    - `cat file2 file1>>file3 `  追加
  - more httpd.conf   `more /etc/passwd` 空格翻页，Q退出 ，回车是下一行
  - less httpd.conf
- tail -3 /etc/passwd 显示尾部几行
- head -3 /etc/passwd 显示头部几行

### 目录操作类命令

- mkdir -p test/test1/test2 递归创建目录 

```
test/
  `-- test1
      `-- test2
```



- rmdir -p test/test1/test2 递归删除目录 

- -a 所有状态

- -R 递归复制

### cp命令



```
.
├── a
├── dir1
│   ├── a
│   └── file1
├── file1

cp file1 dir1/
cp -R a dir1/
```



`.bashrc 隐藏文件`

`cp ~/.bashrc /tmp/bashre`

`cp -i ~/.bashrc /tmp/bashre`

`cp  -a /var/log/wtmp wtmp_2`



### 文件操作类命令

- mv 移动或改名
- rm  `rm -rf test2` `rm -ri test3/`
- touch 新建文件
- diff 比较两个文件的差别
- ln 链接 
  - 硬链接
  - 软链接 -s  `ln -s a c`
- tar -czvf 压缩 `tar -czvf test.tar.gz a b c`
- tar -xzvf 解压 `tar xzvf test.tar.gz`
- rpm 安装文件命令`rpm -ivh httpd-2.2.15-26.el6.centos.x86_64.rpm `

​                                     `rpm -ivh quota-4.01-14.el7.x86_64.rpm`

- find 查找文件 `find /etc -name "*.conf"`

  ​                       //在/etc/目录下查找文件名以“.conf”结尾的文件

  ​						` find . -type f -exec ls -l {} \;`

  ​                          //在当前目录下查找普通文件，并以长格形式显示

- locate 更加强大的查找文件命令 `locate *.doc`

- grep  查找文件中包含有指定字符串的行

```
[root@RHEL7-1 yy]# grep -2 root /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
--
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin

```



### **系统信息类命令** 

- dmesg显示系统诊断信息、操作系统版本号、物理内存大小以及其他信息。
- df命令主要用来查看文件系统的各个分区的占用情况
- free命令主要用来查看系统内存，虚拟内存的大小及占用情况
- ldate命令可以用来查看系统当前的日期和时间

### **进程管理类命令** 

- ps
- pidof  用于查询某个指定服务进程的PID值 `pidof sshd `

- kill
- killall命令用于终止某个指定名称的服务所对应的全部进程

`killall -9 bash`

- top命令可以实时监控进程的状况



### **其他常用命令** 

- clear命令用于清除字符终端屏幕内容
- uname命令用于显示系统信息 `uname -a`
- man命令用于列出命令的帮助手册
- history命令用于显示用户最近执行的命令，可以保留的历史命令数
- wget命令用于在终端中下载网络文件，
- reboot命令用于重新启动系统
- poweroff命令用于立即停止系统，并关闭电源



## 项目三 管理linux用户和组

### 用户和组群配置文件

帐户文件 

- /etc/passwd文件

`root:x:0:0:root:/root:/bin/bash`

`用户名：加密口令：UID:GID：用户描述信息：主目录：命令解释器`

密码文件 

- /etc/shadow文件

` root:$6$lq4Er2YLAtrM2zqJ$fPf7i1L359e9JRqYT2H9iFJBx37/ZnO1RtFmvEy720XpLkfOOcclM.JJwFnAkzu50B6W2E/1.8Mw420naJfM00:18281:0:99999:7:::`

组群文件

- /etc/group文件

`yy:x:500:`

`组群名称：口令：GID：成员列表`

组群口令文件

- /etc/gshadow文件

  `yy:!!::`

-  /etc/login.defs文件



### 管理用户帐户

- 新建用户

`groupadd -g 500 group2`

`useradd -u 510 -g 500 -d /home/user1 -s /bin/bash -p 123456 -f -1 user1`

【例3-1】新建用户user3，UID为1010，指定其所属的私有组为group1（group1组的标识符为1010），用户的主目录为/home/user3，用户的shell为/bin/bash，用户的密码为123456，账户永不过期。

```shell
[root@RHEL7-1 ~]# groupadd -g 1010  group1 
[root@RHEL7-1 ~]# useradd -u 1010 -g 1010  -d /home/user3 -s /bin/bash -p 123456 -f -1 user3
[root@RHEL7-1 ~]# tail -1 /etc/passwd
user3:x:1010:1000::/home/user3:/bin/bash

```



- 设置密码

`passwd user1`

- chage命令

`chage -m 6 -M 60 -W 5 user1`

- usermod命令

- 禁用和恢复用户帐户－Passwd命令

`passwd -l user1`

`passwd -u user1`

- 删除用户

`userdel -r user2`

- 管理组群

- 新建组群

  `groupadd testgroup`

- 修改组群信息

`groupmod -g 2000 testgroup`

`groupmod -n testgorup1 testgroup`

- 删除组群

`groupdel testgorup1`

- 入群

  `gpasswd -a user1 testgroup`
  
  `gpasswd -A user1 testgroup`   指定user1为管理员，tail /etc/gshadow
  
  `gpasswd -d user1 testgroup`  删除组内成员user1

课堂作业：

​		假设有user1,user2,user3,user4四个用户，请将他们添加到usergroup组群中，并将user2设置为管理员，最后将user4删除。

- 安装图形化用户管理界面

`yum  install  system-config-users  -y`

`system-config-users`



```
yum安装报睡眠错误的解决方法
可能是系统自动升级正在运行，yum在锁定状态中。
可以通过强制关掉yum进程：
#rm -f /var/run/yum.pid
然后就可以使用yum了。
```



## 项目四 配置与管理文件系统

`ls /lib/modules/2.6.32-358.el6.x86_64/kernel/fs/`

绝对路径`cd /etc/passwd`

相对路径 `vim passwd`

### 理解文件和文件权限

`-rw-r--r--. 1 root root 0 5月   9 11:45 a.txt`

### 详解文件的各种属性信息

 `-  rwx  r--  r--. 文件类型权限`

文件类型：

d: 表示一个目录。在ext3中，目录是一种特殊的文件

-: 表示一个普通文件

l: 表示符号链接文件，实际上它指向另一个文件

b、c:分别代表区块主设备和其他的外围设备。是特殊类型的文件

s、p：这些文件关系到系统的数据结构和管道，通常很少见到。



### 使用数字表示法修改权限

所谓数字表示法是指将读取（r）、写入（w）和执行（x）分别以4、2、1来表示，没有授予的部分就表示为0，然后再把所授予的权限相加而成。

`chmod 777 b.txt`

### 使用文字表示法修改权限

-  u：user，表示所有者。

- g：group，表示属组。

- o：others，表示其它用户。

- a：all，表示以上三种用户。

操作权限：

读取（r）、写入（w）和执行（x）

操作符号：

- ＋：添加某种权限。

- -：减去某种权限。

- ＝：赋予给定权限并取消原来的权限。

添加权限：

`chmod u+x,g+wx,o+x a.txt`

取消权限：

`chmod a-x a.txt`

赋值权限：

`chmod o=wx c.txt`



> 作业：
> 新建文件c,观察文件权限，分别用数学和文字表示法修改权限
> 数字表示法 -rw-r--r--
> 文字表示法 -rwxrwxrwx

### 改变拥有权chown命令

修改所有者

`chown yy a.txt`

修改所组群

`chgrp yy a.txt `

同时修改所有者和组群

`chown root.root a.txt `

### 修改文件与目录的默认权限

root用户下执行：

umask 002

777-002=775

所得目录的权限是rwxrwxr-x

所得文件的权限是rw-rw-r--

**注意目录有X权限，文件是没有X权限的**

作业：

求在root用户的umask 222所得目录与文件权限

### 设置文件的隐藏属性

`chattr +i a` 添加隐藏属性

`lsattr`显示隐藏属性

### 设置文件特殊权限：SUID、SGID、SBIT

```
ls -ld /tmp/;ls -l /usr/bin/passwd 
drwxrwxrwt. 23 root root 4096 10月 16 08:49 /tmp/
-rwsr-xr-x. 1 root root 30768 2月  22 2012 /usr/bin/passwd
```

4为SUID，2为SGID，1为SBIT

`chmod 4755 a`

**SUID不能用在目录上，SBIT不能用在文件**

### 文件访问控制列表

yy 用户下新建文件a

```
# file: a
# owner: yy
# group: yy
user::rw-
group::rw-
other::r--
```



设置hi的文件访问控制列表

`setfacl -m u:user1:--- a  不给user1查看权限

`setfacl -m g:t:--- a`

查看文件访问控制列表

`getfacl a

测试

新建用户user1，否有权限查看a

### 企业实战与应用

设系统中有两个账号，分别是alex与arod，这两个人除了自己群组之外还共同支持一个名为project的群组。假设这两个用户需要共同拥有/srv/ahome/目录的开发权，且该目录不许其他人进入查阅。请问该目录的权限应如何设定？请先以传统权限说明，再以SGID的功能解析。

## 项目五 配置与管理磁盘

### 熟练使用常用磁盘管理工具

> 思路：对一块新硬盘首先分区，其次格式化，最后挂载

- 查看磁盘设备 fdisk -l

Device Boot      Start         End      Blocks   Id  System

分区	 启动	起始柱面	终止柱面	总块数	分区ID	文件系统类型

- 磁盘命令规则 sda1    sdb2   sdc  sdd

#### 分区

- 分区命令 fdisk /dev/sdb

- n新建分区->p主分区(e扩展)->1主分区号->t更改类型->8e类型号->w保存

  ```
     Device Boot      Start         End      Blocks   Id  System
  /dev/sdb1               1          65      522081   83  Linux
  /dev/sdb2              66         130      522112+  8e  Linux LVM
  /dev/sdb3             131         386     2056320    5  Extended
  /dev/sdb5             131         195      522081   83  Linux
  /dev/sdb6             196         260      522081   83  Linux
  ```

- d删除

- t更改类型

#### 格式化

`mkfs -t ext3 -V -c /dev/sdb1`

- -t指定要创建的文件系统类型

- -v 输出建立文件系统详细信
- -c 检查坏块

#### fsck命令

`fsck -a /dev/sdb1`

- -a如果检查中发现错误，则自动修复

#### mount与umount

- 提前是需要完成分区和格式化

- 新建目录 `mkdir /home/yy/test2`
- 挂载 ` mount /dev/sdb5 /home/yy/test2/`
- 修改权限 `chown yy.yy test2/`
- 卸载 `umount /dev/sdb1`

#### 文件系统的自动挂载

- `vim /etc/fstab `

  `/dev/sdb1       /home/yy/test2  ext3    defaults 0 0`
  
  `/dev/sdb1 /home/yy/test ext4 defaults 0 0`

#### 其它命令

- df 磁盘占用情况 `df -h`
- du 使用情况 `du -h`
- fsck 检查和修复
  - `fsck -a  /dev/sdb1`

### 磁盘配额管理

#### 准备工作

1. 分区`fdisk /dev/sdb`

2. ```
      Device Boot      Start         End      Blocks   Id  System
   /dev/sdb1               1          65      522081   83  Linux
   /dev/sdb2              66         130      522112+  83  Linux
   ```
   
3. 格式化 `mkfs -t ext4 -V -c /dev/sdb2`

4. 创建 /disk2目录 `mkdir /disk2`   (root模式)

5. `chmod 777 /disk2/`

6. 自动挂载 ` vim /etc/fstab `

7. ```
      /dev/sdb2       /disk2  ext4    defaults,usrquota,grpquota 0 0
      ```

      

####  创建quota配额文件

`setenforce 0`关闭安全机制

`quotacheck -cvug /dev/sdb2 -f -m`  创建记录文件

> quotacheck: Scanning /dev/sdb2 [/disk2] done  正常提示
> quotacheck: Checked 2 directories and 2 files

#### 设置用户和组群的磁盘配额

- 软限制  3个文件
- 硬限制  5个文件

1. 设置用户配额

`edquota -u yy `

-u 对用户进行配额管理

-g 对组群进行配额管理

-p 复制配额

```
Disk quotas for user yy (uid 500):
  Filesystem                   blocks       soft       hard     inodes     soft     hard
  /dev/sdb2                         0          0          0          0        3        5
```

2. 对/disk2目录更改用户和组群

`chown yy.yy /disk2/`

3. 启动磁盘配额

`quotaon -avug`

> /dev/sdb2 [/disk2]: group quotas turned on
> /dev/sdb2 [/disk2]: user quotas turned on  成功提示

4. yy用户身份对测试
5. 将yy的配额复制给user1 `edquota -p yy user1`
6. 对组建group1配额，useradd -g group1 user4设置用户主组群，用户的主组群必须是group1 `edquota -g group1`
7. 检查磁盘配额的使用情况`repquota -a`

### 磁盘配额配置企业案例

#### 环境需求

课本p100

#### 解决方案

1. 建立账号 `vim addaccount.sh`

```shell
#!/bin/bash
groupadd myquotagrp
for username in myquota1 myquota2 myquota3 myquota5
do
        useradd -g myquotagrp $username
        echo "password"|passwd --stdin $username
done
```
执行`sh addaccount.sh`文件

2. 启动系统的磁盘配额

- 分区` fdisk /dev/sdb`
- 格式化`mkfs -t ext3 -V -v /dev/sdb1`
- 挂载 `vim /etc/fstab`

`/dev/sdb1 /disk1 ext3 defaults,usrquota,grpquota 1 2`

`mkdir /disk1`

- 建立quota记录文件

`setenforce 0`

`quotacheck -cvug -mf /dev/sdb1`

- 启动磁盘配额

`quotaon -avug`

- 新建限制磁盘配额

`edquota -u myquota1`

```
Disk quotas for user myquota1 (uid 501):
  Filesystem                   blocks       soft       hard     inodes     soft     hard
  /dev/sdb1                         0     250000      300000          2        0        0
```



- 复制磁盘配额

`edquota -p myquota1 -u myquota2`

- 更改群组的磁盘限额

`edquota -g myquotagrp`

```
Disk quotas for group myquotagrp (gid 501):
  Filesystem                   blocks       soft       hard     inodes     soft     hard
  /dev/sdb1                         0     900000    1000000          4        0       0
```
- 更改宽限时间14天

`edquota -t`

```
Grace period before enforcing soft limits for users:
Time units may be: days, hours, minutes, or seconds
  Filesystem             Block grace period     Inode grace period
  /dev/sdb1                     14days                  7days

```

- 查看使用配额情况

`repquota -a 或 repquota /dev/sdb1`



### 在linux中配置软RAID

RAID（Redundant Array of Inexpensive Disks，独立磁盘冗余阵列）用于将多个廉价的小型磁盘驱动器合并成一个磁盘阵列，以提高存储性能和容错功能。**RAID可分为软RAID和硬RAID**。

RAID5：向阵列中的磁盘写数据，奇偶校验数据存放在阵列中的各个盘上，允许单个磁盘出错

#### 创建与挂载RAID设备

- 虚拟机创建四个新硬盘
- 分区`fdisk /dev/sdb`    n->p->1->回车->+500M->t->fd   **类型为fd** （暂时不需要格式化）

```
 Device Boot      Start         End      Blocks   Id  System
/dev/sdb1               1          65      522081   fd  Linux raid autodetect
```

- 使用mdadm命令创建RAID5

`mdadm --create /dev/md0 --level=5 --raid-devices=3 --spare-devices=1 /dev/sd[b-e]1`

磁盘阵列命令,设备名称md0,磁盘阵列5，三个主力盘，一个备用盘，设备名称[b-e]1

- 为新建立的/dev/md0建立文件系统（格式化）

`mkfs -t ext4 -V -c /dev/md0`

- 将RAID设备挂载

```
mkdir /media/md0
mount /dev/md0 /media/md0/
df
```

- 查看建立的RAID5的情况

`mdadm --detail /dev/md0`

#### RAID5的数据恢复

- 将损坏的RAID成员标记为失效

`mdadm /dev/md0 --fail /dev/sdc1`

- 移除失效的RAID成员

`mdadm /dev/md0 --remove /dev/sdc1`

- 添加一个新的RAID成员

`mdadm /dev/md0 --add /dev/sde1`



### LVM逻辑卷管理

####  添加2块硬盘，sdb建立LVM类型的分区。（sdc暂时不分区）

`fdisk /dev/sdb`

`n>p>1>回车>+500M>t>8e`

```
   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1               1          65      522081   8e  Linux LVM
/dev/sdb2              66         130      522112+  8e  Linux LVM
```

LVM流程：pv物理卷->vg卷组->lv逻辑卷

#### 建立物理卷

建立物理卷

`pvcreate /dev/sdb1`

查看物理卷

`pvdisplay`

物理卷信息

```
"/dev/sdb1" is a new physical volume of "509.84 MiB"
  --- NEW Physical volume ---
  PV Name               /dev/sdb1
  VG Name               
  PV Size               509.84 MiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               DYtu4Q-nFkN-3ppj-12jQ-zIBs-xYVh-ejERdp

```

#### 建立卷组

建立卷组

`vgcreate vg0 /dev/sdb1`

查看卷组信息

`vgdisplay `

卷组信息

```
--- Volume group ---
  VG Name               vg0
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               508.00 MiB
  PE Size               4.00 MiB
  Total PE              127
  Alloc PE / Size       0 / 0   
  Free  PE / Size       127 / 508.00 MiB
  VG UUID               MvfvjN-iHRF-oXkC-Y8qg-6YmG-1PlV-Dl4mng

```

#### 建立逻辑卷

建立逻辑卷

` lvcreate -L 20M -n lv0 vg0`

查看

`lvdisplay`

逻辑卷信息

```
--- Logical volume ---
  LV Path                /dev/vg0/lv0
  LV Name                lv0
  VG Name                vg0
  LV UUID                HA7mbe-f4A3-ifP5-NuI6-iXlW-nHto-oEmHEQ
  LV Write Access        read/write
  LV Creation host, time centos6.4-1, 2020-05-25 10:58:38 +0800
  LV Status              available
  # open                 0
  LV Size                20.00 MiB
  Current LE             5
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:0

```



#### 增加新的物理卷到卷组

`pvcreate /dev/sdb2`

`pvcreate /dev/sdc`  尝试把第三块硬盘变成物理卷

`vgextend vg0 /dev/sdb2`

`vgextend vg0 /dev/sdc` 尝试把第三块硬盘添加到vg0卷组

#### 逻辑卷容量的动态调整

添加容量

`lvextend -L +10M /dev/vg0/lv0`

减少容量

`lvreduce -L -5M /dev/vg0/lv0`

#### 删除逻辑卷\卷组\物理卷

删除流程：lv逻辑卷->vg卷组->pv物理卷

如果有挂载的请先卸载

`umount /dev/vg0/lv0`

删除逻辑卷

`lvremove /dev/vg0/lv0`

删除卷组

`vgremove vg0`

删除物理卷

`pvremove /dev/sdb[1-2]`

#### 格式化，挂载

`mkfs -t ext3 -V -c /dev/vg0/lv0`

` mkdir /media/lv0`

**挂载之前先格式化设备**

`mount /dev/vg0/lv0 /media/lv0/`

## 期中复习

1. 新建与安装Linux操作系统.(见书本p11)
2. 管理用户和组

- `useradd -d /home/user02 user02`
- `tail -3 /etc/passwd`
- `passwd user02`
- `groupadd group1`
- `gpasswd -a user02 group1`
- `tail -3 /etc/group`

3. 管理文件系统

- `su user01`
- `mkdir test;cd test`
- `touch file1;ll`
- `chmod o+w file1;ll ` 或 `chmod 666 file1;ll`
- `chmod g-r file1;ll`
- `chmod 755 file1;ll `

4. 管理磁盘

- `fdisk /dev/sdb`
- `n->p->1->回车->+500M`
- `n->e->2->回车->+10G`
- `n->l->回车->+500M`
- `w`
- `mkfs -t vfat -V -c /dev/sdb1`
- `mkfs -t ext3 -V -c /dev/sdb5`
- `fsck -a /dev/sdb1`
- `fsck -a /dev/sdb5`
- `mkdir /mnt/vfat;mkdir /mnt/ext3`
- `mount /dev/sdb1 /mnt/vfat/`
- `mount /dev/sdb5 /mnt/ext3/`

## 管理Linux服务器的网络配置

### 配置主机名

方法1

`hostnamectl status` 查看主机状态

`hostnamectl set-hostname my.smile.com`  修改主机名

方法2

` nmcli general hostname` 查看主机状态

`nmcli general hostname rhel` 修改主机名

方法3

`nmtui`

### 网络配置

1. Ip地址   `nmtui`

2. 子网掩码

3. 网关

4. DNS

5. 主机名 

   查看ip地址  `ip addr`

### 创建网络连接

`nmcli device status ` 查看设备状态（物理网卡）

`nmcli connection show`  查看连接（配置，逻辑网卡）

`nmcli connection add con-name eth0 type ethernet ifname ens33 `  添加一个名字叫eth0的连接，使用物理接口ens33

`nmcli connection modify eth0 ipv4.addresses 192.168.10.1/24 ipv4.gateway 192.168.10.1 ipv4.dns 192.168.10.1`  设置IP地址，子网掩码，网关和DNS

`nmcli connection modify eth0 -ipv4.dns 192.168.10.1`  删除DNS

`nmcli connection modify eth0 ipv4.method manual`  手动配置

`nmcli connection modify eth0 connection.autoconnect yes` 自动生效

`nmcli connection up eth0` 激活

`nmcli connection delete ens33`  删除连接

### 其它命令

`vim /etc/resolv.conf`  dns配置文件

`traceroute 192.168.10.2` 跟踪路由

`netstat` -an 查看端口

`netstat -an | grep :80 ` 查看80端口

### 配置SSH

服务器ip地址：192.168.10.1 主机名:server

客户机ip地址：192.168.10.2  主机名:client



`systemctl status sshd` 查看ssh是否安装

`firewall-cmd --list-all` 查看防火墙，默认ssh是放行的

`/etc/ssh` 密钥存放位置

#### 基于口令的验证—用账户和密码来验证登录

`ssh root@192.168.10.1`  ==> `yes`

禁用root管理员远程登录

`sudo vim /etc/ssh/sshd_config`

`PermitRootLogin no` 不允许root用户登录   esc-->shift+:-->wq

`systemctl restart sshd`  重启sshd服务

注意实验完成后恢复设置后重启 `#PermitRootLogin yes`

#### 基于密钥的验证

服务器上创建student帐号并设置密码

`ssh-keygen -t rsa` 生成密钥(在客户机上生成)

`/root/.ssh/id_rsa` 客户机存放密钥的位置

`/root/.ssh/id_rsa/known_hosts`  

`ssh-copy-id student@192.168.10.1` 将客户机的公钥上传到服务器

`ssh student@192.168.10.1` 以命令行登录服务器

`ssh -X student@192.168.10.1` 以图形化登录服务器

`/home/student/.ssh/authorized_keys` 服务器上存放客户机公钥的位置

#### 远程传输命令

上传

`scp a.txt 192.168.10.1:/home/yy` 使用密码登录

`scp a.txt student@192.168.10.1:/home/student` 使用密钥登录

`scp -r test/ 192.168.10.1:/home/yy` 上传文件夹

下载

`scp 192.168.10.1:/home/yy/b.txt /home/yy/`

#### 远程登录工具

- putty

---

###　Centos６的网络配置

### 常见网络配置文件

- `/etc/sysconfig/network`主机名，网关
- `/etc/sysconfig/network-scripts/ifcfg-eth0`  网卡
- `/etc/hosts`  早期静态域名解析
- `/etc/resolv.conf` 指定DNS服务器

- 配置主机名 

  - `hostname yesulin` 重启后失效
  - `vim /etc/sysconfig/network` 永久保存

  ```bash
  NETWORKING=yes
  HOSTNAME=yesulin
  ```

- 使用ifconfig配置IP地址（重启后失效）

`ifconfig` 查看网卡相关信息

`ifconfig eth0 192.168.0.168 netmask 255.255.255.0` 配置IP地址

`fconfig eth0:1 192.168.0.208 netmask 255.255.255.0` 配置虚拟网上IP地址

- 禁用和启用网卡
  - 方法1
    - `ifconfig eth0 down`禁用
    - `ifconfig eth0 up` 启用
  - 方法2
    - `ifdown eth0`禁用
    - `ifup eth0` 启用
- 使用route命令

`route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.70.2 dev eth0`添加

`route del -net 192.168.3.0 netmask 255.255.255.0 gw 192.168.70.2 dev eth0`删除

- 配置物理地址(MAC)

`ifdown eth0` 首先禁用网卡

`ifconfig eth0 hw ether 00:11:22:33:44:55` 更改物理地址

- 网卡配置文件

`vim /etc/sysconfig/network-scripts/ifcfg-eth0 `

```bash
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.1.1
NETMASK=255.255.225.0
DNS1=192.168.1.100
GATEWAY=192.168.1.254
```

案例：为上述eth0网卡再绑定一个IP地址192.168.1.3

`cd /etc/sysconfig/network-scripts/`

`cp ifcfg-eth0 ifcfg-eth0:1`

`vim ifcfg-eth0:1`

```bash
DEVICE=eth0:1
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.1.3
NETMASK=255.255.255.0
DNS1=192.168.1.100
GATEWAY=192.168.1.254
HWADDR=00:0C:29:20:31:8B
```

注意：学生机如果出现错误可以尝试删除所有网上，uuidgen eth0,接着重新编辑配置文件

- 使用setup命令
- 使用service

`service network restart` 重启服务

`service 服务名 start/stop/status/restart/reload`

## vim编程与调式

### 熟练使用vim编辑器

#### 启动与退出vim

- w 保存
- w filename 另存为
- wq!  保存并退出
- q! 不保存退出

#### vim的工作模式

- 编辑模式
  - h j k l 移动 
  - dd 删除（剪切）
  - yy 复制
  - p 粘贴
  - ctrl+f,ctrl+b 翻页
  - x （del）X 回格
  - G 最后一行  gg首行
  - u 撤消
  - ctrl+r 重做
  - /  查找 n往下查找 N往上查找
- 插入模式 i
- 命令模式 Esc->shift+:
  - :w 保存
  - :w! 强制保存
  - :wq 保存并退出
  - :q 退出
  - :q! 强制退出
  
  课堂练习：p140子任务4

### 正则表达式

正则表达式就是处理字符串的方法

`grep -n 'the' httpd.conf`  查找包含the的行

`grep -in 'the' httpd.conf ` 查找包含the的行 ,忽略大小写

` grep -n 'oo' httpd.conf ` 查找所有包含oo的行

`grep -n '[^R]oo' httpd.conf` 查找包含oo的行,并且排除R开头

`grep -n '[0-9]' httpd.conf` 查找包含数字的行



## 学习shell script

支持数组,循环,条件与逻辑判断

```shell
#!/bin/bash
echo -e "hello world\a \n"
exit 0

```

sh  ./hello.sh

```shell
#!/bin/bash

read -p "input1:" name1
read -p "input2:" name2

echo -e "out:" $name1,$name2
                                  
```

## 使用GCC

### 安装gcc

1. rpm 要解决依赖关系
2. yum 要配置本地源（网络源）

#### 配置yum本地源

`mkdir /iso`

`mount /dev/cdrom /iso`

`vim /etc/yum.repos.d/dvd.repo`

```
[dvd]
name=dvd
baseurl=file:///iso
gpgcheck=0
enabled=1            
```

cd /etc/yum.repos.d/  ，删除CentOS-Base.repo

>  测试安装是否成功

>  `yum list`

#### 使用yum安装gcc 

`yum install gcc`



### 程序：打印Hello World

```c
#include <stdio.h>
int main(){
	printf("hello world\n");
	return 0;
}
```

`gcc -c hello.c `  ===>`hello.o`目标文件===>`gcc -o hello.exe hello.o`执行文件



 ## 配置与管理Samba服务器（网络邻居）



### 安装samba服务

`yum install samba`

### 启动与停止samba服务

启动

`service smb start`

停止

`service smb stop`

重启

`service smb restart`

### 配置文件smb.conf

#### 匿名访问

`vim /etc/samba/smb.conf `

```
 74         workgroup = WORKGROUP
 75         server string = File server %v
101         security = share

配置文件后面另起一行写
289 [public]
290 comment=public
291 path=/share
292 guest ok=yes
293 public=yes
294 read only=no
```

新建目录并修改权限

`  mkdir /share`

`chmod 777 /share`

关闭安全机制和防火墙

`setenforce 0`

启动smb服务

`service smb start`

测试连接

方法1

`smbclient -L 目标ip地址`   不需要输入密码，直接回车

方法2

`mkdir -p /mnt/sambadata`

`mount -t cifs //目标ip地址/public /mnt/sambadata/`  不需要输入密码，直接回车



#### 用户名和密码访问

`vim /etc/samba/smb.conf `

```
101         security = user

296 [test1]
297 comment=test1 file
298 path=/test1
299 public=no
300 guest ok=no
301 read only=no
```

新建目录并修改权限

`mkdir /test1`

`chmod 777 /test1/`

添加用户账号和smb账号

`useradd test1
passwd test1
smbpasswd -a test1`

关闭安全机制和防火墙

`setenforce 0`

测试连接

方法1

`smbclient -L 172.16.128.193 -U test1%qwer1234` 

方法2

`mkdir /mnt/samtest1`

`mount -t cifs //172.16.128.193/test1 /mnt/samtest1/ -o username=test1%qwer1234`

## 配置与管理DHCP服务器

安装DHCP

`yum install dhcp -y`

配置文件路径

`vim /etc/dhcp/dhcpd.conf`

```bash
ddns-update-style none;
log-facility local7;
subnet 192.168.1.0 netmask 255.255.255.0{
        range 192.168.1.100 192.168.1.200;
        option domain-name-servers 192.168.1.1;
        option  routers 192.168.1.254;
        option broadcast-address 192.168.1.255;
        default-lease-time 600;
        max-lease-time 7200;
}

```

启动dhcp

`service dhcpd start`

保留地址配置应用

```bash
host CTO{
        hardware ethernet 00:0C:29:23:AC:AB;
        fixed-address 192.168.1.150;
}
```

错误解决办法

查找错误命令 `dhcpd`

```
编辑 /etc/rc.d/init.d/dhcpd 文件，将其中的
user=dhcpd
group=dhcpd
改为
user=root
group=root
```

删除文件

`rm /etc/yum.repos.d/CentOS-Base.repo`

DHCP服务器 192.168.1.1

其它固定服务器 192.168.1.2  192.168.1.30

地址池 192.168.1.100 192.168.1.200

service network restart 重启网卡



## 配置与管理ＤＮＳ服务器

安装bind和bind-chroot

`yum install bind -y`

`yum install bind-chroot -y`

启动，停止，重启

`service named start`

`service named stop`

`service named restart`

### named.conf全局配置文件

需要启动named服务才能出来全局配置文件

> `vim /var/named/chroot/etc/named.conf`

```bash
options {
        listen-on port 53 { any; };
        listen-on-v6 port 53 { ::1; };
        directory       "/var/named";
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        allow-query     { any; };
        recursion yes;

        dnssec-enable yes;
        dnssec-validation yes;
        dnssec-lookaside auto;

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
        type hint;
        file "named.ca";
};

include "/etc/named.zones";
include "/etc/named.root.key";
```

### named.zones主配置文件

创建主配置文件

`cp -p named.rfc1912.zones named.zones`

> `vim /var/named/chroot/etc/named.zones`

```bash
zone "long.com" IN{
        type master;
        file "long.com.zone";
        allow-update {none;};
};

zone "168.192.in-addr.arpa" IN{
        type master;
        file "192.168.zone";
        allow-update{none;};
};
```

### 创建long.com.zone正向区域文件

**请注意更换路径**

`cd /var/named/chroot/var/named/`

复制

`cp -p named.localhost long.com.zone`

`vim /var/named/chroot/var/named/long.com.zone`

```bash
$TTL 1D
@       IN SOA  @ rname.invalid. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
@       IN      NS      dns.long.com.
@       IN      MX      10      mail.long.com.

dns     IN      A       192.168.1.2
mail    IN      A       192.168.0.3
slave   IN      A       192.168.1.4
www     IN      A       192.168.0.5
forward IN      A       192.168.0.6
computer        IN      A       192.168.22.98
ftp     IN      A       192.168.0.11
stu     IN      A       192.168.10.22
web     IN      CNAME   www.long.com.
```



### 创建192.168.zone 反向区域文件

`cp -p named.loopback 192.168.zone`

`vim /var/named/chroot/var/named/192.168.zone `

```bash
$TTL 1D
@       IN SOA  @ rname.invalid. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
@       IN      NS      dns.long.com.
@       IN      MX      10      mail.long.com.

2.1     IN      PTR     dns.long.com.
3.0     IN      PTR     mail.long.com.
4.1     IN      PTR     slave.long.com.
5.0     IN      PTR     www.long.com.
6.1     IN      PTR     forward.long.com.
98.22   IN      PTR     computer.long.com.
11.0    IN      PTR     ftp.long.com.
22.10   IN      PTR     stu.long.com.

```

### 配置linux客户端和测试

`vim /etc/resolv.conf ` 配置客户端DNS服务的IP地址

```bash
search long.com
nameserver 192.168.1.1                      
```

测试命令

1. nslookup命令
2. dig www.long.com
3. host www.long.com

## 配置与管理Apache服务器

### 常规设置Apache服务器

启动

`service httpd start`

配置文件地址

`vim /etc/httpd/conf/httpd.conf `

根目录

` 57 ServerRoot "/etc/httpd"`

超时设置

`70 Timeout 300`

最大用户数

` 102 <IfModule prefork.c>
 103 StartServers       8
 104 MinSpareServers    5
 105 MaxSpareServers   20
 106 ServerLimit      500
 107 MaxClients       500
 108 MaxRequestsPerChild  4000
 109 </IfModule>`

管理员邮箱

`262 ServerAdmin ysl@163.com`

域名

`275 ServerName www.example.com:80`

网页目录

` 292 DocumentRoot "/var/www/html"`

编码

`762 AddDefaultCharset UTF-8`

### 用户个人主页

新建用户和密码

`useradd ysl`

`passwd ysl`

修改家目录权限

`chmod 705 /home/ysl`

创建用户个人主页目录和网页

`mkdir /home/ysl/public_html`

`vim /home/ysl/public_html/index.html`

修改配置文件

禁用 ` 366  #UserDir disabled`

启用` 373    UserDir public_html`

` 381 <Directory /home/*/public_html>
 382     AllowOverride FileInfo AuthConfig Limit
 383     Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
 384     <Limit GET POST OPTIONS>
 385         Order allow,deny
 386         Allow from all
 387     </Limit>
 388     <LimitExcept GET POST OPTIONS>
 389         Order deny,allow
 390         Deny from all
 391     </LimitExcept>
 392 </Directory>`

### 虚拟目录

`mkdir -p /virdir/`

`vim /virdir/index.html`

配置文件添加

` 411 Alias /test "/virdir"`

### 拒绝访问设置（基本网站）<Directory "/var/www/html">

拒绝IP地址为192.168.1.2访问

` 345      Order deny,allow
 346      Deny from 192.168.1.2`

拒绝192.168.11.2访问虚拟目录

` 412 <Directory "/virdir/>
 413         Order deny,allow
 414         Deny from 192.168.11.2 
 416 </Directory>`

### 配置虚拟主机

#### 基于IP地址的虚拟主机

添加一网卡多IP(临时)

`ifconfig eth0:1 192.168.11.11 netmask 255.255.255.0`

`ifconfig eth0:2 192.168.11.12 netmask 255.255.255.0`

新建目录和网页

`mkdir /var/www/ip1`

`mkdir /var/www/ip2`

`vim /var/www/ip1/index.html`

`vim /var/www/ip2/index.html`

配置文件

`1014 <VirtualHost 192.168.11.11>
1015     ServerAdmin webmaster@dummy-host.example.com
1016     DocumentRoot /var/www/ip1
1017     ServerName dummy-host.example.com
1018     ErrorLog logs/dummy-host.example.com-error_log
1019     CustomLog logs/dummy-host.example.com-access_log common
1020 </VirtualHost>
1021 <VirtualHost 192.168.11.12>
1022     ServerAdmin webmaster@dummy-host.example.com
1023     DocumentRoot /var/www/ip2
1024     ServerName dummy-host.example.com
1025     ErrorLog logs/dummy-host.example.com-error_log
1026     CustomLog logs/dummy-host.example.com-access_log common
1027 </VirtualHost>`

### 基于端口号的虚拟主机

新建目录和页面

`mkdir /var/www/port8080 /var/www/port8090`

`echo "this is 8080 ports web.">>/var/www/port8080/index.html`

`echo "this is 8090 ports web.">>/var/www/port8090/index.html`

配置文件

设置监听端口

`136 Listen 8080`

`137 Listen 8090`



`<VirtualHost 192.168.11.1:8080>
    ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot /var/www/port8080
    ServerName dummy-host.example.com
    ErrorLog logs/dummy-host.example.com-error_log
    CustomLog logs/dummy-host.example.com-access_log common
</VirtualHost>
<VirtualHost 192.168.11.1:8090>
    ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot /var/www/port8090
    ServerName dummy-host.example.com
    ErrorLog logs/dummy-host.example.com-error_log
    CustomLog logs/dummy-host.example.com-access_log common
</VirtualHost>`



## 配置与管理FTP服务器

安装vsftpd和ftp

`yum install vsftpd -y`

`yum install ftp -y`

启动ftp：

`service vsftpd start`

案例1：搭建一台ftp服务器，允许匿名用户上传和下载文件，匿名用户的根目录设置为/var/ftp

配置文件`vim /etc/vsftpd/vsftpd.conf`

` 12 anonymous_enable=YES
13 anon_root=/var/ftp`

` 28 anon_upload_enable=YES`

` 32 anon_mkdir_write_enable=YES`

修改目录权限

`ll -ld /var/ftp/pub/`

`chown ftp /var/ftp/pub/`

`chmod 777 /var/ftp/pub/`

关掉安全机制

`setenforce 0`

客户机测试连接

`ftp 192.168.11.1` 

默认用户是"ftp"

案例2：本地用户名和密码登录

`useradd -s /sbin/nologin team1`

`useradd -s /sbin/nologin team2`

`passwd team1`

`passwd team2`

配置文件

`12 anonymous_enable=no`

` 16 local_enable=YES`
 `17 local_root=/var/www/html`

`100 chroot_list_enable=YES`
`102 chroot_list_file=/etc/vsftpd/chroot_list`

配置允许用户列表

`vim /etc/vsftpd/chroot_list`

```
team1
team2
```

## 期末复习

1. 掌握虚拟机的启动，网络配置，本地源配置，保证两台机器物理能通。
2. 掌握服务器的配置，samba，dhcp,dns,ftp,apache等
3. 测试客户机能否正常访问服务器
4. 其它知识，如文件权限，新建目录，安装软件等。

DHCP服务

```bash
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp*/dhcpd.conf.sample
#   see 'man 5 dhcpd.conf'
#
ddns-update-style none;
log-facility local7;
subnet 192.168.1.0 netmask 255.255.255.0{
	range 192.168.1.3   192.168.1.150;
	option domain-name-servers 192.168.1.3;
	option domain-name "dns.jnrp.cn";
	option routers 192.168.1.254;
	option subnet-mask 255.255.255.0;
	option broadcast-address 192.168.1.255;
	default-lease-time 600;
	max-lease-time 7200;
}

host webserver{
	hardware ethernet 12:34:56:78:AB:CD;
	fixed-address 192.168.1.10;
}

}
host smbserver{
	hardware ethernet 12:34:56:78:AB:FF;
	fixed-address 192.168.1.5;
}

```

DNS服务器

```bash
1.vim /var/named/chroot/etc/named.conf
----------------------------------------------------
options {
 11     listen-on port 53 { any; };
 12     listen-on-v6 port 53 { ::1; };
 13     directory   "/var/named";
 14     dump-file   "/var/named/data/cache_dump.db";
 15         statistics-file "/var/named/data/named_stats.txt";
 16         memstatistics-file "/var/named/data/named_mem_stats.txt";
 17     allow-query     { any; };
 18     recursion yes;
 19 
 20     dnssec-enable yes;
 21     dnssec-validation yes;
 22     dnssec-lookaside auto;
 23 
 24     /* Path to ISC DLV key */
 25     bindkeys-file "/etc/named.iscdlv.key";
 26 
 27     managed-keys-directory "/var/named/dynamic";
 28 };
 29 
 30 logging {
 31         channel default_debug {
 32                 file "data/named.run";
 33                 severity dynamic;
 34         };
 35 };
 36 
 37 zone "." IN {
 38     type hint;
 39     file "named.ca";
 40 };
 41 
 42 include "/etc/named.zones";
 43 include "/etc/named.root.key";
+++++++++++++++++++++++++++++++++++++++++++++++++++++
2.vim /var/named/chroot/etc/named.zones
------------------------------------------------------
 43 zone "jnrplinux.com" IN {
 44     type master;
 45     file "jnrplinux.com.zone";
 46     allow-update { none; };
 47 };
 48 
 49 zone "168.192.in-addr.arpa" IN {
 50     type master;
 51     file "192.168.zone";
 52     allow-update { none; };
 53 };
+++++++++++++++++++++++++++++++++++++++++++++++++
3.vim /var/named/chroot/var/named/jnrplinux.com.zone
---------------------------------------------------
  1 $TTL 1D
  2 @   IN SOA  @ rname.invalid. (
  3                     0   ; serial
  4                     1D  ; refresh
  5                     1H  ; retry
  6                     1W  ; expire
  7                     3H )    ; minimum
  8 @           IN  NS  dns.jnrplinux.com.
  9 @           IN  MX  10  mail.jnrplinux.com.
 10 
 11 dns         IN  A   192.168.1.2
 12 cw          IN  A   192.168.1.11
 13 xs          IN  A   192.168.1.12
 14 jl          IN  A   192.168.1.13
 15 oa          IN  A   192.168.1.14
++++++++++++++++++++++++++++++++++++++++++++++
4. vim /var/named/chroot/var/named/192.168.zone 
---------------------------------------------
  1 $TTL 1D
  2 @   IN SOA  @ rname.invalid. (
  3                     0   ; serial
  4                     1D  ; refresh
  5                     1H  ; retry
  6                     1W  ; expire
  7                     3H )    ; minimum
  8 @       IN  NS      dns.jnrplinux.com.
  9 @       IN  MX  10  mail.jnrplinux.com.
 10 
 11 2.1     IN  PTR     dns.jnrplinux.com.
 12 11.1    IN  PTR     cw.jnrplinux.com.
 13 12.1    IN  PTR     xs.jnrplinux.com.
 14 13.1    IN  PTR     jl.jnrplinux.com.
 15 14.1    IN  PTR     oa.jnrplinux.com.

```






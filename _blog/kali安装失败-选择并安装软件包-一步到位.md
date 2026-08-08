---
title: kali安装失败-选择并安装软件包-一步到位
author: 轻抚酸
tags:
  - kali
  - bug
categories:
  - - 随笔
    - 实操
date: 2025-07-25 22:32:37
---
## 起因

&nbsp;&nbsp;&nbsp;&nbsp;为了尝试 “rm -rf /\*“ 的威力导致的kali无用（心虚），需要重新装一个。

&nbsp;&nbsp;&nbsp;&nbsp;但是吧，如题，在这一步卡住了，网上找blog【[kali 安装步骤失败，选择并安装软件包，失败解决方法 “换源”\_kali安装步骤失败 选择并安装软件-CSDN博客](https://blog.csdn.net/Mengxi123jdndhux/article/details/127710371)】，但是并没有解决，我进入tty2终端后”nano /etc/apt/sources.list”发现里面是空的！就算写上去也没用，折腾好久也没搞定。
&nbsp;&nbsp;&nbsp;&nbsp;\x7e~有图省事直接拿自己csdn账号的图(~~

## 解决

&nbsp;&nbsp;&nbsp;&nbsp;最后还是选择简（逃）单（课）方式——直接下载别人安装好的虚拟机文件压缩包！依旧是kali官网上的【[Kali Linux | Penetration Testing and Ethical Hacking Linux Distribution](https://www.kali.org/ "Kali Linux | Penetration Testing and Ethical Hacking Linux Distribution")】

&nbsp;&nbsp;&nbsp;&nbsp;点击download进入下载界面如图：

![PixPin_2025-07-22_15-16-57.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-16-57.png)

&nbsp;&nbsp;&nbsp;&nbsp;这次选择右边的卡片，然后按照自己的虚拟PC软件选就好了。一般下载上面的，下面的是字面意思每周更新所以不是稳定版，一般用户直接点下载图标就好了。【下载图标右边的三是啥最下面会有解释，最终下载的都是一样的压缩包！不想麻烦直接点下载就好了】

![PixPin_2025-07-22_15-19-39.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-19-39.png)

&nbsp;&nbsp;&nbsp;&nbsp;下载完成后放到对应位置就可以解压缩了，这是可以直接使用虚拟PC软件打开的，这里用VM浅浅演示一下。

&nbsp;&nbsp;&nbsp;&nbsp;首先打开VM，点击打开虚拟机，找到对应的文件位置，进去发现一个VM的.vmx启动文件，双击打开就好了。【vmx是啥最下面会提】

![PixPin_2025-07-22_15-38-12.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-38-12.png)

&nbsp;&nbsp;&nbsp;&nbsp;左下角可以看到账户名和密码都是kali，ok，现在就可以启动启动了！

![PixPin_2025-07-22_15-41-40.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-41-40.png)

## Learn Time!

**1、** 演示里VM打开的.vmx文件是啥？

![PixPin_2025-07-22_15-44-14.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-44-14.png)

&nbsp;&nbsp;&nbsp;&nbsp;其实从windows对.vmx文件的解释也可以看出来是配置文件（用记事本打开试试）

![PixPin_2025-07-22_15-43-23.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-43-23.png)

**2、** 下载图标右边第一个“torrent”是啥？

其实这就是常说的 BT种子/磁力链接 文件，直接点击下载会发现只是个几百k的小文件，和我们直接下载的压缩包就多了个.torrent（当然名字并不重要）。可以在网盘或者讯飞用来添加BT下载任务来下载，下载速度挺快的，如果电脑直接下载速度感人的话可以试试~

想简单了解可以移步【[torrent（BT种子）文件的简单介绍与使用-CSDN博客](https://blog.csdn.net/2401_86399278/article/details/149335332 "torrent（BT种子）文件的简单介绍与使用-CSDN博客")】
![PixPin_2025-07-22_15-48-07.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-48-07.png)

![PixPin_2025-07-22_15-50-39.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-50-39.png)

**3、** 下载图标右边第二个“docs”是啥？

&nbsp;&nbsp;&nbsp;&nbsp;点击发现是个链接，并不是“第三种下载方式”。毕竟 “docs” 翻译过来就是 “文档” 的意思。里面也是如其意的是帮助你下载的【官方帮助文档】，四个虚拟pc软件的文档也都应当的在一个网址上。

**4、** 最后一个“sum”是啥？

&nbsp;&nbsp;&nbsp;&nbsp;点击看卡片翻转过来显示了一串字母数字组合【SHA-256哈希值】。其实是用来帮你判断下载的.7z文件是否是完整的。在linux里有个命令可以查看文件的【SHA-256哈希值】`sha256sum filename`，如下。不过现在的话基本不会出现下载的文件不完整的事情就是。

![e47c4b86e2164fb1a5c1016c201c94e4.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/e47c4b86e2164fb1a5c1016c201c94e4.png)

![PixPin_2025-07-22_15-55-56.png](/images/2025/%E5%A4%8F-5-7/kali%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85-%E4%B8%80%E6%AD%A5%E5%88%B0%E4%BD%8D/PixPin_2025-07-22_15-55-56.png)

命令详情可以移步【[https://zhuanlan.zhihu.com/p/689918610](https://zhuanlan.zhihu.com/p/689918610 "https://zhuanlan.zhihu.com/p/689918610")】

（如有不恰当的地方欢迎指正哦 ~o(●’◡’●)o）

**参考博客：**

【[bios里的vmx是什么意思\_mob649e8169ec5f的技术博客\_51CTO博客](https://blog.51cto.com/u_16175522/12092522 "bios里的vmx是什么意思_mob649e8169ec5f的技术博客_51CTO博客")】

【[torrent是什么文件？torrent文件怎么打开？ - 系统之家](https://www.xitongzhijia.net/xtjc/20230104/272154.html "torrent是什么文件？torrent文件怎么打开？ - 系统之家")】

【[BT种子(torrent)&磁力链接的简介与使用 - 哔哩哔哩](https://www.bilibili.com/opus/770355741148053553 "BT种子(torrent)&磁力链接的简介与使用 - 哔哩哔哩")】


## 0x00

非教学目的学习阻碍记录文章。`环境 + 解决 + 延伸`

文章内容已做脱敏处理，不得用于任何非法犯罪活动，否则后果自行承担。

*记录的本质是建立检索索引。只要某个知识点解决了具体的微小阻碍即具备记录价值。​​*



## 0x01-知识前置

> 在开始之前，得先了解基础的CDN知识

#### CDN 本质

CDN 的本质是反代服务器集群，主要反代对象是**第四层传输层**和**第七层应用层**

```txt
[客户端] <---- (1) TCP/TLS 握手 ----> [CDN 边缘节点] 
                                          ||
                                     (2) 预建立 / 长连接
                                          ||
                                          \/
                                      [源站]
```

1. 为了避免多次 TLS 握手，CDN 与 源站之间会维持一个长连接

2. 为了能够解密、分析并缓存 HTTPS 流量，域名证书（私钥和公钥证书）必须托管在 CDN 平台
3. 由于能够明文看到 HTTP 内容，可额外充当 Web防火墙使用，可以封禁ip，过滤爬虫，监控扫描

#### CDN 特性

CDN 作为高可用功能完备的**中间层**反代服务器集群，可以用来做的事情非常之多

1. 防止请求暴增请求变慢或瘫痪，负载均衡
2. 配置 WAF，拦截危险请求与爬虫等
3. 缓存静态文件，加快访问速度
4. 作为中间层隐藏了源站IP
5. 反代服务器进行 SSL 加密等繁重任务，减轻源服务器负担

6. 等等

#### CDN 记录

1. 大部分 CDN 都是使用的 **CNAME 记录来反代**的，除了：

   1. **高防IP**、特定节点独享等

   2. 像 **Cloudflare** 这类采用 **NS** 接入方式的 CDN，需要把用户域名的完整 DNS 托管权（NS记录）托管到 **Cloudflare** 服务器上，这种模式下不需要手动配 CNAME，而是由 **Cloudflare** 的 DNS 系统直接接管并返回其 Anycast 节点的 A/AAAA 记录

~~如果是 edu 的话那么可以认为都是 CNAME 记录~~

2. `cname记录`与任意其他记录比如`NS记录`、`SOA记录`、`a记录`都排斥且只能有一个`cname记录`，举例一行 dnsx-a记录结果
```json
{"host":"livepush.gxtcmu.edu.cn","ttl":21600,"resolver":["8.8.8.8:53"],"a":["120.233.18.218","120.241.130.235","183.232.224.146","120.233.17.155","120.233.18.66","120.241.149.224","120.233.21.53","120.233.18.149","120.232.131.170","120.241.130.207","120.233.20.237","120.241.149.168","120.233.19.60","183.232.224.147","120.233.21.105","120.233.20.93"],"cname":["livepush.gxtcmu.edu.cn.livepush.myqcloud.com","livepush.gxtcmu.edu.cn.tlivepush.com","yunlivepush.msf.tencent-cloud.com"],"all":["livepush.gxtcmu.edu.cn.\t21600\tIN\tCNAME\tlivepush.gxtcmu.edu.cn.livepush.myqcloud.com.","livepush.gxtcmu.edu.cn.livepush.myqcloud.com.\t300\tIN\tCNAME\tlivepush.gxtcmu.edu.cn.tlivepush.com.","livepush.gxtcmu.edu.cn.tlivepush.com.\t120\tIN\tCNAME\tyunlivepush.msf.tencent-cloud.com.","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.18.218","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.241.130.235","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t183.232.224.146","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.17.155","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.18.66","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.241.149.224","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.21.53","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.18.149","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.232.131.170","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.241.130.207","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.20.237","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.241.149.168","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.19.60","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t183.232.224.147","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.21.105","yunlivepush.msf.tencent-cloud.com.\t300\tIN\tA\t120.233.20.93","\n;; OPT PSEUDOSECTION:\n; EDNS: version 0; flags:; udp: 512"],"status_code":"NOERROR","timestamp":"2026-07-21T15:56:11.06355124+08:00"}
```
看似又有 a 记录 又有 cname 记录而且不止一个 cname，但这是递归 dns 查找的假象，看`all`，第一个 cname 域名指向一个第二个 cname 域名，第二个 cname 域名指向第三个 cname 域名，第三个 cname 域名含有很多 a 记录，这就是 前面 a 记录的由来，递归 dns 查询把中间的这些经过的 cname 和 a 记录都打印了出来，所以其中中间经过的所有 dns 服务器设置都是合规的。



## 0x02

#### 1. 如何确定一行 dnsx-a 中的子域名是否带有 cdn 呢？

```json
{"host":"live.gxtcmu.edu.cn","ttl":600,"resolver":["9.9.9.9:53"],"a":["210.36.99.65"],"all":["live.gxtcmu.edu.cn.\t600\tIN\tA\t210.36.99.65","\n;; OPT PSEUDOSECTION:\n; EDNS: version 0; flags:; udp: 512"],"status_code":"NOERROR","timestamp":"2026-07-21T15:56:11.373754544+08:00"}
```

**回答**

目前来讲就看是否有 cname 记录，如果有就看是否命中 `cdn_name.txt`文件，命中则存在 cdn，否则不存在

*至于那些不靠 CNAME 记录的带 cdn 域名，感觉靠找的 IP 库`resolvers.txt`并不靠谱目前就不考虑吧*

**记录**



#### 2. 解决dnsx->过滤dnsIP->naabu

让 **Ai** 写一个 python 代码，从 `dnsx-a.jsonl` 中提取六个文件：所有域名集合、所有IP集合、仅CDN域名集合、仅CDN IP集合、过滤了CDN后的域名集合、过滤了CDN域名所有IP后的IP集合。代码 `-h` 如下：

```shell
> python .\dnsx-过滤dnsIP.py -h                                                    
usage: dnsx-过滤dns域名.py [-h] [-j JSONL] [-c CDN] [-o OUTPUT] [-s]

DNSx CDN Filter Tool

optional arguments:
  -h, --help            show this help message and exit
  -j JSONL, --jsonl JSONL
                        dnsx jsonl 文件路径
  -c CDN, --cdn CDN     cdn 后缀文本文件路径
  -o OUTPUT, --output OUTPUT
                        输出文件的文件夹路径 (默认当前文件夹)
  -s, --silent          静默模式，不输出任何日志和 IP
```

****

**命令**

```bash
python3 dnsxForCDN.py -c cdn_cname.txt -j dnsx_a.jsonl -o normalized/ | naabu
```

**记录**

1、工具默认输出-过滤了CDN域名所有IP后的IP集合，用于交给后续工具比如 **naabu**




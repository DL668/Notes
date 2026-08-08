## 0x00

非教学目的学习阻碍记录文章。`环境 + 解决 + 延伸`

文章内容已做脱敏处理，不得用于任何非法犯罪活动，否则后果自行承担。

*记录的本质是建立检索索引。只要某个知识点解决了具体的微小阻碍即具备记录价值。​​*



## 0x01

#### 1. 需要提取 dnsx 扫描结果中解析成功的 host 主机地址（jsonl）

```json
{"host":"****.***.edu.cn","ttl":600,"resolver":["9.9.9.9:53"],"a":["210.36.99.200"],"cname":["proxy.***.edu.cn"],"all":["****.***.edu.cn.\t600\tIN\tCNAME\tproxy.***.edu.cn.","proxy.***.edu.cn.\t43148\tIN\tA\t210.36.99.200","\n;; OPT PSEUDOSECTION:\n; EDNS: version 0; flags:; udp: 512"],"status_code":"NOERROR","timestamp":"2026-07-21T15:57:15.406335056+08:00"}
{"host":"zyyxsys.***.edu.cn","ttl":3498,"resolver":["149.112.112.112:53"],"soa":[{"name":"***.edu.cn","ns":"ns01.***.edu.cn","mailbox":"root.***.edu.cn","serial":2100000175,"refresh":86400,"retry":3600,"expire":604800,"minttl":10800}],"all":["\n;; OPT PSEUDOSECTION:\n; EDNS: version 0; flags:; udp: 1232","***.edu.cn.\t3498\tIN\tSOA\tns01.***.edu.cn. root.***.edu.cn. 2100000175 86400 3600 604800 10800"],"status_code":"NXDOMAIN","status_code_raw":3,"timestamp":"2026-07-21T15:57:15.391645157+08:00"}
```

**命令**

```bash
jq -r 'select(.a)|.host' dns/dnsx扫描.jsonl
```

**记录**

1、为啥只要含有 a记录 的主机地址

看似会漏掉 CNAME、纯IP6、非web服务等资产，但是这次过滤的目的就是找到**可直接攻击的web服务**

2、`-r`有啥用

意思是**输出原始字符串**而非以 JSON 内的格式打印，去掉了引号，\n\t啥的也会生效

 3、`select()` 函数

字面意思，筛选值为 `true` 的行



#### 2. 需要提取 dnsx 扫描结果中解析成功的 IP（jsonl）

```json
内容如 1.
```

**命令**

```bash
jq -r 'select(.a)|.a[]?' dns/dnsx扫描.jsonl
或
jq -r '.a[]?' dns/dnsx扫描.jsonl
```

**记录**

1、`.a[]?`详情

`.a[]`是为了轮询拿到数组里面的每个元素，防止一个域名绑定多个 `ip`;

`?`是防止程序在遇到错误时中断并退出，这里主要是遇到 `a` 字段为 `null` 或者非数组标量等非预期时不打印 `error` 并静默跳过



#### 3. 提取 httpx 首页探测文件部分内容生成摘要（jsonl）

```json
{"timestamp":"2026-07-15T16:07:34.741696553+08:00","port":"443","url":"https://WWW.**.edu.cn","input":"WWW.**.edu.cn","title":"**学院","scheme":"https","webserver":"none","content_type":"text/html","method":"GET","host":"***.**.edu.cn","host_ip":"222.204.96.5","path":"/","time":"839.606606ms","a":["222.204.96.5"],"aaaa":["2001:250:6c23::3:8704"],"tech":["HSTS","Slick","Swiper","Vue.js","fullPage.js","jQuery"],"words":40848,"lines":2168,"status_code":200,"content_length":109223,"failed":false,"knowledgebase":{"PageType":"nonerror","pHash":0},"resolvers":["1.0.0.1:53","127.0.0.53:53"]}
{"timestamp":"2026-07-15T16:07:35.475310937+08:00","port":"443","url":"https://WWW.**.edu.cn","input":"www.**.edu.cn","title":"**中医药大学","scheme":"https","content_type":"text/html","method":"GET","host":"WWW.**.edu.cn","host_ip":"210.36.99.200","path":"/","time":"1.359787891s","a":["210.36.99.200"],"aaaa":["2001:250:3419:a001::202"],"cname":["proxy.**.edu.cn"],"tech":["Bootstrap","Swiper","jQuery","jQuery Migrate"],"words":33368,"lines":2970,"status_code":200,"content_length":141667,"failed":false,"knowledgebase":{"PageType":"nonerror","pHash":0},"resolvers":["8.8.8.8:53","1.1.1.1:53"]}
```

**命令**

```bash
jq -r '[.url, .title, .status_code, (.tech // [] | join(",")), .webserver] | @tsv' web/httpx_low.jsonl
```

**记录**

1、`@tsv`是将数组变成tsv格式输出

2、对`.tech // [] | join(",")`

`//`是替代运算符，当字段为空或不存在时使用的默认值；`join("str")` 函数是把数组变成指定字符分割的字符串



#### 4. 提取 naabu 的host+port形式开放端口（jsonl）

```json
{"host":"www.***.edu.cn","ip":"101.6.15.66","timestamp":"2026-07-18T07:57:05.015261215Z","port":80,"protocol":"tcp","tls":false}
{"host":"ehall.***.edu.cn","ip":"218.64.115.218","timestamp":"2026-07-18T07:57:05.015329093Z","port":22,"protocol":"tcp","tls":false}
{"host":"ehall.***.edu.cn","ip":"218.64.115.218","timestamp":"2026-07-18T07:57:05.015329093Z","port":80,"protocol":"tcp","tls":false}
```

**命令**

```bash
jq -r '.host + ":" + (.port|tostring)' ports/目标.jsonl
```

**记录**

1、只有**字符串**之间可以使用加号，连接

2、`tostring` 会将不存在返回为`null`的本不打印的字符串打印出来`null:22`



#### 5. 通过title或技术栈提取 httpx 高价值入口（jsonl）

```json
如上3. 
```

**代码**

```bash
jq -r 'select((.title // "" | test("admin|login|sign in|dashboard|console|portal|sso|vpn|jenkins|gitlab|nexus|harbor|grafana|kibana|swagger|api"; "i")) or ((.tech // []) | tostring | test("Jenkins|GitLab|Grafana|Kibana|Spring|Laravel|Django|WordPress|Drupal|Confluence|Jira"; "i")) ) | [.url, .status_code, .title, (.tech // [] | join(","))] | @tsv' web/httpx_webIP.jsonl
```

**记录**

1、`test(regex; flags)`函数，用于匹配输入字符串是否匹配正则表达式`regex`，是返回 `true` 否则返回 `false`



#### 6. 对 httpx 路径探测的结果提取有价值的状态码的响应

```json
如上5. 
```

**代码**

```bash
jq -r 'select(.status_code == 200 or .status_code == 204 or .status_code == 301 or .status_code == 302 or .status_code == 401 or .status_code == 403) | [.url, .status_code, .title] | @tsv' web/httpx_paths_small.jsonl
```

**记录**

1、`select` 函数内的双等号`==`，对于非字符串字段直接写原始字符串，字符串比较相等需要带上引号，数组的话需要先`[]`读取出来

2、除了`==`还有`>`、`not`、`<=`、`!=`、`一对多小括号：(.id == ("a", "b", "c"))`、`IN运算符：(.category」IN（"books","toys"))`


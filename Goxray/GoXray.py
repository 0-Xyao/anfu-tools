import re
import time
import subprocess
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def animate():
    print("GoXray")
    for i in range(10):
        time.sleep(0.1)
        print(".", end='', flush=True)
    print("\n")

# 扫描
def get_url():
    animate()
    print("Scanning URLs...")
    with open("1.txt", 'r') as f:
        lines = f.readlines()
        urls = [line.strip() for line in lines]
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(do_scan, url) for url in urls]
            for future in tqdm(as_completed(futures), total=len(futures), desc="Progress", unit="URL"):
                pass
        print("GoXray 脚本任务已经全部结束啦 ~ 请去xray目录文件下看结果吧！！")

# 报告
def do_scan(targeturl):
    scan_command = "xray执行程序的地址 webscan --basic-crawler {} --html-output {}.html".format(targeturl, time.strftime("%Y%m%d%H%M%S", time.localtime()))
    result, error = subprocess.Popen(scan_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    if error:
        print("报错:" + error)


if __name__ == '__main__':
    print("Author: 小妖")
    print("Github: www.0-sec.org")
    get_url()
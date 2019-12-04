#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json
import os

url = 'https://www.baidupcs.com/rest/2.0/pcs/file?method=batchdownload&app_id=250528&zipcontent=%7B%22fs_id%22%3A%5B%221025072055159776%22%5D%7D&sign=DCb740ccc5511e5e8fedcff06b081203:CKf%2BY6AijfANBRTm8%2BFKgjMv%2BdQ%3D&uid=3828142840&time=1549167097&dp-logid=753953991543021165&dp-callid=0&shareid=1418175071&vuk=2735418373&from_uk=3828142840'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'h-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=E5B6F3FE1FDDE9EEE22EBE2A3A116A21:FG=1; BIDUPSID=E5B6F3FE1FDDE9EEE22EBE2A3A116A21; PSTM=1532089471; BDUSS=0hXaE5ON2FYai1TcUZ5SEp2UWRKVH5od3BCVWVRalZ4b1p3LTZ0TU9jUnp-RDljQVFBQUFBJCQAAAAAAAAAAAEAAABio9oPwMvErNfTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHNvGFxzbxhcR; PANWEB=1; SCRC=97fd12152e06ba809fdd033e05c57c2a; STOKEN=3c70a4f4543e521c36bf2f48f01a601208141e4f94fa906a0bf3d1ad46bd44b1; MCITY=-%3A; BDSFRCVID=m6_OJeC62w7R6gR9_2qnhhEO6ZxLuArTH6aomEU5j3FBDH7GuhP-EG0Pqx8g0Ku-fYxPogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tR4f_C_2JDP3HjrGh4rohCCDMeT22-us55rAQhcH0hOWsIO_jf7xefLh0MorWq5W0b5u_IQ72pnsJC38DUC0D6bLDH-qJ6_sbKT03JA8MJnEDRTphPTMq4tHeUOG0URZ5mAqoqOl0f7zVCTH-pJTM-kkXNjLBMrnbNrnaIQqahjDbqRYbljkMTtNWq5mW-343bRT0xKy5KJvfJoDDhomhP-UyNbMWh37JgnlMKoaMp78jR093JO4y4Ldj4oxJp8eWJLDVItbtIDMMCvGh4rohCuShMr2aK6B5Po2WbCQ5PJP8pcNLTDK5T0FjU7qqlRiaIb3Bp5vJtnaqlKl0lO1j4_eMMTPB4CJ2eJd-POL0J6lKq5jDh38b6ksD-RC5q5L-D7y0hvctb3cShPmQMjrDRLbXU6BK5vPbNcZ0l8K3l02VKO_e6LWD5JQDH8qqbQX2COXsROs2ROOKRcgq4bohjPNKN79BtQmJJrf_pD52PLB_pv13P7sQfRB2hQH06oNQg-q3R7kLnnaHlcsj47ADRIYhJ_L0x-jLIQhVn0MWhjDSR64-PnJyUnybPnnBT3R3H8HL4nv2JcJbM5m3x6qLTKkQN3TJMIEtJIDoCPbJKK3ePFkMRoSMJK8qxby26nhKD39aJ5nJD_bDqTa0-CBBTDL5f730x4qaRnK2Pn-QpP-HJ7O0t5tyIuQ0t5iXUuLbeODKl0MLn5tbb0xynoDqtA-eMnMBMPe52OnaIbg3fAKftnOM46JehL3346-35543bRTohFLtKKBhD8xjTRJ2CCSbfTJ546-bPo2WbCQaCQr8pcNLTDK5T-wjxJNql4H-Co3Bp5vJfcW8-5qKlO1j4_ehtoPt4Ie3erRaI3TbRnmKq5jDh3a25ksD-Rte45kMNRy0hvctb3cShPmQMjrDRLbXU6BK5vPbNcZ0l8K3l02VKO_e4bK-TrLDaDqtM5; __cfduid=d14569dc419299c7aa53f2ee2473047441548839466; recommendTime=android2019-1-10%2023%3A00%3A00; delPer=0; PSINO=7; BDRCVFR[nnelRoIzZZm]=mk3SLVN4HKm; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1548213861,1548916822; BDCLND=tUNWiazAyRkV8yKWz6dAxLqun0g2Eoe7vDGLKkujq5c%3D; cflag=13%3A3; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1549079765; PANPSC=11943951597206902809%3A%2B81kGQfJNqVmDcgoDIAUmyOAoXNFwReXaiA%2FXcu7nVWE%2BOIrd2nRUH1zrFo7iguBMMKOMtLkW71wFJ9JmemY6TdROfoEwLDdfbZ%2FbYW506b1X5adGuj0LCC9yOinRwwiKg6bXhEDmDblx9uR5zc7VqobC%2F8PQKg%2FucRG%2BvaTatV%2F6cHXN0p1RdzN5H7TMMhsLCFZ7HPnpb2hc8sexGDNJyxpw24b%2F7yfH2ZgbBWZKWh3MYyx6aD0yXcxjLHpoPTJ',
    'Host': 'pan.baidu.com',
    'Referer': 'https://pan.baidu.com/share/init?surl=-jFf2FFj5bVkTxJhJ8WsDg',
    'Upgrade-Insecure-Requests': '1',
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

content = requests.get(url, headers=headers).content.decode('utf-8')
save_file('/tmp/lagou.txt', save_content)

exit()

'''
 爬取数据
'''

# https://www.lagou.com/jobs/5497378.html
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'h-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=ABAAABAAAGGABCBD1AB331ECC731B131DC93ACFC97D633F; _ga=GA1.2.1570399977.1547543937; _gid=GA1.2.904590377.1547543937; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547543937; user_trace_token=20190115171857-96313a73-18a6-11e9-b244-525400f775ce; LGUID=20190115171857-96313edb-18a6-11e9-b244-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; TG-TRACK-CODE=index_navigation; SEARCH_ID=04ce84b1a6ff4739a43e429c6c06dd3e; LGSID=20190116145532-b76b8058-195b-11e9-b641-525400f775ce; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221685590256f5bf-04cb761f33cdbe-1e2e130c-2073600-16855902570317%22%2C%22%24device_id%22%3A%221685590256f5bf-04cb761f33cdbe-1e2e130c-2073600-16855902570317%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LG_LOGIN_USER_ID=5eebf05d2b0679c4c0bb5a9401dd4497974bf84b805d291b; _putrc=9379C8B07F768DDD; login=true; unick=%E4%B8%81%E5%AE%87%E6%98%8E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=58; _gat=1; gate_login_token=3984c1aa190e8d15892536f9a782b5377e1b3754ac92ce9b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547623779; LGRID=20190116152938-7b465de8-1960-11e9-b665-525400f775ce',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/5122421.html',
    'Upgrade-Insecure-Requests': '1',
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def fetch_url(url):
    '''获取内容并转码'''
    return requests.get(url, headers=headers).content.decode('utf-8')  # 解码


def parse_company(content):
    '''获取公司名'''
    reg = re.findall(r'company">(.*)招聘</div>', content)
    return reg[0] if reg else ''


def parse_job_name(content):
    '''获取职位名称'''
    reg = re.findall(r'class="job-name" title="(.*)">', content)
    return reg[0] if reg else ''


def parse_job_des(content):
    '''获取职位描述'''
    reg = re.findall(r'class="job-detail">(.*)</div>', content)
    return reg[0] if reg else ''


def parse_addr(content):
    '''获取地址'''
    reg = re.findall(r'class="work_addr">(.*)</div>', content)
    return reg[0] if reg else ''


def parse_salary(content):
    '''获取薪资'''
    reg = re.findall(r'class="salary">(.*)<', content)
    return reg[0] if reg else ''


def parse_outline_tag(content):
    '''匹配是否已下线'''
    reg = re.findall(r'outline_tag">.*(下线).*</span>', content)
    return True if reg and reg[0] else False
    # Python 的三目运算符变种： 为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）


def save_file(filename, content):
    with open(filename, 'a', encoding='utf8') as f:
        f.write(content)
        print('已保存为：' + filename)


def main():
    job_id = 5000600
    while job_id < 5001000:
        url = 'https://www.lagou.com/jobs/' + str(job_id) + '.html'  # 循环处理
        content = fetch_url(url)
        job_name = parse_job_name(content)
        job_des = parse_job_des(content)
        addr = parse_addr(content)
        if not job_name or parse_outline_tag(content) or 'php' not in job_des or '广州' not in addr:
            print(str(job_id) + ' ' + job_name)
            job_id += 1
            continue
        company = parse_company(content)
        salary = parse_salary(content)
        save_content = str(job_id) + ' ' + company + ' ' + job_name + ' ' + salary + "\n"
        save_file('/tmp/lagou.txt', save_content)
        job_id += 1


if __name__ == "__main__":
    main()

'''
 分析数据
'''

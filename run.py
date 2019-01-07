#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import os
from libs.common.date import *

if __name__ == '__main__':
    now = get_date_string()
    current_xml_dir = "./reports/xml"
    current_html_dir = "./reports/html/{0}".format(now)
    os.system("pytest -s -q --alluredir {0}".format(current_xml_dir))
    os.system("allure generate {0} -o {1}".format(current_xml_dir, current_html_dir))
    os.system("allure open {0}".format(current_html_dir))
    print("result generated at {0}".format(current_html_dir))
# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "lijingxin6/lijingxin6.github.io@master"
}

# 站点设置
site_name = "自然语言处理爱好者"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "李敬鑫"
email = "lijingix666@gmail.com"
author_homepage = "https://www.lijingxin.xyz"
description = "A NLPer"
key_words = ['DeepLearning', 'NLP', '李敬鑫', 'blog']
language = 'zh-CN'
# external_links = [
#     {
#         "name": "Maverick",
#         "url": "https://github.com/AlanDecode/Maverick",
#         "brief": "🏄‍ Go My Own Way."
#     },
#     {
#         "name": "三無計劃",
#         "url": "https://www.imalan.cn",
#         "brief": "熊猫小A的主页。"
#     }
# ]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/lijingxin6",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/lijingxin6",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/2294989641/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''

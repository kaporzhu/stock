# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
    pinyin = ['b', 'ba', 'bo', 'bai', 'bei', 'bao', 'ban', 'ben', 'bang', 'beng', 'bi', 'bie', 'biao', 'bian', 'bin', 'bing', 'p', 'pa', 'po', 'pai', 'pao', 'pou', 'pan', 'pen', 'pang', 'peng', 'pi', 'pie', 'piao', 'pian', 'pin', 'ping', 'm', 'ma', 'mo', 'me', 'mai', 'mao', 'mou', 'man', 'men', 'mang', 'meng', 'mi', 'mie', 'miao', 'miu', 'mian', 'min', 'ming', 'f', 'fa', 'fo', 'fei', 'fou', 'fan', 'fen', 'fang', 'feng', 'd', 'da', 'de', 'dai', 'dei', 'dao', 'dou', 'dan', 'dang', 'deng', 'di', 'die', 'diao', 'diu', 'dian', 'ding', 't', 'ta', 'te', 'tai', 'tao', 'tou', 'tan', 'tang', 'teng', 'ti', 'tie', 'tiao', 'tian', 'ting', 'n', 'na', 'nai', 'nei', 'nao', 'no', 'nen', 'nang', 'neng', 'ni', 'nie', 'niao', 'niu', 'nian', 'nin', 'niang', 'ning', 'l', 'la', 'le', 'lai', 'lei', 'lao', 'lou', 'lan', 'lang', 'leng', 'li', 'lia', 'lie', 'liao', 'liu', 'lian', 'lin', 'liang', 'ling', 'g', 'ga', 'ge', 'gai', 'gei', 'gao', 'gou', 'gan', 'gen', 'gang', 'geng', 'k', 'ka', 'ke', 'kai', 'kou', 'kan', 'ken', 'kang', 'keng', 'h', 'ha', 'he', 'hai', 'hei', 'hao', 'hou', 'hen', 'hang', 'heng', 'j', 'ji', 'jia', 'jie', 'jiao', 'jiu', 'jian', 'jin', 'jiang', 'jing', 'q', 'qi', 'qia', 'qie', 'qiao', 'qiu', 'qian', 'qin', 'qiang', 'qing', 'x', 'xi', 'xia', 'xie', 'xiao', 'xiu', 'xian', 'xin', 'xiang', 'xing', 'zh', 'zha', 'zhe', 'zhi', 'zhai', 'zhao', 'zhou', 'zhan', 'zhen', 'zhang', 'zheng', 'ch', 'cha', 'che', 'chi', 'chai', 'chou', 'chan', 'chen', 'chang', 'cheng', 'sh', 'sha', 'she', 'shi', 'shai', 'shao', 'shou', 'shan', 'shen', 'shang', 'sheng', 'r', 're', 'ri', 'rao', 'rou', 'ran', 'ren', 'rang', 'reng', 'z', 'za', 'ze', 'zi', 'zai', 'zao', 'zou', 'zang', 'zeng', 'c', 'ca', 'ce', 'ci', 'cai', 'cao', 'cou', 'can', 'cen', 'cang', 'ceng', 's', 'sa', 'se', 'si', 'sai', 'sao', 'sou', 'san', 'sen', 'sang', 'seng', 'y', 'ya', 'yao', 'you', 'yan', 'yang', 'yu', 'ye', 'yue', 'yuan', 'yi', 'yin', 'yun', 'ying', 'w', 'wa', 'wo', 'wai', 'wei', 'wan', 'wen', 'wang', 'weng', 'wu']
    url = 'http://pandavip.www.net.cn/check/check_ac1.cgi?domain=%s.com'

    def handle(self, *args, **options):
        available_domains = []
        total_domains = 0
        failed_domains = 0
        for p1 in self.pinyin:
            for p2 in self.pinyin:
                total_domains += 1
                try:
                    if 'Domain exists' not in requests.get(self.url%(p1+p2)).text:
                        available_domains.append(p1+p2)
                except:
                    failed_domains

        if available_domains:
            send_mail('Available domains',
                      '%s[%d-%d]'%(' '.join(available_domains), total_domains, failed_domains),
                      settings.EMAIL_HOST_USER, [settings.SERVER_EMAIL])
        else:
            send_mail('NO available domain is released today',
                      '[%d-%d]'%(total_domains, failed_domains),
                      settings.EMAIL_HOST_USER, [settings.SERVER_EMAIL])

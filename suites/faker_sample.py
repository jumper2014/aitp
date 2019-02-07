#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# https://faker.readthedocs.io/en/master/locales/zh_CN.html

from faker import Faker

if __name__ == '__main__':
    fake = Faker('zh_CN')
    for i in range(10):
        print(fake.country())
        # '诺福克岛'

        print(fake.street_suffix())
        # '街'

        print(fake.country_code(representation="alpha-2"))
        # 'CN'

        print(fake.postcode())
        # '217215'

        print(fake.district())
        # '华龙'

        print(fake.building_number())
        # 'x座'

        print(fake.address())
        # '云南省惠州市南湖刘路B座 842027'

        print(fake.province())
        # '安徽省'

        print(fake.street_address())
        # '李街I座'

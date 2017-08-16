# -*- coding=utf-8 -*-

# get ali phone numbers

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.ext.declarative import declarative_base
import requests as req
import time
import json

engine = create_engine('postgresql://postgres:postgres@localhost/my_db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

base_model = declarative_base()


class AliPhoneInfo(base_model):
	__tablename__ = 'ali_phone_info'

	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	addr = Column(String(64), nullable=False)
	phone_num = Column(String(32), nullable=False)

	def __init__(self, addr, phone_num):
		self.addr = addr
		self.phone_num = phone_num
		

def get_ali_phone_nums():
	url = "https://aliqin.tmall.com/numlevel/prettyNumReservedSold.do?"

	for i in range(0,100):
		url_params = {"_tb_token_":"5dfd81b357134", "_ksTs":"1502769432870_67", "m":"sold", "callback":"jsonp{0}".format(i), "_input_charset":"UTF-8"}
		req_cookies = {"_tb_token_":"5dfd81b357134", "cna":"", "cookie2":"1fb8d8aab4dbb1bf43ec2cfe41ffd9c0", "t":"292d73ee676a5bd9b3a7b27bd8df8253"}

		res = req.get(url, params=url_params, cookies=req_cookies)

		print i
		print "status_code:",res.status_code

		# print "content:", res.text[res.text.index("{"):res.text.rindex("}")]

		res_json = res.text[res.text.index("{"):res.text.rindex("}")+1]
		# print res_json

		res_dict = json.loads(res_json)

		# for key in res_dict.keys():
			# print key

		for item in res_dict.get("data").get("unsold"):
			data = item.split(" ")
			# print data[0],data[1]
			print "归属地:", data[0]
			print "手机号:", data[1]
			phone_num = session.query(AliPhoneInfo).filter(AliPhoneInfo.phone_num == data[1]).all()
			if len(phone_num) > 0:
				print "the num has getted!!!!"
				continue
			phone_info = AliPhoneInfo(data[0], data[1])
			session.add(phone_info)

		session.commit()
		time.sleep(1)


	session.close()


if __name__ == "__main__":
	try:
		get_ali_phone_nums()
	except Exception as e:
		print "get ali phone nums error:" , e




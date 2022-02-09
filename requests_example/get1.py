from requests import get
from bs4 import BeautifulSoup as bsp
from threading import Thread
from time import time

def main():
	headers = {
		"cookie":"SESSIONID=HrPazhGMeQ21VPmJbGUStdJ2p2jJ7hgPjP9vAgDNUWh; JOID=UVsQB0_UPoMFVldqBtNZ1NaAeRoU9xuhJnJ0TyTwHaYndXNJIy1SgWBRUW0Hi3lWnFUhd5eMx6OLpI1FOCVDNcs=; osd=VlAcBU7TNY8HV1BhCtFY092MexsT_BejJ3V_QybxGq0rd3JOKCFQgGdaXW8GjHJanlQmfJuOxqSAqI9EPy5PN8o=; __snaker__id=LTdZ3qzJ0jvvZf6q; _zap=b41c394c-877a-406e-a5b5-6e3cf5c4215a; _xsrf=eyiBe6zVtc4DBCNEXfgoE2DkmBnIQzs8; d_c0=\"AKAQ9NYpdxSPTsy0ahmjGoG3382YzBYFwiw=|1644374306\"; r_cap_id=\"MWY3OGNkMTA3MGM1NGJkZTgyZmM5N2NhNDkwOTE0ODM=|1644374308|2a25282f9aaddebeec2988554f1359c7c5dbc62a\"; cap_id=\"ZDMwOWRmYzcwMTJmNGY4Nzg2YWY3ZTExYzE3YzcyZGU=|1644374308|fa0d1761651393a4d579d6e940c4af3d66f14d31\"; l_cap_id=\"Y2YwMTc1NDk4MzYyNDQ5MjgwNGU3YTY5N2Y2ZTJiM2Y=|1644374308|6de2520c201b745a432ee9f55f4c451d5136d415\"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1644374308,1644380629,1644391422; NOT_UNREGISTER_WAITING=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1644392122; ariaDefaultTheme=undefined; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1644392121|1644391420; captcha_session_v2=\"2|1:0|10:1644392122|18:captcha_session_v2|88:MkgyaGxKSFBEazhNb0xycmZsZXgvdzVBYWV4VDlBRkwrM28ycTZiV21hZ0ZDNHh3YUtWd0Rjemk2dnFzbTBISg==|6138b9e4eee54bddde72613700e37617ff32075799a2f6c7dfc7f411ad22adc7\"; gdxidpyhxdE=8C3lPvP8vKv08ri6Ho9vhcxvy/GLxS\pmlyI9WiGDZ0uJQjpch6PGUxIHi/0QcK6Hos00+fQhTzJtRwWb4iUZZaKi6fvRvw73sITJDxeUfOsI/7EnzxauS8+pJCZPi+mvLaxEk\WbabpvJ+oBx18iEmop\8tKj7T0ojzefrHgBDbQ/Qk:1644393024146; _9755xjdesxxd_=32; YD00517437729195:WM_NI=/FMTjcAithghrObdVhJGYca68ClJ8rqVV7FyA3NrFP3+HURvzlFBqUltziy1DcEHJYV7vfs/M5Re0dGv9le63jhyq5vNGhZYR4x0l4Mz7lWr9voiUF3jrUlasPbGsJDxcVk=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eeace47b90aba7a7e1458ab48ba6c14e939f8eafb6258990fe86c94997ec9d94c12af0fea7c3b92aed9a83b5e96983b7bc89e664b291ae85d5648a999784e43efc9da4abbb7ab38a9ad8c57383ed8293c55cf1f588b6d17ebab48aa3f45fb0acb68afc3b88bd8ba9c95396e9ba87f2258feb9e86b37085aaf78de83ef1b6a89af43fb6928989d95392ecb8d1ef408fa6f98dd67afbaaa18ad84ef1b6beb6ef6bb190aea8f24288a8adb7ea37e2a3; YD00517437729195:WM_TID=2tl0ALNhughBFQEQFUd7qfLieMXU5S8R",
		"host":"zhuanlan.zhihu.com",
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
	}
	res = get(url="https://zhuanlan.zhihu.com/p/109467098",
				headers=headers)
	html = bsp(res.text, "html.parser")
	main_div = html.find_all("div",
				class_="RichText ztext Post-RichText css-hnrfcf")[0]
	imgs = [i.find_all("img")[0] for i in main_div.find_all("figure")]
	# print(imgs.__len__())
	links = [i['src'] for i in imgs]
	# print(links)
	'''
	for index, l in enumerate(links):
		open("res/%d.jpg"%index, "wb+").write(get(l).content)
	'''
	for index, l in enumerate(links):
		Thread(target=lambda idx, lk:open("res/%d.jpg" % idx, "wb+") \
					.write(get(lk).content),
				args=(index, l)).start()
	#'''

if __name__ == '__main__':
	main()

import requests
from bs4 import BeautifulSoup as bsp

def getAllLinks(_id, count):
	url_main = "http://www.5haoxue.net/jiaocai/920-%d" % _id
	ret = []
	ret.append(url_main + ".html")
	for i in range(count-1):
		ret.append(url_main + ("-%d" % (i+2)) + ".html")
	return ret

require_data = [
	[19, 4],
	[20, 2],
	[21, 3],
	[22, 1],
	[23, 2],
	[28, 1],
	[29, 1],
	[46, 1],
	[47, 2],
	[48, 1],
	[49, 2],
	[50, 2],
	[51, 1],
	[52, 2],
	[56, 1],
	[57, 1],
]

g_idx = 1;

def getSinglePassage(ll):
	global g_idx
	for link in ll:
		res = requests.get(link)
		html = bsp(res.text, "html.parser")
		img_src = html.find_all("div", class_="det-nr")[0].find_all("img")[0]['src']
		with open("res/chinese_textbook/%d.jpg" % g_idx, "wb+") as f:
			f.write(requests.get(img_src).content)
		g_idx += 1

def main():
	for meta in require_data:
		getSinglePassage(getAllLinks(*meta))

if __name__ == "__main__":
	main()

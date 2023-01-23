import requests
import json
import os, sys
import subprocess

repositories = [] # 公用的，存放从gitee openAPI获取的信息

class GiteeInterface(object):
    def __init__(self, access_token):
        self.access_token = access_token
        # Content-Type: application/json;charset=UTF-8
        self.HEADERS = {
            "Content-type": "application/json",
            "charset": "UTF-8"
        }
        self._all_repos = "https://gitee.com/api/v5/user/repos"

    def getAllRepos(self):
        global repositories
        # 正常情况不超过100，否则需要遍历多页面（未实现）
        response = requests.get(
            url=self._all_repos,
            headers=self.HEADERS,
            params={
                "access_token": self.access_token,
                "sort": "full_name",
                "page": 1,
                "pre_page": 100
            }
        )
        data = json.loads(response.text)
        response.close()
        for i in data:
            # 提取需要信息
            repositories.append([i["path"], i["html_url"], i["private"]])
        
    def downloadAllRepos(self):
        if len(repositories) == 0:
            self.getAllRepos()
        try:
            os.mkdir("./repos")
        except:
            pass
        for repo in repositories:
            print("\033[0;33;49mcloning REPOSITORY[%s]\033[0m" % repo[0])
            os.system("git clone {} {}".format(repo[1], "./repos/"+repo[0]))

class GitHubInterface(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self._api_url = "https://api.github.com/user/repos"
        self.HEADERS = {
            "Authorization": f"Bearer {self.access_token}"
        }

    def uploadAllRepos(self):
        global repositories
        fl = []
        for repo in repositories:
            # 先创建仓库
            response = requests.post(
                url=self._api_url,
                headers=self.HEADERS,
                json={
                    "name": repo[0],
                    "private": repo[2]
                }
            )
            if response.status_code != 201:
                # 创建失败
                print(f"create:failed {repo[0]}")
                fl.append([repo[0], response.status_code])
                continue
            print(f"\033[0;33;49m[create:successful]{repo[0]}\033[0m")
            # 开始上传
            # 先获取目标地址
            addr = json.loads(response.text)["ssh_url"] # 事实证明用ssh能绕过https的某些问题
            subprocess.check_call(f"git remote add _for_mover_github {addr}", cwd=f"./repos/{repo[0]}")
            subprocess.check_call("git push _for_mover_github master", cwd=f"./repos/{repo[0]}")
            print(f"\033[0;33;49m[push:successful]{repo[0]}\033[0m")
            
            # 调试过程中，若中途出错，注释前半段并执行这一句，用于删除github的所有远程库
            # print(requests.delete(f"https://api.github.com/repos/[用户名]/{repo[0]}", headers={"Authorization": f"Bearer {self.access_token}"}))
        
        # 错误信息方便检查
        print(fl)

def main():
    # args: python main.py [-d:download / -m:move] [access_token_of_gitee] [[access_token_of_github]]
    # 初始化接口
    GiteeAPI = GiteeInterface(sys.argv[2])
    
    if sys.argv[1] == "-d":
        GiteeAPI.downloadAllRepos()
    elif sys.argv[1] == "-m":
        if len(sys.argv) == 4:
            GitHubAPI = GitHubInterface(sys.argv[3])
        else:
            exit(1)
        # 先下载下来
        GiteeAPI.downloadAllRepos()
        GitHubAPI.uploadAllRepos()
    else:
        print("error: bad mode")

if __name__ == "__main__":
    main()

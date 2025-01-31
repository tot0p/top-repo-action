import os
import requests
from MDTable import *

#autor tot0p
#github = https://github.com/tot0p/tot0p


class Project:

    def __init__(self,Name,description,Url,Stars,MostUseLa,lc,langURL,user):
        self.Name = Name
        self.Url = Url
        self.Stars = Stars
        self.MostUseLa = MostUseLa
        self.license = lc
        self.description = description
        self.user = user
        r = requests.get(langURL)
        g = list(r.json().keys())
        if g != []:
            self.langs = ', '.join(g)
        else:
            self.langs = ""
user = os.getenv('USERNAME')
INCLUDE_ORG_REPOS = os.getenv('INCLUDE_ORG_REPOS')
NAME_OF_BALISE = os.getenv('NAME_OF_BALISE')
COMMIT_MESSAGE = os.getenv('COMMIT_MESSAGE')

try :
    TOP = int(os.getenv('TOP'))
except:
    TOP = 3
    print("TOP not found, set to 3")

url = "https://api.github.com/users/"+user+"/repos"
DEL_START  ="<!--"+ NAME_OF_BALISE +"-->"
DEL_END    ="<!--/"+ NAME_OF_BALISE +"-->"
n = 0
readmefile=open('README.md','r',encoding='utf-8')
lines = readmefile.readlines()
readmefile.close()
start =-1
end = -1
for line in lines:
    if DEL_START in line:
        start = n
    if DEL_END in line:
        end = n
    n+=1
if start == -1 or end == -1:
    print("Error: Delimiter not found")
    exit(1)
partONe = lines[:start+1]
conttemp = lines[start+1:end]
partTwo = lines[end:]
r = requests.get(url)

repos = []
reponse = r.json()
if 'message' in reponse:
    print(reponse['message'])
    exit(1)

for repo in reponse:
    func = lambda : repo['license']['name'] if repo['license'] else None
    repos.append(Project(repo['name'],repo['description'],repo['html_url'],repo['stargazers_count'],repo['language'],func(),repo['languages_url'],user))

if INCLUDE_ORG_REPOS == "true":
    # add repos from organization
    url = "https://api.github.com/users/"+user+"/orgs"
    r = requests.get(url)
    for org in r.json():
        url = "https://api.github.com/orgs/"+str(org['login'])+"/repos"
        r = requests.get(url)
        for repo in r.json():
            func = lambda : repo['license']['name'] if repo['license'] else None
            repos.append(Project(repo['name'],repo['description'],repo['html_url'],repo['stargazers_count'],repo['language'],func(),repo['languages_url'],org['login']))


reposSort = sorted(repos, key=lambda x: x.Stars, reverse=True)

## remove repo with name of user
reposSort = [x for x in reposSort if x.Name != user]


txt = []
count =0
if TOP > len(reposSort):
    TOP = len(reposSort)
for repo in reposSort[:TOP]:
    count+=1
    txt.append({"Top":count,"Repo":"<a href=\""+repo.Url+"\"><img src=\"https://denvercoder1-github-readme-stats.vercel.app/api/pin/?username="+repo.user+"&repo="+repo.Name+"&theme=dark\" width=\"480px\"/></a>"})


table = Table(header=['Top', 'Repo'],data=[[x["Top"],x["Repo"]] for x in txt]).__str__() +"\n"

txt = [table]

if "".join(conttemp) == txt[0]:
    print("No new content")
    exit(0)
result = partONe + txt + partTwo

readmefile=open('README.md','w',encoding='utf-8')
readmefile.writelines(result)
readmefile.close()

os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
os.system('git config --local user.name "github-actions[bot]"')
os.system('git add .')
os.system('git commit -m "'+COMMIT_MESSAGE+'"')
os.system('git push')

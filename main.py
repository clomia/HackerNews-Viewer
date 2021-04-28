import requests
from flask import Flask, render_template, request
from sibal import fuck
base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"
print(new)
# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"
db = {}
app = Flask("DayNine")

def make_detail_url(id):
    return f"{base_url}/items/{id}"

def get_main(url):
  id_list = []
  title_list = []
  url_list = []
  point_list = []
  author_list = []
  comments_list = []
  created_at_list = []
  JSON = requests.get(url).json()
  search_count = JSON.get("hitsPerPage")
  for post in JSON.get("hits"):
    id_list.append(post.get('objectID'))
  for post in JSON.get("hits"):
    title_list.append(post.get('title'))
  for post in JSON.get("hits"):
    url_list.append(post.get('url'))
  for post in JSON.get("hits"):
    point_list.append(post.get('points'))
  for post in JSON.get("hits"):
    author_list.append(post.get('author'))
  for post in JSON.get("hits"):
    comments_list.append(post.get('num_comments'))
  for post in JSON.get("hits"):
    created_at_list.append(f"  {(post.get('created_at')[:10])}  Time : {(post.get('created_at')[11:-5])}  ")
  BIGLIST = []
  for i in range(search_count):
    dic = {"ID":id_list[i],"TITLE":title_list[i],"URL":url_list[i],"POINT":point_list[i],"AUTHER":author_list[i],"comments":comments_list[i],"created_at":created_at_list[i]}
    BIGLIST.append(dic)
  return BIGLIST


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api

@app.route("/")
def mainpage():
  order = request.args.get('order_by')
  if order == "new":
    if "new" in db:
      BIGLIST = db.get("new")
      print(f"캐시 데이터베이스를 사용합니다")
      USED_DB = "yes"
    else :  
      BIGLIST = get_main(new)
      db["new"] = BIGLIST
      print(f"캐시 데이터베이스가 생성되었습니다")
      USED_DB = "no"
  elif order == "refresh":
    BIGLIST = get_main(new)
    db["new"] = BIGLIST
    USED_DB = "no"
  else:
    if "popular" in db :
      BIGLIST = db.get("popular")
      print(f"캐시 데이터베이스를 사용합니다")
      USED_DB = "yes"
    else :
      BIGLIST = get_main(popular)
      db["popular"] = BIGLIST
      print(f"캐시 데이터베이스가 생성되었습니다")
      USED_DB = "no"
  return render_template(
      "index.html",BIGLIST=BIGLIST,USED_DB=USED_DB)

@app.route("/<id>")
def gothread(id):
  if id in db:
    print(f"캐시 데이터베이스를 사용합니다 \n 키 = {id}")
    USED_DB = 'yes'
    dictinary = db.get(id)
    title = dictinary.get('title')
    link = dictinary.get('link')
    points = dictinary.get('points')
    author = dictinary.get('author')
    children = dictinary.get('children')
    ID = dictinary.get('ID')
    comments_count = dictinary.get('comments_count')
    textlist = dictinary.get('textlist')
  else :
    USED_DB = 'no'
    print(requests.get(make_detail_url(id)))
    JSON = requests.get(make_detail_url(id)).json()
    ID = JSON.get("id")
    children = JSON.get("children")
    title = JSON.get("title")
    link = JSON.get("url")
    points = JSON.get("points")
    author = JSON.get("author") 
    comments_list = JSON.get('children')
    textlist = []
    for commentsdict in comments_list:
        textelement = commentsdict.get("text")
        Author = JSON.get("author")
        if Author == None or textelement == None:
          textlist.append("[삭제된 글입니다 | DELETED]")
        else : textlist.append(f'<h1>메인 작성자| MAIN Writer: {Author}</h1>\n{textelement}')
        repitedlist = commentsdict.get('children')
        fuck.NOOOO(repitedlist)
        textlist.extend(fuck.Returnlist())
    comments_count = len(textlist)  
    db[id] = {"title":title,"link":link,"points":points,"author":author,"children":children,"ID":ID,"comments_count":comments_count,"textlist":textlist}
    print(f"캐시 데이터베이스가 생성되었습니다 \n 키 = {id}")
  return render_template(
      "detail.html",
      title=title,
      link=link,
      points=points,
      author=author,
      children=children,
      ID=ID,
      comments_count=comments_count,
      textlist=textlist,USED_DB=USED_DB)



app.run(host="0.0.0.0")

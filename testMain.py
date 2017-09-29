import requests

testDic = {
    100: ("one", "two"),
    200: ("three",)
}

#print(testDic[100])
#print(locals())

r = requests.get('https://api.github.com/events')

print(r.headers)

print(r.cookies['github_cookie_name'])
from requests_html import HTMLSession

url = 'https://www.instagram.com/inazmashrestha/'

s = HTMLSession()
r = s.get(url)

g = r.html.html
print(g)
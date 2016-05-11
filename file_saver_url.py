import urllib.request

url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'

with url
print ("downloading with urllib")
urllib.request.urlretrive(url, "code.zip")

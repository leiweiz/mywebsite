from django.shortcuts import render

from models import *

def index(request):

	return render(request, 'index.html', {})


from leiweiz.utils.crawlers import mitbbs_spider
def mitbbs(request):
	content = {}
	if 'keywords' not in request.GET:
		content['no_kw'] = 'no_kw'
	elif 'pages' not in request.GET:
		content['no_p'] = 'no_p'
	else:
		keywords = request.GET['keywords'].split(' ')
		pages = int(request.GET['pages'])
		content['results'] = mitbbs_spider(max_pages=pages, key_words=keywords)
		for keyword in keywords:
			try:
				item = Keywords.objects.get(keyword=keyword)
				item.count = item.count + 1
			except:
				item = Keywords(keyword=keyword, page='JobHunting',count=1)
			finally:
				item.save()
	return render(request, 'mitbbs.html', content)
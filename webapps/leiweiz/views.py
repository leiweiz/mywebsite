# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render

from models import *

def index(request):

	return render(request, 'index.html', {})


from leiweiz.utils.crawlers import *
def mitbbs(request):
	content = {}
	if 'keywords' not in request.GET:
		content['no_kw'] = 'no_kw'
	elif 'pages' not in request.GET:
		content['no_p'] = 'no_p'
	elif 'content_page' not in request.GET:
		content['content_page'] = 'no_c_p'
	else:
		keywords = request.GET['keywords'].split(' ')
		pages = int(request.GET['pages'])
		content_page = request.GET['content_page'].strip()
		
		boards = None
		if content_page:
			boards = MitbbsPages.objects.filter(cn_page__contains=content_page)
		if not boards:
			boards = MitbbsPages.objects.filter(cn_page='待字闺中')
		for board in boards:
			specific_board = board.en_page
			if 'results' in content:
				new_results = mitbbs_spider(specific_board=specific_board,max_pages=pages, key_words=keywords)
				content['results'].update(new_results)
			else:
				content['results'] = mitbbs_spider(specific_board=specific_board,max_pages=pages, key_words=keywords)
		for keyword in keywords:
			try:
				item = Keywords.objects.get(keyword=keyword)
				item.count = item.count + 1
			except:
				item = Keywords(keyword=keyword, page=specific_board,count=1)
			finally:
				item.save()
	return render(request, 'mitbbs.html', content)
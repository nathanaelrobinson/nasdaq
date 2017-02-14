from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from stockmarket.models import Stock
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils import timezone


def index(request):
	unordered_stock_list = get_list_or_404(Stock)
	stock_list = sorted(unordered_stock_list, key=lambda stock: stock.value, reverse=True)
	return render(request, 'stockmarket/index.html', {'stock_list' : stock_list})

"""	
	----Above code is shorter version of below, keeping for reference----
	stock_list = Stock.objects.order_by('-ipo_date')[:5]
	template = loader.get_template('stockmarket/index.html')
	context = {'stock_list': stock_list,}
	return HttpResponse(template.render(context,request))
"""
def stockpage(request, stock_id):
	stock = get_object_or_404(Stock, pk=stock_id)
	return render(request, 'stockmarket/stockdetail.html', {'stock' : stock})

def vote(request):
	latest_stocks = Stock.objects.order_by('ipo_date')[:20]
	return render(request, 'stockmarket/vote.html', {'latest_stocks' : latest_stocks})

def buy(request, stock_id):
    stock_choice = get_object_or_404(Stock, pk=stock_id)

    stock_choice.transactions += 1
    stock_choice.value += 1
    stock_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('stockmarket:index'))
def sell(request, stock_id):
    stock_choice = get_object_or_404(Stock, pk=stock_id)

    stock_choice.transactions += 1
    stock_choice.value -= 1
    stock_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('stockmarket:index'))

def newsubmission(request):
    newstock = Stock(
        stock_name= request.POST['new_name'],
        stock_code= request.POST['new_code'],
        ipo_date = timezone.now()
        )
    newstock.save()

    return HttpResponseRedirect(reverse('stockmarket:index'))



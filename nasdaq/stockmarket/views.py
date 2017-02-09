from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from stockmarket.models import Stock
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.core.urlresolvers import reverse
from django.urls import reverse



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
	latest_stocks = Stock.objects.order_by('ipo_date')[:5]
	return render(request, 'stockmarket/vote.html', {'latest_stocks' : latest_stocks})

def buyandsell(request, stock_id):
    stock_choice = get_object_or_404(Stock, pk=stock_id)
    try:
        selected_choice = stock_choice.get(pk=request.POST['stock_choice'])
    except (KeyError, Stock.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'stock/vote.html', {
            'latest_stocks': latest_stocks,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.value += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('stockmarket:index'))




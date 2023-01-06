from django.db.models import Sum, Count, Q
from wb_app.models import Goods, OrderFeedWeekly


def create_orders_30(dict_dates):
    dict_out = dict()

    records = Goods.objects.all().values()
    for item in records:
        barcode = item['barcode']
        temp = {'barcode': barcode, 'sales_period_1': 0, 'sales_period_3': 0, 'sales_period_7': 0, 'sales_period_30': 0,
                'inday_period_1': 0, 'inday_period_3': 0, 'inday_period_7': 0, 'inday_period_30': 0}


        period_30 = OrderFeedWeekly.objects.filter(barcode=barcode, dateOrder__lte=dict_dates['first'], dateOrder__gte=dict_dates['last_30'],
                                                   selfBay='').aggregate(Count('barcode'), sales_status=Count('barcode', filter=Q(status='Выкуплен')),
                                                                         sum_logistics=Sum('logisticFloat', filter=Q(status='Выкуплен')),
                                                                         sum_costprice=Sum('costPriceFloat', filter=Q(status='Выкуплен')))


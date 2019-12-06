from IPython.core.magics.config import reg
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from models import MDtbOrder, MDtbOrderCheck

admin.site.index_title = '欢迎使用minana订单管理系统'
admin.site.site_title = 'minana_orders'
admin.site.site_header = 'minana订单管理系统'


@admin.register(MDtbOrder)
class MDtbOrderAdmin(admin.ModelAdmin):
    list_per_page = 15  # 每页显示多少条数据
    list_display = ['order_id', 'shelf_name', 'quantity', 'status', 'customer_name', 'remark',
                    'payment_method', 'create_date', 'update_date', 'del_flag']  # 展示字段
    ordering = ['order_id']  # ordering设置默认排序字段，负号表示降序排序
    list_filter = ['status']  # 过滤器
    search_fields = ['order_id', 'shelf_name', 'quantity', 'payment_method']  # 搜索


@admin.register(MDtbOrderCheck)
class MDtbOrderCheckAdmin(admin.ModelAdmin):
    list_per_page = 15  # 每页显示多少条数据
    list_display = ['name', 'state', 'create_date']  # 展示字段
    ordering = ['name']  # ordering设置默认排序字段，负号表示降序排序
    list_filter = ['state']  # 过滤器
    search_fields = ['name']  # 搜索
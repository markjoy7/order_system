# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MDtbOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    shelf_name = models.CharField(max_length=60, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    ready_quantity = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    del_flag = models.IntegerField()
    daying_flg = models.IntegerField()

    class Meta:
        # # managed = False
        db_table = 'm_dtb_order'


class MDtbOrderCheck(models.Model):
    name = models.CharField(max_length=50)
    state = models.IntegerField()
    create_date = models.DateTimeField()

    class Meta:
        # # managed = False
        db_table = 'm_dtb_order_check'


class MDtbOrderDetail(models.Model):
    order_id = models.IntegerField()
    taobao_order_id = models.BigIntegerField(blank=True, null=True)
    shipment_num = models.TextField(blank=True, null=True)
    uuid_sku = models.CharField(max_length=150)
    orderid_uuid_sku = models.CharField(unique=True, max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()
    rebuy = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    del_flag = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_order_detail'


class MDtbOrderEntryLog(models.Model):
    product_id = models.IntegerField()
    shelf_name = models.CharField(max_length=255)
    create_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_order_entry_log'


class MDtbOrderPeihuo(models.Model):
    order_id = models.IntegerField()
    orderid_uuid_sku = models.CharField(unique=True, max_length=255)
    uuid_sku = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_order_peihuo'


class MDtbProductSku(models.Model):
    uuid = models.CharField(max_length=100, blank=True, null=True)
    uuid_sku = models.CharField(unique=True, max_length=150)
    stock = models.IntegerField()
    type = models.IntegerField()
    orders_hold = models.IntegerField(blank=True, null=True)
    quantity_unreceived = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    del_flag = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_product_sku'


class MDtbSameContactOrders(models.Model):
    contact = models.CharField(primary_key=True, max_length=255)
    order_id = models.IntegerField(blank=True, null=True)
    order_ids = models.CharField(max_length=255, blank=True, null=True)
    order_count = models.IntegerField(blank=True, null=True)
    product_count = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    del_flag = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_same_contact_orders'


class MDtbShelf(models.Model):
    name = models.CharField(max_length=60)
    size = models.IntegerField(blank=True, null=True)
    is_empty = models.IntegerField()
    del_flag = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_shelf'


class MDtbStockShelf(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_stock_shelf'


class MDtbUuidSkuTag(models.Model):
    uuid_sku = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    shelf_name = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_uuid_sku_tag'


class MDtbYundan(models.Model):
    id = models.BigAutoField(primary_key=True)
    shipment_num = models.CharField(unique=True, max_length=100)
    taobao_order_id = models.BigIntegerField(blank=True, null=True)
    reach_date = models.DateTimeField(blank=True, null=True)
    buyer_message = models.TextField(blank=True, null=True)
    skus = models.TextField(blank=True, null=True)
    sku_quantity = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'm_dtb_yundan'

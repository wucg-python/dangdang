# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddress(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=8, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    tellphone = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_address'


class TBook(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    publisher = models.CharField(max_length=20, blank=True, null=True)
    publish_time = models.DateField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    dang_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    word_number = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    format = models.CharField(max_length=10, blank=True, null=True)
    page = models.CharField(max_length=10, blank=True, null=True)
    impression = models.IntegerField(blank=True, null=True)
    package = models.CharField(max_length=20, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    picture = models.CharField(max_length=1000, blank=True, null=True)
    ed_recomment = models.TextField(blank=True, null=True)
    content_recomment = models.TextField(blank=True, null=True)
    author_brief = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    media_comment = models.TextField(blank=True, null=True)
    sales_nummber = models.IntegerField(blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    launch_time = models.DateField(blank=True, null=True)
    comment_nummber = models.IntegerField(blank=True, null=True)
    cates = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)

    def discount(self):
        dis = self.dang_price/self.price * 10
        return "%.2f" % dis

    class Meta:
        # managed = False
        db_table = 't_book'


class TCar(models.Model):
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_car'


class TCategory(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_category'


class TOrder(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_order'


class TOrderItem(models.Model):
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_order_item'


class TUser(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_user'

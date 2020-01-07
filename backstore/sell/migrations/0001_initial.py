# Generated by Django 2.2.5 on 2020-01-07 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('so_iden', models.CharField(max_length=15, verbose_name='销售订单编号')),
                ('so_serial', models.CharField(max_length=4, verbose_name='流水号')),
                ('so_type', models.IntegerField(choices=[(0, '普通发票'), (1, '退换货')], verbose_name='订单类型')),
                ('so_date', models.DateField(auto_now_add=True, verbose_name='订单日期')),
                ('deliver_ware_house', models.CharField(max_length=20, verbose_name='发货仓库名字')),
                ('deliver_ware_house_iden', models.CharField(max_length=6, verbose_name='发货仓库编码')),
                ('so_remarks', models.TextField(max_length=400, verbose_name='订单备注')),
                ('so_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='销售订单状态')),
                ('so_creator', models.CharField(max_length=20, verbose_name='订单创建人名字')),
                ('so_creator_iden', models.CharField(max_length=20, verbose_name='订单创建人编码')),
                ('so_createDate', models.DateTimeField(auto_now_add=True, verbose_name='订单创建日期')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_so', to='base.Customer', verbose_name='客户')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_so', to='base.Organization', verbose_name='组织')),
            ],
            options={
                'verbose_name': '销售订单',
            },
        ),
        migrations.CreateModel(
            name='SoDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sod_num', models.IntegerField(verbose_name='销售数量')),
                ('sod_taxRate', models.IntegerField(default=13, null=True, verbose_name='税率')),
                ('sod_tax_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='含税单价')),
                ('sod_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='无税单价')),
                ('sod_tax_sum', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='含税总额')),
                ('sod_sum', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='无税总额')),
                ('sod_tax_price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='税金总额')),
                ('sod_remarks', models.TextField(max_length=200, null=True, verbose_name='订单明细备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_sod', to='base.Material', verbose_name='物料')),
                ('sell_order', models.ForeignKey(on_delete=models.Model, related_name='so_sod', to='sell.SellOrder', verbose_name='销售订单')),
            ],
            options={
                'verbose_name': '销售订单明细',
            },
        ),
    ]

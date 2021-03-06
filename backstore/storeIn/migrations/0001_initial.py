# Generated by Django 2.2.5 on 2020-01-10 13:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_auto_20200110_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyInStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bis_iden', models.CharField(max_length=15, verbose_name='入库单编号')),
                ('bis_serial', models.CharField(max_length=4, verbose_name='入库单流水号')),
                ('bis_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='采购入库日期')),
                ('bis_remarks', models.TextField(max_length=400, verbose_name='采购入库单备注')),
                ('bis_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], default=0, verbose_name='采购入库单状态')),
                ('bis_creator', models.CharField(max_length=20, verbose_name='采购入库单创建人名字')),
                ('bis_creator_iden', models.CharField(max_length=20, verbose_name='采购入库单创建人工号')),
                ('bis_createDate', models.DateTimeField(auto_now_add=True, verbose_name='采购入库单创建日期')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_bis', to='base.Organization', verbose_name='组织')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_bis', to='base.Supplier', verbose_name='供应商')),
                ('totalwarehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_ware_house_bis', to='base.TotalWareHouse', verbose_name='总仓')),
            ],
            options={
                'verbose_name': '材料出库单',
            },
        ),
        migrations.CreateModel(
            name='BisDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bd_paper_num', models.IntegerField(verbose_name='应入库数量')),
                ('bd_real_num', models.IntegerField(verbose_name='实际入库数量')),
                ('bd_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税单价')),
                ('bd_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税总额')),
                ('po_iden', models.CharField(max_length=15, verbose_name='采购订单号')),
                ('pr_iden', models.CharField(max_length=15, verbose_name='请购订单号')),
                ('buy_in_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bis_bd', to='storeIn.BuyInStore', verbose_name='采购入库单')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_bd', to='base.Material', verbose_name='物料')),
            ],
            options={
                'verbose_name': '采购入库单明细',
            },
        ),
    ]

from django.db import models

class tbl_account(models.Model):
    acc_id=models.CharField(primary_key=True,max_length=100)
    acc_name=models.CharField(max_length=100)
    acc_district=models.CharField(max_length=100)
    acc_place=models.CharField(max_length=100)
    acc_category=models.CharField(max_length=100)
    acc_phone=models.CharField(max_length=100)
    acc_email=models.CharField(max_length=100)
    acc_remark=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_account"

class idgen(models.Model):
    aid=models.IntegerField()
    oid=models.IntegerField()
    nid=models.IntegerField()
    vid=models.IntegerField()
    uid=models.IntegerField()
    cid=models.IntegerField()
    clid=models.IntegerField()
    tid=models.IntegerField()
    class Meta:
        db_table="idgen"

class tbl_organization(models.Model):
    org_id=models.CharField(primary_key=True,max_length=100)
    org_name=models.CharField(max_length=100)
    org_city=models.CharField(max_length=100)
    org_location=models.CharField(max_length=100)
    org_phone=models.CharField(max_length=100)
    org_email=models.CharField(max_length=100)
    org_category=models.CharField(max_length=100)
    org_contact_person_name=models.CharField(max_length=100)
    org_license_no=models.CharField(max_length=100)
    org_status=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_organization"

class tbl_notification(models.Model):
    not_id=models.CharField(primary_key=True,max_length=100)
    not_athority=models.CharField(max_length=100)
    not_data=models.CharField(max_length=200)
    not_date=models.CharField(max_length=100)
    not_status=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_notification"

class tbl_visitor(models.Model):
    vis_id=models.CharField(primary_key=True,max_length=100)
    org_id=models.ForeignKey(tbl_organization,on_delete=models.CASCADE)
    vis_name=models.CharField(max_length=100)
    vis_phone=models.CharField(max_length=100)
    vis_email=models.CharField(max_length=100)
    vis_date=models.CharField(max_length=100)
    vis_time=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_visitor"

class tbl_complaint(models.Model):
    comp_id=models.CharField(primary_key=True,max_length=100)
    comp_data=models.CharField(max_length=100)
    comp_date=models.CharField(max_length=100)
    comp_name=models.CharField(max_length=100)
    comp_address=models.CharField(max_length=100)
    comp_phone=models.CharField(max_length=100)
    comp_status=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_complaint"

class tbl_test_campaign(models.Model):
    test_id=models.CharField(primary_key=True,max_length=100)
    test_city=models.CharField(max_length=100)
    test_venue=models.CharField(max_length=100)
    test_time=models.CharField(max_length=100)
    test_date=models.CharField(max_length=100)
    test_remark=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_test_campaign"

class tbl_contact_list(models.Model):
    cont_id=models.CharField(primary_key=True,max_length=100)
    org_id=models.ForeignKey(tbl_organization,on_delete=models.CASCADE)
    cont_name=models.CharField(max_length=100)
    cont_phone=models.CharField(max_length=100)
    cont_email=models.CharField(max_length=100)
    cont_date=models.CharField(max_length=100)
    cont_time=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_contact_list"

class tbl_login(models.Model):
    user_name=models.CharField(primary_key=True,max_length=100)
    pwd=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_login"
# Create your models here.

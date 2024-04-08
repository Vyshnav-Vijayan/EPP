from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from app.models import tbl_account,idgen,tbl_notification,tbl_organization,tbl_visitor,tbl_complaint,tbl_test_campaign,tbl_contact_list,tbl_login
def index(request):
    return render(request,"index.html")
def head(request):
    return render(request,"head_section.html")
def contact(request):
    return render(request,"contact.html")
def tbl(request):
    return render(request,"table_view.html")
def vmb(request):
    return render(request,"vertical_menubar.html")


#Admin section

def admin_home(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"admin_home.html")
def admin_menu_bar(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"admin_menu_bar.html")

def add_account(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"add_account.html")
def add_account2(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.aid)
            a=a+1
            a1="ACC"+str(a)
            obj=tbl_account()
            obj.acc_id=a1
            obj.acc_name=request.POST.get('account_name')
            obj.acc_district=request.POST.get('account_district')
            obj.acc_place=request.POST.get('account_place')
            obj.acc_category=request.POST.get('account_category')
            obj.acc_phone=request.POST.get('account_phone')
            obj.acc_email=request.POST.get('account_email')
            obj.acc_remark=request.POST.get('account_remark')
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.aid=a
            objid1.save()
            data2=tbl_login()
            data2.user_name=a1
            data2.pwd=request.POST.get('account_phone')
            data2.category=request.POST.get('account_category')
            data2.save()
        return render(request,"add_account.html")

def remove_account(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_account.objects.all()
        return render(request,"remove_account.html",{'d':obj})
def remove_account2(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_account.objects.get(acc_id=id1)
        obj.delete()
        return redirect("/remove_account")

def update_account(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_account.objects.all()
        return render(request,"update_account.html",{'d':obj})
def update_account2(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_account.objects.get(acc_id=id1)
        return render(request,"update_account2.html",{'d':obj})
def update_account3(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            obj=tbl_account.objects.get(acc_id=id1)
            obj.acc_id=request.POST.get('account_id')
            obj.acc_name=request.POST.get('account_name')
            obj.acc_district=request.POST.get('account_district')
            obj.acc_place=request.POST.get('account_place')
            obj.acc_category=request.POST.get('account_category')
            obj.acc_phone=request.POST.get('account_phone')
            obj.acc_email=request.POST.get('account_email')
            obj.acc_remark=request.POST.get('account_remark')
            obj.save()
            return redirect("/update_account")

def add_notification(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"add_notification.html")
def add_notification2(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.nid)
            a=a+1
            a1="NOT"+str(a)
            obj=tbl_notification()
            obj.not_id=a1
            obj.not_athority=request.POST.get('notification_authority')
            obj.not_data=request.POST.get('notification_data')
            obj.not_date=request.POST.get('notification_date')
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.nid=a
            objid1.save()
        return render(request,"add_notification.html")

def remove_notification(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_notification.objects.all()
        return render(request,"remove_notification.html",{'d':obj})
def remove_notification2(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_notification.objects.get(not_id=id1)
        obj.delete()
        return redirect("/remove_notification")

def add_organization(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"add_organization.html")
def add_organization2(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.oid)
            a=a+1
            a1="ORG"+str(a)
            obj=tbl_organization()
            obj.org_id=a1
            obj.org_name=request.POST.get('organization_name')
            obj.org_city=request.POST.get('organization_city')
            obj.org_location=request.POST.get('organization_location')
            obj.org_phone=request.POST.get('organization_phone')
            obj.org_email=request.POST.get('organization_email')
            obj.org_category=request.POST.get('organization_category')
            obj.org_contact_person_name=request.POST.get('organization_contact_person_name')
            obj.org_license_no=request.POST.get('organization_license_no')
            obj.org_status="verified"
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.oid=a
            objid1.save()
            data2=tbl_login()
            data2.user_name=a1
            data2.pwd=request.POST.get('organization_phone')
            data2.category=request.POST.get('organization_category')
            data2.save()
        return render(request,"add_organization.html")
def remove_organization(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.all()
        return render(request,"remove_organization.html",{'d':obj})
def remove_organization2(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.get(org_id=id1)
        obj.delete()
        obj1=tbl_login.objects.get(user_name=id1)
        obj1.delete()
        return redirect("/remove_organization")
def update_organization(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.all()
        return render(request,"update_organization.html",{'d':obj})
def update_organization2(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.get(org_id=id1)
        return render(request,"update_organization2.html",{'d':obj})
def update_organization3(request,id1):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            obj=tbl_organization.objects.get(org_id=id1)
            obj.org_name=request.POST.get('organization_name')
            obj.org_city=request.POST.get('organization_city')
            obj.org_location=request.POST.get('organization_location')
            obj.org_phone=request.POST.get('organization_phone')
            obj.org_email=request.POST.get('organization_email')
            obj.org_category=request.POST.get('organization_category')
            obj.org_contact_person_name=request.POST.get('organization_contact_person_name')
            obj.org_license_no=request.POST.get('organization_license_no')
            obj.save()
        return redirect("/update_organization")

def verify_organization(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.filter(org_status="notverified")
        return render(request,"verify_organization.html",{'d':obj})

def acceptorg(request,id):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        data=tbl_organization.objects.get(org_id=id)
        data.org_status="verified"
        data.save()
        return redirect('/verify_organization')
def rejectorg(request,id):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        data=tbl_organization.objects.get(org_id=id)
        data.org_status="rejected"
        data.save()
        return redirect('/verify_organization')

def view_complaint(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_complaint.objects.all()
        return render(request,"view_complaint.html",{'d':obj})

def admin_report1(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.all()
        return render(request,"admin_report1.html",{'d':obj})
def admin_report2(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_contact_list.objects.all()
        return render(request,"admin_report2.html",{'d':obj})

# public section

def public_menu_bar(request):
    return render(request,"public_menu_bar.html")
def public_add_organization(request):
    return render(request,"public_add_organization.html")
def public_add_organization2(request):
    if request.method=='POST':
        objid=idgen.objects.get(id=1)
        a=int(objid.oid)
        a=a+1
        a1="ORG"+str(a)
        obj=tbl_organization()
        obj.org_id=a1
        obj.org_name=request.POST.get('organization_name')
        obj.org_city=request.POST.get('organization_city')
        obj.org_location=request.POST.get('organization_location')
        obj.org_phone=request.POST.get('organization_phone')
        obj.org_email=request.POST.get('organization_email')
        obj.org_category=request.POST.get('organization_category')
        obj.org_contact_person_name=request.POST.get('organization_contact_person_name')
        obj.org_license_no=request.POST.get('organization_license_no')
        obj.org_status="notverified"
        obj.save()
        objid1=idgen.objects.get(id=1)
        objid1.oid=a
        objid1.save()
    return render(request,"public_add_organization.html")

def public_view_organization(request):
    obj=tbl_organization.objects.all()
    return render(request,"public_view_organization.html",{'d':obj})
def public_search_organization(request):
    return render(request,"public_search_organization.html")
def public_search_organization2(request):
    data=request.POST.get('organization_name')
    if data:
        result=tbl_organization.objects.filter(org_name__icontains=data)
        if result:
            return render(request,"public_search_organization.html",{'d':result})
        else:
            return HttpResponse("No Data!!!")
    else:
        return HttpResponse("No Organizaion")
        
def public_view_notification(request):
    obj=tbl_notification.objects.all()
    return render(request,"public_view_notification.html",{'d':obj})

def public_add_complaint(request):
    return render(request,"public_add_complaint.html")
def public_add_complaint2(request):
    if request.method=='POST':
        objid=idgen.objects.get(id=1)
        a=int(objid.cid)
        a=a+1
        a1="COMP"+str(a)
        obj=tbl_complaint()
        obj.comp_id=a1
        obj.comp_data=request.POST.get('complaint_data')
        obj.comp_date=request.POST.get('complaint_date')
        obj.comp_name=request.POST.get('complaint_name')
        obj.comp_address=request.POST.get('complaint_address')
        obj.comp_phone=request.POST.get('complaint_phone')
        obj.comp_status="accepted"
        obj.save()
        objid1=idgen.objects.get(id=1)
        objid1.cid=a
        objid1.save()
    return render(request,"public_add_complaint.html")

def public_login(request):
    return render(request,"public_login.html")

def public_login2(request):
    data=tbl_login.objects.all()
    if request.method == 'POST':
        u=request.POST.get('log_id')  
        p=request.POST.get('password')
        flag=0
        for da in data:
            if u==da.user_name and p==da.pwd:
                type=da.category
                flag=1
                if type=="health":
                    request.session['hid']=u
                    return redirect('/health_home')
                elif type=="police":
                    request.session['pid']=u
                    return redirect('/police_home')
                elif type=="organization":
                    request.session['oid']=u
                    return redirect('/organization_home')
                elif type=="admin":
                    request.session['aid']=u
                    return redirect('/admin_home')
                else:
                    return render(request,"public_login.html", {'error': "Invalid"})  
                    #return HttpResponse("Invalid")
        if flag==0:
            #return HttpResponse("user doesn't exist")  
            return render(request,"public_login.html", {'error': "Invalid username or password"})
        
def admin_logout(request):
    if 'aid' not in request.session:
        return render(request,"index.html")
    else:
        del request.session['aid']
        return render(request,"index.html")
def health_logout(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        del request.session['hid']
        return render(request,"index.html")
def police_logout(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        del request.session['pid']
        return render(request,"index.html")
def organization_logout(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        del request.session['oid']
        return render(request,"index.html")

        


# organization section

def organization_home(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"organization_home.html")
def organization_menu_bar(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"organization_menu_bar.html")
def organization_add_visitor(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        s=request.session['oid']
        return render(request,"organization_add_visitor.html",{'data':s})
def organization_add_visitor2(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.vid)
            a=a+1
            a1="VIS"+str(a)
            obj=tbl_visitor()
            obj.vis_id=a1
            obj.org_id_id=request.POST.get('organization_id')
            obj.vis_name=request.POST.get('visitor_name')
            obj.vis_phone=request.POST.get('visitor_phone')
            obj.vis_email=request.POST.get('visitor_email')
            obj.vis_date=request.POST.get('visitor_date')
            obj.vis_time=request.POST.get('visitor_time')
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.vid=a
            objid1.save()
            s1=request.session['oid']
            return render(request,"organization_add_visitor.html",{'data':s1})
def organization_view_visitor(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"organization_view_visitor.html")
def organization_view_visitor2(request):
    if 'oid' not in request.session:
        return render(request,"index.html")
    else:
        data=request.POST.get('visitor_date')
        if data:
            result=tbl_visitor.objects.filter(vis_date__icontains=data).filter(org_id_id=request.session['oid'])
            if result:
                return render(request,"organization_view_visitor.html",{'d':result})
            else:
                return HttpResponse("No visitors on this time!!!")
        else:
            return HttpResponse("Date not selected")

# health section

def health_home(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"health_home.html")
def health_menu_bar(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"health_menu_bar.html")
def health_add_notification(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"health_add_notification.html")
def health_add_notification2(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.nid)
            a=a+1
            a1="NOT"+str(a)
            obj=tbl_notification()
            obj.not_id=a1
            obj.not_athority=request.POST.get('notification_authority')
            obj.not_data=request.POST.get('notification_data')
            obj.not_date=request.POST.get('notification_date')
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.nid=a
            objid1.save()
        return render(request,"health_add_notification.html")
def health_remove_notification(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_notification.objects.all()
        return render(request,"health_remove_notification.html",{'d':obj})
def health_remove_notification2(request,id1):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_notification.objects.get(not_id=id1)
        obj.delete()
        return redirect("/health_remove_notification")
def health_add_test_campaign(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"health_add_test_campaign.html")
def health_add_test_campaign2(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.tid)
            a=a+1
            a1="TEST"+str(a)
            obj=tbl_test_campaign()
            obj.test_id=a1
            obj.test_city=request.POST.get('test_campaign_city')
            obj.test_venue=request.POST.get('test_campaign_venue')
            obj.test_time=request.POST.get('test_campaign_time')
            obj.test_date=request.POST.get('test_campaign_date')
            obj.test_remark=request.POST.get('test_campaign_remark')
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.tid=a
            objid1.save()
        return render(request,"health_add_test_campaign.html")
def health_remove_test_campaign(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_test_campaign.objects.all()
        return render(request,"health_remove_test_campaign.html",{'d':obj})
def health_remove_test_campaign2(request,id1):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_test_campaign.objects.get(test_id=id1)
        obj.delete()
        return redirect("/health_remove_test_campaign")
def health_update_test_campaign(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_test_campaign.objects.all()
        return render(request,"health_update_test_campaign.html",{'d':obj})
def health_update_test_campaign2(request,id1):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_test_campaign.objects.get(test_id=id1)
        return render(request,"health_update_test_campaign2.html",{'d':obj})
def health_update_test_campaign3(request,id1):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            obj=tbl_test_campaign.objects.get(test_id=id1)
            obj.test_city=request.POST.get('test_campaign_city')
            obj.test_venue=request.POST.get('test_campaign_venue')
            obj.test_time=request.POST.get('test_campaign_time')
            obj.test_date=request.POST.get('test_campaign_date')
            obj.test_remark=request.POST.get('test_campaign_remark')
            obj.save()
        return redirect("/health_update_test_campaign")

def health_search_organization(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"health_search_organization.html")

def health_search_organization2(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        data=request.POST.get('organization_name')
        if data:
            result=tbl_organization.objects.filter(org_name__icontains=data)
            if result:
                return render(request,"health_search_organization.html",{'d':result})
            else:
                return HttpResponse("No Data!!!")
def health_search_organization3(request,id1):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.get(org_id=id1)
        return render(request,"health_search_organization2.html",{'d':obj})
def health_search_organization4(request):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            obj_id=request.POST.get('organization_id')
            obj_date=request.POST.get('visitor_date')
            request.session['a1']=obj_id
            request.session['a2']=obj_date
            data=tbl_visitor.objects.filter(org_id_id=obj_id).filter(vis_date=obj_date)
            return render(request,"health_search_organization3.html",{'d':data})


# police section

def police_home(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"police_home.html")
def police_menu_bar(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"police_menu_bar.html")

def police_add_notification(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"police_add_notification.html")
def police_add_notification2(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            objid=idgen.objects.get(id=1)
            a=int(objid.nid)
            a=a+1
            a1="NOT"+str(a)
            obj=tbl_notification()
            obj.not_id=a1
            obj.not_athority=request.POST.get('notification_authority')
            obj.not_data=request.POST.get('notification_data')
            obj.not_date=request.POST.get('notification_date')
            obj.save()
            objid1=idgen.objects.get(id=1)
            objid1.nid=a
            objid1.save()
        return render(request,"police_add_notification.html")
def police_remove_notification(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_notification.objects.all()
        return render(request,"police_remove_notification.html",{'d':obj})
def police_remove_notification2(request,id1):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_notification.objects.get(not_id=id1)
        obj.delete()
        return redirect("/police_remove_notification")

def police_search_organization(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        return render(request,"police_search_organization.html")
def police_search_organization2(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        data=request.POST.get('organization_name')
        if data:
            result=tbl_organization.objects.filter(org_name__icontains=data)
            if result:
                return render(request,"police_search_organization.html",{'d':result})
            else:
                return HttpResponse("No Data!!!")
def police_search_organization3(request,id1):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_organization.objects.get(org_id=id1)
        return render(request,"police_search_organization2.html",{'d':obj})
def police_search_organization4(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        if request.method=='POST':
            obj_id=request.POST.get('organization_id')
            obj_date=request.POST.get('visitor_date')
            request.session['a1']=obj_id
            request.session['a2']=obj_date
            data=tbl_visitor.objects.filter(org_id_id=obj_id).filter(vis_date=obj_date)
            return render(request,"police_search_organization3.html",{'d':data})
    
def police_view_contact_list(request):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        obj=tbl_contact_list.objects.all()
        return render(request,"police_view_contact_list.html",{'d':obj})
    

def contactlist(request,id1):
    if 'pid' not in request.session:
        return render(request,"index.html")
    else:
        objid=idgen.objects.get(id=1)
        a=int(objid.clid)
        a=a+1
        a1="CONT"+str(a)
        data=tbl_visitor.objects.get(vis_id=id1)
        data2=tbl_contact_list()
        data2.cont_id=a1
        data2.org_id_id=data.org_id_id
        data2.cont_name=data.vis_name
        data2.cont_phone=data.vis_phone
        data2.cont_email=data.vis_email
        data2.cont_date=data.vis_date
        data2.cont_time=data.vis_time
        data2.save()
        objid1=idgen.objects.get(id=1)
        objid1.clid=a
        objid1.save()
        send_mail('Department of Hospital Management','We detected that you passed through an epidemic desease area so, this is to notify that you need to check up your body at your nearest health center as soon as possible.','from@example.co',[data.vis_email,])
        data=tbl_visitor.objects.filter(org_id_id=request.session['a1']).filter(vis_date=request.session['a2'])
        return render(request,"police_search_organization3.html",{'d':data})
    
        
def contactlist2(request,id1):
    if 'hid' not in request.session:
        return render(request,"index.html")
    else:
        objid=idgen.objects.get(id=1)
        a=int(objid.clid)
        a=a+1
        a1="CONT"+str(a)
        data=tbl_visitor.objects.get(vis_id=id1)
        data2=tbl_contact_list()
        data2.cont_id=a1
        data2.org_id_id=data.org_id_id
        data2.cont_name=data.vis_name
        data2.cont_phone=data.vis_phone
        data2.cont_email=data.vis_email
        data2.cont_date=data.vis_date
        data2.cont_time=data.vis_time
        data2.save()
        objid1=idgen.objects.get(id=1)
        objid1.clid=a
        objid1.save()
        send_mail('Department of Hospital Management','We detected that you passed through an epidemic desease area so, this is to notify that you need to check up your body at your nearest health center as soon as possible.','from@example.co',[data.vis_email,])
        data=tbl_visitor.objects.filter(org_id_id=request.session['a1']).filter(vis_date=request.session['a2'])
        return render(request,"health_search_organization3.html",{'d':data})
# Create your views here.

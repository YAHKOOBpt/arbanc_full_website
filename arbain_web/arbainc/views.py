from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Land_acq,Plot_dev,Residential_villa,Commercial,Food,Spices,Cosmetics,Bg_export,Health_care,Bg_health,Start_constr,Start_finance,img_consulting,StratUp,Construction,Infrastructure,Client,Home_heading,Mining
import os
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    main_head =Home_heading.objects.all()

    exp_Food=Food.objects.all()
    exp_spices=Spices.objects.all()
    exp_Cosmetic=Cosmetics.objects.all()

    startup_constr = Start_constr.objects.all()
    startup_finanace =Start_finance.objects.all()

    consulting_Bg_img = img_consulting.objects.all()

    health_care = Health_care.objects.all()

    client = Client.objects.all()

    invst_startup=StratUp.objects.all()
    invst_Infrast=Infrastructure.objects.all()

    land =Land_acq.objects.all()
    plot =Plot_dev.objects.all()
    residential=Residential_villa.objects.all()
    Commercial_vila=Commercial.objects.all()

    bg_expor=Bg_export.objects.all()
    bg_heal=Bg_health.objects.all()

    



    context ={
        'main_head':main_head,
        'exp_Food':exp_Food,
        'exp_spices':exp_spices,
        'exp_Cosmetic':exp_Cosmetic,

        'startup_constr':startup_constr,
        'startup_finanace':startup_finanace,

        'consulting_Bg_img':consulting_Bg_img,

        'health_care':health_care,

        'client':client,

        'invst_startup':invst_startup,
        'invst_Infrast':invst_Infrast,

        'land':land,
        'plot':plot,
        'residential':residential,
        'Commercial_vila':Commercial_vila,

        'bg_expor':bg_expor,
        'bg_heal':bg_heal,


    }
    return render(request,'user/index.html',context)

# user consulting section start 

def User_consult(request):
    startup_constr = Start_constr.objects.all()
    startup_finanace =Start_finance.objects.all()

    consulting_Bg_img = img_consulting.objects.all()

    context={
        'startup_constr':startup_constr,
        'startup_finanace':startup_finanace,

        'consulting_Bg_img':consulting_Bg_img,
    }
    return render(request,'user/consulting.html',context)


# user consulting section ends


# user investment section start

def User_startup(request):
    start = StratUp.objects.all()
    context={
        'start':start
    }
    return render(request,'user/inv_startup.html',context)

def User_Infranstructor(request):
    infra = Infrastructure.objects.all()
    context={
        'infra':infra
    }
    return render(request,'user/inv_infrastr.html',context)

def User_Construction(request):
    constr = Construction.objects.all()
    context={
        'constr':constr
    }
    return render(request,'user/inv_construction.html',context)

def User_Investment(request):
    invest = Construction.objects.all()
    context={
        'invest':invest
    }
    return render(request,'user/investment.html',context)

def User_mining(request):
    mine =Mining.objects.all()
    context={
        'mine':mine
    }
    return render(request,'user/mining.html',context)

# user investment section end 


# user realty section start 

def User_realty(request):
    land =Land_acq.objects.all()
    plot =Plot_dev.objects.all()
    residential=Residential_villa.objects.all()
    Commercial_vila=Commercial.objects.all()

    context ={
        'land':land,
        'plot':plot,
        'residential':residential,
        'Commercial_vila':Commercial_vila,
    }

    return render(request,'user/realty.html',context)

def User_land(request):
    land = Land_acq.objects.all()
    context ={
        'land':land
    }
    return render(request,'user/land_1.html',context)

def User_plot(request):
    Plot = Plot_dev.objects.all()
    context ={
        'Plot':Plot
    }
    return render(request,'user/plot_1.html',context)

def User_residential(request):
    Residential = Residential_villa.objects.all()
    context ={
        'Residential':Residential
    }
    return render(request,'user/residential_1.html',context)

def User_commercial(request):
    commercial = Commercial.objects.all()
    context ={
        'commercial':commercial
    }
    return render(request,'user/commercial_1.html',context)

# user realty section ends

# user export section start 
def User_export(request):
    export_food = Food.objects.all()
    export_spices = Spices.objects.all()
    export_cosmetic= Cosmetics.objects.all()

    bg_expor=Bg_export.objects.all()
    context ={
        'export_food':export_food,
        'export_spices':export_spices,
        'export_cosmetic':export_cosmetic,
        'bg_expor':bg_expor
        
    }
    return render(request,'user/export.html',context)

# user export section ends 

# user health care section start 

def User_health(request):
    health = Health_care.objects.all()
    
    context ={
        'health':health,
    }
    return render(request,'user/health_care.html',context)


# user health care section end


def client(request):
    client = Client.objects.all()
    context={
        'client':client
    }
    return render(request,'user/our_clients.html',context)


################################    ###################################


def arbainclogin(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request,user)
               return redirect("arbain_admin")
          else:
               messages.info(request,'Username or password incorrect')
               return redirect('arbainclogin')


     return render(request,'admi/arbainclogin.html')


def SignOut(request):
     logout(request)
     return redirect('arbainclogin')




@login_required(login_url='login')
def home(request):
    return render(request,'admi/index.html')



# def base(request):
#     base1=Land_acq.objects.all()

#     context={'base1':base1}
#     return render(request,'admi/base.html',context)


# start manage realty

def adm_land(request):
    land=Land_acq.objects.all()
    if request.method == "POST":
        Item = Land_acq()
        Item.title = request.POST.get('heading')
        Item.description = request.POST.get('description')
        if len(request.FILES) != 0:
            Item.image = request.FILES['img']
            Item.image_1 = request.FILES['img_1']
            Item.image_2 = request.FILES['img_2']
        Item.save()
        messages.success(request,"successfully complited")
        return redirect('adm_land') 
    context={'land':land}   

    return render(request,'admi/Land_acquisition.html',context)

def edit_land(request,pk):
    edt_land =Land_acq.objects.get(id=pk)

    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_land.image) > 0:
                os.remove(edt_land.image.path)
            edt_land.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_land.image_1) > 0:
                os.remove(edt_land.image_1.path)
            edt_land.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_land.image_2) > 0:
                os.remove(edt_land.image_2.path)
            edt_land.image_2 = request.FILES['img_2']

        edt_land.title=request.POST.get('heading')
        edt_land.description=request.POST.get('description')
        edt_land.save() 
        messages.success(request,"update successfully")
        return redirect('adm_land')  
    context={'edt_land':edt_land}
    
    return render(request,'admi/edit_land.html',context)

def delete_land(request,pk):
    del_land=Land_acq.objects.filter(id=pk)
    del_land.delete()
    return redirect('adm_land')



def adm_plot(request):
    plot =Plot_dev.objects.all()
    if request.method == 'POST':
        Plot = Plot_dev()
        Plot.title= request.POST.get("heading")
        Plot.description=request.POST.get("description")
        if len(request.FILES)!= 0:
            Plot.image=request.FILES["img"]
            Plot.image_1 = request.FILES['img_1']
            Plot.image_2 = request.FILES['img_2']
        Plot.save()
        messages.success(request,"successfully complited")
        return redirect('adm_plot')
    context ={
        'plot':plot
        }
    return render(request,'admi/plot_development.html',context)

def edit_plot(request,pk):
    edt_plot=Plot_dev.objects.get(id=pk)

    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_plot.image) > 0:
                os.remove(edt_plot.image.path)
            edt_plot.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_plot.image_1) > 0:
                os.remove(edt_plot.image_1.path)
            edt_plot.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_plot.image_2) > 0:
                os.remove(edt_plot.image_2.path)
            edt_plot.image_2 = request.FILES['img_2']

        edt_plot.title=request.POST.get('heading')
        edt_plot.description=request.POST.get('description')
        edt_plot.save()
        messages.success(request,"Update successfully")
        return redirect('adm_plot')
    context={
        'edt_plot':edt_plot
        }
    return render(request,'admi/edit_plot.html',context)

def delete_plot(request,pk):
    del_plot =Plot_dev.objects.filter(id=pk)
    del_plot.delete()
    return redirect('adm_plot')




def adm_residential(request):
    resid_villa=Residential_villa.objects.all()
    if request.method == 'POST':
        resid_villa= Residential_villa()
        resid_villa.title=request.POST.get("heading")
        resid_villa.description=request.POST.get("description")
        if len(request.FILES)!= 0:
            resid_villa.image=request.FILES['img']
            resid_villa.image_1 = request.FILES['img_1']
            resid_villa.image_2 = request.FILES['img_2']
        resid_villa.save()
        messages.success(request,"Successfully Complited")
        return redirect('adm_residential')
    context ={'resid_villa':resid_villa}
    return render(request,'admi/Residential_villa.html',context)

def edit_residential(request,pk):
    edt_villa=Residential_villa.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_villa.image) > 0:
                os.remove(edt_villa.image.path)
            edt_villa.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_villa.image_1) > 0:
                os.remove(edt_villa.image_1.path)
            edt_villa.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_villa.image_2) > 0:
                os.remove(edt_villa.image_2.path)
            edt_villa.image_2 = request.FILES['img_2']

        edt_villa.title = request.POST.get('heading')
        edt_villa.description = request.POST.get('description')
        edt_villa.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_residential')

    context={"edt_villa":edt_villa}

    return render(request,'admi/edit_residential.html',context)

def delete_residential(request,pk):
    del_villa =Residential_villa.objects.filter(id=pk)
    del_villa.delete()
    return redirect('adm_residential')



def adm_commercial(request):
    com_office=Commercial.objects.all()
    if request.method == 'POST':
        com_office=Commercial()
        com_office.title=request.POST.get("heading")
        com_office.description=request.POST.get("description")
        if len(request.FILES)!= 0:
            com_office.image=request.FILES['img']
            com_office.image_1 = request.FILES['img_1']
            com_office.image_2 = request.FILES['img_2']
        com_office.save()
        messages.success(request,"Successfully Complited")
        return redirect('adm_commercial')
    context={'com_office':com_office}
    return render(request,'admi/commercial_office.html',context)

def edit_commercial(request,pk):
    edt_office = Commercial.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_office.image) > 0:
                os.remove(edt_office.image.path)
            edt_office.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_office.image_1) > 0:
                os.remove(edt_office.image_1.path)
            edt_office.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_office.image_2) > 0:
                os.remove(edt_office.image_2.path)
            edt_office.image_2 = request.FILES['img_2']
        edt_office.title = request.POST.get('heading')
        edt_office.description = request.POST.get('description')
        edt_office.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_commercial')
    context={'edt_office':edt_office}
    return render(request,'admi/edit_commercial.html',context)

def delete_commercial(request,pk):
    del_office = Commercial.objects.filter(id=pk)
    del_office.delete()
    return redirect('adm_commercial')

# end manage realty




# start manage export 
def adm_food(request):
    food = Food.objects.all()
    if request.method == 'POST':
        food = Food()       
        food.description = request.POST.get('description')
        if len(request.FILES)!= 0:
            food.image=request.FILES['img']
        food.save()
        messages.success(request,'Successfully Complited')
        return redirect('adm_food')
    
    context ={'food':food}
    return render(request,'admi/food.html',context)

def edit_food(request,pk):
    edt_food = Food.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_food.image) > 0:
                os.remove(edt_food.image.path)
            edt_food.image = request.FILES['img']

        edt_food.description = request.POST.get('description')
        edt_food.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_food')
    context = {'edt_food':edt_food}
    return render(request,'admi/edit_food.html',context)

def delete_food(request,pk):
    del_food=Food.objects.filter(id=pk)
    del_food.delete()
    return redirect('adm_food')



def adm_spices(request):
    spice = Spices.objects.all()
    if request.method == "POST":
        spice =Spices()
        spice.description=request.POST.get('description')
        if len(request.FILES)!= 0:
            spice.image=request.FILES['img']
        spice.save()
        messages.success(request,'Successfully Complited')
        return redirect('adm_spices')
    context = {
        'spice': spice
        }
    return render(request,'admi/Spices.html',context)

def edit_spices(request,pk):
    edt_spice=Spices.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_spice.image) > 0:
                os.remove(edt_spice.image.path)
            edt_spice.image = request.FILES['img']

        edt_spice.description = request.POST.get('description')
        edt_spice.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_spices')
    context = {'edt_spice':edt_spice}
    return render(request,'admi/edit_spices.html',context)

def delete_spices(request,pk):
    del_spice=Spices.objects.filter(id=pk)
    del_spice.delete()
    return redirect('adm_spices')



def adm_cosmetic(request):
    cosmetic = Cosmetics.objects.all()
    if request.method == "POST":
        cosmetic =Cosmetics()
        cosmetic.description=request.POST.get('description')
        if len(request.FILES)!= 0:
            cosmetic.image=request.FILES['img']
        cosmetic.save()
        messages.success(request,'Successfully Complited')
        return redirect('adm_cosmetic')
    context = {'cosmetic': cosmetic}
    return render(request,'admi/cosmetics.html',context)

def edit_cosmetic(request,pk):
    edt_cosmetic=Cosmetics.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_cosmetic.image) > 0:
                os.remove(edt_cosmetic.image.path)
            edt_cosmetic.image = request.FILES['img']
        edt_cosmetic.description = request.POST.get('description')
        edt_cosmetic.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_cosmetic')
    context = {'edt_cosmetic':edt_cosmetic}
    return render(request,'admi/edit_cosmetics.html',context)

def delete_cosmetic(request,pk):
    del_cosmetic=Cosmetics.objects.filter(id=pk)
    del_cosmetic.delete()
    return redirect('adm_cosmetic')



def Bg_exports(request):
    img_export=Bg_export.objects.all()
    if request.method == "POST":
        img_export=Bg_export()
        if len(request.FILES)!= 0:
            img_export.image=request.FILES['img']
        img_export.save()
        messages.success(request,"Successfully Complited")
        return redirect('Bg_exports')
    context={'img_export':img_export}
    return render(request,'admi/Export_BGimg.html',context)

def edit_Bg_exports(request,pk):
    edt_img=Bg_export.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(edt_img.image)>0:
                os.remove(edt_img.image.path)
            edt_img.image = request.FILES['img']
        edt_img.save()
        messages.success(request,"Update Successfully")
        return redirect('Bg_exports')
    context={
        'edt_img': edt_img
    }
    return render(request,'admi/edit_Export_Bg.html',context)

def delete_Bg_exports(request,pk):
    del_img=Bg_export.objects.filter(id=pk)
    del_img.delete()
    return redirect('Bg_exports')

# end manage export 

# start manage healthcare

def adm_health(request):
    health=Health_care.objects.all()
    if request.method == "POST":
        health = Health_care()
        
        health.description = request.POST.get('description')
        if len(request.FILES) != 0:
            health.image = request.FILES['img']
            health.image_1 = request.FILES['img_1']
            health.image_2 = request.FILES['img_2']
        health.save()
        messages.success(request,"successfully complited")
        return redirect('adm_health') 
    context={'health':health} 
    return render(request,'admi/Health_Care.html',context)

def edit_health(request,pk):
    edt_health=Health_care.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_health.image) > 0:
                os.remove(edt_health.image.path)
            edt_health.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_health.image_1) > 0:
                os.remove(edt_health.image_1.path)
            edt_health.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_health.image_2) > 0:
                os.remove(edt_health.image_2.path)
            edt_health.image_2 = request.FILES['img_2']        
        edt_health.description=request.POST.get('description')
        edt_health.save()
        messages.success(request,"Update successfully")
        return redirect('adm_health')
    context={'edt_health':edt_health}
    return render(request,'admi/edit_health.html',context)

def delete_health(request,pk):
    del_health = Health_care.objects.filter(id=pk)
    del_health.delete()
    return redirect('adm_health')



def Bg_health_care(request):
    img_health=Bg_health.objects.all()
    if request.method == "POST":
        img_health=Bg_health()
        if len(request.FILES)!= 0:
            img_health.image=request.FILES['img']
        img_health.save()
        messages.success(request,"Successfully Complited")
        return redirect('Bg_exports')
    context={
        'img_health':img_health
        }
    return render(request,'admi/Health_BGimg.html',context)

def edit_Bg_health_care(request,pk):
    edt_Bg_img=Bg_health.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(edt_Bg_img.image)>0:
                os.remove(edt_Bg_img.image.path)
            edt_Bg_img.image = request.FILES['img']
        edt_Bg_img.save()
        messages.success(request,"Update Successfully")
        return redirect('Bg_health_care')
    context={
        'edt_Bg_img': edt_Bg_img
    }   
    return render(request,'admi/edit_Bg_health_care.html',context)

def delete_Bg_health_care(request,pk):
    del_Bg_img=Bg_health.objects.filter(id=pk)
    del_Bg_img.delete()
    return redirect('Bg_health_care')

# end manage healthcare


# start manage consulting

def adm_Startup_const(request):
    construction = Start_constr.objects.all()
    if request.method == "POST":
        construction =Start_constr()
        construction.description=request.POST.get('description')
        construction.save()
        messages.success(request,'Successfully Complited')
        return redirect('adm_Startup_const')
    context = {'construction': construction}
    return render(request,'admi/Startup_construction.html',context)

def edit_Startup_const(request,pk):
    edt_construction=Start_constr.objects.get(id=pk)
    if request.method == "POST":
        edt_construction.description = request.POST.get('description')
        edt_construction.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_Startup_const')
    context = {'edt_construction':edt_construction}
    return render(request,'admi/edit_startup_constru.html',context)

def delete_Startup_const(request,pk):
    del_construction=Start_constr.objects.filter(id=pk)
    del_construction.delete()
    return redirect('adm_Startup_const')



def adm_Startup_finance(request):
    finance = Start_finance.objects.all()
    if request.method == "POST":
        finance =Start_finance()
        finance.description=request.POST.get('description')
        finance.save()
        messages.success(request,'Successfully Complited')
        return redirect('adm_Startup_finance')
    context = {
        'finance': finance
        }
    return render(request,'admi/finance.html',context)

def edit_Startup_finance(request,pk):
    edt_finance=Start_finance.objects.get(id=pk)
    if request.method == "POST":
        edt_finance.description = request.POST.get('description')
        edt_finance.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_Startup_finance')
    context = {'edt_finance':edt_finance}
    return render(request,'admi/edit_finance.html',context)

def delete_Startup_finance(request,pk):
    del_finance=Start_finance.objects.filter(id=pk)
    del_finance.delete()
    return redirect('adm_Startup_finance')


def adm_img_consulting(request):
    img_cons=img_consulting.objects.all()
    if request.method == "POST":
        img_cons=img_consulting()
        if len(request.FILES)!= 0:
            img_cons.image=request.FILES['img']
        img_cons.save()
        messages.success(request,"Successfully Complited")
        return redirect('adm_img_consulting')
    context={
        'img_cons':img_cons
        }
    return render(request,'admi/Consulting_img.html',context)

def edit_img_consulting(request,pk):
    edt_img_cons=img_consulting.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(edt_img_cons.image)>0:
                os.remove(edt_img_cons.image.path)
            edt_img_cons.image = request.FILES['img']
        edt_img_cons.save()
        messages.success(request,"Update Successfully")
        return redirect('adm_img_consulting')
    context={
        'edt_img_cons': edt_img_cons
    }
    return render(request,'admi/edit_img_cosulting.html',context)

def delete_img_consulting(request,pk):
    del_img=img_consulting.objects.filter(id=pk)
    del_img.delete()
    return redirect('adm_img_consulting')

# end manage consulting



# start manage investment 

def adm_StartUp(request):
    startup=StratUp.objects.all()
    if request.method == "POST":
        startup = StratUp()
        
        startup.description = request.POST.get('description')
        if len(request.FILES) != 0:
            startup.image = request.FILES['img']        
            startup.image_1 = request.FILES['img_1']
            startup.image_2 = request.FILES['img_2']
        startup.save()
        messages.success(request,"successfully complited")
        return redirect('adm_StartUp') 
    context={
        'startup':startup
        } 
    return render(request,'admi/StartUp.html',context)

def edit_StartUp(request,pk):
    edt_startup=StratUp.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_startup.image) > 0:
                os.remove(edt_startup.image.path)
            edt_startup.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_startup.image_1) > 0:
                os.remove(edt_startup.image_1.path)
            edt_startup.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_startup.image_2) > 0:
                os.remove(edt_startup.image_2.path)
            edt_startup.image_2 = request.FILES['img_2']

        edt_startup.description = request.POST.get('description')
        edt_startup.save()
        messages.success(request,"Update successfully")
        return redirect('adm_StartUp')
    context={
        'edt_startup':edt_startup
        }
    return render(request,'admi/edit_startup.html',context)

def delete_StartUp(request,pk):
    del_startup = StratUp.objects.filter(id=pk)
    del_startup.delete()
    return redirect('adm_StartUp')



def adm_Construction(request):
    construct=Construction.objects.all()
    if request.method == "POST":
        construct = Construction()
        
        construct.description = request.POST.get('description')
        if len(request.FILES) != 0:
            construct.image = request.FILES['img']                  
            construct.image_1 = request.FILES['img_1']
            construct.image_2 = request.FILES['img_2']
        construct.save()
        messages.success(request,"successfully complited")
        return redirect('adm_Construction') 
    context={
        'construct':construct
        } 
    return render(request,'admi/invest_Construction.html',context)

def edit_Construction(request,pk):
    edt_Construc=Construction.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_Construc.image) > 0:
                os.remove(edt_Construc.image.path)
            edt_Construc.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_Construc.image_1) > 0:
                os.remove(edt_Construc.image_1.path)
            edt_Construc.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_Construc.image_2) > 0:
                os.remove(edt_Construc.image_2.path)
            edt_Construc.image_2 = request.FILES['img_2']    
        edt_Construc.description=request.POST.get('description')
        edt_Construc.save()
        messages.success(request,"Update successfully")
        return redirect('adm_Construction')
    context={
        'edt_Construc':edt_Construc
        }
    return render(request,'admi/edit_construction.html',context)

def delete_Construction(request,pk):
    del_Construc = Construction.objects.filter(id=pk)
    del_Construc.delete()
    return redirect('adm_Construction')



def adm_infrastructure(request):
    infrastruc=Infrastructure.objects.all()
    if request.method == "POST":
        infrastruc = Infrastructure()       
        infrastruc.description = request.POST.get('description')
        if len(request.FILES) != 0:
            infrastruc.image = request.FILES['img']
            infrastruc.image_1 = request.FILES['img_1']
            infrastruc.image_2 = request.FILES['img_2']
        infrastruc.save()
        messages.success(request,"successfully complited")
        return redirect('adm_infrastructure') 
    context={
        'infrastruc':infrastruc
        } 
    return render(request,'admi/infrastructure.html',context)

def edit_infrastructure(request,pk):
    edt_infrastruc=Infrastructure.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_infrastruc.image) > 0:
                os.remove(edt_infrastruc.image.path)
            edt_infrastruc.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_infrastruc.image_1) > 0:
                os.remove(edt_infrastruc.image_1.path)
            edt_infrastruc.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_infrastruc.image_2) > 0:
                os.remove(edt_infrastruc.image_2.path)
            edt_infrastruc.image_2 = request.FILES['img_2']    
        edt_infrastruc.description=request.POST.get('description')
        edt_infrastruc.save()
        messages.success(request,"Update successfully")
        return redirect('adm_infrastructure')
    context={
        'edt_infrastruc':edt_infrastruc
        }
    return render(request,'admi/edit_infrastructure.html',context)

def delete_infrastructure(request,pk):
    del_infrastruc = Infrastructure.objects.filter(id=pk)
    del_infrastruc.delete()
    return redirect('adm_infrastructure')


def adm_mining(request):
    mine=Mining.objects.all()
    if request.method == "POST":
        mine = Mining()       
        mine.description = request.POST.get('description')
        if len(request.FILES) != 0:
            mine.image = request.FILES['img']
            mine.image_1 = request.FILES['img_1']
            mine.image_2 = request.FILES['img_2']
        mine.save()
        messages.success(request,"successfully complited")
        return redirect('adm_mining') 
    context={
        'mine':mine
        } 
    return render(request,'admi/mining.html',context)

def edit_mining(request,pk):
    edt_mine=Mining.objects.get(id=pk)
    if request.method == "POST":
        if 'img' in request.FILES:
            if len(edt_mine.image) > 0:
                os.remove(edt_mine.image.path)
            edt_mine.image = request.FILES['img']

        if 'img_1' in request.FILES:
            if len(edt_mine.image_1) > 0:
                os.remove(edt_mine.image_1.path)
            edt_mine.image_1 = request.FILES['img_1']

        if 'img_2' in request.FILES:
            if len(edt_mine.image_2) > 0:
                os.remove(edt_mine.image_2.path)
            edt_mine.image_2 = request.FILES['img_2']    
        edt_mine.description=request.POST.get('description')
        edt_mine.save()
        messages.success(request,"Update successfully")
        return redirect('adm_mining')
    context={
        'edt_mine':edt_mine
        }
    return render(request,'admi/edit_mining.html',context)

def delete_mining(request,pk):
    del_mine = Mining.objects.filter(id=pk)
    del_mine.delete()
    return redirect('adm_mining')

# end manage investment

# start client management 
def adm_clint(request):
    clients =Client.objects.all()
    if request.method == 'POST':
        clients = Client()
        clients.title= request.POST.get("heading")
        clients.description=request.POST.get("description")
        if len(request.FILES)!= 0:
            clients.image=request.FILES["img"]
        clients.save()
        messages.success(request,"successfully complited")
        return redirect('adm_clint')
    context ={
        'clients':clients
        }
    return render(request,'admi/clients.html',context)

def edit_client(request,pk):
    edt_clients=Client.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(edt_clients.image)>0:
                os.remove(edt_clients.image.path)
            edt_clients.image = request.FILES['img']
        edt_clients.title=request.POST.get('heading')
        edt_clients.description=request.POST.get('description')
        edt_clients.save()
        messages.success(request,"Update successfully")
        return redirect('adm_clint')
    context={'edt_clients':edt_clients}
    return render(request,'admi/edit_client.html',context)

def delete_client(request,pk):
    del_plot =Client.objects.filter(id=pk)
    del_plot.delete()
    return redirect('adm_clint')

# end client management 

# start home management 
def home_head(request):
    head = Home_heading.objects.all()
    if request.method == 'POST':
        head = Home_heading()
        head.title = request.POST.get('heading')
        head.title_1 = request.POST.get('heading1')
        head.save()
        messages.success(request,'Successfully Complited')
        return redirect('home_head')
    
    context ={'head':head}
    return render(request,'admi\home_heading.html',context)

def edit_home_head(request,pk):
    edt_head=Home_heading.objects.get(id=pk)
    if request.method == "POST":
        edt_head.title=request.POST.get('heading')
        edt_head.title_1=request.POST.get('heading1')
        edt_head.save()
        messages.success(request,"Update successfully")
        return redirect('home_head')
    context={
        'edt_head':edt_head
        }
    return render(request,'admi/edit_home_heading.html',context)

def delete_home_head(request,pk):
    del_head=Home_heading.objects.filter(id=pk)
    del_head.delete()
    return redirect('home_head')
# ends home management

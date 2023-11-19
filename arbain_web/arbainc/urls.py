
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="home"),

# investment urls section start 

    path('User_startup',views.User_startup,name="User_startup"),
    
    path('User_Infranstructor',views.User_Infranstructor,name="User_Infranstructor"),

    path('User_Construction',views.User_Construction,name="User_Construction"),

    path('User_mining',views.User_mining,name="User_mining"),

# investment user urls section ends

# consulting section start 
    path('User_consult',views.User_consult,name="User_consult"),


# consulting section ends

# Realty user urls section start

    path('User_realty',views.User_realty,name="User_realty"),

    path('User_land',views.User_land,name="User_land"),

    path('User_plot',views.User_plot,name="User_plot"),

    path('User_residential',views.User_residential,name="User_residential"),

    path('User_commercial',views.User_commercial,name="User_commercial"),
# Realty user urls section ends

# export section start 
    path('User_export',views.User_export,name="User_export"),

# export section ends

# health care section start 
    path('User_health',views.User_health,name="User_health"),


# health care section ends

# client section start    

    path('client',views.client,name="client"),

# client section ends 


######################    admin    ########################

    path('arbainclogin',views.arbainclogin,name="arbainclogin"),
    path('SignOut',views.SignOut,name="SignOut"),

    path('arbain_admin',views.home,name="arbain_admin"),
    
    # path('base',views.base,name="base"),
# start manage realty 
    path('adm_land',views.adm_land,name="adm_land"),
    path('edit_land/<int:pk>/',views.edit_land,name="edit_land"),
    path('delete_land/<int:pk>/',views.delete_land,name="delete_land"),
    
    path('adm_plot',views.adm_plot,name="adm_plot"),
    path('edit_plot/<int:pk>/',views.edit_plot,name="edit_plot"),
    path('delete_plot/<int:pk>/',views.delete_plot,name="delete_plot"),

    path('adm_residential',views.adm_residential,name="adm_residential"),
    path('edit_residential/<int:pk>/',views.edit_residential,name="edit_residential"),
    path('delete_residential/<int:pk>/',views.delete_residential,name="delete_residential"),

    path('adm_commercial',views.adm_commercial,name="adm_commercial"),
    path('edit_commercial/<int:pk>/',views.edit_commercial,name="edit_commercial"),
    path('delete_commercial/<int:pk>/',views.delete_commercial,name="delete_commercial"),
# end manage realty 
    

# start manage export 
    path('adm_food',views.adm_food,name="adm_food"),
    path('edit_food/<int:pk>/',views.edit_food,name="edit_food"),
    path('delete_food/<int:pk>/',views.delete_food,name="delete_food"),

    path('adm_spices',views.adm_spices,name="adm_spices"),
    path('edit_spices/<int:pk>/',views.edit_spices,name="edit_spices"),
    path('delete_spices/<int:pk>/',views.delete_spices,name="delete_spices"),

    path('adm_cosmetic',views.adm_cosmetic,name="adm_cosmetic"),
    path('edit_cosmetic/<int:pk>/',views.edit_cosmetic,name="edit_cosmetic"),
    path('delete_cosmetic/<int:pk>/',views.delete_cosmetic,name="delete_cosmetic"),

    path('Bg_exports',views.Bg_exports,name="Bg_exports"),
    path('edit_Bg_exports/<int:pk>/',views.edit_Bg_exports,name="edit_Bg_exports"),
    path('delete_Bg_exports/<int:pk>/',views.delete_Bg_exports,name="delete_Bg_exports"),

# end manage export 
#   
# start manage healthcare

    path('adm_health',views.adm_health,name="adm_health"),
    path('edit_health/<int:pk>/',views.edit_health,name="edit_health"),
    path('delete_health/<int:pk>/',views.delete_health,name="delete_health"),
    
    path('Bg_health_care',views.Bg_health_care,name="Bg_health_care"),
    path('edit_Bg_health_care/<int:pk>/',views.edit_Bg_health_care,name="edit_Bg_health_care"),
    path('delete_Bg_health_care/<int:pk>/',views.delete_Bg_health_care,name="delete_Bg_health_care"),
# end manage healthcare   

# start manage consulting
    path('adm_Startup_const',views.adm_Startup_const,name="adm_Startup_const"),
    path('edit_Startup_const/<int:pk>/',views.edit_Startup_const,name="edit_Startup_const"),
    path('delete_Startup_const/<int:pk>/',views.delete_Startup_const,name="delete_Startup_const"),

    path('adm_Startup_finance',views.adm_Startup_finance,name="adm_Startup_finance"),
    path('edit_Startup_finance/<int:pk>/',views.edit_Startup_finance,name="edit_Startup_finance"),
    path('delete_Startup_finance/<int:pk>/',views.delete_Startup_finance,name="delete_Startup_finance"),

    
    path('adm_img_consulting',views.adm_img_consulting,name="adm_img_consulting"),
    path('edit_img_consulting/<int:pk>/',views.edit_img_consulting,name="edit_img_consulting"),
    path('delete_img_consulting/<int:pk>/',views.delete_img_consulting,name="delete_img_consulting"),

# end manage consulting 

# start manage investment  

    path('adm_StartUp',views.adm_StartUp,name="adm_StartUp"),
    path('edit_StartUp/<int:pk>/',views.edit_StartUp,name="edit_StartUp"),
    path('delete_StartUp/<int:pk>/',views.delete_StartUp,name="delete_StartUp"),

    path('adm_Construction',views.adm_Construction,name="adm_Construction"),
    path('edit_Construction/<int:pk>/',views.edit_Construction,name="edit_Construction"),
    path('delete_Construction/<int:pk>/',views.delete_Construction,name="delete_Construction"),

    path('adm_infrastructure',views.adm_infrastructure,name="adm_infrastructure"),
    path('edit_infrastructure/<int:pk>/',views.edit_infrastructure,name="edit_infrastructure"),
    path('delete_infrastructure/<int:pk>/',views.delete_infrastructure,name="delete_infrastructure"),

    path('adm_mining',views.adm_mining,name="adm_mining"),
    path('edit_mining/<int:pk>/',views.edit_mining,name="edit_mining"),
    path('delete_mining/<int:pk>/',views.delete_mining,name="delete_mining"),

# end manage investment

# start client management 
    path('adm_clint',views.adm_clint,name="adm_clint"),
    path('edit_client/<int:pk>/',views.edit_client,name="edit_client"),
    path('delete_client/<int:pk>/',views.delete_client,name="delete_client"),
    
# end client management     

# start home management 
    path('home_head',views.home_head,name="home_head"),
    path('edit_home_head/<int:pk>/',views.edit_home_head,name="edit_home_head"),
    path('delete_home_head/<int:pk>/',views.delete_home_head,name="delete_home_head"),

# ends home management    
]



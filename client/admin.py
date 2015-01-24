from django.contrib import admin
from client.models import Visa, Stage, Client, Institution, Coe, Invoice


admin.site.register(Visa)
admin.site.register(Stage)
admin.site.register(Institution)
admin.site.register(Client)
admin.site.register(Coe)
admin.site.register(Invoice)
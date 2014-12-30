from django.contrib import admin
from client.models import Visa, Stage, Client, Institution


admin.site.register(Visa)
admin.site.register(Stage)
admin.site.register(Institution)
admin.site.register(Client)
from django.contrib import admin

from ckeditor_demo.demo_application import models


admin.site.register(models.ExampleModel)
admin.site.register(models.ExampleNonUploadModel)

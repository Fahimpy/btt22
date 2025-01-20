from django.contrib import admin
from .models import Person
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # অ্যাডমিন প্যানেলে দেখানোর জন্য কলামগুলি নির্ধারণ করুন
    list_display = ('name', 'designation', 'school_name', 'mobile_no', 'category')
    list_filter = ('category',)  # ক্যাটেগরি ফিল্টার যুক্ত করুন
    search_fields = ('name', 'school_name', 'designation')  # অনুসন্ধানের জন্য ফিল্ড যুক্ত করুন
    list_editable = ()

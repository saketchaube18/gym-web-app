from django.contrib import admin

# Register your models here.

from app.models import Contact, MembershipPlan, Enrollment, Trainer, Gallery


# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Gallery)

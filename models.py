from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group

class Permission(models.Model):
    name = models.CharField(max_length=16)
    content_type = models.ForeignKey(ContentType, related_name="row_permissions")
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, null=True, blank=True, raw_id_admin=True)
    group = models.ForeignKey(Group, null=True, blank=True, raw_id_admin=True)
    
    class Admin:
        list_display = ('content_type', 'user', 'group', 'name')
        list_filter = ('name',)
        search_fields = ['object_id', 'content_type', 'user', 'group']
        
    class Meta:
        verbose_name = 'permission'
        verbose_name_plural = 'permissions'
        
    def __unicode__(self):
        return u"%s | %s | %d | %s" % (self.content_type.app_label, self.content_type, self.object_id, self.name)
        

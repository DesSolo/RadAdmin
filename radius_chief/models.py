from django.db import models
from .choices import OPERATORS_CHOICE


class Nas(models.Model):
    nasname = models.CharField(max_length=128)
    shortname = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    ports = models.IntegerField(blank=True, null=True)
    secret = models.CharField(max_length=60)
    server = models.CharField(max_length=64, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas'


class RadAcct(models.Model):
    radacctid = models.BigAutoField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(unique=True, max_length=32)
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasipaddress = models.CharField(max_length=15)
    nasportid = models.CharField(max_length=15, blank=True, null=True)
    nasporttype = models.CharField(max_length=32, blank=True, null=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctupdatetime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctinterval = models.IntegerField(blank=True, null=True)
    acctsessiontime = models.PositiveIntegerField(blank=True, null=True)
    acctauthentic = models.CharField(max_length=32, blank=True, null=True)
    connectinfo_start = models.CharField(max_length=50, blank=True, null=True)
    connectinfo_stop = models.CharField(max_length=50, blank=True, null=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.CharField(max_length=50)
    callingstationid = models.CharField(max_length=50)
    acctterminatecause = models.CharField(max_length=32)
    servicetype = models.CharField(max_length=32, blank=True, null=True)
    framedprotocol = models.CharField(max_length=32, blank=True, null=True)
    framedipaddress = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'radacct'


class RadCheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=OPERATORS_CHOICE)
    value = models.CharField(max_length=253)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'radcheck'
        unique_together = ('username', 'attribute')


class RadGroupCheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=OPERATORS_CHOICE)
    value = models.CharField(max_length=253)

    def __str__(self):
        return self.groupname

    class Meta:
        managed = False
        db_table = 'radgroupcheck'
        unique_together = ('groupname', 'attribute')


class RadGroupReply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=OPERATORS_CHOICE)
    value = models.CharField(max_length=253)

    def __str__(self):
        return self.groupname

    class Meta:
        managed = False
        db_table = 'radgroupreply'
        unique_together = ('groupname', 'attribute')


class RadPostAuth(models.Model):
    username = models.CharField(max_length=64)
    pass_field = models.CharField(db_column='pass', max_length=64)
    reply = models.CharField(max_length=32)
    authdate = models.DateTimeField()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'radpostauth'


class RadReply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=OPERATORS_CHOICE)
    value = models.CharField(max_length=253)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'radreply'
        unique_together = ('username', 'attribute')


class RadUserGroup(models.Model):
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    priority = models.IntegerField()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'radusergroup'

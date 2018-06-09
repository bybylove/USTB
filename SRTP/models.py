from django.db import models

# Create your models here.


class team(models.Model):
    name = models.CharField(max_length=30)
    #队伍名称
    college = models.CharField(max_length=30)
    #所属学院
class student(models.Model):
    name = models.CharField(max_length=30)
    #名字
    college = models.CharField(max_length=30,default=None,null=True )
    #所属学院
    team = models.ForeignKey(team,on_delete=models.SET_NULL,null=True,related_name='team_member')

class teacher(models.Model):
    name = models.CharField(max_length=30)
    #名字
    college = models.CharField(max_length=30)
    #所属学院
    position = models.CharField(max_length=30)
    #职位
class report(models.Model):
    title = models.CharField(max_length=30)
    #论文标题
    content = models.TextField(max_length=21845, null = True)
    #论文内容



class srtp(models.Model):
    name = models.CharField(max_length=30)
    # 项目名称
    start_time = models.DateField(null=True)
    # 启动时间
    team = models.ForeignKey(team,on_delete=models.SET_NULL,null=True,related_name='srtp_team')
    # 参与队伍
    teacher = models.ForeignKey(teacher,on_delete=models.SET_NULL,null=True,related_name='srtp_teacher')
    # 指导教师
    money = models.IntegerField(null=True)
    # 经费
    middle_report = models.OneToOneField(report,on_delete=models.SET_NULL,null=True,related_name='srtp_port')
    # 中期报告
    final_report = models.OneToOneField(report,on_delete=models.SET_NULL,null=True)
    # 结题报告
from django.db import models

# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=30)
    # 名字
    College = models.CharField(max_length=30, default=None, null=True)
    # 所属学院
class teacher(models.Model):
    Name = models.CharField(max_length=30)
    # 名字
    College = models.CharField(max_length=30)
    # 所属学院
    Position = models.CharField(max_length=30)
    # 职位
class report(models.Model):
    Title = models.CharField(max_length=30)
    # 论文标题
    Content = models.TextField(max_length=21845, null=True)
    # 论文内容
class opinion(models.Model):
    TeacherName = models.CharField(max_length=30)
    Content = models.TextField(max_length=21845, null=True)
class graduation_project(models.Model):
    Student = models.OneToOneField(student ,on_delete=models.CASCADE,null=False,related_name='student_project')
    Teacher = models.ForeignKey(teacher ,on_delete=models.SET_NULL,null=True ,related_name='teacher_project')
    Judger = models.ManyToManyField(teacher,related_name='judger_project')
    MiddleReport = models.OneToOneField(report,on_delete=models.SET_NULL,null=True,related_name='middle_report_project')
    FinalReport = models.OneToOneField(report,on_delete=models.SET_NULL,null=True,related_name='final_report_project')
    AssignmentBook = models.OneToOneField(report,on_delete=models.SET_NULL,null=True,related_name='assignment_book_project')
    SelectTopic = models.OneToOneField(report,on_delete=models.SET_NULL,null=True,related_name='select_topic_project')
    TeacherOpinion = models.OneToOneField(opinion,on_delete=models.SET_NULL,null=True,related_name='teacher_opinion_project')
    JudgerOpinion = models.OneToOneField(opinion, on_delete=models.SET_NULL, null=True,related_name='judger_opinion_project')
from django.db import models

# Create your models here.

# 108第二學期相關：

class Courses1082(models.Model):
    instructor_name = models.CharField(max_length=50, blank=True, null=True)
    curriculum_name = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return (self.instructor_name + " " + self.curriculum_name + " " +  self.time)


class Coursesreport1082x2(models.Model):
    course = models.ForeignKey(Courses1082, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        course = self.course.curriculum_name
        instructor = self.course.instructor_name
        t = self.course.time
        report = self.report_text
        return ("%s %s %s %s") % (course, instructor,  t, report)

class Coursesreport1082x1(models.Model):
    course = models.ForeignKey(Courses1082, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        course = self.course.curriculum_name
        instructor = self.course.instructor_name
        t = self.course.time
        report = self.report_text
        return ("%s %s %s %s") % (course, instructor,  t, report)


# 108第一學期相關：

class Courses1081(models.Model):
    instructor_name = models.CharField(max_length=50, blank=True, null=True)
    curriculum_name = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return (self.instructor_name + " " + self.curriculum_name + " " +  self.time)


class Coursesreport1081x1(models.Model):
    course = models.ForeignKey(Courses1081, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        course = self.course.curriculum_name
        instructor = self.course.instructor_name
        t = self.course.time
        report = self.report_text
        return ("%s %s %s %s") % (course, instructor,  t, report)


class Coursesreport1081x2(models.Model):
    course = models.ForeignKey(Courses1081, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        course = self.course.curriculum_name
        instructor = self.course.instructor_name
        t = self.course.time
        report = self.report_text
        return ("%s %s %s %s") % (course, instructor,  t, report)
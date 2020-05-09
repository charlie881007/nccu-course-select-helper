from django.shortcuts import render
from .models import Courses1082, Courses1081

# Create your views here.
def show_search_page(request):
    return render(request, 'search/search.html')


def show_result_page(request):
    keyword_course = request.POST["course"]
    keyword_teacher = request.POST["teacher"]
    keyword_time = request.POST["time"]

    objects1082 = Courses1082.objects.all()

    if keyword_course.strip() != "" and keyword_teacher.strip() != "" and keyword_time.strip() != "":
        course_query = objects1082.filter(instructor_name__contains=keyword_teacher, curriculum_name__contains=keyword_teacher, time__contains=keyword_time)
    elif keyword_course.strip() != "" and keyword_teacher.strip() != "":
        course_query = objects1082.filter(curriculum_name__contains=keyword_course, instructor_name__contains=keyword_teacher)
    elif keyword_course.strip() != "" and keyword_time.strip() != "":
        course_query = objects1082.filter(curriculum_name__contains=keyword_course, time__contains=keyword_time)
    elif keyword_teacher.strip() != "" and keyword_time.strip() != "":
        course_query = objects1082.filter(instructor_name__contains=keyword_teacher, time__contains=keyword_time)
    elif keyword_course.strip() != "":
        course_query = objects1082.filter(curriculum_name__contains=keyword_course)
    elif keyword_teacher.strip() != "":
        course_query = objects1082.filter(instructor_name__contains=keyword_teacher)
    elif keyword_time.strip() != "":
        course_query = objects1082.filter(time__contains=keyword_time)
    else:
        course_query = []

    course_list=[]
    report_list = []
    for course in course_query:
        report_quantity = len(course.coursesreport1082x2_set.all())
        for q in range(report_quantity):
            course_list.append(course)
        for report in course.coursesreport1082x2_set.all():
            report_list.append(report)
    output_list_1082x2 = zip(course_list, report_list)

    course_list = []
    report_list = []
    for course in course_query:
        report_quantity = len(course.coursesreport1082x1_set.all())
        for q in range(report_quantity):
            course_list.append(course)
        for report in course.coursesreport1082x1_set.all():
            report_list.append(report)
    output_list_1082x1 = zip(course_list, report_list)

    objects1081 = Courses1081.objects.all()



    if keyword_course.strip() != "" and keyword_teacher.strip() != "" and keyword_time.strip() != "":
        course_query = objects1081.filter(instructor_name__contains=keyword_teacher,
                                          curriculum_name__contains=keyword_teacher, time__contains=keyword_time)
    elif keyword_course.strip() != "" and keyword_teacher.strip() != "":
        course_query = objects1081.filter(curriculum_name__contains=keyword_course,
                                          instructor_name__contains=keyword_teacher)
    elif keyword_course.strip() != "" and keyword_time.strip() != "":
        course_query = objects1081.filter(curriculum_name__contains=keyword_course, time__contains=keyword_time)
    elif keyword_teacher.strip() != "" and keyword_time.strip() != "":
        course_query = objects1081.filter(instructor_name__contains=keyword_teacher, time__contains=keyword_time)
    elif keyword_course.strip() != "":
        course_query = objects1081.filter(curriculum_name__contains=keyword_course)
    elif keyword_teacher.strip() != "":
        course_query = objects1081.filter(instructor_name__contains=keyword_teacher)
    elif keyword_time.strip() != "":
        course_query = objects1081.filter(time__contains=keyword_time)
    else:
        course_query = []

    course_list = []
    report_list = []
    for course in course_query:
        report_quantity = len(course.coursesreport1081x1_set.all())
        for q in range(report_quantity):
            course_list.append(course)
        for report in course.coursesreport1081x1_set.all():
            report_list.append(report)
    output_list_1081x1 = zip(course_list, report_list)

    course_list = []
    report_list = []
    for course in course_query:
        report_quantity = len(course.coursesreport1081x2_set.all())
        for q in range(report_quantity):
            course_list.append(course)
        for report in course.coursesreport1081x2_set.all():
            report_list.append(report)
    output_list_1081x2 = zip(course_list, report_list)

    return render(request, 'search/result.html', {'output_list_1082x1': output_list_1082x1,
                                                   'output_list_1082x2': output_list_1082x2,
                                                   'output_list_1081x1': output_list_1081x1,
                                                   'output_list_1081x2': output_list_1081x2})

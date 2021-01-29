from .models import Course

def calculate(request):
    course_list=Course.objects.all()
    #get the entire sum of credits
    total_credit=sum([course.credit for course in course_list])
    major_credit=sum([course.credit for course in course_list.filter(course_type="MJ")])
    minor_credit=sum([course.credit for course in course_list.filter(course_type="MN")])
    #get the sum of grades
    if(Course.desired_standard=="default"):
        total_sum=sum([course.grade for course in course_list.filter(standard="default")])+sum([course.grade*(4.5/4.3) for course in course_list.filter(standard="alt_1")])+sum([course.grade*(4.5/3.7) for course in course_list.filter(standard="alt_2")])
        major_sum=sum([course.grade for course in course_list.filter(course_type="MJ",standard="default")])+sum([course.grade*(4.5/4.3) for course in course_list.filter(course_type="MJ",standard="alt_1")])+sum([course.grade*(4.5/3.7) for course in course_list.filter(course_type="MJ",standard="alt_2")])
        minor_sum=sum([course.grade for course in course_list.filter(course_type="MN",standard="default")])+sum([course.grade*(4.5/4.3) for course in course_list.filter(course_type="MN",standard="alt_1")])+sum([course.grade*(4.5/3.7) for course in course_list.filter(course_type="MN",standard="alt_2")])

    elif(Course.desired_standard=="alt_1"):
        total_sum = sum([course.grade*(4.3/4.5) for course in course_list.filter(standard="default")]) + sum([course.grade for course in course_list.filter(standard="alt_1")]) + sum([course.grade * (4.3 / 3.7) for course in course_list.filter(standard="alt_2")])
        major_sum = sum([course.grade*(4.3/4.5) for course in course_list.filter(course_type="MJ", standard="default")]) + sum([course.grade  for course in course_list.filter(course_type="MJ", standard="alt_1")]) + sum([course.grade * (4.3 / 3.7) for course in course_list.filter(course_type="MJ", standard="alt_2")])
        minor_sum = sum([course.grade*(4.3/4.5) for course in course_list.filter(course_type="MN", standard="default")]) + sum([course.grade for course in course_list.filter(course_type="MN", standard="alt_1")]) + sum([course.grade * (4.3 / 3.7) for course in course_list.filter(course_type="MN", standard="alt_2")])
    else:
        total_sum = sum([course.grade * (3.7/ 4.5) for course in course_list.filter(standard="default")]) + sum([course.grade*(3.7/4.3) for course in course_list.filter(standard="alt_1")]) + sum([course.grade for course in course_list.filter(standard="alt_2")])
        major_sum = sum([course.grade * (3.7 / 4.5) for course in course_list.filter(course_type="MJ", standard="default")]) + sum([course.grade *(3.7/4.3) for course in course_list.filter(course_type="MJ", standard="alt_1")]) + sum([course.grade for course in course_list.filter(course_type="MJ", standard="alt_2")])
        minor_sum = sum([course.grade * (3.7 / 4.5) for course in course_list.filter(course_type="MN", standard="default")]) + sum([course.grade *(3.7/4.3)for course in course_list.filter(course_type="MN", standard="alt_1")]) + sum([course.grade  for course in course_list.filter(course_type="MN", standard="alt_2")])


    total_avg=total_credit/total_sum
    major_avg=major_credit/major_sum
    minor_avg=minor_credit/minor_sum
    return total_avg,major_avg,minor_avg
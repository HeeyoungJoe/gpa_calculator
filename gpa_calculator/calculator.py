from .models import Course

def calculate(standard):
    course_list=Course.objects.all()
    #get the entire sum of credits
    total_credit=sum([course.credits for course in course_list])
    major_credit=sum([course.credits for course in course_list.filter(course_type="MJ")])
    minor_credit=sum([course.credits for course in course_list.filter(course_type="MN")])
    #get the sum of grades
    if(standard==4.5):
        total_sum=sum([course.grade for course in course_list.filter(standard=4.5)])+sum([course.grade*(4.5/4.3) for course in course_list.filter(standard=4.3)])+sum([course.grade*(4.5/3.7) for course in course_list.filter(standard=3.7)])
        major_sum=sum([course.grade for course in course_list.filter(course_type="MJ",standard=4.5)])+sum([course.grade*(4.5/4.3) for course in course_list.filter(course_type="MJ",standard=4.3)])+sum([course.grade*(4.5/3.7) for course in course_list.filter(course_type="MJ",standard=3.7)])
        minor_sum=sum([course.grade for course in course_list.filter(course_type="MN",standard=4.5)])+sum([course.grade*(4.5/4.3) for course in course_list.filter(course_type="MN",standard=4.3)])+sum([course.grade*(4.5/3.7) for course in course_list.filter(course_type="MN",standard=3.7)])

    elif(standard==4.3):
        total_sum = sum([course.grade*(4.3/4.5) for course in course_list.filter(standard=4.5)]) + sum([course.grade for course in course_list.filter(standard=4.3)]) + sum([course.grade * (4.3 / 3.7) for course in course_list.filter(standard=3.7)])
        major_sum = sum([course.grade*(4.3/4.5) for course in course_list.filter(course_type="MJ", standard=4.5)]) + sum([course.grade  for course in course_list.filter(course_type="MJ", standard=4.3)]) + sum([course.grade * (4.3 / 3.7) for course in course_list.filter(course_type="MJ", standard=3.7)])
        minor_sum = sum([course.grade*(4.3/4.5) for course in course_list.filter(course_type="MN", standard=4.5)]) + sum([course.grade for course in course_list.filter(course_type="MN", standard=4.3)]) + sum([course.grade * (4.3 / 3.7) for course in course_list.filter(course_type="MN", standard=3.7)])
    else:
        total_sum = sum([course.grade * (3.7/ 4.5) for course in course_list.filter(standard=4.5)]) + sum([course.grade*(3.7/4.3) for course in course_list.filter(standard=4.3)]) + sum([course.grade for course in course_list.filter(standard=3.7)])
        major_sum = sum([course.grade * (3.7 / 4.5) for course in course_list.filter(course_type="MJ", standard=4.5)]) + sum([course.grade *(3.7/4.3) for course in course_list.filter(course_type="MJ", standard=4.3)]) + sum([course.grade for course in course_list.filter(course_type="MJ", standard=3.7)])
        minor_sum = sum([course.grade * (3.7 / 4.5) for course in course_list.filter(course_type="MN", standard=4.5)]) + sum([course.grade *(3.7/4.3)for course in course_list.filter(course_type="MN", standard=4.3)]) + sum([course.grade  for course in course_list.filter(course_type="MN", standard=3.7)])


    total_avg=total_credit/total_sum
    major_avg=major_credit/major_sum
    minor_avg=minor_credit/minor_sum


    return total_avg,major_avg,minor_avg
from .models import Course


def calculate(standard):
    course_list = Course.objects.all()
    # get the entire sum of credits
    total_credit = sum([course.credits for course in course_list])
    major_credit = sum([course.credits for course in course_list.filter(course_type="MJ")])
    minor_credit = sum([course.credits for course in course_list.filter(course_type="MN")])
    # get the sum of grades
    if (standard == 4.5):
        total_sum = sum([course.grade * course.credits for course in course_list.filter(standard=4.5)]) + sum(
            [course.grade*course.credits * (4.5 / 4.3) for course in course_list.filter(standard=4.3)]) + sum(
            [course.grade*course.credits * (4.5 / 3.7) for course in course_list.filter(standard=3.7)])
        major_sum = sum(
            [course.grade * course.credits for course in course_list.filter(course_type="MJ", standard=4.5)]) + sum(
            [course.grade*course.credits * (4.5 / 4.3) for course in course_list.filter(course_type="MJ", standard=4.3)]) + sum(
            [course.grade*course.credits * (4.5 / 3.7) for course in course_list.filter(course_type="MJ", standard=3.7)])
        minor_sum = sum(
            [course.grade * course.credits for course in course_list.filter(course_type="MN", standard=4.5)]) + sum(
            [course.grade*course.credits * (4.5 / 4.3) for course in course_list.filter(course_type="MN", standard=4.3)]) + sum(
            [course.grade*course.credits * (4.5 / 3.7) for course in course_list.filter(course_type="MN", standard=3.7)])

    elif (standard == 4.3):
        total_sum = sum(
            [course.grade * (4.3 / 4.5) * course.credits for course in course_list.filter(standard=4.5)]) + sum(
            [course.grade*course.credits for course in course_list.filter(standard=4.3)]) + sum(
            [course.grade*course.credits * (4.3 / 3.7) for course in course_list.filter(standard=3.7)])
        major_sum = sum([course.grade * (4.3 / 4.5) * course.credits for course in
                         course_list.filter(course_type="MJ", standard=4.5)]) + sum(
            [course.grade*course.credits for course in course_list.filter(course_type="MJ", standard=4.3)]) + sum(
            [course.grade*course.credits * (4.3 / 3.7) for course in course_list.filter(course_type="MJ", standard=3.7)])
        minor_sum = sum([course.grade * (4.3 / 4.5) * course.credits for course in
                         course_list.filter(course_type="MN", standard=4.5)]) + sum(
            [course.grade*course.credits for course in course_list.filter(course_type="MN", standard=4.3)]) + sum(
            [course.grade*course.credits * (4.3 / 3.7) for course in course_list.filter(course_type="MN", standard=3.7)])
    elif (standard == 3.7):
        total_sum = sum([course.grade*course.credits * (3.7 / 4.5) for course in course_list.filter(standard=4.5)]) + sum(
            [course.grade*course.credits * (3.7 / 4.3) for course in course_list.filter(standard=4.3)]) + sum(
            [course.grade*course.credits for course in course_list.filter(standard=3.7)])
        major_sum = sum(
            [course.grade*course.credits * (3.7 / 4.5) for course in course_list.filter(course_type="MJ", standard=4.5)]) + sum(
            [course.grade*course.credits * (3.7 / 4.3) for course in course_list.filter(course_type="MJ", standard=4.3)]) + sum(
            [course.grade*course.credits for course in course_list.filter(course_type="MJ", standard=3.7)])
        minor_sum = sum(
            [course.grade*course.credits * (3.7 / 4.5) for course in course_list.filter(course_type="MN", standard=4.5)]) + sum(
            [course.grade*course.credits * (3.7 / 4.3) for course in course_list.filter(course_type="MN", standard=4.3)]) + sum(
            [course.grade*course.credits for course in course_list.filter(course_type="MN", standard=3.7)])
    else:
        total_sum = 0
        major_sum = 0
        minor_sum = 0

    total_avg = total_sum/total_credit
    major_avg = major_sum/major_credit
    minor_avg = minor_sum/minor_credit
    is_working = "yes"

    return total_avg, major_avg, minor_avg, is_working

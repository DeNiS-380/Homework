number_of_completed_homework_assignments = 12
number_of_hours_spent = 1.5
course_name = "Python"
number_of_hours_spent_min = number_of_hours_spent * 60
time_for_one_task = number_of_hours_spent_min / number_of_completed_homework_assignments
print("Курс:", course_name, "."" Всего задач:", number_of_completed_homework_assignments, "."" Затрачено часов:",
number_of_hours_spent, "."" Среднее время выполнения одного задания:", time_for_one_task, "минут")
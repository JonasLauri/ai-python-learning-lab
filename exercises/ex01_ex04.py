# EXERCISE 1
# # person = {"name": "Jonas", "age": 31, "skills": ["Python", "SQL", "GIT"]}

# salaries = [1200, 1800, 2500, 3100, 1500]

# for salary in salaries:
#     if salary > 2000:
#         print(salary)


# EXERCISE 2
# jobs = [
#     {"title": "Data Analyst", "salary": 1800, "remote": True},
#     {"title": "Python Developer", "salary": 2600, "remote": False},
#     {"title": "BI Engineer", "salary": 3200, "remote": True},
# ]


# for job in jobs:
#     if job["salary"] >= 2000 and job["remote"]:
#         print(job["title"])


# EXERCISE 3
# jobs = [
#     {"title": "Data Analyst", "salary": 1800, "remote": True},
#     {"title": "Python Developer", "salary": 2600, "remote": False},
#     {"title": "BI Engineer", "salary": 3200, "remote": True},
#     {"title": "Junior Data Analyst", "salary": 1500, "remote": True},
# ]

# total_salary = 0
# counter_remote = 0

# for job in jobs:
#     if job["remote"]:
#         # Calculate salary of remote jobs
#         total_salary += job["salary"]
#         # Count remote jobs
#         counter_remote += 1

# # Share results of count and average salary of remote job
# print(
#     f"Total count of remote job offers: {counter_remote}\n Average salary of remote job: {total_salary / counter_remote:.0f}"
# )


# EXERCISE 3.2 - REFACTORING
# The challange refactoring with list comprehesion and built-in calculation functions
# remote_jobs = [job["salary"] for job in jobs if job["remote"]]

# print(
#     f"Total count of remote job offers: {len(remote_jobs)}\n"
#     f"Average salary of remote job: {sum(remote_jobs) / len(remote_jobs):.0f}"
# )

# The challange refactoring with generators expressions (+ division by zero error guard)
# total = sum(job["salary"] for job in jobs if job["remote"])
# count = sum(1 for job in jobs if job["remote"])
# average = total / count if count > 0 else 0

# print(
#     f"Total count of remote job offers: {count}\n"
#     f"Average salary of remote job: {average:.0f}"
# )


# EXERCISE 4
jobs = [
    {"title": "Data Analyst", "salary": 1800, "remote": True},
    {"title": "Python Developer", "salary": 2600, "remote": False},
    {"title": "BI Engineer", "salary": 3200, "remote": True},
    {"title": "Junior Data Analyst", "salary": 1500, "remote": True},
    {"title": "Data Engineer", "salary": 4100, "remote": False},
]

# Get total number of jobs
total_jobs = len(jobs)

# Get number, pecentage and avg. salary of remote jobs
remote_list = [job["salary"] for job in jobs if job["remote"]]
remote_count = len(remote_list)
remote_percentage = round((remote_count / total_jobs) * 100)
remote_average = round(sum(remote_list) / remote_count)

# Get number, pecentage and avg. salary of non-remote jobs
no_remote_list = [job["salary"] for job in jobs if not job["remote"]]
no_remote_count = len(no_remote_list)
no_remote_percentage = round((no_remote_count / total_jobs) * 100)
no_remote_average = round(sum(no_remote_list) / no_remote_count)

# Find highest salary and its job title
# max_salary = max(job["salary"] for job in jobs)
# max_salary_title = [job["title"] for job in jobs if max_salary == job["salary"]]
# Find highest salary and its job title using refactor method
max_job = max(jobs, key=lambda job: job["salary"])

# Sharing results according to what task is asking
print(
    f"Total number of jobs: {total_jobs}\n"
    f"Number and percentage of remote jobs: {remote_count} which is {remote_percentage} % of total jobs\n"
    f"Average salary of remote and non-remote jobs: {remote_average} and {no_remote_average} respectively\n"
    f"Highest salary and job title: {max_job['title']} which is {max_job['salary']}"
)

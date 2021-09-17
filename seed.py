from classrooms.models import Classroom
from accounts.models import User, Organization
from classrooms.models import Room, Assignment, Submission, Note
import json
import random
import string
import pytz
from datetime import datetime, timedelta, tzinfo
from django.utils import timezone

# Seeding users
# f = open('MOCK_DATA.json')

# data = json.load(f)

# print('Hello')

# for i in data:
#     user = User.objects.create_user(email=i['email'], name=i['name'], password=i['name'])
#     user.phone = i['phone']
#     user.save()

#     print('User saved, ', user.email)


# Creating Organizations
# f = open('MOCK_DATA(1).json')

# data = json.load(f)
# for i in data:
#     user = User.objects.order_by('?')[0]
#     org = Organization(owner=user, name=i['name'])
#     org.save()
#     print('Organization created: ', org.name)


# Creating Members
# f = open('MOCK_DATA.json')

# data = json.load(f)

# for i in data:
#     try:
#         user = User.objects.get(email=i['email'])
#         org = Organization.objects.order_by('?')[0]
#         member = Member(user=user, organization=org)
#         member.save()
#         print('Member created with organization: ', org.name)
#     except User.DoesNotExist:
#         print('User does not exist!')


for i in range(0, 100):
    # Generate random name for classroom
    # using random.choices()
    # generating random strings
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    desc = ''.join(random.choices(string.ascii_uppercase + string.digits, k=500))
    # org = Organization.objects.order_by('?')[0]
    classroom = Classroom(name=res, description=desc)
    classroom.save()

    print('Classroom created: ', classroom.name)


# classrooms = Classroom.objects.all()
# for classroom in classrooms:
#     members = classroom.organization.members.all()
#     print('----------------- Classroom: ---------------', classroom.name)
#     for member in members:
#         cs = ClassroomStudent(classroom=classroom, member=member)
#         cs.save()
#         print(member.user.email)


# for i in range(0, 100):
#     N = 20
#     # using random.choices()
#     # generating random strings
#     res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
#     classroom = Classroom.objects.order_by('?')[0]
#     dt = timezone.now() + timedelta(days=random.randint(0, 10))
#     room = Room(classroom=classroom, schedule_on=dt, title=res)
#     room.save()
#     print('Room created with title: ', room.title)


# for i in range(0, 100):
#     N = 50
#     # using random.choices()
#     # generating random strings
#     res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
#     classroom = Classroom.objects.order_by('?')[0]
#     dt = timezone.now() + timedelta(days=random.randint(0, 10))
#     assignment = Assignment(classroom=classroom, submission_on=dt, title=res)
#     assignment.save()
#     print('assignment created with title: ', assignment.title)


# classrooms = Classroom.objects.all()

# for classroom in classrooms:
#     # print(classroom.assignments.all())
#     # print(classroom.students.order_by('?')[0])
#     for assign in classroom.assignments.all():
#         st = classroom.students.order_by('?')[0]
#         sub = Submission(assignment=assign, )

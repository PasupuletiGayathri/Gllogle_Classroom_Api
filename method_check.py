import sys
from apiclient import errors
from googleapiclient.errors import HttpError
from google.api_core.exceptions import AlreadyExists, NotFound

sys.path.append("/home/shivasai/Desktop/windows-backup/backup/classroom_api/prerequisites")
from quickstart import main


service = main()
def create_course():
    course = {
    'name': '10th Grade Biology',
    'section': 'Period 2',
    'descriptionHeading': 'Welcome to 10th Grade Biology',
    'description': """We'll be learning about about the
                 structure of living creatures from a
                 combination of textbooks, guest lectures,
                 and lab work. Expect to be excited!""",
    'room': '301',
    'ownerId': 'me',
    'courseState': 'PROVISIONED'
    }
    try:
        course = service.courses().create(body=course).execute()
        print('Course created: %s %s' % (course.get('name'), course.get('id')))
    except:
        return None

def get_course(course_id):
    try:
        course = service.courses().get(id=course_id).execute()
        return (course,course['name'])
    except errors.HttpError as error:
        # print(f'Course with ID "{course_id}" not found.')
        return None
        

def list_course():
    courses = []
    page_token = None

    while True:
        response = service.courses().list(pageToken=page_token,
                                        pageSize=100).execute()
        courses.extend(response.get('courses', []))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break
    lst = []
    if not courses:
        return None
    else:
        for course in courses:
            lst.append(course['id'])
    return lst

def update_course(course_id):
    lst = list_course()
    if course_id in lst:
        print('hai')
        course = service.courses().get(id=course_id).execute()
        course = {}
        course['section'] = 'Period 006'
        course['room'] = '3000'
        course = service.courses().update(id=course_id, body=course).execute()
        return (course['section'], course['room'])
    else:
        # if error.resp.status in [404, 500, 503]:
        return None

def delete_course(course_id):
    courses_to_delete = list_course()
    if course_id in courses_to_delete:

        try:
            course = service.courses().get(id=course_id).execute()
            course['courseState'] = 'ARCHIVED'
            course = service.courses().update(id=course_id, body=course).execute()
            print('course deleted')
        except errors.HttpError as error:
            print('Unable to delete file %s' % course_id)


def patch_course(course_id):
    course = {
    'section': 'Period 54',
    'room': '309'
    }
    try:
        course = service.courses().patch(id=course_id,
                                        updateMask='section,room',
                                        body=course).execute()
        return (course['section'], course['room'])
    except errors.HttpError as error:
        pass
import quickstart
from apiclient import errors
from quickstart import main
import logging

logging.basicConfig(filename='method.log',
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
logging.info("Execution of code starts from here.")
service = main()

#Devloping the API methods for create,list,get,patch and delete

#Method for create a new course
def create_course():
    service = main()
    course = {
    'name': '11 th grade physics',
    'section': 'Period 2',
    'descriptionHeading': 'Welcome to 11 th grade physics',
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
        print('Course created: %s %s' % (course.get('name')))
        logging.info("Create a new course providing with details")
    except errors.HttpError as error:
        print(f'Course with ID "{course_id}" not found.')
        logging.info("Created course id is not found")

#Method for get the specific course based on course id
def get_course(course_id):
    service = main()
    try:
        course = service.courses().get(id=course_id).execute()
        return (course['name'],course['section'],course['room'])
        logging.info("Getting the particular course id details.")
    except errors.HttpError as error:
        print(f'Course with ID "{course_id}" not found.')
        logging.info("The particular id is not present.")

#Method for list out all the courses that present        
def list_courses():
    service = main()
    courses = []
    page_token = None

    while True:
        response = service.courses().list(pageToken=page_token,
                                        pageSize=100).execute()
        courses.extend(response.get('courses', []))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break
    #Create an empty list to store the list of course id        
    lst = []
    if not courses:
        return 'No courses found.'
        logging.info("No courses were found")
    else:
        for course in courses:
            lst.append(course['id'])
            print(course.get('name'), course.get('id'), course.get('section'), course.get('room'))
            logging.info("List out all the course ids that are created")
    return lst

#Method for update the data that present in that specific id
def update_course(course_id):
    service = main()
    course = service.courses().get(id=course_id).execute()
    course['name'] = '10th Grades Social'
    course['room'] = '305'
    try:
        course = service.courses().update(id=course_id, body=course).execute()
        return (course['name'], course['room'])
        logging.info("The name and room number for that particular id will be updated.")
    except:
        return f'no such {course_id} found.'
        logging.info("No such course id is present.")

#Method for delete the specific id
def delete_course(course_id):
    service = main()
    courses_to_delete = list_courses()
    if course_id in courses_to_delete:

        try:
            course = service.courses().get(id=course_id).execute()
            course['courseState'] = 'ARCHIVED'
            course = service.courses().delete(id=course_id).execute()
            print('course deleted')
            logging.info("Provided course id is removed from the list.")
        except errors.HttpError as error:
            print('Unable to delete file %s' % course_id)

#Method for  patching the particular id
def patch_course(course_id):
    service = main()
    course = {
    'section': 'Period 56',
    'room': '310'
    }
    course = service.courses().patch(id=course_id,
                                    updateMask='section,room',
                                    body=course).execute()
    print('Course "%s" updated.' % course.get('name'))
    logging.info("Successfully done the patch method for that course id.")
    return (course['section'],course['room'])

if __name__ == "__main__":
    #Here we call rhe methods
    #create_course()
    #print(get_course('360754771685'))
    list_courses()
    #print(update_course('360754771685'))
    #print(patch_course('360759874329'))
    #print(delete_course('360052421094'))
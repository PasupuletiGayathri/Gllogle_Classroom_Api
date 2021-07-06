from apiclient import errors

from method import main
from method import (get_course, list_courses,
                            update_course, patch_course)

class NotDeleted(Exception):
    pass

class NegativeIndexError(Exception):
    pass


class Successful(Exception):
    pass

class ValueNotEqual(Exception):
    pass


service = main()

def get_courses(course_id):
    if type(get_course(id)) != tuple or type(get_course(id)[0]) != dict:
        raise TypeError('Must return a given datatype')
    
    elif str(id) != get_course(id)[0]['id']:
        raise ValueNotEqual('The id is not found or not created')
    
    elif get_course(id) == None :
        raise TypeError('NO course found with given id') 

    else :
        msg = 'Successfully Created or delivered'
        return msg

def list_course():
    if len(list_course()) == 0: 
        raise NegativeIndexError('No Courses are created', 'LIST_COURSES') 
        
def delete_courses(course_id):
    if id  not in list_courses():
        raise NotDeleted('Course is Not Deleted')
    

def update_courses(course_id):
    if update_course(course_id) == None:
        raise TypeError('No Such  id found to update')

def patch_courses(id):
    if patch_course(id) == None:
        raise TypeError('Values are not updated or No such id is present update')
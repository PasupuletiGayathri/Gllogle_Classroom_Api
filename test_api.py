######################################################################################################
#Pupose of the Script
################################################################################################################################################

#Create and execute test cases in pytest for the all the operations GET, CREATE, DELETE, UPDATE, PATCH and LIST for the google classroom api.

#################################################################################################################################################

#Below points has been considered in the script.

####################################################################################################################################################
#1.Firstly we have to create the credentials to google classroom api.

#2.Download the credentials.json and generate a token by using quickstart.py python code.

#3.Provide methods for create, list, get, update, patch and delete to the course of google classroom.

#4.Write down both positive and negative test cases for that methods with a valid message.

#####################################################################################################################################################
import logging
import method
import pytest
from quickstart import main
import sys
import os
from typing import Type
import pytest
import time
from method import (get_course, list_courses, create_course,
                            delete_course, update_course, patch_course)


from test_method import (get_courses, delete_courses, 
                      list_course, update_courses, patch_courses)


from test_method import NotDeleted, NegativeIndexError

logger=logging.getLogger(__name__)

logging.basicConfig(filename='pytest.log',
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)

logging.info("Execution of code starts from here.")

logging.info("Assigned all the course ids to a variable")
course_id = list_courses()
#####################################################################################################

'''This test case is used whether the id is created or not'''

def test_create_course():
    logging.info("Method for creating a course.")
    assert dict,type(course_id[0])
    logging.info("Test case for create course is successfully passed.")

'''This negative test case is used whether the id is created or not'''

def test_negative_create():
    logging.info("Method for creating a course.")
    assert dict!=type(course_id[1])
    logging.info("Negative Test case for create course is successfully passed.")

#########################################################################################################
'''Test case for list out the course id's'''

def test_list_course():
    logging.info("Checking whether the id is present in the list or not")
    id = '360052810654'
    res = method.list_courses()
    assert id in  course_id, "course_id is not provided in the list"
    assert list == type(res), 'return type of the function is not list'
    logging.info("Test case for for list out the id's is passed successfully")

'''Negative Test case for list out the course id's'''

def test_negative_list():
    logging.info("Negative test case for list method.")
    with pytest.raises(Exception) as exc_info:
        logging.info(str(exc_info.value))
    print(str(exc_info.value))
    logging.info("Negative Test case for list method for list out the id's is passed successfully")

#######################################################################################################
def test_get_course():

    '''Test case for get the particular course id'''

    logging.info("Check the condition whether the id is not equals to 16")
    #assert len(course[0])>0, 'length is less than zero no course is created'
    assert method.get_course(course_id[0])[0]) == '10th Grades Social', 'course not found'
   #assert type(course_id[0])==dict, 'return type of the function is not dict'
    logging.info("Test case for get method is passed successfully") 

def test_negative_get():

    '''Negative Test case for get the particular course id'''

    logging.info("Execution started to the negative test case for get_course")
    with pytest.raises(Exception) as exc_info:
        get_courses(couse_id[0])
    logging.info(str(exc_info.value))
    print(str(exc_info.value))
    logging.info("Negative Test case for get method is passed successfully")

#######################################################################################################
def test_update_course():

    '''Test case for update the data for a particular id'''

    logging.info("Performing the test case for updating the data for specific id.")
    update_id1= method.update_course(course_id[1])
    list_room = method.get_course(course_id[1])
    print(update_id1)
    print(list_room)
    assert(update_id1 == list_room[2])
    logging.info("Test case for update method is passed successfully")

def test_negative_update():
    
    '''Negative Test case for update the data for a particular id'''

    with pytest.raises(Exception) as exc_info:
        update_courses(course_id[1])
    logging.info(str(exc_info.value))
    print(str(exc_info.value))
    logging.info("Negative Test case for update method is passed successfully")

########################################################################################################
def test_delete_course():

    ''' Test case for delete the particular id present in list'''

    logging.info("Execution entered into test_delete_course function")
    delete_course(course_id)
    id = '360769114563'
    assert id not in course_id, 'Id has not deleted successfully'
    logging.info("Execution successfully completed for function test_delete_course")

def test_negative_delete():

    '''Negative test case for delete the particular id present in the list '''

    logging.info("Execution entered into test_delete_course function")
    delete_course(course_id[5])
    logging.info("Execution started for negative test case to delete the particular id")
    with pytest.raises(NotDeleted) as exc_info:
        delete_courses(course_id[5])
    logging.info(str(exc_info.value))
    print(str(exc_info.value))

###########################################################################################################  
def test_patch_course():

    '''Test case for patch update the particular ids'''

    logging.info("Performing the test case for patch method based on ids and update.")
    patch_id1 = patch_course(course_id[2])
    patch_id2 = patch_course(course_id[3])
    print(patch_id1)
    print(patch_id2)
    assert patch_id1 == patch_id2
    logging.info("test case for updation of the course id's is successfully passed.")

def test_negative_patch():

    ''' Negative Test case for patch update the particular ids'''

    logging.info("Performing the negative test case for patch method based on ids and update.") 
    with pytest.raises(Exception) as exc_info:
        patch_courses(couse_id[3])
    logging.info(str(exc_info.value))
    print(str(exc_info.value))
    logging.info("Negative test case for updation of the course id's is successfully passed.")
###################################################################################################

logging.info("Execution of code stops here.")

if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
    
#################################################################################################

#Script_name                        :           test.py
#Script_Version                     :           1.0
#Prepared by                        :           Gayathri.Pasupuleti@infinite.com
#Create Date                        :           10-JUNE-2021
#Last Modification Date             :           14-JUNE-2021
#################################################################################################
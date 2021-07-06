import method
import pytest
import os
from typing import Type
import time
import logging

logger=logging.getLogger(__name__)

logger.info('Execution of positive test cases is started')

@pytest.fixture()
def get_data():
    return 360652990442

#This Function is used for checking whether create course method is working properly or not.
def test_create(get_data):
    msgs = method.get_course(get_data)
    logger.info('Execution entered into test_create_check function')
    #Getting the input value by using pytestfixture and storing into a variable
    res = method.get_course(get_data)
    assert msgs == 'Successfully Created or delivered', 'Successfully created'
    assert dict == type(res[0]), 'return type of the function is not dict'
    assert 'creationTime' in res[0].keys(), 'course has not been created'
    assert str(get_data)== res[0]['id'], 'No such course is present with given id'
    logger.debug('error')
    logger.info('Execution successfully completed for function test_create_check')
    
#This Function is used for checking whether get course method is working properly or not.
def test_get_check(get_data):
    logger.info('Execution entered into test_get_check function')
    #Getting the input value by using pytestfixture and storing into a variable
    res = method.get_course(get_data)
    assert len(res)>0, 'length is less than zero no course is created'
    #assert len(res[0])==16, 'length is not equal to 16 as per default conditions'
    assert type(res[0])==dict, 'return type of the function is not dict'
    logger.info('Execution successfully completed for function test_get_check')
   
# This Function is used for checking whether update course method is working properly or not.
def test_update_check(get_data):
    logger.info('Execution entered into test_update_check function')
    #Getting the input value by using pytestfixture and storing into a variable
    method.update_courses(get_data)
    data1 = method.get_course(get_data)
    data2 = method.update_courses(get_data)
    logger.info(data2)
    logger.info(data1)
    assert str(data1[0]['section'])==data2[0], "section are equal and course hasn't been updated"
    assert str(data1[0]['room'])==data2[1], "room numbers are equal and course hasn't been updated"
    logger.info('Execution successfully completed for function test_update_check')

#This Function is used for checking whether list course method is working properly or not.
def test_list_check():
    logger.info('Execution entered into test_list_check function')
    #Getting the list of ids present in classroom
    res = method.list_courses()
    assert list == type(res), 'return type of the function is not list'
    logger.info('Execution successfully completed for function test_list_check')
   
#This Function is used for checking whether delete course method is working properly or not.
def test_delete_check(get_data):
    logger.info('Execution entered into test_delete_check function')
    #Getting the list of ids present in classroom
    delete_course(get_data)
    res = list_courses()
    assert get_data not in res, 'Id has not deleted successfully'
    logger.info('Execution successfully completed for function test_delete_check')
   
#This Function is used for checking whether path_update_course method is working properly or not.
def test_patch_update(get_data):
    #Getting the input value by using pytestfixture and storing into a variable.
    method.patch_update(get_data)
    data1 = method.get_course(get_data)
    data2 = method.patch_update(get_data)
    assert 'section' in data1[0].keys(), "section are equal and course hasn't been updated"
    assert str(data1[0]['room'])==data2[1], "room numbers are equal and course hasn't been updated"
    logger.info('Execution successfully completed for function test_patch_update')

# logger.info('*'*70)
logger.info('Execution of Negative testcases started')

# #Negative Test Cases

def test_create_failure(get_data):
    logger.info('Execution started for test_create_failure')
    with pytest.raises(Exception) as exc_info:
        get_courses(get_data)
    logger.info(str(exc_info.value))
    print(str(exc_info.value))
    
def test_get_failure(get_data):
    logger.info('Execution started for test_get_failure')
    with pytest.raises(Exception) as exc_info:
        get_courses(get_data)
    logger.info(str(exc_info.value))
    print(str(exc_info.value))
    
def test_update_failure(get_data):
    logger.info('Execution started for test_update_failure')
    with pytest.raises(Exception) as exc_info:
        update_courses(get_data)
    logger.info(str(exc_info.value))
    print(str(exc_info.value))
    
def test_list_check_failure():
    logger.info('Execution started for test_list_check_failure')
    with pytest.raises(Exception) as exc_info:
        res = list_courses()
    logger.info(str(exc_info.value))
    print(str(exc_info.value))
    
def test_patch_failure(get_data):
    logger.info('Execution started for test_patch_failure') 
    with pytest.raises(Exception) as exc_info:
        patch_courses(get_data)
    logger.info(str(exc_info.value))
    print(str(exc_info.value))
    
def test_delete_failure(get_data):
    method.delete_course(get_data)
    logger.info('Execution started for test_delete_failure')
    with pytest.raises("Not Deleted") as exc_info:
        delete_courses(get_data)
    logger.info(str(exc_info.value))
    print(str(exc_info.value))
    
if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
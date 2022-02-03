"""
Dan Smestad ITEC 2905-80 Capstone Due: 2/3/2021.
Python Lab4. 
Python testing your code. 
Start your test functions with the word test!
Arrange Action Assert

Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from operator import index
from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_cant_create_class_with_negative_students(self):
        with self.assertRaises(StudentError):  # context manager 
            test_class = ClassList(-1)


    def test_cant_create_class_with_negative_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(0)    

    def test_can_create_class_with_positive_number_of_students(self):
        test_class = ClassList(1)  #no assertion written with contaxt manger.
        # ? could this test be improved, do we need this. I say probably not needed.

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## *DONE* write a test that adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    ## TODO/working write a test that adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_add_some_example_students__removes_stundent_not_in_list(self):
        test_class = ClassList(4)
        test_class.add_student('Example')
        test_class.add_student('Another Example')
        with self.assertRaises(StudentError):
           test_class.remove_student('Example') 


    ## TODO write a test that removes a student from an 
    # empty list, and asserts a StudentError is raised



    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        # I love how the when adding notes the # is auto populating. 
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## *DONE* write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_is_none_if_classlist_is_empty(self):
        test_class = ClassList(2)  #Arranging.
        index = test_class.index_of_student('Test Student')  # Action.
        self.assertIsNone(index)  #Assert.
 
 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_when_class_list_is_not_empty(self):    
        test_class = ClassList(1)
        index =test_class.index_of_student()   
        self.assertIsNot(index)
   
    ## TODO write a test for your new is_class_full method when the class is full. 
    # use assertTrue.
    
    ## TODO write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.

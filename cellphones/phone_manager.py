"""
Dan Smestad ITEC 2905-80 Capstone Due: 2/3/2021.
Python Lab4. EXTRA CREDIT
Python testing your code. 

"""

# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None
        
        
    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)


class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self, max_phone):

        if max_phone > 1:
            raise PhoneError('Only one phone per employee allowed')

        self.phones = []
        self.employees = []
        self.max_phone = max_phone

       
    def add_employee(self, employee):
        # raise exception if two employees with same ID are added.
        if employee not in self.employees:
            self.employees.append(employee)
        else:    
            raise Exception('Employee %s already exixts, can\'t add again' % employee)
        

    def add_phone(self, phone):
        # raise exception if two phones with same ID are added.
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise PhoneError('Phone %s already exixts, can\'t add again' % phone)

    def assign(self, phone_id, employee):
        # Find phone in phones list:
        # if phone is already assigned to an employee, 
        # do not change list, raise exception                  
        # TODO if employee already has a phone, do not change list, 
        # and raise exception
        # TODO if employee already has this phone, don't make any 
        # changes. This should NOT raise an exception.
        for phone in self.phones:
            if phone.id in self.employees:
                raise PhoneError('Phone %s already assigned, can\'t assign' % phone_id)
            else:
                phone.assign(employee.id)    
        for employee in self.employees:
            if phone.id in self.phones:
                raise PhoneError('Phone already assined to employee, max phone is one' % employee)
            else:                
                phone.assign(employee.id)
        for phone in self.phones:
            if phone == phone:
                return
        # for phone in self.phones:
        #     if phone.id == phone_id:
        #         phone.assign(employee.id)
        #         return
           
       
    def un_assign(self, phone_id):
        # Finds phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO should return None if the employee does not have a phone
        # TODO the method should raise an exception if the employee 
        # does not exist

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None


class PhoneError(Exception):
    pass

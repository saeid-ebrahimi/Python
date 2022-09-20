class Teacher:
    def set_id(self, init_id):
        self.id = init_id

    def set_first_name(self, init_first_name):
        self.first_name = init_first_name

    def set_last_name(self, init_last_name):
        self.last_name = init_last_name

    def set_working_hours(self, init_working_hours):
        self.working_hours = init_working_hours

    def set_payment(self, base_payment):
        self.payment = base_payment

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_working_hours(self):
        return self.working_hours

    def get_payment(self):
        return self.payment
    
    def __init__(self, init_first_name='[unassigned]', init_last_name="[unassigned]",
                 init_id="[unassigned]", init_working_hours=0, init_payment=20000):
        self.id = init_id
        self.first_name = init_first_name
        self.last_name = init_last_name
        self.working_hours = init_working_hours
        self.payment = init_payment

    def total_payment(self):
        return self.working_hours * self.payment

    def __str__(self):
        s = '''Teacher characteristics: 
        full name: {} {}
        ID: {}
        total working hours: {}
        base payment: {}'''.format(self.first_name, self.last_name, self.id, self.working_hours, self.payment)

    teacher = Teacher()
    print(teacher)

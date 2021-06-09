class Term_instance:
    def __init__(self,term,reading,level):
        self.term = term
        self.reading = reading
        self.level = level

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self,pay)
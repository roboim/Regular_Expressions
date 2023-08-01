class Contact:
    def __init__(self, lastname='',firstname='', surname='', organization='', position='', phone='', email=''):
        self.lastname = lastname
        self.firstname = firstname
        self.surname = surname
        self.organization = organization
        self.position = position
        self.phone = phone
        self.email = email

    def __str__(self):
        return ' '.join([self.lastname, self.firstname, self.surname, self.organization,
                         self.position, self.phone, self.email])

    def check_fio(self):
        fields_fio = []
        if self.surname == '' and self.firstname == '':
            self.lastname = self.lastname.strip()
            fields_fio = self.lastname.split()
            if len(fields_fio) == 3:
                self.lastname = fields_fio[0]
                self.firstname = fields_fio[1]
                self.surname = fields_fio[2]
            elif len(fields_fio) == 2:
                self.lastname = fields_fio[0]
                self.firstname = fields_fio[1]

        elif self.surname == '' and self.firstname != '':
            fields_fio = self.lastname.split()
            if len(fields_fio) == 1:
                fields_fio = self.firstname.split()
                self.firstname = fields_fio[0]
                self.surname = fields_fio[1]
        # print(f'{self.lastname}, {self.firstname}, {self.surname}')
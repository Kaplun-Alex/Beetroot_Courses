class Mail:

    def __init__(self, mail: str):
        self.mail = mail
        self.type_ = str
        self.max_lenght = 64
        self.not_contains = ['-@', '@-', '.@', '@.', '#', '..', '@@']
        self.contains = ['@', '.']

    @property
    def validator(self):
        if type(self.mail) != self.type_:
            print('Not string')
            return False
        elif len(self.mail) >= self.max_lenght:
            print('To mutch symbols')
            return False
        elif self.mail[0] == '.' or self.mail[-1] == '.' or self.mail[-2] == '.':
            print('Це вобще зашквар братан')
            return False
        else:
            for i in self.not_contains:
                fnd = self.mail.find(i)
                if fnd != -1:
                    print('Error symbol find - ', i)
                    return False
                else:
                    pass
        for i in self.contains:
            fnd = self.mail.find(i)
            if fnd == -1:
                print('Mail symbol not find - ', i)
                return False
            else:
                pass
        return self.mail

m = Mail('alexzeu@ukr.net')
print(m.validator)

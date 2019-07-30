class User:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname

    def initials(self):
        return "{}. {}.".format(self.name[0],self.lastname[0])


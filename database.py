from mongoengine import connect, Document, StringField, IntField

connect('users')

class singleUserRegister(Document):
    email= StringField(required=True)
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    phoneNumber=IntField(required=True)
    college=StringField(required=True)
    competition= StringField(required=True)


class competition(Document):
    name= StringField(required=True)

class teamUserRegistration(Document):
    emailFive= StringField(required=True)
    firstNameFive = StringField(required=True)
    lastNameFive = StringField(required=True)
    phoneNumberFive=IntField(required=True)

    emailFour= StringField(required=True)
    firstNameFour = StringField(required=True)
    lastNameFour = StringField(required=True)
    phoneNumberFour=IntField(required=True)

    emailThree= StringField(required=True)
    firstNameThree = StringField(required=True)
    lastNameThree = StringField(required=True)
    phoneNumberThree=IntField(required=True)

    emailTwo= StringField(required=True)
    firstNameTwo = StringField(required=True)
    lastNameTwo = StringField(required=True)
    phoneNumberTwo=IntField(required=True)


    emailOne= StringField(required=True)
    firstNameOne = StringField(required=True)
    lastNameOne = StringField(required=True)
    phoneNumberOne=IntField(required=True)

    college=StringField(required=True)
    competition= StringField(required=True)
    

def addSingleRegistration(email,lastName,firstName,phoneNumber,college, competition):
    user = singleUserRegister(
        email = email,
        firstName = firstName,
        lastName = lastName,
        phoneNumber = phoneNumber,
        college = college,
        competition = competition
    ).save()


def compAdd(name):
    comp= competition(
        competition=name
    )

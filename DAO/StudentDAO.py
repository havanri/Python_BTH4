import  abc
from Entities.Student import Student
class StudentDAO(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(student : Student):
        pass

    @abc.abstractmethod
    def update(student : Student):
        pass

    @abc.abstractmethod
    def delete(studentId : int):
        pass

    @abc.abstractmethod
    def findById(studentId : int):
        pass

    @abc.abstractmethod
    def findAll(self):
        pass


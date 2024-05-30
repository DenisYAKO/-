import unittest
from abc import ABC, abstractmethod

class Hospital(ABC):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.__patients = []

    @property
    def patients(self):
        return self.__patients

    @abstractmethod
    def admit_patient(self, patient_name):
        pass

    @abstractmethod
    def discharge_patient(self, patient_name):
        pass

class PediatricHospital(Hospital):

    def __init__(self, name, capacity, pediatric_capacity):
        super().__init__(name, capacity)
        self.__pediatric_capacity = pediatric_capacity
        self.__pediatric_patients = []

    @property
    def pediatric_patients(self):
        return self.__pediatric_patients

    def admit_patient(self, patient_name):
        if len(self.patients) < self.capacity:
            self.patients.append(patient_name)
            print(f"Пациент {patient_name} принят в больницу {self.name}.")
            return True
        else:
            print(f"Невозможно принять пациента {patient_name}: больница {self.name} заполнена.")
            return False

    def discharge_patient(self, patient_name):
        if patient_name in self.patients:
            self.patients.remove(patient_name)
            print(f"Пациент {patient_name} выписан из больницы {self.name}.")
            return True
        else:
            print(f"Пациент {patient_name} не найден в больнице {self.name}.")
            return False

    def admit_pediatric_patient(self, patient_name):
        if len(self.pediatric_patients) < self.__pediatric_capacity:
            self.__pediatric_patients.append(patient_name)
            self.patients.append(patient_name)
            print(f"Пациент {patient_name} выписан из больницы {self.name}.")
            return True
        else:
            print(f"Невозможно принять пациента {patient_name}: больница {self.name} заполнена.")
            return False

    def discharge_pediatric_patient(self, patient_name):
        if patient_name in self.pediatric_patients:
            self.__pediatric_patients.remove(patient_name)
            self.patients.remove(patient_name)
            print(f"Пациент {patient_name} выписан из больницы {self.name}.")
            return True
        else:
            print(f"Пациент {patient_name} не найден в больнице {self.name}.")
            return False

class SurgicalHospital(Hospital):

    def __init__(self, name, capacity, surgical_capacity):
        super().__init__(name, capacity)
        self.__surgical_capacity = surgical_capacity
        self.__surgical_patients = []

    @property
    def surgical_patients(self):
        return self.__surgical_patients

    def admit_patient(self, patient_name):
        if len(self.patients) < self.capacity:
            self.patients.append(patient_name)
            print(f"Пациент {patient_name} принят в больницу {self.name}.")
            return True
        else:
            print(f"Невозможно принять пациента {patient_name}: больница {self.name} заполнена.")
            return False

    def discharge_patient(self, patient_name):
        if patient_name in self.patients:
            self.patients.remove(patient_name)
            print(f"Пациент {patient_name} выписан из больницы {self.name}.")
            return True
        else:
            print(f"Пациент {patient_name} не найден в больнице {self.name}.")
            return False

    def admit_surgical_patient(self, patient_name):
        if len(self.surgical_patients) < self.__surgical_capacity:
            self.__surgical_patients.append(patient_name)
            self.patients.append(patient_name)
            return True
        else:
            return False

    def discharge_surgical_patient(self, patient_name):
        if patient_name in self.surgical_patients:
            self.__surgical_patients.remove(patient_name)
            self.patients.remove(patient_name)
            return True
        else:
            return False

class Mental_Health_Clinic(Hospital):
    __slots__ = ('__name',)

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def print_name(self):
        print("Психиатрическая клиника называется: ", self.name)

    def admit_patient(self, patient_name):
        print("Невозможно принять пациента в психиатрическую клинику.")

    def discharge_patient(self, patient_name):
        print("Невозможно выписать пациента из психиатрической клиники.")

my_clinic = Mental_Health_Clinic("Психиатрическая больница")
my_clinic.print_name()

class TestHospital(unittest.TestCase):

    def test_admit_patient(self):
        pediatric_hospital = PediatricHospital("PediatricHospital", 5, 2)
        self.assertTrue(pediatric_hospital.admit_patient("John"))

    def test_discharge_patient(self):
        pediatric_hospital = PediatricHospital("PediatricHospital", 5, 2)
        pediatric_hospital.admit_patient("John")
        self.assertTrue(pediatric_hospital.discharge_patient("John"))

    def test_admit_pediatric_patient(self):
        pediatric_hospital = PediatricHospital("PediatricHospital", 5, 2)
        self.assertTrue(pediatric_hospital.admit_pediatric_patient("Peter"))

    def test_discharge_pediatric_patient(self):
        pediatric_hospital = PediatricHospital("PediatricHospital", 5, 2)
        pediatric_hospital.admit_pediatric_patient("Peter")
        self.assertTrue(pediatric_hospital.discharge_pediatric_patient("Peter"))

    def test_admit_surgical_patient(self):
        surgical_hospital = SurgicalHospital("SurgicalHospital", 5, 3)
        self.assertTrue(surgical_hospital.admit_surgical_patient("Mike"))

    def test_discharge_surgical_patient(self):
        surgical_hospital = SurgicalHospital("SurgicalHospital", 5, 3)
        surgical_hospital.admit_surgical_patient("Mike")
        self.assertTrue(surgical_hospital.discharge_surgical_patient("Mike"))

if __name__ == '__main__':
    unittest.main(buffer=False)
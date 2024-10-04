from datetime import date
from enum import Enum


class StatusOrder(Enum):
    RECEIVE = "RECEIVE"
    ON_PROGRESS = "ON_PROGRESS"
    PARTS_WAIT = "PARTS_WAIT"
    DELIVERY = "DELIVERY"


class Problem(Enum):
    BROKEN_DISPLAY = "BROKEN_DISPLAY"
    SOFTWARE_ISSUE = "SOFTWARE_ISSUE"
    BATTERY_CHANGE = "BATTERY_CHANGE"


class Persona:
    def __init__(self, rut, first_name, last_name, email, phone):
        self.rut = rut
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


class Tech(Persona):
    def __init__(self, rut, first_name, last_name, email, phone, speciality):
        super().__init__(rut, first_name, last_name, email, phone)
        self.speciality = speciality


class Client(Persona):
    def __init__(self, rut, first_name, last_name, email, phone):
        super().__init__(rut, first_name, last_name, email, phone)
        self.devices = []

    def register_device(self, device):
        self.devices.append(device)


class Device:
    def __init__(self, brand, model, problem):
        self.brand = brand
        self.model = model
        self.problem = problem


class WorkOrder:
    def __init__(self, tech, device):
        self.tech = tech
        self.device = device
        self.diagnosis = None
        self.startDate = date.today()
        self.endDate = None
        self.status = StatusOrder.RECEIVE

    def change_status(self, status):
        self.status = status

    def do_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis


class WorkShop:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.techs = []
        self.workOrders = []

    def register_clients(self, client):
        self.clients.append(client)

    def register_techs(self, tech):
        self.techs.append(tech)

    def register_order(self, order):
        self.workOrders.append(order)

    def get_report_devices(self):
        report = {}
        for work in self.workOrders:
            if work.device.model not in report:
                report[work.device.model] = 0

            report[work.device.model] += 1
        return report

    def get_report_techs(self):
        pass


taller = WorkShop("One parts")
client1 = Client("1", "Juan", "Amarantis", "juan@gmail.com", "000")

movil1 = Device("Iphone", "Apple", Problem.BATTERY_CHANGE)
movil2 = Device("Table", "Apple", Problem.SOFTWARE_ISSUE)


client1.register_device(movil1)
client1.register_device(movil2)


tech1 = Tech("2", "Maria", "Perez", "maria@gmail.com", "111", Problem.BATTERY_CHANGE)
orden1 = WorkOrder(tech1, movil1)
orden2 = WorkOrder(tech1, movil2)
taller.register_order(orden1)
taller.register_order(orden2)


print(taller.get_report_devices())

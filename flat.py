class Bill:
    """"
    Object that contains data abaut bill,
    such as total amaunt and period of the bill
    """

    def __init__(self, amaunt, period):
        self.amaunt = amaunt
        self.period = period


class Flatmate:
    """"
    Create flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amaunt * weight
        return to_pay

from enum import Enum


class MetricType(Enum):

    PRICE = "price"
    COUNT = "count"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
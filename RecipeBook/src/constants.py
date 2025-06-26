from enum import StrEnum, auto

class DietaryTag(StrEnum):
    VEGAN = auto()
    VEGETARIAN = auto()
    GLUTEN_FREE = auto()
    NUT_FREE = auto()
    NON_VEGETARIAN = auto()
    NOT_APPLICABLE = auto()

class MeasurementUnits(StrEnum):
    OZ = auto()
    COUNT = auto()
    CUP = auto()
    TEA_SPOON = "tsp"
    TABLE_SPOON = "tbsp"
    TO_TASTE = auto()
    GM = auto()
    ML = auto()

    @classmethod
    def from_str(cls, unit):
        return cls(unit)
    

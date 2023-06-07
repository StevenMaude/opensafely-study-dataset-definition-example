from ehrql import Dataset
from ehrql.tables.beta.tpp import patients

dataset = Dataset()
dataset.define_population(patients.date_of_birth.is_on_or_before("1999-12-31"))

dataset.year_of_birth = patients.date_of_birth.year

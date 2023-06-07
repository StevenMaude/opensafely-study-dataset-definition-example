from ehrql import Dataset
from ehrql.tables.beta.tpp import open_prompt, patients

dataset = Dataset()
dataset.define_population(patients.date_of_birth.is_on_or_before("1999-12-31"))

most_recent_consultation = (
    open_prompt.sort_by(open_prompt.consultation_date)
    .last_for_patient()
    .consultation_date
)

dataset.most_recent_consultation = most_recent_consultation

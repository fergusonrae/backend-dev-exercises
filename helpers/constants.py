FLATTEN_SQL = """
    SELECT records.id, records.relationship_id, records.age, records.education_num, records.capital_gain, records.capital_loss,
    records.hours_week, records.over_50k, workclasses.name as workclass, education_levels.name as education_level,
    marital_statuses.name as marital_status, occupations.name as occupation, races.name as race,
    sexes.name as sex, countries.name as country
    FROM records
    LEFT JOIN workclasses ON records.workclass_id = workclasses.id
    LEFT JOIN education_levels ON records.education_level_id = education_levels.id
    LEFT JOIN marital_statuses ON records.marital_status_id = marital_statuses.id
    LEFT JOIN occupations ON records.occupation_id = occupations.id
    LEFT JOIN races ON records.race_id = races.id
    LEFT JOIN sexes ON records.sex_id = sexes.id
    LEFT JOIN countries ON records.country_id = countries.id
    """
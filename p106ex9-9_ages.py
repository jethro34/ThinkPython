
matches = 0

for diff in range(13, 51):
    for d_age in range(1, 100):
        d_age_str = str(d_age).zfill(2)
        m_age_str = str(d_age + diff)
        if d_age_str == m_age_str[::-1]:
            matches += 1
            if matches == 6:
                likely_d_age = d_age_str
            elif matches == 8:
                print("the daughter was", likely_d_age, "years-old.")

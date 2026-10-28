import csv
import random

# Set random seed for reproducibility
random.seed(42)

job_titles_by_dept = {
    "Data & Analytics": ["Data Analyst", "Data Scientist", "Analytics Engineer", "Data Analytics Manager"],
    "Machine Learning & AI": ["Machine Learning Engineer", "AI Architect", "ML Ops Engineer", "Research Scientist"],
    "Data Engineering": ["Data Engineer", "Big Data Engineer", "Data Architect", "ETL Developer"],
    "Business Intelligence": ["BI Developer", "BI Analyst", "Tableau Specialist", "BI Manager"],
    "Enterprise Software": ["Software Engineer", "Cloud Architect", "Solutions Architect", "Tech Lead"]
}

exp_levels = ["EN", "MI", "SE", "EX"]
exp_weights = [0.15, 0.35, 0.40, 0.10] # Entry, Mid, Senior, Executive

emp_types = ["FT", "PT", "CT", "FL"]
emp_type_weights = [0.90, 0.04, 0.04, 0.02]

company_sizes = ["S", "M", "L"]
company_size_weights = [0.20, 0.55, 0.25]

remote_ratios = [0, 50, 100]
remote_weights = [0.30, 0.25, 0.45]

work_years = [2021, 2022, 2023, 2024]
year_weights = [0.15, 0.25, 0.30, 0.30]

education_levels = ["Bachelor's", "Master's", "Doctorate"]
edu_weights_by_exp = {
    "EN": [0.70, 0.25, 0.05],
    "MI": [0.55, 0.38, 0.07],
    "SE": [0.40, 0.48, 0.12],
    "EX": [0.25, 0.55, 0.20]
}

countries = [
    ("United States", "US", "USD", 1.0),
    ("United Kingdom", "GB", "GBP", 1.27),
    ("Germany", "DE", "EUR", 1.09),
    ("Canada", "CA", "CAD", 0.74),
    ("India", "IN", "INR", 0.012),
    ("Australia", "AU", "AUD", 0.66),
    ("France", "FR", "EUR", 1.09),
    ("Spain", "ES", "EUR", 1.09),
    ("Singapore", "SG", "USD", 1.0),
    ("Netherlands", "NL", "EUR", 1.09)
]

country_weights = [0.45, 0.12, 0.10, 0.08, 0.08, 0.05, 0.04, 0.03, 0.03, 0.02]

# Base salary range in USD by role level
base_salary_ranges = {
    "EN": (55000, 95000),
    "MI": (90000, 145000),
    "SE": (135000, 210000),
    "EX": (195000, 340000)
}

# Role multiplier
role_multipliers = {
    "AI Architect": 1.30,
    "Data Architect": 1.25,
    "Research Scientist": 1.22,
    "Machine Learning Engineer": 1.18,
    "Data Analytics Manager": 1.15,
    "Data Science Manager": 1.20,
    "BI Manager": 1.10,
    "Cloud Architect": 1.20,
    "Tech Lead": 1.22,
    "Data Scientist": 1.08,
    "Data Engineer": 1.06,
    "ML Ops Engineer": 1.12,
    "Solutions Architect": 1.18,
    "Analytics Engineer": 1.02,
    "BI Developer": 0.95,
    "Data Analyst": 0.88,
    "BI Analyst": 0.85,
    "Tableau Specialist": 0.90,
    "ETL Developer": 0.92,
    "Big Data Engineer": 1.10,
    "Software Engineer": 1.00
}

data = []
num_records = 1050

for i in range(1, num_records + 1):
    emp_id = f"EMP{i:04d}"
    year = random.choices(work_years, weights=year_weights)[0]
    exp = random.choices(exp_levels, weights=exp_weights)[0]
    emp_type = random.choices(emp_types, weights=emp_type_weights)[0]
    
    # Department & Role
    dept = random.choice(list(job_titles_by_dept.keys()))
    job_title = random.choice(job_titles_by_dept[dept])
    
    # Country & Location
    country_info = random.choices(countries, weights=country_weights)[0]
    emp_residence, country_code, currency, ex_rate = country_info
    comp_location = emp_residence if random.random() < 0.88 else random.choice(countries)[0]
    
    company_size = random.choices(company_sizes, weights=company_size_weights)[0]
    remote_ratio = random.choices(remote_ratios, weights=remote_weights)[0]
    
    edu_level = random.choices(education_levels, weights=edu_weights_by_exp[exp])[0]
    
    # Salary calculation in USD
    low, high = base_salary_ranges[exp]
    base_usd = random.randint(low, high)
    
    # Apply multipliers
    multiplier = role_multipliers.get(job_title, 1.0)
    
    # Year growth factor (e.g. 2021: 0.90, 2024: 1.12)
    year_factor = 1.0 + (year - 2022) * 0.06
    
    # Remote bonus (fully remote roles get slight boost)
    remote_factor = 1.05 if remote_ratio == 100 else (1.02 if remote_ratio == 50 else 1.0)
    
    # Size factor
    size_factor = 1.08 if company_size == "L" else (1.02 if company_size == "M" else 0.95)
    
    # Education factor
    edu_factor = 1.08 if edu_level == "Doctorate" else (1.04 if edu_level == "Master's" else 1.0)
    
    # Country economic factor
    geo_factor = 1.0 if country_code == "US" else (0.85 if country_code in ["GB", "DE", "CA", "AU", "NL"] else 0.35 if country_code == "IN" else 0.80)
    
    final_usd = int(base_usd * multiplier * year_factor * remote_factor * size_factor * edu_factor * geo_factor)
    
    # Calculate local currency salary
    local_salary = int(final_usd / ex_rate) if currency != "USD" else final_usd
    
    data.append([
        emp_id,
        year,
        exp,
        emp_type,
        job_title,
        local_salary,
        currency,
        final_usd,
        emp_residence,
        remote_ratio,
        comp_location,
        company_size,
        dept,
        edu_level
    ])

headers = [
    "Employee_ID",
    "Work_Year",
    "Experience_Level",
    "Employment_Type",
    "Job_Title",
    "Salary",
    "Salary_Currency",
    "Salary_in_USD",
    "Employee_Residence",
    "Remote_Ratio",
    "Company_Location",
    "Company_Size",
    "Department",
    "Education_Level"
]

csv_file_path = r"C:\Users\ommis\.gemini\antigravity-ide\scratch\salary-analysis-dashboard\salary_analysis_dataset.csv"

with open(csv_file_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Successfully generated {len(data)} records in {csv_file_path}")

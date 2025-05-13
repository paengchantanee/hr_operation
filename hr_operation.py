# Input
total_emp = int(input("Total employees: "))
avg_hr_salary = int(input("Average HR salary: "))
industry =input("Industry(general, manufacturing, it, service): ")

# Number of employees per one HR
emp_per_hr = {
    'general': 100,
    'manufacturing': 120,
    'it': 80,
    'service': 90
}

# HR ratio
payroll_percent = 0.4
recruitment_percent = 0.6

# HR reduction ratio
payroll_reduction = 0.4
recruitment_reduction = 0.3

# Total number of HR before reduction
total_hr = round(total_emp / emp_per_hr[industry])

payroll_hr = total_hr * payroll_percent
recruitment_hr = total_hr * recruitment_percent
# Cost before reduction
cost_before = total_hr * avg_hr_salary

# Total number of HR after reduction
payroll_after = round(payroll_hr * (1 - payroll_reduction))
recruitment_after = round(recruitment_hr * (1 - recruitment_reduction))

total_hr_after = payroll_after + recruitment_after
# Cost after reduction
cost_after = total_hr_after * avg_hr_salary

# Cost saving and reduction percentage
cost_saving = cost_before - cost_after
reduction_percent = ((total_hr - total_hr_after) / total_hr) * 100

print()
print(f"HR needed: {total_hr} (Payroll: {round(payroll_hr)}, Recruitment: {round(recruitment_hr)})")
print(f"Cost before automation: {cost_before:,} THB/month")
print()
print(f"HR after automation: {total_hr_after} (Payroll: {payroll_after}, Recruitment: {recruitment_after})")
print(f"Cost after automation: {cost_after:,} THB/month")
print(f"Cost saved: {cost_saving:,} THB/month")
print(f"HR reduced: {reduction_percent:.1f}%")
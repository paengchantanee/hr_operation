# hr_cost_calculator.py
import streamlit as st

st.title("HR Cost Reduction Calculator")

total_emp = st.number_input("Total employees", min_value=1, value=100)
avg_hr_salary = st.number_input("Average HR salary (THB/month)", min_value=1, value=30000)
industry = st.selectbox("Industry", ['general', 'manufacturing', 'it', 'service'])

emp_per_hr = {
    'general': 100,
    'manufacturing': 120,
    'it': 80,
    'service': 90
}

payroll_percent = 0.4
recruitment_percent = 0.6

payroll_reduction = 0.4
recruitment_reduction = 0.3

if industry:
    total_hr = round(total_emp / emp_per_hr[industry])

    payroll_hr = total_hr * payroll_percent
    recruitment_hr = total_hr * recruitment_percent

    cost_before = total_hr * avg_hr_salary

    payroll_after = round(payroll_hr * (1 - payroll_reduction))
    recruitment_after = round(recruitment_hr * (1 - recruitment_reduction))

    total_hr_after = payroll_after + recruitment_after
    cost_after = total_hr_after * avg_hr_salary

    cost_saving = cost_before - cost_after
    reduction_percent = ((total_hr - total_hr_after) / total_hr) * 100

    st.subheader("📊 Results")
    st.write(f"**HR needed:** {total_hr} (Payroll: {round(payroll_hr)}, Recruitment: {round(recruitment_hr)})")
    st.write(f"**Cost before automation:** {cost_before:,.0f} THB/month")
    st.write("---")
    st.write(f"**HR after automation:** {total_hr_after} (Payroll: {payroll_after}, Recruitment: {recruitment_after})")
    st.write(f"**Cost after automation:** {cost_after:,.0f} THB/month")
    st.write(f"**Cost saved:** {cost_saving:,.0f} THB/month")
    st.write(f"**HR reduced:** {reduction_percent:.1f}%")

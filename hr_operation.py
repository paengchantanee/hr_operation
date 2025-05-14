import streamlit as st

st.title("HR Operation")

total_emp = st.number_input("Total employees", min_value=1, value=500)
avg_hr_salary = st.number_input("Average HR salary (THB/month)", min_value=15000, value=35000)
#industry = st.selectbox("Industry", ['general', 'manufacturing', 'it', 'service'])

'''
emp_per_hr = {
    'general': 100,
    'manufacturing': 120,
    'it': 80,
    'service': 90
}
'''
emp_per_hr = 100

productivity_gain = 0.3

#if industry:

    #total_hr = round(total_emp / emp_per_hr[industry])
total_hr = round(total_emp / emp_per_hr)
cost_before = total_hr * avg_hr_salary

total_hr_after = round(total_hr / (1+productivity_gain))
cost_after = total_hr_after * avg_hr_salary

cost_saving = cost_before - cost_after
reduction_percent = ((total_hr - total_hr_after) / total_hr) * 100

st.subheader("Results")
st.write(f"**HR needed:** {total_hr}")
st.write(f"**Cost before automation:** {cost_before:,.0f} THB/month")
st.write("---")
st.write(f"**HR after automation:** {total_hr_after}")
st.write(f"**Cost after automation:** {cost_after:,.0f} THB/month")
st.write(f"**Cost saved:** {cost_saving:,.0f} THB/month")
st.write(f"**HR reduced:** {reduction_percent:.1f}%")

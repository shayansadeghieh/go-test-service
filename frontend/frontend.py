import streamlit as st
from fastapi import FastAPI

app = FastAPI() 

@app.post("/update")
def update_test(passed: bool):
    test_status(passed)    
    return 

def test_status(test_passed):
    if test_passed:
        return '<div style="background-color:#00FF00;height:20px;width:20px;border-radius:50%;"></div>'
    else:
        return '<div style="background-color:#FF0000;height:20px;width:20px;border-radius:50%;"></div>'

# Sample data
test_results = {
    "Test 1": True,
    "Test 2": True,
    "Test 3": True,
    "Test 4": False,
    "Test 5": True
}

# Display the table
st.write("<h2>Integration  Results</h2>", unsafe_allow_html=True)
st.write("<style>table {border-collapse: collapse;} th, td {border: 1px solid black;padding: 8px;text-align: center;}</style>", unsafe_allow_html=True)
st.write("<table><tr><th>Test</th><th>Status</th></tr>", unsafe_allow_html=True)
for test, status in test_results.items():
    st.write("<tr><td>{}</td><td>{}</td></tr>".format(test, test_status(status)), unsafe_allow_html=True)
st.write("</table>", unsafe_allow_html=True)
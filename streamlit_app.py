import streamlit as st

st.set_page_config(
    page_title="Smart College Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Smart College Assistant")
st.write("College Utilities Dashboard")

menu = st.sidebar.selectbox(
    "Select Tool",
    [
        "Attendance Calculator",
        "Result Calculator",
        "Fee Balance Calculator",
        "Library Fine Calculator",
        "Hostel Fee Calculator",
        "Student Information"
    ]
)

# ==========================
# ATTENDANCE
# ==========================

if menu == "Attendance Calculator":

    st.header("Attendance Calculator")

    total = st.number_input(
        "Total Classes",
        min_value=1
    )

    attended = st.number_input(
        "Attended Classes",
        min_value=0
    )

    if st.button("Calculate Attendance"):

        percentage = (attended / total) * 100

        st.success(
            f"Attendance: {percentage:.2f}%"
        )

        if percentage >= 75:
            st.info("Eligible for Exam")
        else:
            st.error("Not Eligible for Exam")

# ==========================
# RESULT
# ==========================

elif menu == "Result Calculator":

    st.header("Result Calculator")

    m1 = st.number_input("Subject 1 Marks")
    m2 = st.number_input("Subject 2 Marks")
    m3 = st.number_input("Subject 3 Marks")
    m4 = st.number_input("Subject 4 Marks")
    m5 = st.number_input("Subject 5 Marks")

    if st.button("Calculate Result"):

        avg = (m1 + m2 + m3 + m4 + m5) / 5

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"

        result = "Pass" if avg >= 50 else "Fail"

        st.success(f"Average Marks: {avg:.2f}")
        st.info(f"Grade: {grade}")
        st.info(f"Result: {result}")

# ==========================
# FEE BALANCE
# ==========================

elif menu == "Fee Balance Calculator":

    st.header("Fee Balance Calculator")

    total_fee = st.number_input(
        "Total Fee"
    )

    paid_fee = st.number_input(
        "Paid Fee"
    )

    if st.button("Calculate Balance"):

        balance = total_fee - paid_fee

        st.success(
            f"Pending Fee: ₹{balance}"
        )

# ==========================
# LIBRARY FINE
# ==========================

elif menu == "Library Fine Calculator":

    st.header("Library Fine Calculator")

    days = st.number_input(
        "Delayed Days",
        min_value=0
    )

    if st.button("Calculate Fine"):

        fine = days * 5

        st.success(
            f"Fine Amount: ₹{fine}"
        )

# ==========================
# HOSTEL FEE
# ==========================

elif menu == "Hostel Fee Calculator":

    st.header("Hostel Fee Calculator")

    monthly_fee = st.number_input(
        "Monthly Hostel Fee"
    )

    months = st.number_input(
        "Months Stayed",
        min_value=1
    )

    if st.button("Calculate Hostel Fee"):

        total = monthly_fee * months

        st.success(
            f"Total Hostel Fee: ₹{total}"
        )

# ==========================
# STUDENT INFO
# ==========================

elif menu == "Student Information":

    st.header("Student Information")

    students = {

        "101": {
            "Name": "Rahul",
            "Branch": "CSE",
            "Year": "3rd"
        },

        "102": {
            "Name": "Priya",
            "Branch": "ECE",
            "Year": "2nd"
        },

        "103": {
            "Name": "Amit",
            "Branch": "IT",
            "Year": "4th"
        }
    }

    student_id = st.text_input(
        "Enter Student ID"
    )

    if st.button("Get Student Details"):

        if student_id in students:

            st.success(
                "Student Found"
            )

            st.json(
                students[student_id]
            )

        else:

            st.error(
                "Student Not Found"
            )
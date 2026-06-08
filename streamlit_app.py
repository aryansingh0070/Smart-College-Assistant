import streamlit as st

st.set_page_config(page_title="Smart College Assistant", page_icon="🎓")

st.title("🎓 Smart College Assistant")

menu = st.sidebar.selectbox(
    "Select Tool",
    [
        "Attendance Calculator",
        "Result Calculator",
        "Library Fine Calculator"
    ]
)

if menu == "Attendance Calculator":

    st.header("Attendance Calculator")

    total = st.number_input("Total Classes", min_value=1)

    attended = st.number_input("Attended Classes", min_value=0)

    if st.button("Calculate Attendance"):

        percentage = (attended / total) * 100

        st.success(f"Attendance: {percentage:.2f}%")

        if percentage >= 75:
            st.info("Eligible for Exam")
        else:
            st.error("Not Eligible for Exam")

elif menu == "Result Calculator":

    st.header("Result Calculator")

    m1 = st.number_input("Subject 1 Marks")
    m2 = st.number_input("Subject 2 Marks")
    m3 = st.number_input("Subject 3 Marks")
    m4 = st.number_input("Subject 4 Marks")
    m5 = st.number_input("Subject 5 Marks")

    if st.button("Calculate Result"):

        avg = (m1 + m2 + m3 + m4 + m5) / 5

        st.success(f"Average Marks: {avg:.2f}")

elif menu == "Library Fine Calculator":

    st.header("Library Fine Calculator")

    days = st.number_input("Delayed Days", min_value=0)

    if st.button("Calculate Fine"):

        fine = days * 5

        st.success(f"Fine Amount: ₹{fine}")
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate


# ==========================
# ATTENDANCE TOOL
# ==========================

@tool
def attendance_calculator(total_classes: int, attended_classes: int):
    """
    Calculate attendance percentage and exam eligibility.
    """

    percentage = (attended_classes / total_classes) * 100

    status = (
        "Eligible for Exam"
        if percentage >= 75
        else "Not Eligible for Exam"
    )

    return {
        "Attendance Percentage": round(percentage, 2),
        "Status": status
    }


# ==========================
# RESULT TOOL
# ==========================

@tool
def result_calculator(
    m1: int,
    m2: int,
    m3: int,
    m4: int,
    m5: int
):
    """
    Calculate average marks, grade and pass/fail status.
    """

    avg = (m1 + m2 + m3 + m4 + m5) / 5

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"

    result = (
        "Pass"
        if avg >= 50
        else "Fail"
    )

    return {
        "Average": avg,
        "Grade": grade,
        "Result": result
    }


# ==========================
# FEE BALANCE TOOL
# ==========================

@tool
def fee_balance_calculator(
    total_fee: float,
    amount_paid: float
):
    """
    Calculate pending fee amount.
    """

    pending = total_fee - amount_paid

    return {
        "Pending Fee": pending
    }


# ==========================
# LIBRARY FINE TOOL
# ==========================

@tool
def library_fine_calculator(
    delayed_days: int
):
    """
    Calculate library fine.
    """

    fine = delayed_days * 5

    return {
        "Fine Amount": fine
    }


# ==========================
# HOSTEL FEE TOOL
# ==========================

@tool
def hostel_fee_calculator(
    monthly_fee: float,
    months: int
):
    """
    Calculate hostel fee.
    """

    total = monthly_fee * months

    return {
        "Total Hostel Fee": total
    }


# ==========================
# BONUS TOOL
# ==========================

students = {
    "101": {
        "name": "Rahul",
        "branch": "CSE",
        "year": "3rd"
    },
    "102": {
        "name": "Priya",
        "branch": "ECE",
        "year": "2nd"
    }
}


@tool
def student_information(student_id: str):
    """
    Retrieve student details using Student ID.
    """

    students = {
        "101": {
            "name": "Rahul",
            "branch": "CSE",
            "year": "3rd"
        },
        "102": {
            "name": "Priya",
            "branch": "ECE",
            "year": "2nd"
        }
    }

    if student_id in students:
        student = students[student_id]

        return f"""
Student Found

Name: {student['name']}
Branch: {student['branch']}
Year: {student['year']}
"""

    return "Student Not Found"

# ==========================
# LLM
# ==========================

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# ==========================
# PROMPT
# ==========================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an AI College Assistant.

            Analyze the user query.

            Automatically choose the correct tool.

            If multiple calculations are required,
            use multiple tools and combine results.
            """
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)


# ==========================
# TOOLS LIST
# ==========================

tools = [
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_information
]


# ==========================
# AGENT
# ==========================

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# ==========================
# TEST QUERY
# ==========================
response = agent_executor.invoke(
    {
        "input":
        "Get details of student ID 101"
    }
)

print("\n")
print("=" * 50)
print("FINAL OUTPUT")
print("=" * 50)
print(response["output"])
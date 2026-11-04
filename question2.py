import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Marks Analysis System")
st.write("Course: Python Programming")

names = []
genders = []
marks = []

for i in range(3):
    st.subheader("Student " + str(i + 1))

    name = st.text_input("Student Name", key="name" + str(i))

    gender = st.radio(
        "Gender", ["Male", "Female"], key="gender" + str(i)
    )

    mark = st.number_input(
        "Marks", min_value=0, max_value=100,
        value=0, step=1, key="marks" + str(i)
    )

    names.append(name.strip())
    genders.append(gender)
    marks.append(mark)

if st.button("Submit"):
    try:
        if "" in names:
            raise ValueError("Student name cannot be empty.")

        marks_array = np.array(marks)
        mean_marks = np.mean(marks_array)
        maximum_marks = np.max(marks_array)

        results = []

        for mark in marks:
            if mark >= 50:
                results.append("Pass")
            else:
                results.append("Fail")

        df = pd.DataFrame({
            "Name": names,
            "Gender": genders,
            "Course": ["Python Programming"] * 3,
            "Marks": marks_array,
            "Result": results
        })

        st.subheader("Student Data")
        st.dataframe(df)

        st.subheader("Analysis")
        st.write(f"Mean Marks: {mean_marks:.2f}")
        st.write(f"Maximum Marks: {maximum_marks}")

        sorted_df = df.sort_values("Marks", ascending=True)

        st.subheader("Sorted Student Records")
        st.dataframe(sorted_df)

        st.subheader("Marks Graph")

        plt.figure()
        plt.bar(range(3), marks_array, color="royalblue")
        plt.xticks(range(3), names)
        plt.xlabel("Student")
        plt.ylabel("Marks")
        plt.title("Student Marks")
        plt.ylim(0, 100)

        st.pyplot(plt.gcf())
        plt.close()

    except ValueError as error:
        st.error(str(error))
        
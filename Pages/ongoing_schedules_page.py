import Scripts.Utilities as Utils
from Scripts.constants import *
from annotated_text import annotated_text
from Scripts.data_loader import get_appointment_data, get_doctors_data, get_users_data

def add_info(container, title, content, label, is_doctor):
    # TODO :- Dark Theme Not Working
    # for colour palette reference :- https://material.io/archive/guidelines/style/color.html#color-color-palette

    
    Utils.add_space(container)

    if is_doctor:
        background = "#00E5FF"
        color = "black"
    else:
        background = "#C6FF00"
        color = "black"

    with container:
        annotated_text(
                (title, label, background, color)
        )

        annotated_text(
                (content, "APPOINTMENT BOOKED", "inherit", "inherit")
        )

def set_headings(container, title):
    if title == "Patients":
        color = "#C6FF00"
    else:
        color = "#00E5FF"


    Utils.website_heading(
        container,
        content=title,
        symbol=".",
        font_size=40,
        color=color,
        text_align="center"
    )


def show_ongoing_schedules_page(st):
    Utils.website_heading(
        st,
        content="Our Ongoing Schedules",
        symbol="📅",
        font_size=60,
        color="goldenrod",
        text_align="center"
    )

    Utils.add_space(st)

    patient_container, doctor_container = st.columns(2)

    set_headings(patient_container, "Patients")
    set_headings(doctor_container, "Doctors")


    appointment_data = get_appointment_data()
    patient_data = get_users_data()
    doctor_data = get_doctors_data()

    for doctor_id, value in appointment_data.items():
        if value["schedule"]:
            for schedule_date in value["schedule"].keys():
                for schedule_time, patient_id in value["schedule"][schedule_date].items():

                    add_info(
                        patient_container,
                        title=patient_data[patient_id]["name"],
                        content="User {} has booked an appointment with doctor {} on {} at {}".format(patient_data[patient_id]["name"], doctor_data[doctor_id]["name"], schedule_date, schedule_time),
                        label=f"@{patient_id}",
                        is_doctor=False
                    )

                    add_info(
                        doctor_container,
                        title=doctor_data[doctor_id]["name"],
                        content="Doctor {} has been alloted an appointment with patient {} on {} at {}".format(doctor_data[doctor_id]["name"], patient_data[patient_id]["name"], schedule_date, schedule_time),
                        label=f"@{doctor_id}",
                        is_doctor=True
                    )

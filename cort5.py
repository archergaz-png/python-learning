def student_info(name, surname, fathername, *subjects, **details):
    print("ФИО:", name, surname, fathername )
    print("Предметы:", subjects)
    print("Дополнительно:", details)

student_info(
    "Иван", "Васильев", "Петрович", 
    "математика",
    "физика",
    age=18,
    group="10А"
)
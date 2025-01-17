from tika import parser
from os import listdir


def main():
    for file in listdir("static"):
        file_path = "static/" + file
        file_name = file.split(".")[0]

        if file_name in ["Кротов_Царская дорога 1702",
                         "7-й_Конгресс_18",
                         "Кротов_Матросы поморы", "Документы_Петровский_Петергоф_Том_2",
                         "Документы_Петровский_Петергоф_Том_1",
                         "Павленко", "Майкова_Военные_журналы_юрналы_Петра_1",
                         "История_отечественного_судостроение_Т_1_",
                         "7-й_Конгресс_18мая_compressed",
                         "Майкова_Военные_журналы_юрналы_Петра_1",] or file_path.endswith(".djvu"):
            continue

        print("Try parsing " + file_name)
        pdf_text = parser.from_file(file_path)["content"]
        pdf_text = pdf_text.encode("latin", errors="replace").decode("windows-1251")
        print("saving " + file_name)

        with open(f"res1/{file_name}.txt", "w", encoding="utf-8") as f:
            f.write(pdf_text)


if __name__ == '__main__':
    main()

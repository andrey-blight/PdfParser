from tika import parser
from os import listdir


def main():
    for file in listdir("static"):
        file_path = "static/" + file
        file_name = file.split(".")[0]


        if file_name in ["Кротов_Царская дорога 1702", "1faa38018bd3ef0b4c0389a171f8f2e7",
                         "7-й_Конгресс_18", "ab83a5d6362983ec339ce0a1ce2b732a",
                         "d77d60b30ac31f0b755bde699f12aa59",
                         "Кротов_Матросы поморы", "Документы_Петровский_Петергоф_Том_2",
                         "Документы_Петровский_Петергоф_Том_1",
                         "Павленко", "Майкова_Военные_журналы_юрналы_Петра_1",
                         "b3d1ca201c8508f1b238f64c6c684ec8",
                         "bb4e0e733fb50704cc0752a48f58dae9",
                         "tbjzpon0w0mcac9v2vp0090g090vjhe9",
                         "История_отечественного_судостроение_Т_1_",
                         "7-й_Конгресс_18мая_compressed"] or file_path.endswith(".djvu"):
            continue

        print("Try parsing " + file_name)
        pdf_text = parser.from_file(file_path)["content"]

        print("saving " + file_name)

        with open(f"res/{file_name}.txt", "w", encoding="utf-8") as f:
            f.write(pdf_text)


if __name__ == '__main__':
    main()
    # pdf_text = parser.from_file("static/tbjzpon0w0mcac9v2vp0090g090vjhe9.pdf.pdf.pdf")["content"]
    # print(pdf_text)

import PySimpleGUI as sg


def converter(units, input):
    if units == 'KM to Miles':
        miles = int(input) / 1.609
        answer_miles = round(miles, 3)
        return f"{answer_miles} Miles"
    if units == 'Sec to Min':
        min = int(input) / 60
        answer_min = round(min, 3)
        return f"{answer_min} Minutes"
    if units == 'KG to Pounds':
        pounds = int(input) / 2.205
        answer_pounds = round(pounds, 3)
        return f"{answer_pounds} Pounds"


layout = [[sg.Input(key='-INPUT-'), sg.Spin(['KM to Miles', 'Sec to Min', 'KG to Pounds'], key="-UNITS-")],
          [sg.Button("CONVERT", key="-CONVERT-"), sg.Text(size=(40, 1), key="-OUTPUT-")]]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-CONVERT-":
        x = values["-INPUT-"]
        if not x.isnumeric():
            window["-OUTPUT-"].update("not a number")
        else:
            print(converter(values["-UNITS-"], values["-INPUT-"]))
            window["-OUTPUT-"].update(converter(values["-UNITS-"], values["-INPUT-"]))

window.close()

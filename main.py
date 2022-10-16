import PySimpleGUI as sg


def converter(units, input):
    if units == 'KM to Miles':
        miles = int(input) / 1.609
        return f"{round(miles, 3)} Miles"
    if units == 'Sec to Min':
        min = int(input) / 60
        return f"{round(min, 3)} Minutes"
    if units == 'KG to Pounds':
        pounds = int(input) / 2.205
        return f"{round(pounds, 3)} Pounds"


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

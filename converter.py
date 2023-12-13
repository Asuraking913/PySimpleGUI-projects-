import PySimpleGUI as sg 

layout = [
    [
        sg.Input(key = 'input'), 
        sg.Spin(['km to m', 'mins to secs'], key = 'value'), 
        sg.Button('convert', key = 'button1')
    ],
    [sg.Text('', key = 'text')]
    ]

window = sg.Window('converter', layout)

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED:
        break 
    
    if event == 'button1':
        input_value = value['input']
        if input_value.isnumeric():
            if value['value'] == 'km to m':
                result = round(float(input_value) * 0.062)
                result_string = f'{input_value} km are {result} miles'
            elif value['value'] == 'mins to secs':
                result = round(float(input_value) * 60)
                result_string = f'{input_value} mins are {result} secs'
            window['text'].update(result_string)
        else:
            window['text'].update('Numeric input only')

window.close()
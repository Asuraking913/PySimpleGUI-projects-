import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 14')
    layout = [
        [
            sg.Text(
                'output', 
                key = 'text key', 
                font = 'Franklin 26', pad = (10, 20), 
                justification = 'right', 
                expand_x = True, 
                right_click_menu = theme_menu,
                )
                ], 
        [sg.Button('clear', expand_x = True, size = (6, 3)), sg.Button('enter', expand_x = True, size = (6, 3))],
        [sg.Button(7, size = (6, 3)), sg.Button(8, size = (6, 3)), sg.Button(9, size = (6, 3)), sg.Button('+', size = (6, 3))],
        [sg.Button(4, size = (6, 3)), sg.Button(5, size = (6, 3)), sg.Button(6, size = (6, 3)), sg.Button('-', size = (6, 3))],
        [sg.Button(1, size = (6, 3)), sg.Button(2, size = (6, 3)), sg.Button(3, size = (6, 3)), sg.Button('*', size = (6, 3))],
        [sg.Button(0, size = (6, 3), expand_x = True), sg.Button('.', size = (6, 3)), sg.Button('/', size = (6, 3))],
    ]
    return sg.Window('calculator', layout)

operation = []
num = []
theme_menu = ['theme_menu', ['lightgrey1', 'bluemono', 'dark', 'lightgray4', 'random']]
window = create_window('lightgrey1')
operation_active = False

while True: 
    event, value = window.read()
    if event ==  sg.WINDOW_CLOSED:
        break 
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
        num.append(event)
        num_string = ''.join(num)
        window['text key'].update(num_string)

    if event in ['-', '+', '*', '/']:
        operation.append(''.join(num))
        num = []
        operation.append(event)
        window['text key'].update('')

    if event == 'enter':
        operation.append(num_string)
        result = eval(''.join(operation))
        window['text key'].update(result)
        operation = []
        num = []

    if event == 'clear':
        operation = []
        num = []
        window['text key'].update('')



window.close()
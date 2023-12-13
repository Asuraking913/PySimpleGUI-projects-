import PySimpleGUI as sg
from time import time

sg.theme('black')

def create_window():

    layout = [
        [sg.Push(), sg.Image('exit.png', key = 'image key', enable_events = True, pad = 0)], 
        [sg.VPush()], 
        [sg.Text('', key = 'text key', font = 'young 50')],
        [
            sg.Button(
                'start', 
                button_color = ('white', 'red'), 
                border_width = 0, 
                key = 'start key', 
                ), 
            sg.Button(
                'lap', 
                button_color =('white', 'red'), 
                border_width = 0, 
                key = 'lap key',
                visible = False)
        ], 
        [sg.Column([[]], key = 'column key')],
        [sg.VPush()]
        
    ]
    return sg.Window('stopwatch', layout, size = (300, 300), no_titlebar = True, element_justification = 'center')

active = False
start_time = 0
window = create_window()
layout_amount = 1

while True:
    event, value = window.read(timeout = 10)

    if event in (sg.WINDOW_CLOSED, 'image key'):
        break 

    if event == 'start key':
        if active:
            active = False
            window['start key'].update('reset')
            window['lap key'].update(visible = False)
            
            

        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
            else:
                active = True
                start_time = time()
                window['start key'].update('stop')
                window['lap key'].update(visible = True)
    
    if active:
        elasped_time = round(time() - start_time, 1)
        window['text key'].update(elasped_time)
    
    if event == 'lap key':
        window.extend_layout(window['column key'], [[sg.Text(f'{layout_amount}'), sg.VSeperator(), sg.Text(f'{elasped_time} secs')]])
        layout_amount += 1 
    
    



window.close()
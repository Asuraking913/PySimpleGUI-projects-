import PySimpleGUI as sg 

field = 400
field = sg.Graph(
    canvas_size = (400, 400), 
    graph_top_right = (0, 0), 
    graph_bottom_left =(field, field), 
    background_color = 'blue'
)

layout  =  [
    [field]
]

window = sg.Window('Snake game', layout)

while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break 

window.close()
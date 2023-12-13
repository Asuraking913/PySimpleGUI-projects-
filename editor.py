import PySimpleGUI as sg
from pathlib import Path

sg.theme('graygraygray')

smileys = [
    'Happy', ['🤣', '😅', '😋'], 
    'Sad', ['😥', '😪','😓'], 
    'Other', ['💀', '🙉', '🐱‍🏍']
]

smileys_event = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']], 
    ['Add', smileys]
]

layout = [
    [sg.Menu(menu_layout)], 
    [sg.Text('Untitled', key = 'text key')], 
    [sg.Multiline(size = (40, 30), key = 'text box', no_scrollbar = True)]
]

window = sg.Window('Editor', layout)

while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break 

    if event == 'Word Count':
        full_text = value['text box']
        word_count1 = full_text.replace('\n', ' ').split(' ')
        word_count = len(word_count1)
        char_count = len(''.join(word_count1))
        sg.popup(f'words: {word_count} \n character: {char_count}')
    
    if event == 'Open':
        file1 = sg.popup_get_file('open', no_window = True)
        file_path = Path(file1)
        if file1:
            window['text box'].update(file_path.read_text())
            window['text key'].update(file1.split('/')[-1])
        
    if event == 'Save':
        file1 = sg.popup_get_file('Save as', no_window = True, save_as = True)
        file_path = Path(file1)
        file_path.write_text(value['text box'])
        window['text key'].update(file1.split('/')[-1])

    
    if event in smileys_event:
        smiley_string = ''.join(event)
        new_text = value['text box'] + ' ' + smiley_string
        window['text box'].update(new_text)
    
    if event == 'Exit':
        break

    
        
        


window.close()
#working with python sets
from pyscript import display, document

grseven_members = {'ambata', 'torculas'}
greigth_members = {'kaur', 'pancho'}
grnine_members = {'navarro','micu'}    
grten_members = {'allas','nardo'}

display(grseven_members | greigth_members | grnine_members | grten_members , target='results')
grten_members.add('manalo')

display(f'Total number of members: {len(grseven_members | greigth_members | grnine_members | grten_members)}', target='results')


def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    last_name = document.getElementById('surname').value.lower().strip()
    grseven_members = {'ambata', 'torculas'}
    greigth_members = {'kaur', 'pancho'}
    grnine_members = {'navarro','micu'}
    grten_members = {'allas','nardo'}
    member_checker = last_name in grseven_members
    member_checker = last_name in greigth_members
    member_checker = last_name in grnine_members
    member_checker = last_name in grten_members

    display_message = (f'Sorry, no {last_name} in the list', f'{last_name} is in the list')
    
    
    display(display_message[member_checker], target='result')

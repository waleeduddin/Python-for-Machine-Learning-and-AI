import ipywidgets as widgets
from IPython.display import display

expression = widgets.Text(
    value='',
    placeholder='Enter calculation',
    description='Expression:',
    disabled=False
)

output = widgets.Output()

def on_button_click(b):
    if b.description == '=':
        with output:
            try:
                result = eval(expression.value)
                print(result)
                expression.value = str(result) # Update the input field with the result
            except Exception as e:
                print("Error")
                expression.value = "Error"
    elif b.description == 'C':
        expression.value = ''
        output.clear_output()
    else:
        expression.value += b.description

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

button_grid = widgets.VBox([widgets.HBox([widgets.Button(description=button) for button in buttons[i:i+4]]) for i in range(0, len(buttons), 4)])

clear_button = widgets.Button(description='C')
clear_button.on_click(on_button_click)

for row in button_grid.children:
    for button in row.children:
        button.on_click(on_button_click)

display(expression, button_grid, clear_button, output)

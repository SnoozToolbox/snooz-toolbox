from qtpy import QtWidgets
from qtpy import QtGui

def compute_box_width(data):
        padding = 40
        inputs_count = 0
        outputs_count = 0
        if 'inputs' in data:
            inputs_count = len(data['inputs'])
        if 'outputs' in data:
            outputs_count = len(data['outputs'])

        i = 0
        max_line = ''
        while i < inputs_count or i < outputs_count:
            input = ''
            if i < inputs_count:
                input = list(data['inputs'].keys())[i]
            output = ''
            if i < outputs_count:
                output = list(data['outputs'].keys())[i]
            line = input + ' ' + output
        
            if len(line) > len(max_line):
                max_line = line

            i = i + 1

        f = QtWidgets.QApplication.font()
        f.setPointSize(8)
        font_metric = QtGui.QFontMetrics(f)

        width = font_metric.width(max_line) 
        return width + padding
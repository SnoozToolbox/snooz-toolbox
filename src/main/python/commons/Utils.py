"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import os

def assemble_output_filename(input_filename, suffix=None, 
    use_input_folder=True, output_folder=None):
    """ Assemble an output filename based on the user settings
    Args:
        input_filename:   The input filename to base the output filename on.
        suffix:           Add a suffix to the input_filename
        use_input_folder: Place output file in the same folder as the input file.
        output_folder:    Set the output folder. Only used if [use_input_folder]
                            is set to FALSE.
    """
    # separate the filename, the folder and the extension
    filepath, filename = os.path.split(input_filename)
    filename, ext = os.path.splitext(filename)

    # Add a suffix if needed
    if suffix is not None:
        filename = filename + suffix
    
    # Add back the extension
    filename = filename + ext

    # Add the output folder based on the user choice
    if use_input_folder == 1:
        output_filename = os.path.join(filepath, filename)
    elif output_folder is not None:
        output_filename = os.path.join(output_folder, filename)
    else:
        output_filename = filename

    return output_filename

def deleteItemsOfLayout(layout):
     if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                 widget.setParent(None)
             else:
                 deleteItemsOfLayout(item.layout())
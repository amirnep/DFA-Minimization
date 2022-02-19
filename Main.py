import Class as c
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

if __name__ == '__main__': #Run Program.
    a = c.minimization()
    a.dfa_minimize()
    print()

drawing = svg2rlg("DFA_Minimized.svg")
renderPDF.drawToFile(drawing, "DFA_Minimized.pdf")
renderPM.drawToFile(drawing, "DFA_Minimized.png", fmt="PNG")

quit = input("Press Enter To Exit Program.")

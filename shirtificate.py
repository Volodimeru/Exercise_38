from fpdf import FPDF
def main():
    name = input("Please enter your name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 46)
    pdf.cell(0,40, txt="CS50 Shirtificate", align="C")
    pdf.image("/workspaces/126890668/shirtificate.png", x=0, y=60, w=210)
    pdf.set_font("helvetica", "B", 26)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-190,250,txt=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")
if __name__=="__main__":
    main()
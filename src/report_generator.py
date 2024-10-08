# report_generator.py

from fpdf import FPDF

def generate_pdf_report(compliance_report, output_file):
    pdf = FPDF()
    pdf.add_page()

    # Set title and header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="GPO Compliance Report", ln=True, align='C')

    # Add content
    pdf.set_font("Arial", size=12)
    for entry in compliance_report:
        policy = entry['policy']
        compliance = entry['compliance']
        pdf.cell(200, 10, txt=f"Policy: {policy}, Compliance: {compliance}", ln=True)

    # Output the PDF to the specified file
    pdf.output(output_file)

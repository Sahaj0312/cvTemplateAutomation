import docx
import sys
from docx2pdf import convert


doc = docx.Document('coverletterTemplate.docx')

for para in doc.paragraphs:
    # Replace text if it exists in the paragraph
    if '$company' in para.text:
        para.text = para.text.replace('$company', sys.argv[2])

    if '$position' in para.text:
        para.text = para.text.replace('$position', sys.argv[1])

# Save the modified document
doc.save(f'coverLetter{sys.argv[2]}.docx')
convert(f'coverLetter{sys.argv[2]}.docx', f'coverLetter{sys.argv[2]}.pdf')

#input_file= "/home/delhivery/backend_pdf_to_csv_server/BalSheet.pdf"
#output_csv = "/home/delhivery/backend_pdf_to_csv_server/2.csv"

import re
import pdfplumber
import numpy as np
from numpy import savetxt
import pandas as pd
from .settings import MEDIA_URL,  BASE_DIR

def pdf_to_csv(input_file):
    
    output_csv = input_file.replace(".pdf",".csv")
    lines = []
    start = False

    with pdfplumber.open(input_file) as pdf:
        pages = pdf.pages
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                if not start and line.startswith('Particulars'):
                    #cols = line.split()
                    start = True
                if start:
                    a= re.split('( \d+.\d+ )',line)
                    s = [s for s in a if s != '']
                    lines.append(s)

    df = pd.DataFrame(lines)
    df.to_csv(output_csv, index=False, header=False)


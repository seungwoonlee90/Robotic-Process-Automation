import pandas as pd
import pdfplumber

def main (pdf, start_page:int, last_page:int) :
    res = []
    for i in range(start_page, last_page) :
        page = pdf.pages[i]
        tables = page.extract_tables()
        tt = pd.DataFrame(tables[0])
        res.append(tt)
    df = pd.concat(res).reset_index(drop=True)
    return df

if __name__ == '__main__' :
    start_page = 0
    last_page = 10
    pdf = pdfplumber.open("***.pdf")
    main(pdf, start_page, last_page)
#!/usr/bin/env python
# coding: utf-8

import PyPDF2 as pdf
from PyPDF2 import PdfReader

reader = PdfReader("silberschatz8thedition.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
file = open(r"extract.txt","a")
file.writelines(text)
file.close()

import pymupdf
from pprint import pprint

doc = pymupdf.open("/home/origr/ai_engineer_course/expense-ai/sample_data/ Copy.pdf") # open document
page = doc[1] # get the 1st page of the document
tabs = page.find_tables() # locate and extract any tables on page
print(f"{len(tabs.tables)} found on {page}") # display number of found tables

if tabs.tables:  # at least one table found?
   pprint(tabs[0].extract())  # print content of first table
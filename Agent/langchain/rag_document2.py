from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader("C:/project/python/Knowledge_base/LangChain.pdf")
pages=loader.load()
print("yeshu:",len(pages))

for page in pages:
    print(page.metadata)
    print(page.page_content)
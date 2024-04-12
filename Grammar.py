import language_tool_python

mytext = """I is testing grammar tool using python.it does not costt anything """

def grammarCorrector(text):
    tool = language_tool_python.LanguageTool('en-US')
    result = tool.correct(text)
    return result

output_data = grammarCorrector(mytext)
print(output_data)

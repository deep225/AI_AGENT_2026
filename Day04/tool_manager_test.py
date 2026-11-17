from tool_manager import execute_tool

print("execute_tool('current time'):", execute_tool("what is the current time?"))
print("execute_tool('roll dice'):", execute_tool("Please roll a dice"))
print("execute_tool('generate password'):", execute_tool("generate a random password"))  
print("execute_tool('unknown tool'):", execute_tool("what is python?"))  # This should return None
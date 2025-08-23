# **📝 README – Understanding Duplicate Tool Names in AI Agent SDK**

---

This document explains what happens if we add multiple tools with the same name in an AI Agent SDK configuration.
We’ll also explore the exact class, method, and logic responsible for this behavior, along with bonus examples to make it crystal clear.

___

# **❓ Q1: What happens if we add multiple tools with the same name to an agent?**

### ✅ Answer:

---

If multiple tools with the same name are defined in Agent.tools, the last tool in the list always wins.
Why? Because the SDK internally stores tools in a dictionary (function_map), where duplicate keys (tool names) overwrite earlier entries.

### 🔎 Technical Flow:

The SDK builds a dictionary:

function_map = {tool.name: tool for tool in all_tools if isinstance(tool, FunctionTool)}


Here:

Key = tool.name

Value = tool object

Python dictionaries do not allow duplicate keys.

If you add the same key again → old value is replaced.

As a result, the last tool with that name survives.

### ⚡ Effect:
When the agent tries to run that tool later, it always executes the last one defined, ignoring earlier ones.

___

# **❓ Q2: Which class contains this logic?**

### ✅ Answer:

---

This behavior is implemented in the RunImpl class.

Purpose → It manages the execution flow of the agent.

___

# **❓ Q3: Which method contains the exact logic?**

### ✅ Answer:

---

The dictionary logic lives inside the method: process_model_response.

Inside this method, function_map is built from all available tools.

This is where the overwriting happens if multiple tools have the same name.

### 📘 Python Dictionary Basics (For Beginners)

A dictionary stores data as key → value pairs.

Keys must be unique.

If the same key is inserted again → the new value overwrites the old one.

Values can be duplicates, no restriction there.

## Example:

``` Python
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)  
# Output → {"a": 3, "b": 2}
```
### 👉 The first "a": 1 is lost because "a": 3 replaced it.

___

# **❓ Q4: Why exactly does this behavior happen here?**

### ✅ Answer:

---

It happens because of this dictionary comprehension:

function_map = {tool.name: tool for tool in all_tools if isinstance(tool, FunctionTool)}


All tools are looped over.

Only tools that are instances of FunctionTool are included.

Each tool is added as →

Key: tool.name

Value: tool object

If two tools have the same name, the earlier one is silently replaced by the later one.

### ⚡ Result:
When the agent looks up function_map[output.name] → it always fetches the last tool with that name.

___

# **🎁 Bonus Example**

---

We tested this by defining two tools with the same name ("weather") in our Gemini Agent SDK config.

First "weather" tool → returns sunny weather.

Second "weather" tool → returns rainy weather.

When the agent was asked to "Weather", it always executed the second tool (Rainy one).
👉 Because in the dictionary, the last "weather" replaced the first one.

___

# **✅ Summary**

---

Multiple tools with the same name? → Only the last one survives.

Where is the logic? → In RunImpl → process_model_response.

Why? → Because function_map uses a dictionary, and dictionaries don’t allow duplicate keys.

End effect? → The agent always executes the last tool with that name.

___


``` python
# Simple dict overwrite example
tools = {
    "weather": "Sunny ☀️",
    "weather": "Rainy 🌧️"  # same key overwrites previous one
}

print(tools)  
# Output: {'weather': 'Rainy 🌧️'}

print(tools["weather"])  
# Output: Rainy 🌧️
```

# **1. Concept**
---
In Python, a dictionary (dict) stores data in key–value pairs.
👉 But keys must always be unique.

If you add the same key more than once, the last value overwrites the previous one.
___

# **2. Explanation**

In this dictionary, the key "weather" is used twice.

First it was "Sunny ☀️", then "Rainy 🌧️".

Since keys cannot repeat, Python keeps only the last value.

👉 That’s why the output shows Rainy 🌧️ instead of Sunny ☀️.

# **3. Key Takeaway**

Duplicate keys are not allowed in Python dictionaries.

If duplicates are given, the last value wins.

#!/usr/bin/env python3

# Simple script to replace the 20 developers with 202 in the working file

# Read the working file
with open('just4u-platform-working.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Read all 202 developers JavaScript
with open('all_202_developers.js', 'r', encoding='utf-8') as f:
    developers_js = f.read()

# Find start and end markers of the original array
start_marker = "const allDevelopers = ["
end_marker = "];"

start_pos = content.find(start_marker)
if start_pos == -1:
    print("ERROR: Could not find start marker")
    exit(1)

# Find the end position - look for the next ]; after start
end_search_start = start_pos + len(start_marker)
end_pos = content.find(end_marker, end_search_start)
if end_pos == -1:
    print("ERROR: Could not find end marker")
    exit(1)

# Include the ]; in the replacement
end_pos += len(end_marker)

# Replace the old array with new one
before = content[:start_pos]
after = content[end_pos:]

# Update comment
new_content = before + developers_js.replace("const allDevelopers", "// Complete database of 202 developers with cool names\n\t\tconst allDevelopers") + after

# Write the fixed file
with open('just4u-platform-complete.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully created just4u-platform-complete.html with all 202 developers!")
print("JavaScript should work properly now.")
# Example list of tags
tags = ["John,Doe,Jane", "Alice,Bob,Charlie", "Tom,Jerry"]

# Calculate the number of collaborators for the first tag
collaborators_no = len(tags[0].split(',')) - 1

print(f"Number of collaborators (excluding the first one): {collaborators_no}")

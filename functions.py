def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
result1 = check_pass_fail(75)
result2 = check_pass_fail(30)

print("Marks 75 ka result:", result1)
print("Marks 30 ka result:", result2)
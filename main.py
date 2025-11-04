from pyscript import document, display #type: ignore
def calculate(e):

    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    science = int(document.getElementById("sci").value)
    math = int(document.getElementById("math").value)
    english = int(document.getElementById("eng").value)
    ict = int(document.getElementById("ICT").value)
    fil = int(document.getElementById("Filipino").value)
    pe = int(document.getElementById("PE").value)

    equation = (science + math + english + ict + fil + pe) / 6
    averagegrade = round(equation, 2)

    if averagegrade >= 75:
        display("Status: ✅ Passing Grade", target="passorfail")
    else:
        display("Status: ❌ Failing Grade", target="passorfail")

    display(f"Name: {fname} {lname}", target="name", append=False)
    display(f"Science: {science}", target="grades", append=False)
    display(f"Math: {math}", target="grades")
    display(f"English: {english}", target="grades")
    display(f"ICT: {ict}", target="grades")
    display(f"Filipino: {fil}", target="grades")
    display(f"PE: {pe}", target="grades")
    display(f"Your GWA is: {averagegrade}", target="average", append=False)
    
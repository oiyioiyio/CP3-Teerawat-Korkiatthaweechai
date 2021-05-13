PyramidStep = int(input("Please input pyramid step: "))
for i in range(PyramidStep):
    print(" " * (PyramidStep - i),"*" * (((i + 1) * 2) - 1))
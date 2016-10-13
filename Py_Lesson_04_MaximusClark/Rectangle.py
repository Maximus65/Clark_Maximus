def CalcPerim(le,wi):
    return float((le*2)+(wi*2));

Length = int(input("What is the length of the object?"))
Width = int(input("What is the width of the object? "))

print("Your Rectangle is", CalcPerim(Length,Width), "sq ft around.");

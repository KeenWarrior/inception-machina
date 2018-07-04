
try:
    p = 4567
    b = 56456


    f = open("ab.txt")

    p = b / 0


    # f = open("ab.txt")

    for line in f:
        print(line)

except FileNotFoundError as e:
    print(e.filename)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

# except (FileNotFoundError, ZeroDivisionError) :
#     print("File not found weghrjnwfeokdwOJIH")
# except :
#     print("Divided by zero you moron")

# i = 0/0

# We added it here just for fun

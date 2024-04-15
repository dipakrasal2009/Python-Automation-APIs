number = 7;
start = 6;
end = 10;

for value in range(start,end):
    if value == number:
        print(f"{number} is present in the range[{start},{end}]");
        break;
    else:
        print(f"{number} is not present in the range[{start},{end}]");

#!/usr/bin/python3

def calc(A, B):
  
    if not isinstance(A, int) or not isinstance(B, int):
        return -1
   
    if A < 1 or A > 999 or B < 1 or B > 999:
        return -1
  
    return A * B

def main():
    while True:
        s = input("input A (or 'end' to exit): ")
        if s == "end":
            break
        try:
            A = int(s)
        except ValueError:
            A = s  
        s2 = input("input B: ")
        try:
            B = int(s2)
        except ValueError:
            B = s2
        print("input A * input B = ", calc(A, B))

if __name__ == '__main__':
    main()

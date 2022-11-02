def calc_square_root(n):
    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        print("The my calculator module was not found. "
              "Loading Python math library instead.")
        from math import sqrt

    answer = sqrt(n)
    return answer

def main():
    print(calc_square_root(2))

if __name__ == "__main__":
    main()
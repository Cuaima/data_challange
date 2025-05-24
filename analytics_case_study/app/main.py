import pandas as pd

def main():
    print("Poetry environment is working!")
    df = pd.DataFrame({"hello": [1, 2, 3]})
    print(df)

if __name__ == "__main__":
    main()
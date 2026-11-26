import os

LINE = "Sorry, I heard 'wake me at six' as 'text my ex I miss them' — I didn't send it, but I did draft the apology."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE.strip())


if __name__ == "__main__":
    main()

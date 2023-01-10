import random as rn

def main(player_name, ):
    dice_return = 0
    Roll = input("\nY/N ")
    print(f"Player#{x+1}")
    for i in range(0, dice_count):
        roll = rn.randint(1, 6)
        dice_return += roll
        print(f"#{i+1}: {roll} ")
        print(f"\nTotal: {dice_return}", end='')

if __name__ == "__main__":
    main()

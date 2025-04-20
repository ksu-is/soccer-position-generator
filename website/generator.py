def assign_position(height, weight, speed, foot = "r"): 
    height = int(height)
    weight = int(weight)
    speed = int(speed)
    foot = str(foot)
    goalie = sum([abs(76 - height)*5, abs(170 - weight) , abs(2 - speed)*10])
    winger = sum([abs(65 - height)*5, abs(140 - weight) , abs(10 - speed)*10])
    striker = sum([abs(70 - height)*5, abs(160 - weight) , abs(9 - speed)*10])
    defender = sum([abs(72 - height)*5, abs(180 - weight) , abs(4 - speed)*10])
    midfielder = sum([abs(70 - height)*5, abs(160 - weight) , abs(6 - speed)*10])
    wingback = sum([abs(69 - height)*5, abs(160 - weight) , abs(7 - speed)*10])
    # print (goalie, winger, striker, defender, midfielder, wingback)
    scores = [goalie, winger, striker, defender, midfielder, wingback]
    position = ["Goalie", "Winger", "Striker", "Defender", "Midfielder", "Wingback"]
    index = scores.index(min(scores))
    f = position[index]
    if index in [1, 4, 5]:
        f = "Left " + f if foot == "l" else "Right " + f
    return f

def main():
    print("Enter your player info:")
    height = input("Height (in inches): ")
    weight = input("Weight (in pounds): ")
    speed = input("Speed (1-10): ")
    foot = input("Which foot do you kick with? (Left or Right): ")
    foot = "l" if "l" in foot.lower() else "r"

    var = assign_position(height, weight, speed, foot)
    print(f"Your position is: {var}")

if __name__ == "__main__":
    main()

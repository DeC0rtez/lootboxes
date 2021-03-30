import random

accounts = {
    "Arcanus":
        {
            "balance_silver": 850000,
            "balance_gold": 4500,
            "balance_bonds": 5600,
            "premium_days": 62,
            "tanks": ["Bourrasque", "M22 Locust", "Matilda BP", "PZ. T 15"]
        },

    "Empty":
        {
            "balance_silver": 0,
            "balance_gold": 0,
            "balance_bonds": 0,
            "premium_days": 0,
            "tanks": []
        }
}

tank_prices = {
    "Bisonte C45": 10200,
    "GSOR 1008": 9000,
    "Bourrasque": 7600,
    "ISU-152K": 8700,
    "M4A1 FL 10": 3300,
    "T78": 2800,
    "PZ. T 15": 900,
    "Matilda BP": 1750,
    "M22 Locust": 900,
    "none": 0
}


def add_tank(account_name, tank):
    accounts[account_name]["tanks"].append(tank)

def add_gold(account_name, amount):
    accounts[account_name]["balance_gold"] = accounts[account_name]["balance_gold"] + amount


def add_silver(account_name, amount):
    accounts[account_name]["balance_silver"] = accounts[account_name]["balance_silver"] + amount


def add_premium(account_name, amount):
    accounts[account_name]["premium_days"] = accounts[account_name]["premium_days"] + amount


def get_tank():
    roll = random.randint(0, 10000)
    if roll <= 61:
        return "Bisonte C45"
    elif 61 < roll <= 116:
        return "GSOR 1008"
    elif 116 < roll <= 153:
        return "Bourrasque"
    elif 153 < roll <= 202:
        return "ISU-152K"
    elif 202 < roll <= 324:
        return "M4A1 FL 10"
    elif 324 < roll <= 422:
        return "T78"
    elif 422 < roll <= 763:
        return "PZ. T 15"
    elif 763 < roll <= 1074:
        return "Matilda BP"
    elif 1074 < roll <= 1391:
        return "M22 Locust"
    else:
        return "none"


def get_gold():
    roll = random.randint(0, 10000)
    if roll <= 177:
        return 1000
    elif 177 < roll <= 634:
        return 500
    else:
        return 250


def get_silver():
    roll = random.randint(0, 10000)
    if roll <= 707:
        return 500000
    if 707 < roll <= 2878:
        return 100000
    else:
        return 0


def get_premium():
    roll = random.randint(0, 10000)
    if roll <= 335:
        return 7
    if 335 < roll <= 1195:
        return 3
    if 1195 < roll <= 3756:
        return 1
    else:
        return 0


def lootbox(account_name):
    reward_tank = get_tank()
    if reward_tank != "none":
        print("You got a " + str(reward_tank))
        if reward_tank in accounts[account_name]["tanks"]:
            print("Since you already own it, you get: " + str(tank_prices[reward_tank]) + " gold instead!")
            add_gold(account_name, tank_prices[reward_tank])
        else:
            add_tank(account_name, reward_tank)
    else:
        print("You did not get a tank.")

    reward_gold = get_gold()
    if reward_gold != 0:
        print("You got " + str(reward_gold) + " gold!")
        add_gold(account_name, reward_gold)

    reward_silver = get_silver()
    if reward_silver != 0:
        print("You got " + str(reward_silver) + " silver!")
        add_silver(account_name, reward_silver)

    reward_prem = get_premium()
    if reward_prem != 0:
        print("You got " + str(reward_prem) + " premium days!")
        add_premium(account_name, reward_prem)


def run_trial(account_name, times):
    tanks_before = str(accounts[account_name]["tanks"])
    gold_before = int(accounts[account_name]["balance_gold"])
    silver_before = int(accounts[account_name]["balance_silver"])
    prem_before = int(accounts[account_name]["premium_days"])

    for _ in range(times):
        print("Box #" + str(_ + 1))
        lootbox(account_name)
        print("------------------------")

    tanks_after = str(accounts[account_name]["tanks"])
    gold_after = int(accounts[account_name]["balance_gold"])
    silver_after = int(accounts[account_name]["balance_silver"])
    prem_after = int(accounts[account_name]["premium_days"])

    print("ACCOUNT: " + account_name)
    print("BEFORE:")
    print("Tanks: " + tanks_before)
    print("Gold: " + f"{gold_before:,}")
    print("Silver: " + f"{silver_before:,}")
    print("Premium Days: " + f"{prem_before:,}")
    print("------------------------")
    print("AFTER " + str(times) + " BOXES:")
    print("Tanks: " + tanks_after)
    print("Gold: " + f"{gold_after:,}")
    print("Silver: " + f"{silver_after:,}")
    print("Premium Days: " + f"{prem_after:,}")


run_trial("Arcanus", 75)





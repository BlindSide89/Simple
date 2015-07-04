import random

def main():
    assaultRifles = ["M3A1", "M16A4", "SCAR-L", "CM901", "TYPE 95", "G36C", "ACR 6.8", "MK14", "AK-47", "FAD", "Assault Rifles"]
    subMachine = ["MP5", "UMP45", "PP90M1", "P90", "PM-9", "MP7", "SubMachineGuns"]
    lms = ["L86 LSW", "PKP PECHENEG", "MK46", "M60E4", "LMS"]
    smipers = ["BARRET 50CAL", "L118A", "DRAGUNOV", "AS50", "RSASS", "MSR", "Sniper"]
    shotguns = ["USAS", "KSG 12", "SPAS12", "AA-12", "STRIKER", "Model 1887", "Shotguns"]
    shield = ["RiotShield", "Shields"]



    subMG = ["FMG9", "MP9", "Skorpion", "G18", "SubMG"]
    handguns = ["USP45", "P99", "MP412", "44Magnum", "Five Seven", "DesertEagle", "Pistol"]
    launchers = ["SMAW", "JAVELIN", "STINGER", "XM25", "M320", "RPG", "Launcher"]


    lethal = ["Frag", "Semtex", "ThrowingKnife", "Bouncing Betty", "Claymore", "C4"]
    tactical = ["Flash", "Concussion", "Scrambler", "EmpGrenade", "SmokeGrenade", "TrophySystem", "Tactical Insertion", "Portable Radar"]

    primary = [assaultRifles, subMachine, lms, smipers, shotguns, shield]
    secondary = [subMG, handguns, launchers]

    random.seed()

    primaryHolder = primary[random.randint(0, primary.__len__()-1)]
    primaryConcrete = primaryHolder[random.randint(0, primaryHolder.__len__()-2)]
    print(primaryHolder[primaryHolder.__len__() - 1] +":  " +  primaryConcrete)

    secondaryHolder = secondary[random.randint(0, secondary.__len__()-1)]
    secondaryConcrete = secondaryHolder[random.randint(0, secondaryHolder.__len__()-2)]
    print(secondaryHolder[secondaryHolder.__len__() - 1] +":  " +  secondaryConcrete)

    print("Lethal:   " + lethal[random.randint(0,lethal.__len__()-1)])
    print("Tactical:  " + tactical[random.randint(0, tactical.__len__()-1)])


if __name__ == '__main__':
    main()
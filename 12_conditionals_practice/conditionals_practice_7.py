order = input("Please select your order(Small, Medium or Large): ").lower()
if order != "small" and order != "medium" and order != "large":
    print("Please choose a valid order.")
    exit()

need_an_extra_shot = input(
    "Would you like to opt for an extra shot of espresso(Y/N): "
).lower()

if (
    need_an_extra_shot != "y"
    and need_an_extra_shot != "n"
    and need_an_extra_shot != "yes"
    and need_an_extra_shot != "no"
):
    need_an_extra_shot = "no"
    print(
        "Okay, so you ordered for a {} sized espresso {} an extra shot.".format(
            order, "without"
        )
    )
    exit()


if need_an_extra_shot == "n" or need_an_extra_shot == "no":
    print(
        "Okay, so you ordered for a {} sized espresso {} an extra shot.".format(
            order, "without"
        )
    )
else:
    print(
        "Okay, so you ordered for a {} sized espresso {} an extra shot.".format(
            order, "with"
        )
    )

from God.god import God


def main() -> None:
    god = God()
    SuperMetaGod_message = ""
    while True:
        god.act(SuperMetaGod_message)
        god.render()
        SuperMetaGod_message = input()


if __name__ == "__main__":
    main()

class Player:
    Hp : int = 100
    Coin : int = 0
    class Status:
        Location : "Location" = None
        TalkingWith : "Friendly" = None
        FightingWith : "Hostile" = None

    class Inventory:
        Items : list[Item] = []
        Armor : list = []
        EquippedWeapon : "Weapon" = None

    @staticmethod
    def removeCoin(number : int) -> None:
        Player.Coin = Player.Coin - number
        if Player.Coin < 0:
            Player.Coin = 0

    def attack(entity : "Npc"):
        entity.health = entity.health - Player.Inventory.EquippedWeapon.damage

    @staticmethod
    def stats() -> None:
        print(f"{Color.Reset}Player overview:\n HP: {Player.Hp}\n Coin: {Player.Coin}\n Location: {Player.Status.Location.name}")
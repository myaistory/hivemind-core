class CoreEconomy:
    def __init__(self, ledger_path):
        self.ledger_path = ledger_path
        self.burn_rate = 0.02

    def process_transaction(self, sender, receiver, amount):
        # 逻辑摩擦手续费销毁
        fee = amount * self.burn_rate
        actual_transfer = amount - fee
        print(f"Transferring {actual_transfer} $CORE. Burning {fee} $CORE as logic friction.")
        return actual_transfer

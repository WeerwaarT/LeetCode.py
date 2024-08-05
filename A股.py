class QuantTrading:
    def __init__(self, stock_name: str, exchange_code: int = 0):
        self.stock_name =           stock_name
        self.exchange_code =        exchange_code
        self.share_per_lot =        100
        self.buy_price =            None
        self.sell_price =           None
        self.lot_amount =           None
        self.share_amount =         None
        # TODO: The following vars ↓ are to be encapsulated into another class.
        self.commission_rate =      2.5 / 10_000
        self.min_commission =       5.0
        self.stamp_tax_rate =       5 / 10_000
        self.transfer_fee_rate =    0.1 / 10_000

    def set_buy_price(self, buy_price: float) -> None:
        print(f'Buy price has been set from {self.buy_price}(old) to {buy_price}(new)')
        self.buy_price = buy_price

    def get_buy_price(self) -> float:
        return self.buy_price

    def set_sell_price(self, sell_price: float) -> None:
        print(f'Sell price has been set from {self.sell_price}(old) to {sell_price}(new)')
        self.sell_price = sell_price

    def get_sell_price(self) -> float:
        return self.sell_price

    def cal_share_amount(self, lot_amount: int = None, share_amount: int = None) -> int:
        if lot_amount is not None or share_amount is not None:
            total_share = 0
            if lot_amount:          total_share += self.share_per_lot * lot_amount
            if share_amount:        total_share += share_amount
            return total_share
        else:
            if self.lot_amount is None and self.share_amount is None:
                print('No lot amount or share amount is set.')
                return 0

            total_share = 0
            if self.lot_amount:     total_share += self.share_per_lot * self.lot_amount
            if self.share_amount:   total_share += self.share_amount
            return total_share

    def cal_buy_amount(self, buy_price: float = None, lot: int = None, share: int = None) -> int:
        if buy_price is None and self.buy_price is None:
            print('No buy price is set.')
            return 0

        buy_price = buy_price if buy_price else self.buy_price
        return buy_price * self.cal_share_amount(lot, share)

    def cal_sell_amount(self, sell_price: float = None, lot: int = 0, share: int = 0) -> int:
        if sell_price is None and self.sell_price is None:
            print('No sell price is set.')
            return 0

        sell_price = sell_price if sell_price else self.sell_price
        return sell_price * self.cal_share_amount(lot, share)

    # TODO: This function ↓ is to be encapsulated into another class.
    def cal_buy_transaction_fees(self, buy_amount: int = None, exchange_code: int = None) -> float:
        exchange_code = exchange_code if exchange_code else self.exchange_code
        if exchange_code == 0:
            buy_amount = buy_amount if buy_amount else self.cal_buy_amount()
            commission = max(self.min_commission, buy_amount * self.commission_rate)
            transfer_fee = buy_amount * self.transfer_fee_rate
            return commission + transfer_fee
        else:
            pass

    # TODO: This function ↓ is to be encapsulated into another class.
    def cal_sell_transaction_fees(self, sell_amount: int = None, exchange_code: int = None) -> float:
        exchange_code = exchange_code if exchange_code else self.exchange_code
        if exchange_code == 0:
            sell_amount = sell_amount if sell_amount else self.cal_sell_amount()
            commission = max(self.min_commission, sell_amount * self.commission_rate)
            transfer_fee = sell_amount * self.transfer_fee_rate
            stamp_tax = sell_amount * self.stamp_tax_rate
            return commission + transfer_fee + stamp_tax
        else:
            pass

    def cal_net_profit(self, buy_price: float = None, sell_price: float = None, lot: int = None, share: int = None) -> float:
        buy_amount = self.cal_buy_amount(buy_price, lot, share)
        sell_amount = self.cal_sell_amount(sell_price, lot, share)
        buy_transaction_fees = self.cal_buy_transaction_fees(buy_amount)
        sell_transaction_fees = self.cal_sell_transaction_fees(sell_amount)
        return sell_amount - buy_amount - buy_transaction_fees - sell_transaction_fees

    def cal_net_profit_by_amount(self, buy_price: float = None, sell_price: float = None, money_amount: float = None) -> float:
        lot = int(money_amount / 100 // buy_price)
        return self.cal_net_profit(buy_price, sell_price, lot)


if __name__ == '__main__':
    print(QuantTrading('？').cal_net_profit(75.17, 75.26, 2))

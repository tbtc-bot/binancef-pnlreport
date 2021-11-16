import datetime
import json
import math
from json import JSONEncoder
from typing import Optional

from binance.client import Client
from sys import platform

class OrderStatus:
    def __init__(self,
                 openingCount: int = 0,
                 closingCount: int = 0,
                 openingAmt: float = 0.0,
                 closingAmt: float = 0.0,
                 openingValue: float = 0.0,
                 closingValue: float = 0.0,
                 lastGridPrice: float = 0.0,
                 tpPrice: float = 0.0
                 ):
        self.openingCount: int = openingCount
        self.closingCount: int = closingCount
        self.openingAmt: float = openingAmt
        self.closingAmt: float = closingAmt
        self.openingValue: float = openingValue
        self.closingValue: float = closingValue
        self.lastGridPrice: float = lastGridPrice
        self.tpPrice: float = tpPrice


class IncomeSummary:
    def __init__(self,
                 count: int = 0,
                 netRealizedPnl: float = 0.0,
                 transfer: float = 0.0,
                 welcomeBonus: float = 0.0,
                 realizedPnl: float = 0.0,
                 funding_fee: float = 0.0,
                 commission: float = 0.0,
                 insuranceClear: float = 0.0,
                 crossCollateralTransfer: float = 0.0,
                 commissionRebate: float = 0.0
                 ):
        self.count: int = count
        self.netRealizedPnl: float = netRealizedPnl
        self.transfer: float = transfer
        self.welcomeBonus: float = welcomeBonus
        self.realizedPnl: float = realizedPnl
        self.funding_fee: float = funding_fee
        self.commission: float = commission
        self.insuranceClear: float = insuranceClear
        self.crossCollateralTransfer: float = crossCollateralTransfer
        self.commissionRebate = commissionRebate


class PositionSummary:
    def __init__(self,
                 symbol: str,
                 unrealizedProfit: float = 0.0,
                 entryPrice: float = 0.0,
                 positionAmt: float = 0.0,
                 tradeCount: int = 0,
                 pnl: float = 0.0,
                 exposure: float = 0.0,
                 exposurePerc: float = 0.0,
                 openingOrderCount: int = 0,
                 closingOrderCount: int = 0,
                 openingOrderQty: float = 0.0,
                 closingOrderQty: float = 0.0,
                 openingOrderValue: float = 0.0,
                 closingOrderValue: float = 0.0,
                 grossRealizedPnl: float = 0.0,
                 fundingFee: float = 0.0,
                 commission: float = 0.0,
                 realizedPnlPerc: float = 0.0,
                 tradeCountPerc: float = 0.0,
                 openingOrderValuePerc: float = 0.0,
                 lastGridExposure: float = 0.0,
                 lastGridLoss: float = 0.0,
                 tpPrice: float = 0.0,
                 currentPrice: float = 0.0,
                 diffCurPriceFromTpPerc: float = 0.0,
                 leverage: float = 0.0,
                 lastGridCost: float = 0.0,
                 lastGridEntryPrice: float = 0.0
                 ):
        self.symbol: str = symbol
        self.unrealizedProfit: float = unrealizedProfit
        self.entryPrice: float = entryPrice
        self.positionAmt: float = positionAmt
        self.tradeCount: int = tradeCount
        self.realizedPnl: float = pnl
        self.exposure: float = exposure
        self.exposurePerc: float = exposurePerc
        self.openingOrderCount: int = openingOrderCount
        self.closingOrderCount: int = closingOrderCount
        self.openingOrderQty: float = openingOrderQty
        self.closingOrderQty: float = closingOrderQty
        self.openingOrderValue: float = openingOrderValue
        self.closingOrderValue: float = closingOrderValue
        self.grossRealizedPnl: float = grossRealizedPnl
        self.fundingFee: float = fundingFee
        self.commission: float = commission
        self.realizedPnlPerc: float = realizedPnlPerc
        self.tradeCountPerc: float = tradeCountPerc
        self.openingOrderValuePerc: float = openingOrderValuePerc
        self.lastGridExposure: float = lastGridExposure
        self.lastGridLoss: float = lastGridLoss
        self.lastGridCost: float = lastGridCost
        self.lastGridEntryPrice: float = lastGridEntryPrice
        self.tpPrice: float = tpPrice
        self.currentPrice: float = currentPrice
        self.diffCurPriceFromTpPerc: float = diffCurPriceFromTpPerc
        self.leverage: float = leverage


class BotSummary:
    def __init__(self,
                 name: str,
                 timestamp: int,
                 balance: float = 0.0,
                 totUnrealizedProfit: float = 0.0,
                 totRealizedProfitPerc: float = 0.0,
                 totRealizedProfit: float = 0.0,
                 totInitialMargin: float = 0.0,
                 totOpenOrderInitialMargin: float = 0.0,
                 availableBalance: float = 0.0,
                 totalMaintMargin: float = 0.0,
                 lastGridExposure: float = 0.0,
                 lastGridLoss: float = 0.0,
                 lastGridAvailableBalance: float = 0.0,
                 lastGridExposurePerc: float = 0.0,
                 lastGridLossToLiquidation: float = 0.0
                 # positions: dict[str, PositionSummary] = None,
                 # orders: dict[str, OrderStatus] = None,
                 # incomes: dict[str, IncomeSummary] = None,
                 # positionsTot = None
                 ):
        self.name: str = name
        self.timestamp: int = timestamp
        self.balance: float = balance
        self.totUnrealizedProfit: float = totUnrealizedProfit
        self.totRealizedProfitPerc: float = totRealizedProfitPerc
        self.totRealizedProfit: float = totRealizedProfit
        self.totInitialMargin: float = totInitialMargin
        self.totOpenOrderInitialMargin: float = totOpenOrderInitialMargin
        self.availableBalance: float = availableBalance
        self.totalMaintMargin: float = totalMaintMargin
        self.lastGridExposure: float = lastGridExposure
        self.lastGridLoss: float = lastGridLoss
        self.lastGridAvailableBalance: float = lastGridAvailableBalance
        self.lastGridExposurePerc: float = lastGridExposurePerc
        self.lastGridLossToLiquidation: float = lastGridLossToLiquidation
        self.positions: Optional[dict[str, PositionSummary]] = None
        self.orders: Optional[dict[str, OrderStatus]] = None
        self.incomes: Optional[dict[str, IncomeSummary]] = None
        self.positionsTot: Optional[PositionSummary] = None
        self.start_timestamp: int = 0
        self.end_timestamp: int = 0

    # noinspection PyListCreation
    def to_str(self):
        def zero_to_blank(n: float, f: str):
            return f.format(n) if n != 0 else ''

        tot = self.positionsTot
        fmtl_str =  '| {:12} | {:>12} | {:>18} | {:>15} | {:>12} | {:>12} | {:>21} | {:>16} | {:>26} | {:>16} | {:>15} | {:>15} |'
        fmth_str = '| {:^12} | {:^12} | {:^18} | {:^15} | {:^12} | {:^12} | {:^21} | {:^16} | {:^26} | {:^16} | {:^15} | {:^15} |'
        header  = fmth_str.format('Symbol', 'Unrealized',  'Net Realized', 'Gross Realized', 'Commission', 'Funding', 'Exposure',      'Number of',    'Open Grid Orders',           'Open TP Orders',   'Position', 'Position' )
        header2 = fmth_str.format('',       'Profit',      'Profit',       'Profit',         'Fees',       'Fees',    '(% of wallet)', 'take profits', '  n°  value  (% of wallet)', 'n°  value',        'Amount',   'Entry Price' )

        out_str: list[str] = []
        # out_str.append('#' * len(header))
        # out_str.append('# BOT  {}  updated at: {}'.format(self.name, datetime.datetime.fromtimestamp(self.timestamp / 1000).isoformat(sep=' ', timespec='seconds')))
        # out_str.append('#')
        out_str.append('BOT {}'.format(self.name))
        out_str.append('  from : {}'.format(datetime.datetime.fromtimestamp(self.start_timestamp / 1000).isoformat(sep=' ', timespec='seconds')))
        out_str.append('  to   : {}'.format(datetime.datetime.fromtimestamp(self.end_timestamp / 1000).isoformat(sep=' ', timespec='seconds')))
        out_str.append('')
        out_str.append('Wallet Balance             : {:15,.2f}'.format(self.balance                  ))
        out_str.append('Unrealized Profit          : {:15,.2f}'.format(self.totUnrealizedProfit      ))
        out_str.append('Position Initial Margin    : {:15,.2f}'.format(self.totInitialMargin         ))
        out_str.append('Open Order Initial Margin  : {:15,.2f}'.format(self.totOpenOrderInitialMargin))
        out_str.append('Available Balance          : {:15,.2f}'.format(self.availableBalance         ))
        out_str.append('')
        out_str.append('Today Realized Profit      : {:15,.2f}'.format(self.totRealizedProfit        ))
        out_str.append('Today Realized Profit %    : {:15,.2%}'.format(self.totRealizedProfitPerc    ))
        out_str.append('')
        out_str.append('Last grid exposure         : {:15,.2f}'.format(self.lastGridExposure))
        out_str.append('Last grid loss             : {:15,.2f}'.format(self.lastGridLoss))
        out_str.append('Last grid available balance: {:15,.2f}'.format(self.lastGridAvailableBalance))
        out_str.append('Last grid exposure %       : {:15,.2%}'.format(self.lastGridExposurePerc))
        out_str.append('')
        out_str.append('-' * len(header))
        out_str.append(header)
        out_str.append(header2)
        out_str.append('-' * len(header))
        for p in sorted(self.positions.values(), key=lambda p: -p.realizedPnl):
            out_str.append(fmtl_str.format(
                p.symbol,
                zero_to_blank(p.unrealizedProfit, '{:,.2f}'),
                '{} {:>8}'.format(
                    zero_to_blank(p.realizedPnl, '{:,.2f}'),
                    zero_to_blank(p.realizedPnl / tot.realizedPnl, '({:,.1%})') if tot.realizedPnl != 0 else '-'
                ),
                zero_to_blank(p.grossRealizedPnl, '{:,.2f}'),
                zero_to_blank(p.commission, '{:,.2f}'),
                zero_to_blank(p.fundingFee, '{:,.2f}'),
                '{} {:>8}'.format(
                    zero_to_blank(p.exposure, '{:,.2f}'),
                    zero_to_blank(p.exposurePerc, '({:,.1%})')
                ),
                '{} {:>8}'.format(
                    zero_to_blank(p.tradeCount, '{:d}'),
                    zero_to_blank(p.tradeCountPerc, '({:,.1%})')
                ),
                '{} {:>12} {:>9}'.format(
                    zero_to_blank(p.openingOrderCount, '{:,d}'),
                    zero_to_blank(p.openingOrderValue, '{:,.2f}'),
                    zero_to_blank(p.openingOrderValuePerc, '({:,.1%})')
                ),
                '{} {:>12}'.format(
                    zero_to_blank(p.closingOrderCount, '{:,d}'),
                    zero_to_blank(p.closingOrderValue, '{:,.2f}')
                ),
                zero_to_blank(p.positionAmt, '{:,.6f}'),
                zero_to_blank(p.entryPrice, '{:,.6f}'),
            ))
        out_str.append('=' * len(header))
        out_str.append(fmtl_str.format(
            'TOT',
            zero_to_blank(tot.unrealizedProfit, '{:,.2f}'),
            '{} {:>8}'.format(
                zero_to_blank(tot.realizedPnl, '{:,.2f}'),
                zero_to_blank(1, '({:,.1%})')
            ),
            zero_to_blank(tot.grossRealizedPnl, '{:,.2f}'),
            zero_to_blank(tot.commission, '{:,.2f}'),
            zero_to_blank(tot.fundingFee, '{:,.2f}'),
            '{} {:>8}'.format(
                zero_to_blank(tot.exposure, '{:,.2f}'),
                zero_to_blank(tot.exposurePerc, '({:,.1%})')
            ),
            '{} {:>8}'.format(
                zero_to_blank(tot.tradeCount, '{:,d}'),
                zero_to_blank(1, '({:,.1%})')
            ),
            '{} {:>12} {:>9}'.format(
                zero_to_blank(tot.openingOrderCount, '{:,d}'),
                zero_to_blank(tot.openingOrderValue, '{:,.2f}'),
                zero_to_blank(tot.openingOrderValuePerc, '({:,.1%})')
            ),
            '{} {:>12}'.format(
                zero_to_blank(tot.closingOrderCount, '{:,d}'),
                zero_to_blank(tot.closingOrderValue, '{:,.2f}')
            ),
            '',
            '',
        ))
        out_str.append('-' * len(header))
        return '\n'.join(out_str)

    def to_json(self):
        return json.dumps(self, indent=2, cls=BotSummaryEncoder)


class BotSummaryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def get_binance_bot_summary(bot_name, api_key, api_secret, start_timestamp=0, end_timestamp=0) -> BotSummary:
    client = Client(api_key, api_secret)
    
    print ('binance_bot_summary logs')
    now=datetime.datetime.now(tz=datetime.timezone.utc)
    print ('now=',now)
    bot_summary = BotSummary(bot_name, int(now.timestamp() * 1000))#1000 = seconds to milliseconds

    if start_timestamp == 0:
        start_timestamp = int(datetime.datetime(now.year, now.month, now.day, tzinfo=datetime.timezone.utc).timestamp() * 1000) #1000 = seconds to milliseconds
        print('start_timestamp=0 pertanto lo calcolo: ', start_timestamp)

    if end_timestamp == 0:
        end_timestamp = int(datetime.datetime(now.year, now.month, now.day,23,59,59, tzinfo=datetime.timezone.utc).timestamp() * 1000) #1000 = seconds to milliseconds
        print('end_timestamp=0 pertanto lo calcolo: ', end_timestamp)

    #loggo i valori delle date 
    print("start_timestamp:",start_timestamp," end_timestamp:",end_timestamp)
    start_win=datetime.date.fromtimestamp(start_timestamp/1000)
    end_win=datetime.date.fromtimestamp(end_timestamp/1000)
    print("cerco elementi compresi tra (start_win): ",start_win.strftime("%Y-%m-%d %H:%M:%S")," e (end_win): ",end_win.strftime("%Y-%m-%d %H:%M:%S"))

    bot_summary.start_timestamp = start_timestamp
    bot_summary.end_timestamp = end_timestamp

    positions_by_symbol = {}
    orders_by_symbol = {}

    try:
        account = client.futures_account(timestamp= now.timestamp())
        for p in account['positions']:
            symbol = get_symbol(p)
            positions_by_symbol[symbol] = p
    except Exception as e: 
        print('Eccezione raggiunta durante richiesta futures_account: ',e)
        account = {}
    
    try:
        orders = client.futures_get_open_orders()
    except Exception as e: 
        print('Eccezione raggiunta durante richiesta futures_get_open_orders: ',e)
        orders = []

    for o in orders:
        symbol = get_symbol(o)
        if symbol not in orders_by_symbol:
            orders_by_symbol[symbol] = OrderStatus()
        obs = orders_by_symbol[symbol]
        qty = (float(o['origQty']) - float(o['executedQty'])) * (1 if o['side'] == 'BUY' else -1)
        price = float(o['price'])
        value = price * qty
        pos_qty = float(positions_by_symbol[symbol]['positionAmt']) if symbol in positions_by_symbol else 0.0
        if o['reduceOnly']:
            obs.closingCount = obs.closingCount + 1
            obs.closingAmt = obs.closingAmt + qty
            obs.closingValue = obs.closingValue + value
            if obs.tpPrice == 0:
                obs.tpPrice = price
            elif pos_qty >= 0:
                obs.tpPrice = max(obs.tpPrice, price)
            else:
                obs.tpPrice = min(obs.tpPrice, price)
        elif (pos_qty >= 0 and o['side'] == 'BUY') or (pos_qty < 0 and o['side'] == 'SELL'):
            obs.openingCount = obs.openingCount + 1
            obs.openingAmt = obs.openingAmt + qty
            obs.openingValue = obs.openingValue + value
            if obs.lastGridPrice == 0:
                obs.lastGridPrice = price
            elif pos_qty >= 0:
                obs.lastGridPrice = min(obs.lastGridPrice, price)
            else:
                obs.lastGridPrice = max(obs.lastGridPrice, price)

    trades = []
    tlen = -1
    max_num_incomes = 1000
    last_num_trds = max_num_incomes
    start_timestamp_copy = start_timestamp
    while len(trades) > tlen and last_num_trds == max_num_incomes:
        try:
            tmp_trades = client.futures_account_trades(startTime=start_timestamp_copy, endTime=end_timestamp, limit=max_num_incomes)
        except Exception as e: 
            print('Eccezione raggiunta durante richiesta futures_account_trades: ',e)
            tmp_trades = []

        last_num_trds = len(tmp_trades)
        if last_num_trds > 0:
            max_time = max(tmp_trades, key=lambda k: k['time'])['time']
            tlen = len(trades)
            new_trades = [t for t in tmp_trades if t['time'] < max_time or last_num_trds < max_num_incomes]
            trades.extend(new_trades)
            start_timestamp_copy = max_time

    incomes = []
    ilen = -1
    max_num_incomes = 1000
    last_num_incomes = max_num_incomes
    start_timestamp_copy = start_timestamp
    while len(incomes) > ilen and last_num_incomes == max_num_incomes:
        try:
            tmp_incomes = client.futures_income_history(startTime=start_timestamp_copy, endTime=end_timestamp, limit=max_num_incomes, incomeType='FUNDING_FEE', timestamp= now.timestamp() ) 
        except Exception as e: 
            print('Eccezione raggiunta durante richiesta futures_income_history: ',e)
            tmp_incomes = []

        last_num_incomes = len(tmp_incomes)
        if last_num_incomes > 0:
            max_time = max(tmp_incomes, key=lambda k: k['time'])['time']
            ilen = len(incomes)
            new_incomes = [t for t in tmp_incomes if t['time'] < max_time or last_num_incomes < max_num_incomes]
            incomes.extend(new_incomes)
            start_timestamp_copy = max_time

    asset_prices = {
        'USDT': 1.0
    }
    income_by_symbol: dict[str, IncomeSummary] = {}

    for t in trades:
        symbol = get_symbol(t)
        commission_asset = t['commissionAsset']
        commission_asset_price = get_asset_price(commission_asset, asset_prices, client, end_timestamp, now)
        margin_asset = t['marginAsset']
        margin_asset_price = get_asset_price(margin_asset, asset_prices, client, end_timestamp, now)
        commission = float(t['commission']) * commission_asset_price
        realizedPnl = float(t['realizedPnl']) * margin_asset_price
        if symbol not in income_by_symbol:
            income_by_symbol[symbol] = IncomeSummary()
        tbs = income_by_symbol[symbol]
        if float(t['realizedPnl']) != 0.0:
            tbs.count = tbs.count + 1
        tbs.netRealizedPnl = tbs.netRealizedPnl - commission + realizedPnl
        tbs.realizedPnl = tbs.realizedPnl + realizedPnl
        tbs.commission = tbs.commission + commission

    for t in incomes:
        symbol = t['symbol']
        asset = t['asset']
        asset_price = get_asset_price(asset, asset_prices, client, end_timestamp, now )
        income_type = str(t['incomeType']).lower()
        income = float(t['income']) * asset_price
        if symbol not in income_by_symbol:
            income_by_symbol[symbol] = IncomeSummary()
        tbs = income_by_symbol[symbol]
        if income_type not in ('realizedPnl', 'commission'):
            tbs.netRealizedPnl = tbs.netRealizedPnl + income
            if hasattr(tbs, income_type):
                tbs.__dict__[income_type] = tbs.__dict__[income_type] + income

    tot = PositionSummary('TOTAL')
    tot.unrealizedProfit = 0.0
    tot.tradeCount = 0
    tot.realizedPnl = 0.0
    tot.exposure = 0.0
    tot.exposurePerc = 0.0
    tot.openingOrderCount = 0
    tot.closingOrderCount = 0
    tot.openingOrderValue = 0.0
    tot.closingOrderValue = 0.0
    bot_summary.positions = {}
    bot_summary.positionsTot = tot

    if(account == {}):
        for symbol in income_by_symbol.keys():
            income = income_by_symbol[symbol]
            ps = PositionSummary(symbol)
            bot_summary.positions[symbol] = ps
            ps.tradeCount = income.count if income is not None else 0
            ps.realizedPnl = income.netRealizedPnl if income is not None else 0.0
            ps.grossRealizedPnl = income.realizedPnl if income is not None else 0.0
            ps.fundingFee = income.fundingFee if income is not None else 0.0
            ps.commission = income.commission + income.insuranceClear if income is not None else 0.0
            tot.tradeCount = tot.tradeCount + ps.tradeCount
            tot.realizedPnl = tot.realizedPnl + ps.realizedPnl
            tot.grossRealizedPnl = tot.grossRealizedPnl + ps.grossRealizedPnl
            tot.fundingFee = tot.fundingFee + ps.fundingFee
            tot.commission = tot.commission + ps.commission
        for p in bot_summary.positions.values():
            p.realizedPnlPerc = p.realizedPnl / tot.realizedPnl if tot.realizedPnl != 0 else 0.0
            p.tradeCountPerc = p.tradeCount / tot.tradeCount if tot.tradeCount != 0 else 0.0 
    else:
        bot_summary.balance = float(account['totalWalletBalance'])
        bot_summary.totUnrealizedProfit = float(account['totalUnrealizedProfit'])
        bot_summary.totInitialMargin = float(account['totalPositionInitialMargin'])
        bot_summary.totOpenOrderInitialMargin = float(account['totalOpenOrderInitialMargin'])
        bot_summary.availableBalance = float(account['availableBalance'])
        bot_summary.totalMaintMargin = float(account['totalMaintMargin'])
        
        positions = [p for p in account['positions'] if float(p['positionAmt']) != 0 or get_symbol(p) in income_by_symbol or get_symbol(p) in orders_by_symbol]

        for p in positions:
            symbol = get_symbol(p)
            ps = PositionSummary(symbol)
            bot_summary.positions[symbol] = ps
            income = income_by_symbol[symbol] if symbol in income_by_symbol else IncomeSummary()
            order = orders_by_symbol[symbol] if symbol in orders_by_symbol else None
            ps.leverage = float(p['leverage'])
            ps.unrealizedProfit = float(p['unrealizedProfit'])
            ps.entryPrice = float(p['entryPrice'])
            ps.positionAmt = float(p['positionAmt'])
            ps.tradeCount = income.count if income is not None else 0
            ps.realizedPnl = income.netRealizedPnl if income is not None else 0.0
            ps.openingOrderCount = order.openingCount if order is not None else 0
            ps.closingOrderCount = order.closingCount if order is not None else 0
            ps.openingOrderQty = order.openingAmt if order is not None else 0
            ps.closingOrderQty = order.closingAmt if order is not None else 0
            ps.openingOrderValue = order.openingValue if order is not None else 0.0
            ps.closingOrderValue = order.closingValue if order is not None else 0.0
            ps.grossRealizedPnl = income.realizedPnl if income is not None else 0.0
            ps.fundingFee = income.funding_fee if income is not None else 0.0
            ps.commission = income.commission + income.insuranceClear if income is not None else 0.0
            ps.tpPrice = order.tpPrice if order is not None else 0.0
            ps.currentPrice = (ps.entryPrice * ps.positionAmt + ps.unrealizedProfit) / ps.positionAmt if ps.positionAmt != 0.0 else 0.0
            ps.diffCurPriceFromTpPerc = ps.currentPrice / ps.tpPrice - 1 if ps.tpPrice != 0.0 else 0.0
            tot.unrealizedProfit = tot.unrealizedProfit + ps.unrealizedProfit
            tot.tradeCount = tot.tradeCount + ps.tradeCount
            tot.realizedPnl = tot.realizedPnl + ps.realizedPnl
            ps.exposure = abs(ps.positionAmt * ps.entryPrice) + ps.unrealizedProfit
            ps.exposurePerc = ps.exposure / bot_summary.balance
            if order is not None and order.openingAmt != 0:
                last_grid_amt = ps.positionAmt + order.openingAmt
                ps.lastGridExposure = last_grid_amt * order.lastGridPrice
                ps.lastGridCost = ps.positionAmt * ps.entryPrice + order.openingValue
                ps.lastGridLoss = ps.lastGridExposure - ps.lastGridCost
                ps.lastGridEntryPrice = ps.lastGridCost / last_grid_amt
            else:
                ps.lastGridExposure = ps.exposure
                ps.lastGridLoss = ps.unrealizedProfit
                ps.lastGridCost = ps.positionAmt * ps.entryPrice
                ps.lastGridEntryPrice = ps.entryPrice
            tot.exposure = tot.exposure + ps.exposure
            tot.exposurePerc = tot.exposurePerc + ps.exposurePerc
            tot.openingOrderCount = tot.openingOrderCount + ps.openingOrderCount
            tot.closingOrderCount = tot.closingOrderCount + ps.closingOrderCount
            tot.openingOrderValue = tot.openingOrderValue + ps.openingOrderValue
            tot.closingOrderValue = tot.closingOrderValue + ps.closingOrderValue
            tot.grossRealizedPnl = tot.grossRealizedPnl + ps.grossRealizedPnl
            tot.fundingFee = tot.fundingFee + ps.fundingFee
            tot.commission = tot.commission + ps.commission
            tot.lastGridExposure = tot.lastGridExposure + abs(ps.lastGridExposure)
            tot.lastGridLoss = tot.lastGridLoss + ps.lastGridLoss
            tot.lastGridCost = tot.lastGridCost + ps.lastGridCost

            for p in bot_summary.positions.values():
                p.realizedPnlPerc = p.realizedPnl / abs(tot.realizedPnl) if tot.realizedPnl != 0 else 0.0
                p.tradeCountPerc = p.tradeCount / tot.tradeCount if tot.tradeCount != 0 else 0.0
                p.openingOrderValuePerc = p.openingOrderValue / bot_summary.balance if bot_summary.balance != 0 else 0.0
                tot.openingOrderValuePerc = tot.openingOrderValuePerc + p.openingOrderValuePerc

            bot_summary.lastGridExposure = tot.lastGridExposure
            bot_summary.lastGridLoss = tot.lastGridLoss
            bot_summary.lastGridAvailableBalance = bot_summary.availableBalance + tot.lastGridLoss
            bot_summary.lastGridExposurePerc = tot.lastGridExposure / bot_summary.lastGridAvailableBalance

            mainteniance_perc = bot_summary.totalMaintMargin / bot_summary.totInitialMargin if bot_summary.totInitialMargin != 0.0 else 0.0
            last_grid_tot_initial_margin = bot_summary.totInitialMargin + bot_summary.totOpenOrderInitialMargin
            last_grid_mainteniance_margin = last_grid_tot_initial_margin * mainteniance_perc
            last_grid_max_loss_to_liquidation = bot_summary.lastGridAvailableBalance - last_grid_mainteniance_margin
            bot_summary.lastGridLossToLiquidation = last_grid_max_loss_to_liquidation / bot_summary.lastGridExposure if bot_summary.lastGridExposure != 0.0 else 0
        bot_summary.totRealizedProfitPerc = tot.realizedPnl / (bot_summary.balance - tot.realizedPnl)      

    bot_summary.totRealizedProfit = tot.realizedPnl

    return bot_summary


def get_symbol(p):
    return p['symbol'] + ('_' + p['positionSide'] if p['positionSide'] != 'BOTH' else '')


def get_asset_price(asset, asset_prices, client, end_timestamp,  now):
    try:
        if asset in asset_prices:
            asset_price = asset_prices[asset]
        elif int(now.timestamp()) - end_timestamp > 24 * 60 * 60 * 1000:
            kline = client.get_klines(symbol=asset + 'USDT', interval='1d', limit=1, startTime=end_timestamp)
            asset_price = float(kline[0][4])
            asset_prices[asset] = asset_price
        else:
            avg_price = client.get_avg_price(symbol=asset + 'USDT')
            asset_price = float(avg_price['price'])
            asset_prices[asset] = asset_price
    except:
        asset_price = 1.0
    return asset_price

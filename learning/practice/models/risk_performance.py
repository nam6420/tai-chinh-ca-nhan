"""H3/H4: đo mẫu quá khứ và dòng tiền; không kết nối giao dịch."""
from datetime import date
from math import isfinite, prod
from statistics import stdev


def numbers(values):
    result = list(values)
    if not result or any(not isinstance(x, (int, float)) or not isfinite(x) for x in result):
        raise ValueError('Cần dãy số hữu hạn, không rỗng')
    return result


def returns(values):
    values = numbers(values)
    if len(values) < 2 or min(values) <= 0:
        raise ValueError('Cần ít nhất hai giá trị dương, đã điều chỉnh dòng tiền')
    return [b / a - 1 for a, b in zip(values, values[1:])]


def sample_volatility(rates):
    rates = numbers(rates)
    if len(rates) < 2:
        raise ValueError('Cần ít nhất hai lợi suất')
    return stdev(rates)


def drawdowns(values):
    values = numbers(values)
    if min(values) <= 0:
        raise ValueError('Cần giá trị dương, đã điều chỉnh dòng tiền')
    peak = values[0]
    result = []
    for value in values:
        peak = max(peak, value)
        result.append(value / peak - 1)
    return result


def recovery(loss):
    if not isinstance(loss, (int, float)) or not isfinite(loss) or not 0 <= loss < 1:
        raise ValueError('Mức mất vốn phải từ 0 đến dưới 100%')
    return 1 / (1 - loss) - 1


def twr(starts, ends):
    starts, ends = numbers(starts), numbers(ends)
    if len(starts) != len(ends) or min(starts) <= 0 or min(ends) < 0:
        raise ValueError('Hai dãy cùng cỡ; đầu kỳ dương, cuối kỳ không âm')
    return prod(b / a for a, b in zip(starts, ends)) - 1


def npv(rate, flows, times):
    flows, times = numbers(flows), numbers(times)
    if len(flows) != len(times) or not isfinite(rate) or rate <= -1:
        raise ValueError('Dòng tiền và thời điểm phải khớp; lãi suất > -1')
    return sum(c / (1 + rate) ** t for c, t in zip(flows, times))


def bracketed_irr(flows, times, low=-.9, high=1.):
    """Một nghiệm trong khoảng đổi dấu do người học chọn; KHÔNG chứng minh duy nhất."""
    flows, times = numbers(flows), numbers(times)
    if len(flows) != len(times) or any(t < 0 for t in times) or times != sorted(times):
        raise ValueError('Thời điểm không âm, tăng dần, cùng cỡ dòng tiền')
    if not -1 < low < high or not isfinite(high):
        raise ValueError('Khoảng nghiệm phải hữu hạn và lớn hơn -1')
    a, b = npv(low, flows, times), npv(high, flows, times)
    if a == 0:
        return low
    if b == 0:
        return high
    if a * b > 0:
        raise ValueError('Không đổi dấu tại hai đầu; không kết luận không tồn tại nghiệm')
    for _ in range(160):
        mid = (low + high) / 2
        value = npv(mid, flows, times)
        if value == 0:
            return mid
        if a * value > 0:
            low, a = mid, value
        else:
            high = mid
    return (low + high) / 2


def xirr(flows, dates, low=-.9, high=1.):
    """Số ngày thực/365 cố định; ngày phải tăng dần. Một nghiệm có kẹp."""
    days = [date.fromisoformat(d) for d in dates]
    if not days or days != sorted(days):
        raise ValueError('Ngày không rỗng và tăng dần')
    times = [(d - days[0]).days / 365 for d in days]
    return bracketed_irr(flows, times, low, high)


def sell_book(bids, quantity):
    """Sổ mua tĩnh giá giảm dần. Không giả định lượng thiếu bán được."""
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError('Số lượng cần bán là số nguyên dương')
    left, proceeds, last = quantity, 0., float('inf')
    for price, size in bids:
        if not isfinite(price) or price <= 0 or price > last or not isinstance(size, int) or size < 0:
            raise ValueError('Sổ mua: giá dương giảm dần, lượng nguyên không âm')
        take = min(left, size)
        proceeds += take * price
        left -= take
        last = price
    filled = quantity - left
    return dict(filled=filled, unfilled=left, proceeds=proceeds,
                average=proceeds / filled if filled else None)


if __name__ == '__main__':
    v = [100, 110, 88, 101.2, 106.26]
    print('H3:', returns(v), sample_volatility(returns(v)), drawdowns(v), recovery(.2))
    print('H3 sổ mua:', sell_book([(20000, 200), (19800, 300), (19000, 500)], 1200))
    cf = [-100, -100, 39, 180]
    print('H4 TWR, IRR:', twr([100, 210, 150], [110, 189, 180]), bracketed_irr(cf, [0, 1, 2, 3]))
    print('H4 XIRR:', xirr(cf, ['2023-01-01', '2023-07-01', '2024-07-01', '2025-01-01']))

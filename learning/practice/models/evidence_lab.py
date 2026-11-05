"""H5: kiểm chứng bảng ví dụ, không xây quy tắc giao dịch."""
from math import isfinite, prod


def compound(rates):
    rates = list(rates)
    if not rates or any(not isfinite(x) or x < -1 for x in rates):
        raise ValueError('Lợi suất hữu hạn và không dưới -100%')
    return prod(1 + x for x in rates) - 1


def false_positives(trials, probability):
    if not isinstance(trials, int) or trials <= 0 or not isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError('Số lần thử nguyên dương, xác suất từ 0 đến 1')
    return trials * probability, 1 - (1 - probability) ** trials


def net_period(gross, traded_over_start, one_way_cost):
    """Trừ chi phí tính trên tổng giá trị MUA cộng BÁN chia vốn đầu kỳ."""
    if any(not isfinite(x) for x in (gross, traded_over_start, one_way_cost)):
        raise ValueError('Cần số hữu hạn')
    if gross < -1 or traded_over_start < 0 or one_way_cost < 0:
        raise ValueError('Đầu vào ngoài phạm vi')
    net = gross - traded_over_start * one_way_cost
    if net < -1:
        raise ValueError('Chi phí vượt vốn, mô hình đơn giản không áp dụng')
    return net


def available(period_end, published, decision):
    """Chuỗi ISO YYYY-MM-DD; cần đã kết thúc kỳ VÀ đã công bố."""
    from datetime import date
    end, release, cut = [date.fromisoformat(s) for s in (period_end, published, decision)]
    if release < end:
        raise ValueError('Ngày công bố không thể trước ngày kết thúc kỳ trong bộ ví dụ này')
    return end <= cut and release <= cut


# Tất cả lợi suất dưới đây là dữ liệu HƯ CẤU, không phải chiến lược được đề xuất.
RULES = {'A': [.04, .04, .04, .04, -.03, -.03],
         'B': [.02, .02, .02, .02, .01, .01],
         'C': [-.01, .03, -.01, .03, .02, -.02]}


if __name__ == '__main__':
    for name, rates in RULES.items():
        print(name, 'xây dựng', compound(rates[:4]), 'ngoài mẫu', compound(rates[4:]),
              'ngoài mẫu sau phí', compound([net_period(x, 2, .005) for x in rates[4:]]))
    print('Kiểm định độc lập:', false_positives(100, .05))

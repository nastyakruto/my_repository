import math
x1, y1, x2, y2= map(int, input().split())
def min_way(x1, y1, x2, y2):
    x1_squared = x1*x1
    x2_squared = x2*x2
    y1_squared = y1*y1
    y2_squared = y2*y2
    r1 = math.sqrt(x1_squared + y1_squared)
    r2 = math.sqrt(x2_squared + y2_squared)
    if x1 != 0 or y1!= 0:
        if x2!=0 or y2 != 0:
            r3 = abs(r1-r2)
            angle_radian = abs(math.atan2(y1, x1) - math.atan2(y2, x2))
            angle_degree = angle_radian * 180 / math.pi
            if r1 <= r2:
                len_arc = (math.pi * r2 * angle_degree) / 180
                way_by_arc = len_arc + r3
                way_by_straight = r1 + r2
                ans = min(way_by_arc,way_by_straight)
            else:
                len_arc = (math.pi * r1 * angle_degree) / 180
                way_by_arc = len_arc + r3
                way_by_straight = r1 + r2
                ans = min(way_by_arc,way_by_straight)
            return "%.12f" % ans
        else:
            ans = r1
    else:
        ans = r2
    return "%.12f" % ans
print(min_way(x1, y1, x2, y2))
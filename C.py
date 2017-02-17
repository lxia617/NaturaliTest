# coding=utf-8

points = [
    [-4, -1],
    [-1, -2],
    [2, -4],
    [0, 2],
    [0, 3],
    [5, -2]
]


def min_distance(points):
    sorted_x_points = sorted(points, key=lambda items: items[0])
    tmp_x_points = [x+[idx+1] for idx, x in enumerate(sorted_x_points)]
    sorted_x_points = [[0, 0]] + sorted_x_points
    sorted_y_points = [[0, 0, 0]] + sorted(tmp_x_points, key=lambda items: items[1])

    n = len(points)
    sum_x = [0] * (n+1)
    sum_y = [0] * (n+1)
    for i in xrange(1, n+1):
        sum_x[i] = sum_x[i-1] + sorted_x_points[i][0]
        sum_y[i] = sum_y[i-1] + sorted_y_points[i][1]

    ans = int(1e9)
    for j in xrange(1, n+1):
        i = sorted_y_points[j][2]
        res_x = (i-1) * sorted_x_points[i][0] - sum_x[i-1] + sum_x[n] - sum_x[i] - (n - i) * sorted_x_points[i][0]
        res_y = (j-1) * sorted_y_points[j][1] - sum_y[j-1] + sum_y[n] - sum_y[j] - (n - j) * sorted_y_points[j][1]
        res = res_x + res_y

        ans = min(res, ans)
    return ans

if __name__ == '__main__':
    print 'min distance is', min_distance(points)

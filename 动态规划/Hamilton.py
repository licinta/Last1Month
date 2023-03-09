from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100005)


@lru_cache(None)
# def hamilton(trace: int, endpoint: int, graph: tuple[tuple[int]]) -> int:
def hamilton(trace, endpoint, graph):
    """
    Point that had been travelled were 1 and haven't been travelled 0.
    with an endpoint specified.
    with poor time-complexity, but it's right
    """
    n = len(graph)
    if trace == 0 and endpoint == 0:
        return 0
    if trace == 0 and endpoint != 0:
        return 0xffffff
    ans = 0xffffff
    li = list(map(int, list(str(bin(trace))[2:].rjust(n, '0'))))
    for i, j in enumerate(li):
        if j == 1:
            # find the sub-question's best solution, make the i-th bit its own opposite (1->0).
            temp = trace ^ (1 << (n - i - 1))
            # the last endpoint will be i in sub-question.
            ans = min(ans, hamilton(temp, i, graph) + graph[i][endpoint])
    return ans


def hamilton_dp(graph):
    """
    wrong?
    why
    """
    n = len(graph)
    dp = [[float("inf") for i in range(1 << n)] for j in range(n)]
    #
    dp[0][0] = 0
    for trace in range(1 << n):
        for ne_point in range(n):
            for pre_point in range(n):
                if (trace >> pre_point) & 1 == 0 or (trace >> ne_point) & 1 == 0:
                    continue
                pre_trace = trace ^ (1 << (n - 1 - pre_point))
                dp[ne_point][trace] = min(dp[ne_point][trace], dp[pre_point][pre_trace] + graph[pre_point][ne_point])

    return dp[-1][2 ** n - 2]


if __name__ == "__main__":
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(tuple(map(int, input().split())))
        # from 0 to n-1
    # print(hamilton(2 ** n - 2, n - 1, tuple(graph)))
    print(hamilton_dp(graph))

"""
20
0 42 284 286 248 170 196 290 241 217 356 255 146 209 264 242 327 289 188 387
42 0 326 328 290 212 154 278 229 205 398 297 188 197 252 230 369 331 176 429
284 326 0 74 36 240 202 224 191 151 280 43 138 159 203 181 115 121 180 249
286 328 74 0 38 242 183 217 182 144 282 36 140 152 129 107 41 123 161 251
248 290 36 38 0 204 166 188 155 115 244 7 102 123 167 145 79 85 144 213
170 212 240 242 204 0 105 185 136 112 278 211 125 104 159 137 283 119 83 247
196 154 202 183 166 105 0 124 75 51 274 159 64 43 98 76 224 224 22 305
290 278 224 217 188 185 124 0 113 73 271 181 144 81 98 120 258 273 102 302
241 229 191 182 155 136 75 113 0 40 275 148 95 32 53 75 151 240 53 306
217 205 151 144 115 112 51 73 40 0 281 108 71 8 93 83 185 200 29 312
356 398 280 282 244 278 274 271 275 281 0 251 210 273 222 244 323 159 252 31
255 297 43 36 7 211 159 181 148 108 251 0 109 116 165 143 77 92 137 220
146 188 138 140 102 125 64 144 95 71 210 109 0 63 118 96 181 187 42 241
209 197 159 152 123 104 43 81 32 8 273 116 63 0 85 75 183 208 21 304
264 252 203 129 167 159 98 98 53 93 222 165 118 85 0 22 170 200 76 253
242 230 181 107 145 137 76 120 75 83 244 143 96 75 22 0 148 222 54 275
327 369 115 41 79 283 224 258 151 185 323 77 181 183 170 148 0 164 202 292
289 331 121 123 85 119 224 273 240 200 159 92 187 208 200 222 164 0 202 128
188 176 180 161 144 83 22 102 53 29 252 137 42 21 76 54 202 202 0 283
387 429 249 251 213 247 305 302 306 312 31 220 241 304 253 275 292 128 283 0


1330
"""
# 단속카메라
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    ans = 0
    routes.sort(key = lambda x: x[1])
    camera = -30001

    for route in routes:
        if camera < route[0]:
            ans += 1
            camera = route[1]

    return ans

print(solution(routes))
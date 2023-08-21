n , m = map(int, input().split())
city = [list(map(int,input().split())) for _ in range(n)]
  
city_list = []
chicken_list = []

for i in range(1, n + 1) : 
    for j in range(1, n + 1) :
        if city[i-1][j-1] == 1 :
            city_list.append((i-1,j-1))
        elif city[i-1][j-1] == 2:
            chicken_list.append((i-1,j-1))

def chicken_distance(cities,stores,m) :
    each_chicken_distance = []
    
    for i in cities : 
        min_distance = []
        for j in stores:
          a = abs(i[0] - j[0]) + abs(i[1] - j[1])
          print('ij',i,j)
          print(a)
          min_distance.append(a)
        each_chicken_distance.append(min(min_distance))
    each_chicken_distance.sort()
    return each_chicken_distance

print(chicken_distance(city_list,chicken_list,3))
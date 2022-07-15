Infectious = 261858.0  # 5.1初始传染者
Recovered = 59504.0  # 康复者
Deadth = 9308.0  # 死亡患者数量
Exposed = 0.0  # 潜伏者
N = 1400000000.0  # 全国人口
N1 = 7589499.0  # 香港人口
Susceptible = N1 - Infectious - Deadth  # 易感染者
r1 = 1.0  # 开始发病初期，接触病患的人数  ?

a = 0.125  # 潜伏者患病概率
B = 0.01  # 感染概率  ?

y1 = 0.00126404  # 治愈率/天

k1 = 0.00003814
k2 = 0.05373  # 武汉基本病死率
k3 = 0.035373  # 湖北省病死率
k4 = 0.022  # 全国病死率

iArr = ['0'] * 100
iArr[0] = Infectious
eArr = ['0'] * 100
eArr[0] = Exposed
rArr = ['0'] * 100
rArr[0] = Recovered
sArr = ['0'] * 100
sArr[0] = Susceptible
dArr = ['0'] * 100
dArr[0] = Deadth


def outZero(n):
    if (n < 0.0):
        n = 0
    return n


def nextDay(day):
    # 易感人数迭代
    sArr[day + 1] = sArr[day] - r1 * B * iArr[day] * sArr[day] / N1
    sArr[day + 1] = outZero(sArr[day + 1])
    # 潜伏者人数迭代
    eArr[day + 1] = 20
    # eArr[day + 1] = eArr[day] + r1 * B * sArr[day] * iArr[day] / N1 - a * rArr[day]
    eArr[day + 1] = outZero(eArr[day + 1])
    # 患病人数迭代
    iArr[day + 1] = iArr[day] + a * eArr[day] - (y1 + k1) * iArr[day]
    # 康复人数迭代
    rArr[day + 1] = rArr[day] + y1 * iArr[day]
    rArr[day + 1] = outZero(rArr[day + 1])
    # 死亡患者人数迭代
    dArr[day + 1] = dArr[day] + k1 * iArr[day]


for i in range(0, 30):
    nextDay(i)
print('感染人：')
print(iArr)
print('潜伏人：')
print(eArr)
print('康复人')
print(rArr)
print('易感染人')
print(sArr)
print('死亡人')
print(dArr)
print(y1)

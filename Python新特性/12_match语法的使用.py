status = 400
match status:
    case 200:
        print('访问成功')
    case 404:
        print('访问的资源不存在')
    case 500:
        print('服务器错误')
    case _:
        print('以上都没有匹配成功')

p1 = ('zs',23,'man')
p2 = ('lili',24,'woman')
p3 = ('xiaoqiang',25,'man')
p4 = ('wanwu',25,'male')


def func_test(person):
    match person:
        case (name,_,'man'):
            print(f'{name} is man')
        case (name,_,'woman'):
            print(f'{name} is woman')
        case (name,age,sex):
            print(f'{name=},{age=},{sex=}')
#调用函数
func_test(p1)
func_test(p2)
func_test(p3)
func_test(p4)
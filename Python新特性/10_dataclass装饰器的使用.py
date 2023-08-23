from dataclasses import dataclass, field
from typing import ClassVar
@dataclass
class Player:
    name: str
    postion: str
    age: int
    sex: str = field(default='man', repr=False)
    # msg: str = field(default='')
    msg: str = field(default_factory=str)
    #类变量
    country:ClassVar[str]

# 创建实例对象
p = Player('zs', '北京', 24)
print(p)
Player.country = '中国'
print('类属性：',Player.country)
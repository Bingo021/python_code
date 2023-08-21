# 简单类型变量标注
# a:int = 10
# b:str = 'hello'
# c:float = 3.14
# d:bool = False
# e:bytes = b'world'

# 复杂类型
from typing import List, Set, Dict, Tuple
# x:List[int] = [1,2,3]
# x:Set[str] = {'ab','cd','ef'}
# x:Dict[str,str] = {'name':'zs','sex':'male'}
# x:Dict[str,object] = {'name':'zs','sex':'male','age':23}
# x:Tuple[int] = (3,)
# x:Tuple[int,int,int] = (3,4,5)
# x:Tuple[int,str,float] = (10,'hello',3.14)
# 定义可变大小的元组，使用省略号
# x:Tuple[int,...] =(1,2,3,4)

#3.10新特性list tuple divt set
# x:list[str] = ['a','b','c']
# x:tuple[int] = (2,)
# x:tuple[int,int] = (2,3)
# x:tuple[int,...] = (1,2,3,4,5,6)
# x:set[str] = {'aa','bb','cc'}
x:dict[str,object] = {'k1':1,'k20':4,'k3':6}

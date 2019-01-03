__all__ = ['initTest', 'time']  # 报错解决办法一,测试代码
# import time 之后 将time定义到__all__进去;如__all__ = ['initTest','time']

# __all__ = ['initTest', 'initTest2']  # 报错解决办法二,测试代码

import time  # 这里import time 进来

print('我在:initDemo/__init__.py')

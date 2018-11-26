import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    print("fire-i am ok!~LC")
    print("2倍为")
    return 2 * number

  def qiuhe(self, a, b):
    print('求和为')
    return a+b;

if __name__ == '__main__':
  fire.Fire(Calculator)
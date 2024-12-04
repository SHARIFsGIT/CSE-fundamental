from function import double_it
from kargs_multiple import full_name as name
from deafult_args import * # import all from deafult_args

f_name = name('Input', 'Output')
print(f_name)

result = double_it(100)
print(result)
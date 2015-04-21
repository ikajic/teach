import operations as op

x, y = 5, 10
print 'Using arguments:', x, y
print 'Sum:', op.add(x, y)
print 'Difference:', op.sub(arg1=x, arg2=y)
print 'Difference again:', op.sub(arg2=x, arg1=y)

x, y = 10.0, 0
print 'Using arguments:', x, y
print 'Multiplication:', op.mul(x, x)
print 'Division:', op.div(y, x)
print 'Division:', op.div(x, y)

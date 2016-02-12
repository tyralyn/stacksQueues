Various programs pertaining to stacks and queues, as practice, in Python. 

queueViaStacks: class queueViaStacks, an implementation of a queue in two stacks. The add method checks to see if s2 is empty, and if not, transfers all s2 items over to s1 and then appends the new item onto s1. The remove method checks to see if s1 is empty, and if not, transfers all items from s1 to s2 before removing the topmost item in s2.

singleArrayNStacks: class singleArrayNStacks, which is an implementation of N stacks in a single array. Upon initialization, it takes a number of stacks and an array length. It does not currently address issues of the number of stacks being larger than the array. The sizes of the stacks are constant, and the array is divided as evenly as possible amongst the stack. Variables include lists holding the start indexes (startIndices) and the indices of the tops of the stacks (topOfStack). Methods include testing the stack for fullness or emptiness, pushing and popping items from the stacks, and printing all of the stack elements out. 

stackWithPlates: stacks can only be of a certain height, so once the stack gets tall enough, create another stack, and this super stack should work the same way. Also includes a popAt method, which pops an item on a given stack, and then fills in the rest of the stack with higher-up items. 

stackWithMin: class stackWithMin that has as members a stack, a minStack, and the stackHeight. Every push or pop, the minStack is updated to have the current minimum at the top. push, pop, and min methods are of O(1) time. 
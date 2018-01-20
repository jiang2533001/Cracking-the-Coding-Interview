# Chapter 3 Stacks and Queues

### 3.3 Stack of Plates

__Solution:__ When push a new item into a substack, if the substack is full, just create a new stack and then push that item into new substack. On the other hand, when pop a item from a substack, if the substack is empty, it should be deleted. 

### 3.4 Queue via Stacks:

__Solution:__ There are two stacks, which are stack1 and stack2. When add a new item into this 'Queue', which means push that into stack1. When remove a item, the bottom item of the stack1 should be removed. So shift all items from stack1 to stack2. At this time, the bottom item in stack1 has been moved to the top in the stack2, and then pop the stack2. Eventually, shift all items from stack2 back to stack1.

### 3.5 Sort Stack:

__Solution:__ Pop the original stack and temporary stack, and compare these two items, if item from original stack is less than a item from temporary stack, push item from temporary stack to original stack, and pop new item from temporary to compare with that item again. Otherwise, push item from original stack to temporary stack. Iterate through original stack and process these operations until original stack is empty. Eventually, move all items from temporary stack to original stack. The minimum value is on the top of the original stack.

### 3.6 Animal Shelter:

__Solution:__ There are two separate queue to store dogs and cats. When insert a new animal item into a this animal queue, if it is dog, store it to dog queue otherwise cat queue. On the other hand, set a order to this item when it is inserted. When operate `dequeueAny`, just compare the order of first dog and first cat. 


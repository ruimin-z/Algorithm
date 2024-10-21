
## Deque

The following content is from [Python Documentation](https://docs.python.org/3/library/collections.html#collections.deque)

### class collections.deque([iterable[, maxlen]])¶

Returns a new deque object initialized left-to-right (using append()) with data from **iterable**. If iterable is not specified, the new deque is empty.

Deques are a generalization of **stacks** and **queues** (the name is pronounced “deck” and is short for “double-ended queue”). 

Deques support **thread-safe, memory efficient appends and pops** from _either side_ of the deque with approximately the same `O(1)` performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur `O(n)` memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

If maxlen is not specified or is `None`, deques may grow to an arbitrary length. 
Otherwise, the deque is bounded to the specified maximum length. 
Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end. 
Bounded length deques provide functionality similar to the tail filter in Unix. 
They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

Deque objects support the following methods: 

- append(x), 
- appendleft(x), 
- clear(), 
- copy(), 
- count(x), 
- pop(), 
- popleft(), 
- index(x[, start[, stop]]), 
- insert(i, x), 
- remove(value), 
- reverse(), 
- maxlen

In addition to the above, deques support 
- iteration, 
- pickling, 
- len(d), 
- reversed(d), 
- copy.copy(d),
- copy.deepcopy(d), 
- membership testing with the in operator, and 
- subscript references such as d[0] to access the first element. 

- Indexed access is `O(1)` at both ends but slows to `O(n)` in the middle. For fast random access, use lists instead.

Starting in version 3.5, deques support `__add__()`, `__mul__()`, and `__imul__()`.






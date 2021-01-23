##学习笔记


###Queue源码分析
####0. 概述
一个抽象queue数据结构的Interface，定义了相应的接口，会有实际的类来实现它
####1. Methods
* Insert
包括 add(E e) 和 offer(E e) 两个插入方法。
  其中add方法在超出容量时会抛出异常，而offer方法则会返回特殊值（true/false)

* Remove
包括 remove() 和 poll() 两个从队列中提取队列头元素并从对列中移除元素的方法。
  其中，当队列为空时，remove抛出异常，而poll返回null.
  
* Examine
包括 element() 和 peek() 两个提取队列头元素但不从队列中移除元素的方法。
  其中，当查询元素不存在时， element抛出异常，而peek返回null

###Priority Queue源码分析
####0. 概述
Queue Interface的一个具体实现类， 实现了Queue的所有方法。

####1. 源码解读

* 重载了6个初始化方法，提供了几种不同的初始化一个优先队列的方式:

`PriorityQueue()`
  
`PriorityQueue(int initialCapacity)`

`PriorityQueue(int initialCapacity, Comparator<? super E> comparator)`

`PriorityQueue(Collection<? extends E> c)`

`PriorityQueue(Comparator<? super E> comparator)`

`PriorityQueue(PriorityQueue<? extends E> c)`

`PriorityQueue(SortedSet<? extends E> c)`

* 实现了Queue接口定义的方法，选取一些核心方法分析如下：

```java
public boolean offer(E o) {
    if (o == null)
        throw new NullPointerException();
    int slot = findSlot(-1);
    storage[slot] = o;
    ++used;
    bubbleUp(slot);
    return true;
}
```

```java
int findSlot(int start) {
  int slot;
  if (used == storage.length)
    {
  resize();
  slot = used;
    }
  else
    {
  for (slot = start + 1; slot < storage.length; ++slot)
    {
      if (storage[slot] == null)
        break;
    }
  // We'll always find a slot.
    }
  return slot;
}
```

```java
void bubbleUp(int index) {
  // The element at INDEX was inserted into a blank spot.  Now move
  // it up the tree to its natural resting place.
  while (index > 0)
    {
  // This works regardless of whether we're at 2N+1 or 2N+2.
  int parent = (index - 1) / 2;
  if (Collections.compare(storage[parent], storage[index], comparator)
      <= 0)
    {
      // Parent is the same or smaller than this element, so the
      // invariant is preserved.  Note that if the new element
      // is smaller than the parent, then it is necessarily
      // smaller than the parent's other child.
      break;
    }

  E temp = storage[index];
  storage[index] = storage[parent];
  storage[parent] = temp;

  index = parent;
    }
}
```

offer方法向PriorityQueue中插入一个新元素，若元素为null则抛出NullPointException异常，否则，先通过findSlot方法找到一个插入元素的位置。

接着，根据得到的slot位置，将元素存入storage数组中，并增加使用容量used. 

最后，调用bubbleUp将index插入到树中合适的位置。这一步的时间复杂度是O(log(n))




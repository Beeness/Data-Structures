import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    #enqueue should add an item to the back of the queue.
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    #dequeue should remove and return an item from the front of the queue.
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    #len returns the number of items in the queue.
    return self.size
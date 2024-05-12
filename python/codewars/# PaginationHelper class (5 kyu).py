''' # PaginationHelper class (5 kyu).py
For this exercise you will be strengthening your page-fu mastery. 
You will complete the PaginationHelper class, which is 
a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer 
indicating how many items will be allowed per each page. 
The types of values contained within the collection/array are not relevant.

The following are some examples of how this class is used:

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0) # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

'''


######################################################### MY

# # TODO: complete this class

# class PaginationHelper:
    
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page
#         print(f"{collection}---{items_per_page}")
    
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
    
#     # returns the number of pages
#     def page_count(self):
#         return (len(self.collection)+ self.items_per_page - 1) // self.items_per_page
    
#     # returns the number of items on the given page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         page_count = self.page_count()

#         if page_index < 0 or page_index >= page_count:
#             return -1 
        
#         start_index = page_index * self.items_per_page
#         end_index = start_index + self.items_per_page

#         start_index = min(start_index, len(self.collection))
#         end_index = min(end_index, len(self.collection))

#         return end_index - start_index
    
#     # determines what page an item at the given index is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         item_count = self.item_count()

#         if self.collection == []:
#             return -1
#         if item_index > -1 and item_index <= (self.item_count()-1):
#             page_number = item_index // self.items_per_page
#             return page_number
#         else:
#          return -1



######################################################### BEST PRACTICE && CLEVER

# class PaginationHelper:
#     def __init__(self, collection, items_per_page):
#         self._item_count = len(collection)
#         self.items_per_page = items_per_page

#     def item_count(self):
#         return self._item_count

#     def page_count(self):
#         return -(self._item_count // -self.items_per_page)

#     def page_item_count(self, page_index):
#         return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
#             if 0 <= page_index < self.page_count() else -1

#     def page_index(self, item_index):
#         return item_index // self.items_per_page \
#             if 0 <= item_index < self._item_count else -1


######################################################### MATH

from math import ceil, floor


class PaginationHelper:
  def __init__(self, iterable, items_per_page):
      self.data = iterable[:]
      self.limit = items_per_page
      
  
  def item_count(self):
      return len(self.data)
      
  
  def page_count(self):
      return ceil(self.item_count() / self.limit)
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self, page_index):
      if 0 <= page_index < self.page_count():
          return len(self.data[page_index * self.limit:(page_index + 1) * self.limit])
  
      return -1
      
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self, item_index):
      if  0 <= item_index < self.item_count():
          return floor(item_index / self.limit)
          
      return -1
          
      
  

######################################################### TESTING



helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0)) # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid



helper = PaginationHelper([], 10)
print(helper)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0)) # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid
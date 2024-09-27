class AssertionLibraryError(AssertionError):
    pass
def assert_equal(actual, expected, message=None):

   if actual != expected:
     raise AssertionError(message or f'Expected{expected}, but got {actual}.')
def assert_not_equal(actual, expected,message=None):

   if actual == expected:
       raise AssertionError(message or f"Did not expect{expected}, but got {actual}.")
def assert_true(condition, message=None):
   
   if not condition:
      raise AssertionError(message or f'Expected thr condition to be True, but it was False.')
def assert_false(condition, message=None):
   if condition:
      raise AssertionError(message or f'Expected the condition to be False, but it was True.')
def assert_in(item, container, message=None):
   
   if item not in container:
      raise AssertionError(message or f'Expected {item} to be in  {container}, but it was not.')
def assert_not_in(item, container, message=None):
   
   if item in container:
      raise AssertionError(message or f'Expected {item} not to be in {container}, but it was.')
   

if __name__ == "__main__":
    try:
       assert_equal(10, 13)
       assert_not_equal(30, 48)
       assert_true(True)
       assert_false(False)
       assert_in(3, [2, 4, 6])
       assert_not_in(8, [10, 3, 5])
       print('All assertion passed.')
    except AssertionError as r:
       print(f'AssertionError: {r}')
           
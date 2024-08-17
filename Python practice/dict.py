# text = ["Karan", "Karan", "kar" ,"guru" ,"guru" ]
# de = {word : text.count(word) for word in text}
# print(de)

# text = "hello world hello"
# print(text.split())


# d= {
#     1:"Drag",
#     2:"What",
#     3:"A" 
# }
# print(d)

# for i,v in enumerate(["this" ,"is","Enumerate"]):
#     print(i,v)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# lst = sorted(set(basket))
# print(lst.reverse(),lst)

# invert a dict
# dict = {1:"python",2:"Java",3:"Node"}
# print(dict.items())
# #      key   value  .items() returns 
# dict = {v :  k for k ,v in dict.items() }
# # print(dict)

# Find missing number in a list 
def find_missin(nums):
    count = len(nums)+1
    return  count*(count+1)/2 - sum(nums)

nums = [1,2,3,5]
print(find_missin(nums))

# generate subsets of a set
def subsets(nums):
    result = [[]]   
    for num in nums:
        result += [curr + [num] for curr in result]
    return result
print(subsets(nums))
    
# Find majority element

def major_ele(num):
    
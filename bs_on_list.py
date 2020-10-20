"""
    filename
        bs_on_list.py

    description
        Binary search implemented on a list rather than a BST

    author
        Dylan P. Jackson
"""

def bs(arr, val):
    """
    arr : an ordered array
    val : val to search for in array
    """

    if arr == []:
        raise Exception("Value not found in array")
    mid = len(arr) // 2 
    mid_val = arr[mid]
    if mid_val == val:
        return ("Value in array")
    elif val > mid_val:
        return bs(arr[mid+1:], val)
    else:
        return bs(arr[:mid], val)

def main():
    val = 2
    arr = [1,2,3,4,5,6,7,8]
    print(bs(arr, val))

main()

s = input("Enter numbers by space:\n")

nums1 = s.split(" ")
nums2 = [abs(float(i)) for i in nums1]

for i in nums2:
    print(i)

input()

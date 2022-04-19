N = int(input())
nums = sorted([float(input()) for _ in range(N)])[:7]
for i in nums:
    print("%.3f"%i)
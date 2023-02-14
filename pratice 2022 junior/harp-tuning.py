def harp_tuning():
    instruction = input()

    instructions = []
    nums = [i for i in range(len(instruction)) if instruction[i].isnumeric()]
    last_pos = nums[0]-1
    groups = []
    group = []
    for i in nums:
        # print(i)
        if last_pos+1 == i:
            group.append(i)
            # print(f"group append:{group}")
        else:
            groups.append(group)
            # print(f"groups: {groups}")
            group = [i]
        # print(f"last_pos: {last_pos}")
        last_pos = i
    groups.append(group)

    # print(nums)
    # print(groups)
    instructions = []
    old_i = -1
    for i in groups:
        instructions.append(instruction[old_i+1:i[-1]+1])
        old_i = i[-1]
    instruction.split("-")
    instructions = ",".join(instructions)
    instructions = instructions.replace("+", " tighten ")
    instructions = instructions.replace("-", " loosen ")
    instructions = instructions.replace(",", "\n")
    print(instructions)

harp_tuning()
